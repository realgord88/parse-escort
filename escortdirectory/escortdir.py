# -*- coding: utf-8 -*-

import requests
import sqlite3
import urllib
import lxml.html
from lxml import html
import re

conn = sqlite3.connect('escortdirectory.sqlite')
c = conn.cursor()
h = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.157.62 Safari/537.36)'
    }
s = requests.Session()
session = requests.session()
session.headers.update(h)
girls_urls = []

def parse_urls():
    for page in range(1,172):
        url = session.get('http://www.escortdirectory.com/en/#page=' + str(page))
        doc = lxml.html.document_fromstring(url.text)
        links = doc.xpath('//*[@id="top-escorts"]/div/a')
        for link in links:
            if len(link.values()) > 1:
                if link.values()[1][:8] == '/escort/':
                    girls_urls.append(link.values()[1])

def parse_info():
    category = 'None'
    ethnic = 'None'
    nationality = 'None'
    age = 'None'
    eyes = 'None'
    hair = 'None'
    hair_length = 'None'
    pubic_hair = 'None'
    tattoo = 'None'
    piercing = 'None'
    weight = 'None'
    breast = 'None'
    cup_size = 'None'
    bust_waist_hip = 'None'
    shoe_size = 'None'
    dress_size = 'None'
    orientation = 'None'
    available_for = 'None'
    drinking = 'None'
    height = 'None'

    counter = 1
    for girl_url in girls_urls:
        all_bio = []
        all_bio_param = []
        full_adress = 'http://www.escortdirectory.com/en' + str(girl_url)
        url = session.get(full_adress)
        all_page_html = url.text.encode("utf-8")

        #image url
        temp = all_page_html.find('lightbox-atomium')
        image_start = all_page_html[temp+24:]
        image_end = image_start.find('"')
        image_url = image_start[:image_end]

        doc = lxml.html.document_fromstring(all_page_html)

        #name
        name_girl = doc.xpath('//*[@id="profile-info"]/div[1]/text()')[0]

        #phone
        try:
            phone_girl = doc.xpath('//*[@id="profile-info"]/div[2]/span/text()')[0][9:]
        except IndexError:
            phone_girl = 'None'

        #bio
        bio = doc.xpath('//tr/td/text()')
        for i in bio:
            i = re.sub("^\s+|\n|\r|\t|\s+$", '', i)
            if i != '':
                all_bio.append(i)
        count = 0
        for i in all_bio:
            if i == 'Female':
                break
            else:
                count += 1
        all_bio = all_bio[count:]

        bio_param = doc.xpath('//tr/th/text()')
        for i in bio_param:
            i = re.sub("^\s+|\n|\r|\t|\s+$", '', i)
            if i != '':
                all_bio_param.append(i)
        count = 0
        for i in all_bio_param:
            if i == 'Category:':
                break
            else:
                count += 1
        all_bio_param = all_bio_param[count:len(all_bio)]

        for i in range(13):
            try:
                if all_bio_param[i] == 'Category:':
                    category = all_bio[i]
                if all_bio_param[i] == 'Ethnic:':
                    ethnic = all_bio[i]
                if all_bio_param[i] == 'Nationality:':
                    nationality = all_bio[i]
                if all_bio_param[i] == 'Age:':
                    age = all_bio[i]
                if all_bio_param[i] == 'Eyes:':
                    eyes = all_bio[i]
                if all_bio_param[i] == 'Hair:':
                    hair = all_bio[i]
                if all_bio_param[i] == 'Hair Length:':
                    hair_length = all_bio[i]
                if all_bio_param[i] == 'Pubic hair:':
                    pubic_hair = all_bio[i]
                if all_bio_param[i] == 'Tattoo:':
                    tattoo = all_bio[i]
                if all_bio_param[i] == 'Piercing:':
                    piercing = all_bio[i]
                if all_bio_param[i] == 'Weight:':
                    weight = all_bio[i]
                if all_bio_param[i] == 'Height:':
                    height = all_bio[i]
                if all_bio_param[i] == 'Cup size:':
                    cup_size = all_bio[i]
                if all_bio_param[i] == 'Breast:':
                    breast = all_bio[i]
                if all_bio_param[i] == 'Bust-Waist-Hip:':
                    bust_waist_hip = all_bio[i]
                if all_bio_param[i] == 'Shoe size:':
                    shoe_size = all_bio[i]
                if all_bio_param[i] == 'Dress size:':
                    dress_size = all_bio[i]
                if all_bio_param[i] == 'Orientation:':
                    orientation = all_bio[i]
                if all_bio_param[i] == 'Drinking:':
                    drinking = all_bio[i]
            except IndexError:
                break

        about_me = ''
        about_me_page = doc.xpath('//*[@id="about-me"]/div/div/p/text()')
        for i in range(10):
            try:
                about_me += about_me_page[i]
            except IndexError:
                break

        conn.execute("insert into users (name, url, phone, imageurl, category,\
        ethnic, nationality, age, eyes, hair, hair_length, pubic_hair, tattoo, \
        piercing, weight, height, cup_size, breast, bust_waist_hip, shoe_size, \
        dress_size, orientation, drinking, about_me) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
        (str(name_girl), str(full_adress), str(phone_girl), str(image_url), category, ethnic, nationality, age, eyes, hair, hair_length, pubic_hair, tattoo, \
        piercing, weight, height, cup_size, breast, bust_waist_hip, shoe_size, \
        dress_size, orientation, drinking, about_me ))
        print str(counter) + '/' + str(len(girls_urls))
        counter += 1

parse_urls()
parse_info()


conn.commit()
c.close()
conn.close()
