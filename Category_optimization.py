import requests
import csv
import codecs

class Category_classfication(object):

    def __init__(self, input_file):
        self.input_file = input_file

    def category_api_data_crawl(self):
        with open(self.input_file) as video_meta_file:
            csv_reader = csv.reader(video_meta_file)
            with codecs.open('/home/praveen/Working_files/test.csv', 'w', encoding='utf-8') as output_file:
                for row in csv_reader:
                    video_id = str(row[1]).strip()
                    #print(video_id)
                    video_title = str(row[4]).strip()
                    #print(video_title)
                    video_description = str(row[5]).strip()
                    #print(video_description)
                    video_tags = str(row[6]).strip()
                    #print(video_tags)
                    try:
                        url = 'http://180.151.75.164:8080/ml_st/result/categories?description={}&{}&{}'.format(video_title, video_description, video_tags)
                        inp = requests.get(url)
                        resp = inp.json()
                        print(resp)
                    except Exception as e:
                        print(e)




obj = Category_classfication('/home/praveen/Working_files/example.csv')
obj.category_api_data_crawl()
