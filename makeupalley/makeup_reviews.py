from bs4 import BeautifulSoup
import csv
import requests
import time
from random import randint
import mechanicalsoup
from http import cookiejar
import collections
import difflib
from os import path
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import PIL.Image


from wordcloud import WordCloud, STOPWORDS

# Product: MAC Satin Lipstick in Brave

def getHTMLDoc():

	browser = mechanicalsoup.Browser(soup_config={'features':'html.parser'})
	loginPage = browser.get('https://www.makeupalley.com/account/login.asp')

	form = loginPage.soup.find_all('form')[0]
	form.find('input', {'name':'UserName'})['value'] = 'username'
	form.find('input', {'name':'Password'})['value'] = 'password'
	page = browser.submit(form, loginPage.url)

	# reviews with highest rating
	review_page1 = browser.get('https://www.makeupalley.com/product/showreview.asp/ItemId=6003/SortBy=rating-desc/AgeRange=/SkinToneType=/Satin-Lipstick-in-Brave/MAC/Lipstick')
	review_page2 = browser.get('https://www.makeupalley.com/product/showreview.asp/page=2/pagesize=10/ItemID=6003/SortBy=rating-desc/')
	review_page3 = browser.get('https://www.makeupalley.com/product/showreview.asp/page=3/pagesize=10/ItemID=6003/SortBy=rating-desc/')
	review_page4 = browser.get('https://www.makeupalley.com/product/showreview.asp/page=4/pagesize=10/ItemID=6003/SortBy=rating-desc/')
	review_page5 = browser.get('https://www.makeupalley.com/product/showreview.asp/page=5/pagesize=10/ItemID=6003/SortBy=rating-desc/')
	content =  review_page1.text + review_page2.text + review_page3.text  + review_page4.text + review_page5.text
	soup = BeautifulSoup(content,"html.parser")

	return soup

# get all review comments, strip line spaces and put them into an array
def getComment():

	soup = getHTMLDoc()

	comment_arr = []
	
	comments = soup.find_all('div',attrs = {'class':'comment-content'})

	for comment in comments:
		comment = comment.get_text()
		comment = comment.replace('\t','')
		comment_arr.append(comment)

	return comment_arr

def extractPhrase():

	wordList = []
	word_arr = []
	wordFreq = []
	freq_arr=[]
	similar_word_arr = []
	cleaned_word_arr = []

	junk_arr = ["look","like","was","what","give","!", ".", ",", ".", "?", "''", "/", "i'm", "i","this","that","he","she","she's","is", "----","--", "-", "---", "to","you","they","are","your","yours","you're","will","with","so","u","me","my","all","also","am","so","for","be","cause","do","don't","doesn't","does","not","either","some","it","its","a","at","in","of","on","but","as","when","few","have","has","and","it's","the","about","can","having","just","or","if","first","out","up","too"]

	comments = getComment()

	for comment in comments:
		wordList = comment.split()
		for word in wordList:
			# turn all words into lowercase for processing
			word = word.lower()
			word = word.replace('.','')
			word = word.replace(',','')
			if word not in junk_arr: # if word is (supposedly) meaningful
				word_arr.append(word)


	# find words that are similar
	for word_idx in range(len(word_arr)):
		similar_words = difflib.get_close_matches(word_arr[word_idx],word_arr[:], cutoff = 0.9)
		similar_word_arr.append(similar_words)

	# group words that are similar together into one word
	for word_group in similar_word_arr:
		cleaned_word_arr.append(word_group[0])
	
	# find the frequency of each word
	for word in cleaned_word_arr:
		wordFreq.append(cleaned_word_arr.count(word))

	return(dict(zip(cleaned_word_arr,wordFreq)))


def sortByMostCommonPhrase(freqdict):

	aux = [(freqdict[key], key) for key in freqdict]
	aux.sort()
	aux.reverse()

	return aux

def main():

	out_file = open("word_file.txt","w")

	word_tuple_list = sortByMostCommonPhrase(extractPhrase())

	for word_tuple in word_tuple_list:
		out_file.write(word_tuple[1])
		out_file.write(' ')
	out_file.close()

	d = path.dirname(__file__)
	# Read the whole text.
	text = open(path.join(d, 'word_file.txt')).read()

	# read the mask image
	
	alice_mask = np.array(PIL.Image.open(path.join(d, "mask.png")))
	stopwords = set(STOPWORDS)
	stopwords.add(text)

	wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask, stopwords=stopwords)

	# generate word cloud
	wc.generate(text)

	# store to file
	wc.to_file(path.join(d, "mask.png"))

	# show
	plt.imshow(wc)
	plt.axis("off")
	plt.figure()
	plt.imshow(alice_mask, cmap=plt.cm.gray)
	plt.axis("off")
	plt.show()

main()
