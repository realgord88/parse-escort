# -*- coding: utf-8 -*-

import requests
import sqlite3
import lxml.html
import re
from time import sleep



conn = sqlite3.connect('eurogirlsescort.sqlite')
conn.text_factory = str
c = conn.cursor()

h = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.157.62 Safari/537.36)'
    }
s = requests.Session()
session = requests.session()
session.headers.update(h)
girls_urls = []
urls_pages = open('eurogirlsescort_pages.txt', 'a')
error_log = open('errorlog.txt', 'w')


def parse_urls():
    for page in range(1,745):
        url = session.get('http://www.eurogirlsescort.com/escort/?girl-grid-vp1-page=' + str(page))
        doc = lxml.html.document_fromstring(url.content)
        links = doc.xpath('//*[@id="snippet-girl-grid-grid"]/div/div/div/a')
        for link in links:
            urls_pages.write('http://www.eurogirlsescort.com' + str(link.values()[0]) + '\n')
        print str(page) + '/' + '733' + ' pages'
        sleep(3)
    urls_pages.close()

def parse_girls():
    urls_pages = open('eurogirlsescort_pages.txt', 'r')
    line = urls_pages.readline()
    counter = 1
    while line:
        name = 'None'
        full_adress = line[:-2]
        print full_adress
        try:
            url = session.get(full_adress)
        except requests.exceptions.ConnectionError:
            try:

                url = session.get(full_adress)
            except requests.exceptions.ConnectionError:
                try:

                    url = session.get(full_adress)
                except requests.exceptions.ConnectionError:
                    try:

                        url = session.get(full_adress)
                    except requests.exceptions.ConnectionError:
                        try:
                            sleep(3)
                            url = session.get(full_adress)
                        except requests.exceptions.ConnectionError:
                            try:
                                sleep(3)
                                url = session.get(full_adress)
                            except requests.exceptions.ConnectionError:
                                try:
                                    sleep(3)
                                    url = session.get(full_adress)
                                except requests.exceptions.ConnectionError:
                                    print 'ERROR'
                                    url = session.get('http://www.eurogirlsescort.com/escort/new-stella/34080')
                                    error_log.write(full_adress + '\n')

        all_page_html = url.text.encode("utf-8")
        doc = lxml.html.document_fromstring(all_page_html)

        name_trash = doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/h2[1]/span/text()')
        for i in name_trash:
            i = re.sub("^\s+|\n|\r|\t|'|\s+$", '', i)
            if i != '':
                quote = i.find(',')
                name = i[:quote]
        try:
            age = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[1]/span[2]/text()')[0])
        except IndexError:
            age = 'None'

        try:
            xpath_img = '//img[@alt="' + str(name) + '"]/@src'
        except UnicodeEncodeError:
            xpath_img = 'None'
        except IndexError:
            xpath_img = 'None'

        try:
            image_url = 'http://www.eurogirlsescort.com' + str(doc.xpath(xpath_img)[0])
        except IndexError:
            image_url = 'None'
        except UnicodeEncodeError:
            image_url = 'None'

        bio = {}

        try:
            p2_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[2]/span[1]/text()')[0])
            p2_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[2]/span[2]/text()')[0])
            bio[p2_key] = p2_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p3_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[3]/span[1]/text()')[0])
            p3_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[3]/span[2]/text()')[0])
            bio[p3_key] = p3_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p4_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[4]/span[1]/text()')[0])
            p4_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[4]/span[2]/text()')[0])
            bio[p4_key] = p4_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p5_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[5]/span[1]/text()')[0])
            p5_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[5]/span[2]/text()')[0])
            bio[p5_key] = p5_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p6_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[6]/span[1]/text()')[0])
            p6_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[6]/span[2]/text()')[0])
            bio[p6_key] = p6_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p7_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[7]/span[1]/text()')[0])
            p7_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[7]/span[2]/text()')[0])
            bio[p7_key] = p7_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p8_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[8]/span[1]/text()')[0])
            p8_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[8]/span[2]/text()')[0])
            bio[p8_key] = p8_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p9_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[9]/span[1]/text()')[0])
            p9_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[9]/span[2]/text()')[0])
            bio[p9_key] = p9_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p10_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[10]/span[1]/text()')[0])
            p10_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[10]/span[2]/text()')[0])
            bio[p10_key] = p10_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p11_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[11]/span[1]/text()')[0])
            p11_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[11]/span[2]/text()')[0])
            bio[p11_key] = p11_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p12_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[12]/span[1]/text()')[0])
            p12_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[12]/span[2]/text()')[0])
            bio[p12_key] = p12_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p13_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[13]/span[1]/text()')[0])
            p13_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[13]/span[2]/text()')[0])
            bio[p13_key] = p13_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p14_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[14]/span[1]/text()')[0])
            p14_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[14]/span[2]/text()')[0])
            bio[p14_key] = p14_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p15_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[15]/span[1]/text()')[0])
            p15_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[15]/span[2]/text()')[0])
            bio[p15_key] = p15_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p16_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[16]/span[1]/text()')[0])
            p16_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[16]/span[2]/text()')[0])
            bio[p16_key] = p16_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p17_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[17]/span[1]/text()')[0])
            p17_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[17]/span[2]/text()')[0])
            bio[p17_key] = p17_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p18_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[18]/span[1]/text()')[0])
            p18_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[18]/span[2]/text()')[0])
            bio[p18_key] = p18_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p19_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[19]/span[1]/text()')[0])
            p19_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[19]/span[2]/text()')[0])
            bio[p19_key] = p19_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p20_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[20]/span[1]/text()')[0])
            p20_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/p[20]/span[2]/text()')[0])
            bio[p20_key] = p20_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p21_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[5]/p[1]/span[1]/text()')[0])
            p21_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[5]/p[1]/span[2]/text()')[0])
            bio[p21_key] = p21_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p22_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[5]/p[2]/span[1]/text()')[0])
            p22_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[5]/p[2]/span[2]/text()')[0])
            bio[p22_key] = p22_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p23_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[5]/p[3]/span[1]/text()')[0])
            p23_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[5]/p[3]/span[2]/text()')[0])
            bio[p23_key] = p23_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p24_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[5]/p[4]/span[1]/text()')[0])
            p24_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[5]/p[4]/span[2]/text()')[0])
            bio[p24_key] = p24_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p25_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[5]/p[5]/span[1]/text()')[0])
            p25_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[5]/p[5]/span[2]/text()')[0])
            bio[p25_key] = p25_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p26_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[5]/p[6]/span[1]/text()')[0])
            p26_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[5]/p[6]/span[2]/text()')[0])
            bio[p26_key] = p26_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p27_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[5]/p[7]/span[1]/text()')[0])
            p27_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[5]/p[7]/span[2]/text()')[0])
            bio[p27_key] = p27_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        try:
            p28_key = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[5]/p[8]/span[1]/text()')[0])
            p28_value = str(doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[5]/p[8]/span[2]/text()')[0])
            bio[p28_key] = p28_value
        except IndexError:
            pass
        except UnicodeEncodeError:
            pass

        about = ''
        try:
            about_trash = doc.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]/div/text()')
            for i in about_trash:
                i = i.replace("'", "|")
                re.sub("^\s+|\n|\r|\t|\s+$", '', i)
                about += i + ' '
                about = re.sub(r'\s+', ' ', about)
        except IndexError:
            about = 'None'
        except UnicodeEncodeError:
            about = 'None'


        try:
            email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", about)
            if email:
                 email = email[0]
            else:
                email = 'None'
        except TypeError:
            email = 'None'




        nationality = 'None'
        services = 'None'
        location = 'None'
        height = 'None'
        smoker = 'None'
        bust_type = 'None'
        a_level = 'None'
        ethnicity = 'None'
        hair_lenght = 'None'
        provides = 'None'
        travel = 'None'
        hair_color = 'None'
        orientation = 'None'
        weight = 'None'
        meeting_with = 'None'
        eyes = 'None'

        website = 'None'
        phone = 'None'
        skype = 'None'
        viber = 'None'
        whatsApp = 'None'




        for i in bio.items():
            if i[0] == 'Nationality:':
                nationality = i[1]
            if i[0] == 'Services:':
                services = i[1]
            if i[0] == 'Location:':
                location = i[1]
            if i[0] == 'Height:':
                height = i[1]
            if i[0] == 'Smoker:':
                smoker = i[1]
            if i[0] == 'Bust type:':
                bust_type = i[1]
            if i[0] == 'A-level:':
                a_level = i[1]
            if i[0] == 'Ethnicity:':
                ethnicity = i[1]
            if i[0] == 'Hair lenght:':
                hair_lenght = i[1]
            if i[0] == 'Provides:':
                provides = i[1]
            if i[0] == 'Travel:':
                travel = i[1]
            if i[0] == 'Hair color:':
                hair_color = i[1]
            if i[0] == 'Orientation:':
                orientation = i[1]
            if i[0] == 'Weight:':
                weight = i[1]
            if i[0] == 'Meeting with:':
                meeting_with = i[1]
            if i[0] == 'Eyes:':
                eyes = i[1]

            if i[0] == 'Website:':
                website = i[1]
            if i[0] == 'Phone:':
                phone = re.sub("^\s+|\n|\r|\t|\s+$", '', i[1])
            if i[0] == 'Skype:':
                skype = i[1]
            if i[0] == 'Viber:':
                viber = i[1]
            if i[0] == 'WhatsApp:':
                whatsApp = i[1]


        conn.execute("insert into users (name, url, age, image_url, nationality, services, location, \
        height, smoker, bust_type, a_level, ethnicity, hair_lenght, provides, travel, hair_color, orientation, \
        weight, meeting_with, eyes, website, phone, skype, viber, whatsApp, about, email) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
        (str(name.encode('utf8')), str(full_adress.encode('utf8')), str(age.encode('utf8')), str(image_url.encode('utf8')), str(nationality.encode('utf8')), str(services.encode('utf8')), str(location.encode('utf8')), \
        str(height.encode('utf8')), str(smoker.encode('utf8')), str(bust_type.encode('utf8')), str(a_level.encode('utf8')), str(ethnicity.encode('utf8')), str(hair_lenght.encode('utf8')), str(provides.encode('utf8')), str(travel.encode('utf8')), str(hair_color.encode('utf8')), \
        str(orientation.encode('utf8')), str(weight.encode('utf8')), str(meeting_with.encode('utf8')), str(eyes.encode('utf8')), str(website.encode('utf8')), str(phone.encode('utf8')), str(skype.encode('utf8')), str(viber.encode('utf8')), str(whatsApp.encode('utf8')), str(about.encode('utf8')), str(email.encode('utf8'))))
        conn.commit()
        print str(counter)
        counter += 1
        line = urls_pages.readline()

parse_urls()
parse_girls()



c.close()
conn.close()
