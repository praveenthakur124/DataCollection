from selenium import webdriver
import csv
import codecs
import re
from time import sleep
import random
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys

class Facebook_data(object):

    def __init__(self, facebook_info_file):
        self.facebook_info_file = facebook_info_file

    def facebook_ads_crawl(self):
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com/")
        sleep(5)
        driver.find_element_by_xpath('//*[@id="email"]').send_keys("praveengharwar@gmail.com")
        driver.find_element_by_xpath('//*[@id="pass"]').send_keys("whatisthis")
        driver.find_element_by_id("loginbutton").click()
        sleep(10)
        file_list = []
        with open(self.facebook_info_file) as facebook_user_file:
            with codecs.open("/home/praveen/Working_files/Facebook_works/facebook_ads_id_file3.csv", "w", encoding="utf-8") as Facebook_info_file:
                csv_writer = csv.writer(Facebook_info_file)
                # count = 1
                for facebook_page in facebook_user_file.readlines():
                    facebook_page_id = facebook_page.strip()
                    print(facebook_page_id)
                    file_list.append(facebook_page_id)
                    '''count = count + 1s
                    if count % 20 == 0:
                        time.sleep(900)'''
                    url = "https://www.facebook.com/pg/{}/ads/".format(facebook_page_id)
                    driver.get(url)
                    sleep(random.randint(6, 15))
                    page_src = driver.page_source
                    #regex_video_id = r'/video_path[":/A-z0-9]+(\d+)/g'
                    regex_video_id = r'video_path[":"]+.[\/A-z0-9]+.[\/a-z]+.[\/\d]+'
                    compile_regex = re.compile(regex_video_id)
                    regex_search = compile_regex.findall(page_src)
                    #print(regex_search)
                    for i in regex_search:
                        ad_url = str(i)
                        ad_id = ad_url.split("/")
                        video_ad_id = ad_id[3]
                        print(video_ad_id)
                        file_list.append(video_ad_id)
                    #file_list.append(regex_search)
                    csv_writer.writerow(file_list)
                    file_list = []

        driver.quit()


obj = Facebook_data("/home/praveen/Working_files/Facebook_works/facebook_info_file.csv")
obj.facebook_ads_crawl()


