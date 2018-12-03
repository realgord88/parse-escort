import dryscrape
import sys
import requests
import sqlite3
import lxml.html
import re
from time import sleep
import random

if 'linux' in sys.platform:
    dryscrape.start_xvfb()


conn = sqlite3.connect('eros.sqlite')
conn.text_factory = str
c = conn.cursor()


def parse_city():
    urls_pages = open('city.txt', 'w')
    country_urls = []
    sess = dryscrape.Session(base_url = 'http://www.eros.com')
    sess.visit('/')
    for link in sess.xpath('/html/body/div/div/section/div/div/div/div/a'):
        country_urls.append(link['href'])
    for url in country_urls:
        sess = dryscrape.Session(base_url = url)
        sess.visit('/')
        for link in sess.xpath('//ul/a'):
            urls_pages.write(str(link['href']) + '\n')
        for link in sess.xpath('//ul/li/div/ul/a'):
            urls_pages.write(str(link['href']) + '\n')


def getting_links_cityes():
    urls_pages = open('city.txt', 'r')
    all_girls_pages = open('trash.txt', 'w')
    line = urls_pages.readline()
    while line:
        full_adress = line[:-1]
        print full_adress
        sess = dryscrape.Session()
        sess.visit(full_adress)
        cookies = sess.cookies()
        sess.set_cookie(cookies)
        sess.visit(full_adress)
        for link in sess.xpath('//*[@id="subcats"]/ul/li[2]/a'):
            all_girls_pages.write(link['href'] + '\n')
        line = urls_pages.readline()
    urls_pages.close()
    all_girls_pages.close()

def getting_girls_urls():
    urls_pages = open('trash.txt', 'r')
    all_girls_urls = open('urls.txt', 'a')
    line = urls_pages.readline()
    while line:
        full_adress = line[:-1]
        print full_adress
        sess = dryscrape.Session()
        sess.visit(full_adress)
        cookies = sess.cookies()
        sess.set_cookie(cookies)
        sess.visit(full_adress)
        for link in sess.xpath('//*[@id="adListing"]/li/a'):
             all_girls_urls.write(str(link['href']) + '\n')
        line = urls_pages.readline()
    urls_pages.close()
    all_girls_urls.close()

def test():
    urls_pages = open('trash.txt', 'r')
    all_girls_urls = open('urls.txt', 'a')
    line = urls_pages.readline()
    while line:
        all_list = []
        full_adress = line[:-1]
        print full_adress
        sess = dryscrape.Session()
        sess.visit(full_adress)
        cookies = sess.cookies()
        sess.set_cookie(cookies)
        sess.visit(full_adress)
        for link in sess.xpath('//*[@id="adListing"]/li/a'):
            all_list.append(str(link['href']))

        for page in range(0,20):
            try:
                xpath_pages = '//*[@id="listing"]/div/div[2]/div[1]/div/ul[1]/li[' + str(page) + ']/a'
                next_page = sess.xpath(xpath_pages)
                for i in next_page:
                    i.click()
                    for link in sess.xpath('//*[@id="adListing"]/li/a'):
                        if str(link['href']) in all_list:
                            pass
                        else:
                            all_list.append(str(link['href']))
            except:
                pass

        line = urls_pages.readline()
        print len(all_list)
        for url in all_list:
            all_girls_urls.write(url + '\n')




def parse_girls():
    all_girls_urls = open('urls.txt', 'r')
    line = all_girls_urls.readline()
    number = 1
    while line:
        try:
            full_adress = line[:-1]
            print full_adress
            sess = dryscrape.Session()
            sess.visit(full_adress)
            cookies = sess.cookies()
            sess.set_cookie(cookies)
            sess.visit(full_adress)

            try:
                name = str(sess.xpath('/html/body/div[2]/div/section/div[2]/div[2]/header/div/div[1]/h1')[0].text())
            except:
                name = 'None'

            try:
                image_url = sess.xpath('/html/body/div[2]/div/section/div[2]/div[2]/section[1]/div/div[1]/div[1]/div/div[1]/div/img')
                image_url = image_url[0]['src'][2:]
            except:
                image_url = 'None'

            try:
                email = sess.xpath('/html/body/div[2]/div/section/div[2]/div[2]/section[3]/aside/article[2]/ul/li/span/a/span')
                email = email[0].text()
            except:
                email = 'None'

            try:
                phone = sess.xpath('/html/body/div[2]/div/section/div[2]/div[2]/section[3]/aside/article[1]/ul/li/span/a/span')
                phone = phone[0].text()
            except:
                phone = 'None'


            about_temp = sess.xpath('/html/body/div[2]/div/section/div[2]/div[2]/section[3]/div/div')
            about = ''
            for i in about_temp:
                about += re.sub("^\s+|\n|\r|\t|'|\|/|\xa0|\s+$", '', i.text())

            bio = {}
            bio_labels = sess.xpath('//div/dl/dt')
            bio_attributes = sess.xpath('//div/dl/dd')
            counter = 0
            try:
                for i in bio_attributes:
                    bio[bio_labels[counter].text()] = re.sub("^\s+|\n|\r|\t|'|\|/|\xa0|\s+$", '', i.text())
                    counter += 1
            except:
                pass

            gender = 'None'
            age = 'None'
            ethnicity = 'None'
            hair_color = 'None'
            eye_color = 'None'
            height = 'None'
            weight = 'None'
            measurements = 'None'
            affiliation = 'None'
            availability = 'None'
            available_to = 'None'

            for i in bio.items():
                if i[0] == 'GENDER':
                    gender = i[1]
                if i[0] == 'AGE':
                    age = i[1]
                if i[0] == 'ETHNICITY':
                    ethnicity = i[1]
                if i[0] == 'HAIR COLOR':
                    hair_color = i[1]
                if i[0] == 'EYE COLOR':
                    eye_color = i[1]
                if i[0] == 'HEIGHT':
                    height = i[1]
                if i[0] == 'WEIGHT':
                    weight = i[1]
                if i[0] == 'MEASUREMENTS':
                    measurements = i[1]
                if i[0] == 'AFFILIATION':
                    affiliation = i[1]
                if i[0] == 'AVAILABILITY':
                    availability = i[1]
                if i[0] == 'AVAILABLE TO':
                    available_to = i[1]

            try:
                conn.execute("insert into users (name, url, image_url, email, phone, gender, age, ethnicity, hair_color, eye_color, height, weight, \
                measurements, affiliation, availability, available_to, about) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
                (str(name), str(full_adress), str(image_url), str(email), str(phone), str(gender), str(age), str(ethnicity), str(hair_color), str(eye_color), str(height), str(weight), \
                str(measurements), str(affiliation), str(availability), str(available_to), str(about)))
                conn.commit()
            except UnicodeDecodeError:
                pass
            except UnicodeEncodeError:
                pass

            print number
            number +=1 
        except:
            pass

        line = all_girls_urls.readline()

    all_girls_urls.close()


parse_girls()

c.close()
conn.close()
