# -*- coding: utf-8 -*-

import requests
import sqlite3
import lxml.html
import re
from time import sleep
import sqlite3

conn = sqlite3.connect('eccie.sqlite')
c = conn.cursor()

h = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.157.62 Safari/537.36)'
    }

s = requests.Session()
session = requests.session()
session.headers.update(h)


def parse_girls_list():
	urls_pages = open('girls.txt', 'w')
	for page in range(1,61):
		print page
		url = session.get('http://www.eccie.net/providers.php?location_id=0&letter=&page=' + str(page))
		doc = lxml.html.document_fromstring(url.content)
		links = doc.xpath('//tr/td/ul/li/a[@class="thumbnail"]/@href')
		for link in links:
			urls_pages.write('http://www.eccie.net' + str(link) + '\n')    
	urls_pages.close()


def parse_all_girls():
	urls_pages = open('girls.txt', 'r')
	line = urls_pages.readline()
	counter = 1
	while line:
		name = 'None'
		full_adress = line[:-1]
		print full_adress
		url = session.get(full_adress)
		all_page_html = url.text.encode("utf-8")
		doc = lxml.html.document_fromstring(all_page_html)
		try:
			email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", all_page_html)
			if email:
				email = email[0]
			else:
				email = 'None'
		except TypeError:
			email = 'None'

		try:
			conn.execute("insert into users (url, email) values (?, ?)", (str(full_adress).encode('utf-8'), str(email).encode('utf-8')))
			conn.commit()
		except UnicodeDecodeError:
			pass
		except UnicodeEncodeError:
			pass
		print str(counter) + ' / 1131'
		counter += 1
		line = urls_pages.readline()

parse_all_girls()

c.close()
conn.close()