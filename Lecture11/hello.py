#!/usr/bin/python3

print("Hello World")
def hello(tone="foobar"):
	'''
	The hello function says "Hello world.", but only if asked politely!
	'''
	polite=["please","kindly"]
	rude=["foobar"]
	politoken=False
	rudoken=False
	if tone in polite:
		politoken=True
		print("Yes of course. Hello world.")
	elif tone in rude:
		rudoken=True
		print("Try again.")
	else:
		print("Huh?")
