import csv
import requests
import re
import codecs

class Social_account(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def social_media_crawl(self):
        with open(self.input_file) as channel_id_file:
            with codecs.open('/home/praveen/Working_files/Social_media_works/Indian_channel_social_profile1.csv', 'w', encoding='utf-8') as output_file:
                csv_writer = csv.writer(output_file)
                try:
                    for cha_id in channel_id_file.readlines():
                        data_list = []
                        channel_id = cha_id.strip()
                        data_list.append(channel_id)
                        url = "https://www.youtube.com/channel/{}/about".format(channel_id)
                        inp = requests.get(url)
                        resp = inp.text

                        emailRegex = r"\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,4}\\b"
                        facebookRegex = r"http[s]?:\/\/[www.]*[facebook]*.com\/[A-z 0-9 _]+\/?"
                        twitterRegex = r"http[s]?:\/\/[www.]*[twitter]*.com\/[A-z 0-9 _]+\/?"
                        instagramRegex = r"http[s]?:\/\/[www.]*[instagram]*.com\/[A-z 0-9 _]+\/?"

                        email_compile = re.compile(emailRegex)
                        email_search = email_compile.findall(resp)
                        print(email_search)
                        data_list.append(email_search)

                        facebook_compile = re.compile(facebookRegex)
                        facebook_search = facebook_compile.findall(resp)
                        print(facebook_search)
                        data_list.append(facebook_search)

                        twitter_compile = re.compile(twitterRegex)
                        twitter_search = twitter_compile.findall(resp)
                        print(twitter_search)
                        data_list.append(twitter_search)

                        instagram_compile = re.compile(instagramRegex)
                        instagram_search = instagram_compile.findall(resp)
                        print(instagram_search)
                        data_list.append(instagram_search)

                        csv_writer.writerow(data_list)
                except Exception as e:
                    print(e)


obj = Social_account('/home/praveen/Working_files/Social_media_works/Indian_channel_id_file.csv')
obj.social_media_crawl()
