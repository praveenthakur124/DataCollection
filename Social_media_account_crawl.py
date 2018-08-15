import csv
import requests
import re
import codecs

class Social_account(object):

    def __init__(self, input_file):
        self.input_file = input_file

    def social_media_crawl(self):
        with open(self.input_file) as channel_id_file:
            with codecs.open('/home/praveen/Working_files/test.csv', 'w', encoding='utf-8') as output_file:
                csv_writer = csv.writer(output_file)
                try:
                    for cha_id in channel_id_file.readlines():
                        data_list = []
                        channel_id = cha_id.strip()
                        print(channel_id)
                        data_list.append(channel_id)
                        url = "https://www.youtube.com/channel/{}/about".format(channel_id)
                        inp = requests.get(url)
                        resp = inp.text

                        emailRegex = r"\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,4}\\b"
                        facebookRegex = r"http[s]?:\/\/[www.]*[facebook]*.com\/[A-z 0-9 _]+\/?"
                        twitterRegex = r"http[s]?:\/\/[www.]*[twitter]*.com\/[A-z 0-9 _]+\/?"
                        instagramRegex = r"http[s]?:\/\/[www.]*[instagram]*.com\/[A-z 0-9 _]+\/?"
                        # websiteRegex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+\/?'
                        # googlePlusRegex = r'https?:\/\/plus\.google\.com\/.\/.\/.[A-z0-9]+\/?'
                        linkedinRegex = r'http(s)?:\/\/([\w]+\.)?linkedin\.com\/in\/[A-z0-9\-]+\/?'
                        # pinterestRegex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+\/[A-z0-9]+\/?'

                        try:
                            email_compile = re.compile(emailRegex)
                            email_search = email_compile.findall(resp)[0]
                            print(email_search)
                            data_list.append(email_search)
                        except Exception as e1:
                            print(e1)
                            data_list.append(" ")

                        try:
                            facebook_compile = re.compile(facebookRegex)
                            facebook_search = facebook_compile.search(resp)[0]
                            print(facebook_search)
                            data_list.append(facebook_search)
                        except Exception as e2:
                            print(e2)
                            data_list.append(" ")

                        try:
                            twitter_compile = re.compile(twitterRegex)
                            twitter_search = twitter_compile.findall(resp)[0]
                            print(twitter_search)
                            data_list.append(twitter_search)
                        except Exception as e3:
                            print(e3)
                            data_list.append(" ")

                        try:
                            instagram_compile = re.compile(instagramRegex)
                            instagram_search = instagram_compile.findall(resp)[0]
                            print(instagram_search)
                            data_list.append(instagram_search)
                        except Exception as e4:
                            print(e4)
                            data_list.append(" ")

                        '''website_compile = re.compile(websiteRegex)
                        website_search = website_compile.findall(resp)
                        print(website_search)
                        data_list.append(website_search)

                        google_plus_compile = re.compile(googlePlusRegex)
                        google_plus_search = google_plus_compile.findall(resp)
                        print(google_plus_search)
                        data_list.append(google_plus_search)'''

                        try:
                            linkedin_compile = re.compile(linkedinRegex)
                            linkedin_search = linkedin_compile.findall(resp)[0]
                            print(linkedin_search)
                            data_list.append(linkedin_search)
                        except Exception as e5:
                            print(e5)
                            data_list.append(" ")

                        '''pinterest_compile = re.compile(pinterestRegex)
                        pinterest_search = pinterest_compile.findall(resp)
                        print(pinterest_search)
                        data_list.append(pinterest_search)'''

                        csv_writer.writerow(data_list)
                except Exception as e:
                    print(e)


obj = Social_account('/home/praveen/Working_files/example.csv')
obj.social_media_crawl()
