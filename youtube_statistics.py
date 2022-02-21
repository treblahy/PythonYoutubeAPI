import requests
import json

class YTstats:

    def __init__(self, api_key, channel_id, video_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None
        self.video_id = video_id
        self.video_dislikes = 0

    def get_channel_statistics(self):
        url = f'https://www.googleapis.com/youtube/v3/channels/?part=statistics&id={self.channel_id}&key={self.api_key}'
        
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data["items"][0]["statistics"]
        except:
            data = None

        self.channel_statistics = data
        return data

    def get_video_statistics(self):
        url = f'https://returnyoutubedislikeapi.com/votes?videoId={self.video_id}'
        
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data["dislikes"]
        except:
            data = None

        self.video_statistics = data
        return data

    def dump(self):
        if self.channel_statistics is None:
            return

        channel_title = "treblaHY"
        channel_title = channel_title.replace(" ", "_").lower()
        file_name = channel_title + ".txt"
        with open (file_name, "w") as f:
            f.write("dislikes:" + str(self.video_dislikes))

        print("file dumped")