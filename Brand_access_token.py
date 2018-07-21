import requests
import csv
import codecs

with open("/home/praveen/Working_files/example.csv") as brand_refresh_token:
    with codecs.open("/home/praveen/Working_files/brand_access_token1.csv", "w", encoding="utf-8") as file_access_token:
        access_list = []
        csv_writer = csv.writer(file_access_token)
        try:
            for token in brand_refresh_token.readlines():
                refresh_token = token.split(",")
                channel_id = refresh_token[0].strip()
                print(channel_id)
                access_list.append(channel_id)
                re_token = refresh_token[1].strip()
                print(re_token)
                access_list.append(re_token)
                channel_title = refresh_token[2].strip()
                access_list.append(channel_title)
                print(channel_title)

                url = "https://accounts.google.com/o/oauth2/token"

                data = {"client_id": "137114246433-14si7cbn2vsunrekk4oaismk6cn1agh8.apps.googleusercontent.com",
                        "client_secret": "WPqviHZ1Jtu6Fx5fAiefryQ6",
                        "refresh_token": re_token, "grant_type": "refresh_token"}

                inp = requests.post(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
                print(inp.status_code)

                resp = inp.json()
                if "access_token" in resp:
                    print(resp['access_token'])
                    access_list.append(resp['access_token'])

                else:
                    access_list.append("")
                csv_writer.writerow(access_list)
                access_list = []
        except Exception as e:
            print(e)


