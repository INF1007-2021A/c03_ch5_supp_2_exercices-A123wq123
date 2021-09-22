#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	number = 0
	for character in text:
		if character.isalnum():
			number += 1
		else:
			continue
	print(number)
	return (number)

get_num_letters("nommbre de charactère alpha numérique")

def get_word_length_histogram(text):
	length = 0
	histo=[0]

	for character in text:

		if character.isalnum():
			length += 1

		elif character == " ":

			try:
				histo[length]+=1

			except:
				for i in range(length - histo.index(histo[-1])):
					histo.append(0)
				histo[length]+=1

			length = 0

		else:

			continue

	return histo

def format_histogram(histogram):
	ROW_CHAR = "*"

	return ""

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	return ""


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
