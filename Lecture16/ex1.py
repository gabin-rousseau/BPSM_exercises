#!/usr/bin/python3

survey={}

survey["name"]=input("What is your name?\n")
survey["age"]=input("How old are you?\n")
survey["colour"]=input("What is your favourite colour?\n")
survey["likepy"]=input("Do you like Python? (y/n)\n")
survey["flat"]=input("The world is flat: True or False?\n")

def comments(intel:dict):
	if "Z" in intel.get("name"):
		print(f"\n\n{intel.get('name')}? I don't believe that's really your name.")
	else:
		print("\n\nOK, I believe that is your name.")
	if int(intel.get("age"))> 19:
		print("You're old!")
	if intel.get("colour")=="orange":
		print("Hey, that's my favourite colour too!")
	if intel.get("likepy").lower()=="y":
		print("yay")
	elif intel.get("likepy").lower()=="n":
		print("nay")
	if intel.get("flat")=="True":
		print("Dummy!")

comments(survey)
