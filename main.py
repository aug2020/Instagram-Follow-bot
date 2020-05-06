from selenium import webdriver
from time import sleep
import instaloader
import htmldriver


class myInstaBot:
     def __init__(self, uname, pw, fname):
        self.driver = webdriver.Chrome()
        self.username = uname
        self.password = pw
        self.driver.get("https://instagram.com")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input ").send_keys(self.username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(self.password)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click() # this clicks on the not now for notifications
        sleep(2)
     def get_followers(self, fname, uname, pw): # a method to being following the accounts
        L = instaloader.Instaloader()
        L.login(uname, pw)
        L.save_session_to_file('session.txt')
        profile = instaloader.Profile.from_username(L.context, fname)


        for followee in profile.get_followers():
         self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(followee.username)
         sleep(2)
         self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a/div').click()
         sleep(4)
         self.driver.find_element_by_xpath("//*[text()='Follow']").click()
         sleep(2)

my_bot = myInstaBot('username', 'password', 'account to take followers name')
my_bot.get_followers('account to take followers name','username', 'password')




