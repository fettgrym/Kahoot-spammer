# Kahoot spammer

from selenium import webdriver
import random
import time

def kahoot(room):
	kahoot = 'https://kahoot.it/'
	# Kahoot URL

	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	# add options to the browser

	browser = webdriver.Chrome(options=options)
	browser.get(kahoot)
	time.sleep(0.5)
	# Setting up the browser and goes to kahoot

	room_num = browser.find_element_by_xpath('//*[@id="inputSession"]')
	room_num.send_keys(room)
	# Room input

	enter_click = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div/form/button')
	enter_click.click()
	# Room enter key

	time.sleep(0.7)
	kahoot_name = browser.find_element_by_xpath('//*[@id="username"]')
	kahoot_name.send_keys(name)
	# Username input

	kahoot_enter = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div/form/button')
	kahoot_enter.click()
	# Username enter

	time.sleep(1.3)
	browser.save_screenshot('debug.png')

num = random.randint(1, 1000)
flag = True

room = input('Kahoot room number: ')
name = input('Username: ')
name = name + str(num)

while True:
	kahoot(room)

browser.quit()