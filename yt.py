from selenium import webdriver
import random
import time

driver = webdriver.Chrome('/Users/waranthornchansawang/Downloads/chromedriver')

video_list = ['https://youtu.be/IFTWNgU-lWY']

for i in range(1000):
    print('Running the video for {} time'.format(i))
    driver.get(video_list[0])
    sleeptime = random.randint(90, 100)
    time.sleep(sleeptime)

driver.quit()