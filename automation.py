from selenium import webdriver
from time import sleep
import os

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
        bot.get("http://localhost/login/index.php")
        sleep(3)

        # Send name and password and press on login:
        bot.find_element_by_name("username").send_keys(self.username)

        bot.find_element_by_name("password").send_keys(self.password)
        bot.find_element_by_xpath( #ok xpath
            '//*[@id="loginbtn"]'
        ).click()
        sleep(3)


bot = MoodleBot("admin", "Shani1998#")
bot.login()