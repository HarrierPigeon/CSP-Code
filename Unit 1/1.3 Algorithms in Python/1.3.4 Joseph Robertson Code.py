from __future__ import print_function # use Python 3.0 printing
import random
import pandas as pd
import decimal as deci

  
  
#######

# Joseph Robertson
# 1.3.4 Code

##############
## PART ONE

  

def food_id(food):
	''' Returns categorization of food
	LOL DOCSTRINGS
	food is a string
	returns a string of categories
	'''
	# The data
	fruits = ['apple', 'banana', 'orange']
	citrus = ['orange']
	starchy = ['banana', 'potato']

	# Check the category and report
	if food in fruits:
		if food in citrus:
			return 'Citrus, Fruit'
		else:
			return 'NOT Citrus, Fruit'
		else:
			if food in starchy:
				return 'Starchy, NOT Fruit'
			else:
				return 'NOT Starchy, NOT Fruit'

def food_id_test():
	''' Unit test for food_id
	DOCSTRINGS ARE TEXT STRINGS IN DOCS. NEWSFLASH.
	returns True if good, returns False and prints error if not
	good
	'''
	works = True
	if food_id('orange') != 'Citrus, Fruit':
		works = False
		print('orange bug in food id()')
	if food_id('banana') != 'NOT Citrus, Fruit':
		works = False
		print('banana bug in food_id()')
	# Add tests so that all lines of code are visited during test
	if works:
		print('food_id passed all tests')
		return works

def fofx(x):
	if int(x) != x:
		print(x, 'is not an integer')
	elif (x % 2) == 0:
		if x == 0:
			print(x,'is even') # Zero is not a multiple of six, but is even.
		elif (x % 3) != 0:
			print(x,'is even.')
		else:
			print(x,'is a multiple of six.')
		else:
			print(x,'is odd')

############

# PART TWO

  

def guess_once():
	secret = random.randint(1, 4)
	print('I have a number between 1 and 4.')
	guess = int(raw_input('Guess: '))
	if guess != secret:
		highorlow = ""
		if guess > secret:
			highorlow = 'high,'
		else:
			highorlow = 'low,'
			print('Too',highorlow,'my number was',secret)
		else:
			print('Right, my number is', guess, end='!\n')

  

########

# Quiz_Decimal

  

def randomDecimalInRange(low,high,numberofdecimalpoints, DEBUG = True, EXTENDED_DEBUG = False):

	'''low as Decimal, high as Decimal ,numberofdecimalpoints as integer, optional DEBUG as boolean default = True, optional EXTENDED_DEGUG as boolean, default = False'''
	saniLow = pd.to_numeric(low)
	saniHigh = pd.to_numeric(high)
	randIntegerer = float(random.random())
	granularity = 10**numberofdecimalpoints

	'''
	Granularity is the number of decimal points turned into a power of ten.
	This was written because I didn't want to spend the time finding someone else's function, and I know how to do it.
	'''
	randDec = (float(int(saniLow+((saniHigh-saniLow)*randIntegerer)*granularity))/granularity)
	### Debug Stream
	if EXTENDED_DEBUG == True:
			print("saniLow:",saniLow," saniHigh:",saniHigh," randInt:",randIntegerer,"number of decimal points:",numberofdecimalpoints)
			print("granularity:",granularity)
			print("random decimal:",randDec)
	elif DEBUG == True:
		print(randDec)
	return randDec
 

def quiz_decimal(low,high,decimalplacestoguess = 2, DEBUG = True, EXTENDED_DEBUG = False, CHEATER_MODE = False):
	'''
	quiz_decimal(low,high,decimalplacestoguess = 2, DEBUG = True, EXTENDED_DEBUG = False, CHEATER_MODE = False)
	lowest bound, highest bound, number of decimal places to guess, give debugging information, give way too much information, gives answer before prompt.
	dec, dec, dec, bool, bool.
	'''
	#Sanitizing inputs, because I don't like it when people break my stuff.

	saniLow = pd.to_numeric(low)
	saniHigh = pd.to_numeric(high)
	saniDigits = int(pd.to_numeric(decimalplacestoguess))

	secretDec = randomDecimalInRange(saniLow,saniHigh,saniDigits,DEBUG,EXTENDED_DEBUG) #Is a decimal / float.
	### Add guessing code.

	# *Definitely* just for debugging. :)
	if CHEATER_MODE == True:
		print(secretDec)

	unSaniInput = raw_input('Guess: ')
	saniInput = pd.to_numeric(unSaniInput)

	if (saniInput == secretDec):
		print("You won!")
		return True
	else:
		highorlow = ""
		if (saniInput > secretDec):
			highorlow = "high."
		else:
			highorlow = "low."
		print("too",highorlow,"The number was",secretDec,"and you guessed",saniInput)
		return False

	### DEBUGGING TOOLS
	if EXTENDED_DEBUG = True:
		print("lower bound:",saniLow,"Upper Bound",saniHigh,"Secret:",secretDec)
		print("Range:",(saniHigh-saniLow))
	elif DEBUG = True:
		print("")
	