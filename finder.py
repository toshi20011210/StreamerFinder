from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import os

if os.path.exists("names.txt"):
    os.remove("names.txt")

############ tracker.gg input ##################
# example = 'https://tracker.gg/valorant/match/bbf4d713-48de-4380-ae9b-50401b55fce9'
input = ''
################################################

names = []
texts = []

driver = webdriver.Chrome('./chromedriver')
driver.get(input)
time.sleep(4)
names = driver.find_elements(By.CLASS_NAME, 'trn-ign__username')
for i in range (0, len(names)): 
    with open('names.txt', 'a') as f:
        f.write(names[i].text + '\n')

f = open('names.txt', 'r')
data = f.read()
texts = data.split('\n')

#for i in range (0, len(texts)):
#    print(texts[i])

#youtube
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://www.youtube.com/')
time.sleep(2)

for i in range (0, len(texts)):
    search = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
    search.clear()
    search.send_keys(texts[i])
    search.send_keys(Keys.ENTER)
    time.sleep(3)

#twitch
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[2])
driver.get('https://www.twitch.tv/')
time.sleep(2)
for i in range (0, len(texts)):
    search = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/nav/div/div[2]/div/div/div/div/div[1]/div/div/div/div/input')
    search.send_keys(Keys.CONTROL + "a")
    search.send_keys(Keys.DELETE)
    search.send_keys(Keys.COMMAND + "a")
    search.send_keys(Keys.DELETE)
    search.send_keys(texts[i])
    search.send_keys(Keys.ENTER)    
    time.sleep(3)

driver.quit()
