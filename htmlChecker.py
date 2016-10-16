#  File: htmlChecker.py
#  Description: checking html tags and print out the process
#  Student's Name: Thu Anh Le
#  Student's UT EID: tal864
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 10/18/2015
#  Date Last Modified: 10/19/2015

import re

class Stack:
	# List implementation of Stack
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def __str__(self):
		return '[' + ', '.join(self.items) + ']'

class Tag():

	def __init__ (self, data_file, tag_list):
		self.data_file = data_file
		self.tag_list = tag_list
		
	def getTag(self):
		line = self.data_file.readlines()
		exception = ''
		EXCEPTIONS = ['meta', 'br', 'hr', 'ul']

		for i in line:
			matches = re.findall('<.*?>', i)

			# regular html tags
			for tag in matches:

				for char in tag:
					if char == '<' or char == '>':
						tag = tag.replace(char,'')

				self.tag_list.append(tag)

		# Find exception cases and add it to the list
		for special_tag in EXCEPTIONS:

			for tag in self.tag_list:

				if special_tag in tag:
					# get location of the exception tag to be replaced
					loc = self.tag_list.index(tag) 
					# remove the original form of the special tag
					self.tag_list.remove(tag)
					# insert the special tag
					self.tag_list.insert(loc, special_tag)

		return self.tag_list		

	def processTag(self):
		tagStack = Stack()
		EXCEPTIONS = ['meta', 'br', 'hr', 'ul']

		for tag in self.tag_list:

			if tag[0] != '/' and tag not in EXCEPTIONS:
					tagStack.push(tag)
					print('Tag is ', tag, ': pushed: stack is now ',tagStack)

			elif tag[0] == '/' and tag not in EXCEPTIONS:

				if tagStack.peek() == tag[1:]:
					tagStack.pop()
					print('Tag is ', tag, ': matches: stack is now ', tagStack)

				else:
					print('Error:  tag is', tag, 'but top of stack is', tagStack.peek())
					break

		if tagStack.isEmpty():
			print('Processing complete.  No mismatches found.')

		else:
			print('Processing complete.  Unmatched tags remain on stack: ', tagStack)

def main():
	tag = []
	num = []
	# read data file htmlfile.txt
	data_file = open('htmlfile.txt', 'r')
	# create html object
	html = Tag(data_file, tag)
	# Print out the list of tags from the data file
	print(html.getTag())
	# Print out the process of the tags and whether they are valid
	html.processTag()
main()



