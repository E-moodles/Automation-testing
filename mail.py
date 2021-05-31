import random
import string
from lib2to3.pgen2 import driver
from threading import Thread

import Arrays as Arrays
import driver as driver
import te as te
from selenium import webdriver
from time import sleep
import os

from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By

base_dir = os.getcwd() #our current path

def Path(relative_path):
    return os.path.join(base_dir, relative_path)


#init username and password
class MoodleBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(executable_path=Path("chromedriver.exe"))

    def login(self):
        bot = self.bot
        bot.get("https://accounts.google.com/signin/v2/identifier?hl=iw&continue=https%3A%2F%2Fmail.google.com%2Fmail&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession")
        sleep(1.5)

        # Send name and password and press on login:
        bot.find_element_by_name("identifier").send_keys(self.username)
        bot.find_element_by_xpath(  # next
            '//*[@id="identifierNext"]/div/button/span'
        ).click()
        sleep(3)
        bot.find_element_by_name("password").send_keys(self.password)
        bot.find_element_by_xpath( #ok xpath
            '//*[@id="passwordNext"]/div/button/span'
        ).click()
        sleep(3)


    def testCaseOne(self):
        #case number 1 - the user is enrolled to the course and send correct email:
        bot = self.bot
        sleep(7)
        bot.find_element_by_xpath('//*[@id=":3j"]/div/div').click()  # new mail
        sleep(1.5)
        bot.find_element_by_name("to").send_keys("emoodlesmessage+1.2@gmail.com")
        sleep(1.5)
        bot.find_element_by_name("subjectbox").send_keys(random.choice(string.ascii_letters))
        sleep(7)
        bot.find_element_by_xpath('//*[@id=":9u"]').send_keys(random.choice(string.ascii_letters))
        sleep(5)
        bot.find_element_by_xpath('//*[@id=":8f"]').click()  # send

        #should not return email back




        #check if the message in the forum








    def testCaseTwo(self):
        #case number 2 - the user send wrong email:
        bot = self.bot
        sleep(3)
        bot.find_element_by_xpath('//*[@id=":36"]/div/div').click()  # new mail
        sleep(1.5)
        bot.find_element_by_name("to").send_keys("emoodlesmessage.4@gmail.com")
        sleep(1.5)
        bot.find_element_by_name("subjectbox").send_keys(random.choice(string.ascii_letters))
        sleep(1.5)
        bot.find_element_by_xpath('//*[@id=":9h"]').send_keys(random.choice(string.ascii_letters))
        sleep(1.5)
        bot.find_element_by_xpath('//*[@id=":82"]').click()  # send


        #should return email back





    def testCaseThree(self):
        # case number 3 - the user isnt enrolled to the course and send email:
        bot = self.bot
        sleep(10)
        bot.find_element_by_xpath('//*[@id=":4m"]/div/div').click()  # new mail
        sleep(1.5)
        bot.find_element_by_name("to").send_keys("emoodlesmessage+1.3@gmail.com")
        sleep(1.5)
        bot.find_element_by_name("subjectbox").send_keys(random.choice(string.ascii_letters))
        sleep(7)
        bot.find_element_by_xpath('//*[@id=":b2"]').send_keys(random.choice(string.ascii_letters))
        sleep(5)
        bot.find_element_by_xpath('//*[@id=":7h"]/div[2]').click()  # send


        # should return email back





bot = MoodleBot("checkmoodle@gmail.com", "moodle123")
bot.login()
bot.testCaseThree()