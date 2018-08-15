import requests
import csv
import codecs

class Category_classfication(object):

    def __init__(self, input_file):
        self.input_file = input_file

    def category_api_data_crawl(self):
        with open(self.input_file) as video_meta_file:
            csv_reader = csv.reader(video_meta_file)
            with codecs.open('/home/praveen/Working_files/Test.csv', 'w', encoding='utf-8') as output_file:
                csv_writer = csv.writer(output_file)
                for row in csv_reader:
                    api_resp_list = []
                    video_id = str(row[1]).strip()
                    print(video_id)
                    api_resp_list.append(video_id)
                    video_title = str(row[4]).strip()
                    print(video_title)
                    api_resp_list.append(video_title)
                    video_description = str(row[5]).strip()
                    print(video_description)
                    api_resp_list.append(video_description)
                    video_tags = str(row[6]).strip()
                    print(video_tags)
                    api_resp_list.append(video_tags)

                    api_description = video_title + video_description + video_tags
                    data = {'description': api_description}
                    try:
                        url = 'http://ds.vidooly.com/genre/p'
                        inp = requests.post(url, data=data)
                        print(inp.status_code)
                        resp = inp.json()

                        if 'result' in resp:
                            print(resp['result'])
                            print(resp['status'])
                            api_resp_list.append(resp['result'])
                    except Exception as e:
                        print(e)
                    csv_writer.writerow(api_resp_list)


obj = Category_classfication('/home/praveen/Working_files/example.csv')
obj.category_api_data_crawl()
