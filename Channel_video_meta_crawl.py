import requests
import csv
import codecs

class Video(object):
    def __init__(self, input_file, api_key):
        self.input_file = input_file
        self.api_key = api_key

    def video_crawl(self):

        with open(self.input_file) as channel_id_file:
            with codecs.open('/home/praveen/Working_files/Category_works/Category_channel_meta.csv', 'w', encoding='utf-8') as output_file:
                csv_writer = csv.writer(output_file)
                for cha_id in channel_id_file.readlines():
                    channel_id = cha_id.strip()
                    base_video_url = 'https://www.youtube.com/watch?v='
                    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
                    first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=50'.format(self.api_key, channel_id)
                    url = first_url
                    inp = requests.get(url)
                    resp = inp.json()
                    video_link = []
                    for i in resp['items']:
                        if i['id']['kind'] == 'youtube#video':
                            print(i['id']['videoId'])
                            video_link.append(i['id']['videoId'])

                        for video_id in video_link:
                            meta_list = []
                            url_video = "https://www.googleapis.com/youtube/v3/videos?part=id%2C+snippet&id={}&key={}".format(video_id, self.api_key)

                            inp1 = requests.get(url_video)  # requests on video meta api
                            video_resp = inp1.json()  # assign video api json to video_resp variable

                            for j in video_resp['items']:
                                if j['kind'] == 'youtube#video':  # checking kind is equal to given string
                                    if 'channelId' in j['snippet']:
                                        print(video_id, j['snippet']['channelId'])
                                        meta_list.append(j['snippet']['channelId'])  # append video belonging channel id
                                    else:
                                        meta_list.append("")
                                    print(video_id)
                                    meta_list.append(video_id)
                                    if 'channelTitle' in j['snippet']:
                                        print(video_id, j['snippet']['channelTitle'])
                                        meta_list.append(j['snippet']['channelTitle'])  # append video channel title in list
                                    else:
                                        meta_list.append("")
                                    if 'categoryId' in j['snippet']:
                                        print(video_id, j['snippet']['categoryId'])
                                        meta_list.append(j['snippet']['categoryId'])  # append video categoryId in list
                                    else:
                                        meta_list.append("")
                                    if 'title' in j['snippet']:
                                        print(video_id, j['snippet']['title'])
                                        meta_list.append(j['snippet']['title'])  # append video title in list
                                    else:
                                        meta_list.append("")
                                    if 'description' in j['snippet']:
                                        print(video_id, j['snippet']['description'])
                                        meta_list.append(j['snippet']['description'])  # append video description in list
                                    else:
                                        meta_list.append("")
                                    if 'tags' in j['snippet']:
                                        print(video_id, list(j['snippet']['tags']))
                                        meta_list.append(list(j['snippet']['tags']))  # append video tags in list
                                    else:
                                        meta_list.append("")
                                    if 'publishedAt' in j['snippet']:
                                        print(video_id, j['snippet']['publishedAt'])
                                        meta_list.append(j['snippet']['publishedAt'])  # append video published date
                                    else:
                                        meta_list.append("")
                            # Write video meta in csv file
                            csv_writer.writerow(meta_list)
                        video_link = []


obj = Video('/home/praveen/Working_files/Category_works/Category_channel_id_file.csv', 'AIzaSyC54MhoGU4G3XjIqeTFrmqhENNFPyCyXOk')
obj.video_crawl()
