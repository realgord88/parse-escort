import sys
import requests
import sqlite3
import lxml.html
import re
from time import sleep
import random


conn = sqlite3.connect('eroticmonkey.sqlite')
c = conn.cursor()


h = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.157.62 Safari/537.36)'
    }


def parse_cities():
	urls_pages = open('city.txt', 'w')
	https_proxy  = "http://96.239.193.243:8080"
	proxyDict = {"https"  : https_proxy}
	url = session.get('http://eroticmonkey.com', proxies=proxyDict)
	doc = lxml.html.document_fromstring(url.content)
	links = doc.xpath('//*[@id="nav"]/li/ul/li/a/@href')
	for link in links:
		urls_pages.write('http://eroticmonkey.com'+str(link)+'\n')

def urls_girls():
	urls_pages = open('city.txt', 'r')
	txt_girls = open('girls.txt', 'a')
	https_proxy  = "http://96.239.193.243:8080"
	proxyDict = {"https"  : https_proxy}
	line = urls_pages.readline()
	while line:
		full_adress = line[:-1]
		print (full_adress)
		url = session.get(full_adress, proxies=proxyDict)
		doc = lxml.html.document_fromstring(url.content)
		pages = doc.xpath('//*[@id="reviews_list"]/div[1]/div[5]/div/ul/li[4]/a/text()')[0]
		for page in range(1,int(pages)+1):
			try:
				adress = full_adress + '-' + str(page)
				url = session.get(adress, proxies=proxyDict)
				doc = lxml.html.document_fromstring(url.content)
				girl_url = doc.xpath('//*[@id="reviews_list"]/div/div/div/div/h3/a/@href')
				for girl in girl_url:
					txt_girls.write('http://eroticmonkey.com/' + girl + '\n')
			except requests.exceptions.ConnectionError:
				sleep(5)
		
		line = urls_pages.readline()

