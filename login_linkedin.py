import xlwt
import requests
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

style0 = xlwt.easyxf()
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
i=0

browser = webdriver.Chrome()
browser.get("https://linkedin.com/uas/login")
browser.find_element_by_id("session_key-login").send_keys("anagha712@gmail.com" + Keys.TAB)
browser.find_element_by_id("session_password-login").send_keys("anaghaanu"+ Keys.RETURN)
time.sleep(1)


with open("C:\Python27\URL.txt") as f:
    content = f.readlines()
    for x in content:

		#with open("domainlist.txt") as f:
    	#for line in f:
		url =x

		pages = [url]

		for page in pages:
			page_html = requests.get(page)
			soup = BeautifulSoup(page_html.text, "html.parser")
		
			
			link_pages = url
			#link_html = requests.get(link_pages)
			ws.write(i, 0, url, style0)
			#driver = webdriver.Chrome()
			browser.get(url)
			time.sleep(1)
			link_html = browser.page_source.encode('utf-8')
			

				#print link_html;
			soupl = BeautifulSoup(link_html)


			res1 = soupl.find(class_='org-about-company-module__company-page-url')
			if res1:
				web = soupl.find("div",attrs={"class":"org-about-company-module__company-page-url"})
				if web:
					webs=web.text
					print webs
					ws.write(i, 1, webs, style0)

			res2 = soupl.find(class_='org-about-company-module__company-type')
			if res2:
				typ = soupl.find("p",attrs={"class":"org-about-company-module__company-type"})
				if typ:
					typs=typ.text
					ws.write(i, 2, typs, style0)

			res3 = soupl.find(class_='org-about-company-module__company-staff-count-range')
			if res3:
				cmpny = soupl.find("p",attrs={"class":"org-about-company-module__company-staff-count-range"})
				if cmpny:
					cmpnys=cmpny.text
					ws.write(i, 3, cmpnys, style0)

			res4 = soupl.find(class_='org-about-company-module__founded')
			if res4:
				fnd = soupl.find("p",attrs={"class":"org-about-company-module__founded"})
				if fnd:
					fnds=fnd.text
					ws.write(i, 4, fnds, style0)

			res5 = soupl.find(class_='org-about-company-module__specialities')
			if res5:
				spc = soupl.find("p",attrs={"class":"org-about-company-module__specialities"})
				if spc:	
					spcs=spc.text
					ws.write(i, 5, spcs, style0)

			res6 = soupl.find(class_='org-about-company-module__headquarters')
			if res6:
				hd = soupl.find("p",attrs={"class":"org-about-company-module__headquarters"})
				if hd:
					hds=hd.text
					ws.write(i, 6, hds, style0)

			wb.save('domainscrape2.xls')
			i=i+1
		

browser.quit()

		