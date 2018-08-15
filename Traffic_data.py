import request
import csv
import openpyxl
import codecs

class Collectin_traffic_data(object):

    def __init__(self, access_token):
        self.access_token = access_token


    def collect_video_traffic(self):
        with open("/home/praveen/Working_files/brand_auth_videos.csv") as brand_videos:

            for i in brand_videos.readlines():
                print(i.strip())


obj = Collectin_traffic_data('xecdecdedcd')
obj.collect_video_traffic()