def parse_girls():
	urls_pages = open('girls.txt', 'r')
	
	https_proxy  = "http://63.241.251.182:8080"
	proxyDict = {"https"  : https_proxy}
	line = urls_pages.readline()
	counter = 1
	while line:
		try:
			progress = open('progress.txt', 'w')
			full_adress = line[:-1]
			print (full_adress)
			url = requests.get(full_adress)
			doc = lxml.html.document_fromstring(url.content)

			try:
				email = doc.xpath('//*[@id="qe_email"]/a/text()')
				if email:
					email = email[0]
				else:
					email = 'None'
			except TypeError:
				email = 'None'

			try:
				name = str(doc.xpath('//*[@id="qe_name"]/text()')[0])
			except IndexError:
				name = 'None'

			try:
				image_url = str(doc.xpath('//*[@id="content_right_container"]/div/div[1]/div/div[1]/div/a/@href')[0])
			except IndexError:
				image_url = 'None'

			try:
				phone = str(doc.xpath('//*[@id="qe_phone"]/a/strong/text()')[0])
			except IndexError:
				phone = 'None'

			try:
				state = str(doc.xpath('//*[@id="content_right_container"]/div/div[1]/div/div[2]/div[4]/div[1]/ul/li[1]/text()')[0])
				state = re.sub("^\s+|\n|\r|\t|'|\|/|\xa0|\s+$", '', state)
			except IndexError:
				state = 'None'

			try:
				city = str(doc.xpath('//*[@id="content_right_container"]/div/div[1]/div/div[2]/div[4]/div[1]/ul/li[2]/text()')[0])
				city = re.sub("^\s+|\n|\r|\t|'|\|/|\xa0|\s+$", '', city)
			except IndexError:
				city = 'None'

			try:
				site = doc.xpath('//*[@id="qe_website"]/a/text()')[0]
			except IndexError:
				site = 'None'

			if site == 'None':
				div_number = 5
			else:
				div_number = 6

			bio_labels = doc.xpath('//*[@id="content_right_container"]/div/div[1]/div/div[' + str(div_number) + ']/div[1]/ul/li/b/text()')
			bio_labels2 = doc.xpath('//*[@id="content_right_container"]/div/div[1]/div/div[' + str(div_number) + ']/div[2]/ul/li/b/text()')
			for i in bio_labels2:
				bio_labels.append(i)

			bio_param = doc.xpath('//*[@id="content_right_container"]/div/div[1]/div/div[' + str(div_number) + ']/div[1]/ul/li/text()')
			bio_param2 = doc.xpath('//*[@id="content_right_container"]/div/div[1]/div/div[' + str(div_number) + ']/div[2]/ul/li/text()')
			for i in bio_param2:
				bio_param.append(i)
			
			bio = {}
			ra = 0
			try:
				for i in bio_param:
					bio[bio_labels[ra][:-1]] = re.sub("^\s+|\n|\r|\t|'|\|/|\xa0|\s+$", '', i)
					ra += 1
			except IndexError:
				pass

			Age = 'None'
			Ethnicity = 'None'
			Height = 'None'
			Tranny = 'None'
			Piercings = 'None'
			Smokes = 'None'
			Hair_color = 'None'
			Hair_length = 'None'
			Hair_Style = 'None'
			Appearance = 'None'
			Services = 'None'
			Breast_Size = 'None'
			Breast_Cup = 'None'
			Breast_Appearance = 'None'
			Kitty = 'None'
			Ass = 'None'
			Hygiene = 'None'
			Implants = 'None'
			Body_Type = 'None'
			Tattoos = 'None'
			Pornstar = 'None'
			Punctuality = 'None'

			for i in bio.items():
				if i[0] == 'Age':
					Age = i[1]
				if i[0] == 'Ethnicity':
					Ethnicity = i[1]
				if i[0] == 'Height':
					Height = i[1]
				if i[0] == 'Tranny':
					Tranny = i[1]
				if i[0] == 'Piercings':
					Piercings = i[1]
				if i[0] == 'Smokes':
					Smokes = i[1]
				if i[0] == 'Hair color':
					Hair_color = i[1]
				if i[0] == 'Hair length':
					Hair_length = i[1]
				if i[0] == 'Hair Style':
					Hair_Style = i[1]
				if i[0] == 'Appearance':
					Appearance = i[1]
				if i[0] == 'Services':
					Services = i[1]
				if i[0] == 'Breast Size':
					Breast_Size = i[1]
				if i[0] == 'Breast Cup':
					Breast_Cup = i[1]
				if i[0] == 'Breast Appearance':
					Breast_Appearance = i[1]
				if i[0] == 'Kitty':
					Kitty = i[1]
				if i[0] == 'Ass':
					Ass = i[1]
				if i[0] == 'Hygiene':
					Hygiene = i[1]
				if i[0] == 'Implants':
					Implants = i[1]
				if i[0] == 'Body Type':
					Body_Type = i[1]
				if i[0] == 'Tattoos':
					Tattoos = i[1]
				if i[0] == 'Pornstar':
					Pornstar = i[1]
				if i[0] == 'Punctuality':
					Punctuality = i[1]

			try:
				conn.execute("insert into users (name, url, image_url, email, phone, state, city, site, Age, Ethnicity, Height, Tranny, Piercings, Smokes, \
				Hair_color, Hair_length, Hair_Style, Appearance, Services, Breast_Size, Breast_Cup, Breast_Appearance, Kitty, Ass, Hygiene, Implants, \
				Body_Type, Tattoos, Pornstar, Punctuality) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
	            (str(name), str(full_adress), str(image_url), str(email), str(phone), state, city, site, Age, Ethnicity, Height, Tranny, Piercings, Smokes, \
				Hair_color, Hair_length, Hair_Style, Appearance, Services, Breast_Size, Breast_Cup, Breast_Appearance, Kitty, Ass, Hygiene, Implants, \
				Body_Type, Tattoos, Pornstar, Punctuality))
				conn.commit()
			except UnicodeDecodeError:
				pass
			except UnicodeEncodeError:
				pass
		except requests.exceptions.ProxyError:
			sleep(5)
		except requests.exceptions.ConnectionError:
			sleep(5)
		
		progress.write(str(counter) + ' / 114744')
		counter += 1

		line = urls_pages.readline()

parse_girls()

c.close()
conn.close()