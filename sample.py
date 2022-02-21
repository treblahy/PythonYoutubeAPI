# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.update
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os 
import time
import requests
import json
import pickle
from pydoc import cli
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

class YTstats:
    def __init__(self):
        self.video_dislikes = 0
    def main(self):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secrets.json"

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        youtube = YTstats.get_authenticated_service()

        request = youtube.videos().update(
            part="snippet,status",
            body={
              "id": "lmEgZ7nmsBI",
              "snippet": {
                "categoryId": 22,
                "defaultLanguage": "en",
                "description": "yeeeeeeeeet",
                "tags": [],
                "title": time.ctime()
              },
              "status": {
                "privacyStatus": "public"
              }
            }
        )
        response = request.execute()
        print(response)

    def get_authenticated_service():

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secrets.json"

        if os.path.exists("credentials.json"):
            with open("credentials.json", 'rb') as f:
                credentials = pickle.load(f)
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
            credentials = flow.run_console()
            with open("credentials.json", 'wb') as f:
                pickle.dump(credentials, f)
        return googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

    def get_video_statistics(self):
            url = f'https://returnyoutubedislikeapi.com/votes?videoId=lmEgZ7nmsBI'
        
            json_url = requests.get(url)
            data = json.loads(json_url.text)
            try:
                data = data["dislikes"]
            except:
                data = None
            self.video_statistics = data
            return data

    def dump(self):
        channel_title = "treblaHY"
        channel_title = channel_title.replace(" ", "_").lower()
        file_name = channel_title + ".txt"
        with open (file_name, "w") as f:
            f.write("dislikes:" + str(self.video_dislikes))

        print("file dumped")

yt = YTstats()
yt.main()
yt.get_video_statistics()
yt.dump()