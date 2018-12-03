# -*- coding: utf-8 -*-

import requests
import sqlite3
import lxml.html
import re
from time import sleep

conn = sqlite3.connect('escortguide.sqlite')
conn.text_factory = str
c = conn.cursor()

h = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.157.62 Safari/537.36)'
    }

s = requests.Session()
session = requests.session()
session.headers.update(h)

girls_urls = []

urls_pages = open('escortguide.txt', 'a')
error_log = open('errorlog.txt', 'w')


def parse_urls():
    for page in range(1,65):
        url = session.get('http://www.escortguide.com/#sort=r;name=;page=' + str(page))
        doc = lxml.html.document_fromstring(url.content)
        links = doc.xpath('//*[@id="page"]/div/div/div/div/div/div/div/div/a')
        for link in links:
            urls_pages.write('http://www.escortguide.com' + str(link.values()[0]).replace(' ', '%20') + '\n')
        print str(page) + '/' + '65' + ' pages'
    urls_pages.close()

def parse_girls():
    urls_pages = open('escortguide.txt', 'r')
    line = urls_pages.readline()
    counter = 1
    while line:
        name = 'None'
        full_adress = line[:-2]
        print full_adress
        url = session.get(full_adress)
        all_page_html = url.text.encode("utf-8")
        doc = lxml.html.document_fromstring(all_page_html)
        try:
            name = doc.xpath('//*[@id="profile-container"]/div[1]/span/text()')[0]
        except IndexError:
            pass

        bio = {}

        try:
            p1_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[1]/th/text()')[0])
            p1_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[1]/td/text()')[0])
            bio[p1_key] = p1_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p2_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[2]/th/text()')[0])
            p2_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[2]/td/text()')[0])
            bio[p2_key] = p2_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p3_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[3]/th/text()')[0])
            p3_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[3]/td/text()')[0])
            bio[p3_key] = p3_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p4_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[4]/th/text()')[0])
            p4_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[4]/td/text()')[0])
            bio[p4_key] = p4_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p5_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[5]/th/text()')[0])
            p5_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[5]/td/text()')[0])
            bio[p5_key] = p5_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p6_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[6]/th/text()')[0])
            p6_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[6]/td/text()')[0])
            bio[p6_key] = p6_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p7_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[7]/th/text()')[0])
            p7_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[7]/td/text()')[0])
            bio[p7_key] = p7_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p8_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[8]/th/text()')[0])
            p8_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[8]/td/text()')[0])
            bio[p8_key] = p8_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p9_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[9]/th/text()')[0])
            p9_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[9]/td/text()')[0])
            bio[p9_key] = p9_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p10_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[10]/th/text()')[0])
            p10_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[10]/td/text()')[0])
            bio[p10_key] = p10_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p11_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[11]/th/text()')[0])
            p11_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[11]/td/text()')[0])
            bio[p11_key] = p11_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p12_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[12]/th/text()')[0])
            p12_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[12]/td/text()')[0])
            bio[p12_key] = p12_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p13_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[13]/th/text()')[0])
            p13_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[13]/td/text()')[0])
            bio[p13_key] = p13_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p14_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[14]/th/text()')[0])
            p14_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[14]/td/text()')[0])
            bio[p14_key] = p14_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p15_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[15]/th/text()')[0])
            p15_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[15]/td/text()')[0])
            bio[p15_key] = p15_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p16_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[16]/th/text()')[0])
            p16_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[16]/td/text()')[0])
            bio[p16_key] = p16_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p17_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[17]/th/text()')[0])
            p17_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[17]/td/text()')[0])
            bio[p17_key] = p17_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p18_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[18]/th/text()')[0])
            p18_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[18]/td/text()')[0])
            bio[p18_key] = p18_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p19_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[19]/th/text()')[0])
            p19_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[19]/td/text()')[0])
            bio[p19_key] = p19_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p20_key = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[20]/th/text()')[0])
            p20_value = str(doc.xpath('//*[@id="profile-container"]/div[2]/table/tbody/tr[20]/td/text()')[0])
            bio[p20_key] = p20_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        about = 'None'
        try:
            about = str(doc.xpath('//*[@id="profile-container"]/div[5]/div[2]/p/text()'))[2:]
            about = about[:-2]
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p21_key = doc.xpath('//tr/th/text()')
            for i in p21_key:
                if i == 'Phone:':
                    p21_key = str(i)
            p21_value = doc.xpath('//tr/td/text()')
            for i in p21_value:
                if i[0] == '+':
                    p21_value = str(i)
            bio[p21_key] = p21_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass
        except TypeError:
            pass



        email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", about)
        if email:
             email = email[0]
        else:
            email = 'None'


        try:
            image_url = str(doc.xpath('//*[@id="gallery"]/div[1]/a/img/@src')[0])
        except IndexError:
            image_url = 'None'

        hair = 'None'
        age = 'None'
        height = 'None'
        tattoo = 'None'
        eyes = 'None'
        hair_lenght = 'None'
        pubic_hair = 'None'
        ethnic = 'None'
        breast = 'None'
        smoker = 'None'
        drinking = 'None'
        piercings = 'None'
        bust_waist_hip = 'None'
        weight = 'None'
        cup_size = 'None'
        dress_size = 'None'
        phone = 'None'


        for i in bio.items():
            if i[0] == 'Hair:':
                hair = i[1]
            if i[0] == 'Piercings:':
                piercings = i[1]
            if i[0] == 'Age:':
                age = i[1]
            if i[0] == 'Height:':
                height = i[1]
            if i[0] == 'Smoker:':
                smoker = i[1]
            if i[0] == 'Tattoo:':
                tattoo = i[1]
            if i[0] == 'Eyes:':
                eyes = i[1]
            if i[0] == 'Hair Length:':
                hair_lenght = i[1]
            if i[0] == 'Pubic hair:':
                pubic_hair = i[1]
            if i[0] == 'Ethnic:':
                ethnic = i[1]
            if i[0] == 'Breast:':
                breast = i[1]
            if i[0] == 'Drinking:':
                drinking = i[1]
            if i[0] == 'Bust-Waist-Hip:':
                bust_waist_hip = i[1]
            if i[0] == 'Weight:':
                weight = i[1]
            if i[0] == 'Cup size:':
                cup_size = i[1]
            if i[0] == 'Dress size:':
                dress_size = i[1]
            if i[0] == 'Phone:':
                phone = i[1]


        conn.execute("insert into users (name, url, about, email, image_url, hair, age, height, smoker, tattoo, eyes, piercings, \
        hair_lenght, pubic_hair, ethnic, breast, drinking, bust_waist_hip, weight, cup_size, dress_size, phone) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
        (str(name), str(full_adress), str(about), str(email), str(image_url), str(hair), str(age), str(height), str(smoker), str(tattoo), str(eyes), str(piercings),\
        str(hair_lenght), str(pubic_hair), str(ethnic), str(breast), str(drinking), str(bust_waist_hip), str(weight), str(cup_size), str(dress_size), str(phone)))
        conn.commit()


        print str(counter)
        counter += 1
        line = urls_pages.readline()

parse_girls()

c.close()
conn.close()
