from bs4 import BeautifulSoup
import csv
import requests
import time
from random import randint
import os
import re
import urllib
from urllib.request import urlopen
import datetime, calendar

# get the HTML page
def getHTMLDoc(keyword):
	url = "https://www.google.com/search?q=" + keyword + "&tbm=nws"
	time.sleep(randint(0,2))
	url_request = requests.get(url)
	content = url_request.text
	soup = BeautifulSoup(content, "html.parser")

	return soup

# get article summaries
def scrape_summaries(keyword):

	soup = getHTMLDoc(keyword)

	summary_arr = []
	summary = soup.find_all('div',attrs = {'class':'st'})

	for summary_div in summary:
		summary_arr.append(summary_div.get_text())

	return summary_arr

# get article links
def scrape_links(keyword):

	soup = getHTMLDoc(keyword)
	phrase0 = '/url?q='
	phrase1 = '&sa='


	link_arr = []
	links = soup.find_all('h3')
	for link in links:
		raw_url =  (link.find('a')['href'])
		cleaned_url = raw_url[raw_url.index(phrase0) + len(phrase0):]
		cleaned_url = cleaned_url[0:cleaned_url.index(phrase1)]
		link_arr.append(cleaned_url)
	return link_arr

# get article titles
def scrape_titles(keyword):

	soup = getHTMLDoc(keyword)

	title_arr = []
	titles = soup.find_all('h3')
	for title in titles:
		title = title.get_text()
		title_arr.append(title)

	return title_arr

# get article dates
def scrape_dates(keyword):

	soup = getHTMLDoc(keyword)

	date_arr = []
	dates = soup.find_all('span', attrs = {'class':'f'})
	for date in dates:
		date = date.get_text()
		date = date.split("-",1)[-1]
		if date[0] != 'P':
			date_arr.append(date)

	return date_arr

#get article publications
def scrape_publications(keyword):

	soup = getHTMLDoc(keyword)

	pub_arr = []
	pubs = soup.find_all('span', attrs = {'class':'f'})

	for pub in pubs:

		pub = pub.get_text()

		if ("-" in pub):
			pub = pub.split("-",1)[0]
			pub_arr.append(pub)

	return pub_arr

		
def main():
	# replace "keyword" with desired keyword
	my_summaries = scrape_summaries("keyword") 
	my_links = scrape_links("keyword")
	my_titles = scrape_titles("keyword")
	my_dates = scrape_dates("keyword")
	my_publications = scrape_publications("keyword")


	os.chmod('enter csv file location',755)

	with open('enter csv file location','a') as csvfile:
		writer = csv.writer(csvfile)

		writer.writerow(['Title','Link','Publication','Summary','Date'])

		for i in range(0, len(sparkcognition_summaries)):
			row = [my_titles[i], my_links[i],my_publications[i],my_summaries[i], my_dates[i]]
			writer.writerow(row)

	# Comment out to schedule this program to run at the last day of every month
	'''
	today = datetime.date.today()
	if calendar.monthrange(today.year, today.month)[1] != today.day:
		main()
	'''
main()
