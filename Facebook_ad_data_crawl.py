from selenium import webdriver
import csv
import codecs
import re

class Facebook_data(object):
    def __init__(self,facebook_info_file):
        self.facebook_info_file = facebook_info_file

    def facebook_ads_crawl(self):
        driver = webdriver.Chrome()
        with open(self.facebook_info_file) as facebook_user_file:
            with codecs.open("/home/praveen/Working_files/test.csv", "w", encoding="utf-8") as Facebook_info_file:
                for facebook_page in facebook_user_file.readlines():
                    facebook_page_id = facebook_page.strip()
                    url = "https://www.facebook.com/pg/{}/ads/".format(facebook_page_id)
                    driver.get(url)
                    page_src = driver.page_source
                    page_text = page_src.text

                    regex_video_id = r'/video_path[":/A-z0-9]+(\d+)/g'
                    compile_regex = re.compile(regex_video_id)
                    regex_search = compile_regex.findall(page_text)
                    print(regex_search)


obj = Facebook_data("/home/praveen/Working_files/example.csv")
obj.facebook_ads_crawl()


