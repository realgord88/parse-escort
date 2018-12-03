# -*- coding: utf-8 -*-

import requests
import sqlite3
import lxml.html
import re
from time import sleep

conn = sqlite3.connect('cityvibe.sqlite')
conn.text_factory = str
c = conn.cursor()

h = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.157.62 Safari/537.36)'
    }

s = requests.Session()
session = requests.session()
session.headers.update(h)


def parse_city():
    urls_pages = open('city.txt', 'w')
    url = session.get('http://www.cityvibe.com/')
    doc = lxml.html.document_fromstring(url.content)
    links = doc.xpath('//*[@id="home-cities-country-1"]/div/div/a/@href')
    for link in links:
        urls_pages.write(str(link)[2:]+ '\n')
    urls_pages.close()

def parse_pages():
    urls_pages = open('city.txt', 'r')
    girls_urls = open('girls.txt', 'w')
    line = urls_pages.readline()
    while line:
        full_adress = 'http://' + line[:-2]
        print full_adress
        url = session.get(full_adress)
        doc = lxml.html.document_fromstring(url.content)
        try:
            pages = doc.xpath('//*[@id="posts_main_id"]/h3/b[2]/span/text()')[0]
            for i in range(1, int(pages)+1):
                full_adress = 'http://' + line[:-2] + '?page=' + str(i)
                url = session.get(full_adress)
                doc = lxml.html.document_fromstring(url.content)
                urls = doc.xpath('//*[@id="fuzzDataGrid_listingsGrid_table"]/div/div/div/a/@href')
                for url in urls:
                    if url[:2] == '//':
                        girls_urls.write(url[2:] + '\n')
        except IndexError:
            pass
        line = urls_pages.readline()

def parse_girls():
    girls_urls = open('girls.txt', 'r')
    line = girls_urls.readline()
    counter = 1
    while line:
        full_adress = 'http://' + line[:-1]
        print full_adress
        url = session.get(full_adress)
        doc = lxml.html.document_fromstring(url.content)
        try:
            name = doc.xpath('//*[@id="fuzzController_container_posts-post-viewer_div_id"]/div[2]/div[1]/div[1]/div[1]/div[1]/text()')[0].encode('utf-8')
            name = re.sub("^\s+|\n|\r|\t|'|\s+$", '', name)
        except IndexError:
            name = 'None'
        except UnicodeDecodeError:
            name = 'None'
        except UnicodeEncodeError:
            name = 'None'
        try:
            image_url = 'http://' + str(doc.xpath('//*[@id="fuzzController_container_posts-post-viewer_div_id"]/div[2]/div[1]/div[1]/div[2]/div/img/@src')[0][2:])
        except IndexError:
            image_url = 'None'
        info = doc.xpath('//*[@id="fuzzController_container_posts-post-viewer_div_id"]/div/div/div/div/a/text()')
        phone = 'None'
        email = 'None'
        site = 'None'
        try:
            for i in range(4):
                info.remove(u'\xa0')
        except ValueError:
            pass
        for i in info:
            if i[0] == '(':
                phone = str(i)
            if i[0] == 'h':
                site = str(i)
            if i[0] != '(' and i[0] != 'h':
                email = str(i)
        about = ''
        try:
            about_trash = doc.xpath('//*[@id="fuzzController_container_posts-post-viewer_div_id"]/div[5]/text()')
            for i in about_trash:
                about += re.sub("^\s+|\n|\r|\t|'|\s+$", '', i)
        except UnicodeDecodeError:
            about = 'None'

        try:
            conn.execute("insert into users (name, url, image_url, phone, email, site, about) values (?, ?, ?, ?, ?, ?, ?)", \
            (str(name).encode('utf-8'), str(full_adress).encode('utf-8'), str(image_url).encode('utf-8'), str(phone).encode('utf-8'), str(email).encode('utf-8'), str(site).encode('utf-8'), str(about).encode('utf-8')))
            conn.commit()
        except UnicodeDecodeError:
            pass
        except UnicodeEncodeError:
            pass


        print str(counter)
        counter += 1
        line = girls_urls.readline()

parse_girls()

conn.commit()
c.close()
conn.close()
