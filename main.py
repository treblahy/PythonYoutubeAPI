from turtle import update
from sample import main
from youtube_statistics import YTstats

API_KEY = "AIzaSyA6cgEuuJ0jpqvEFecyZuko3DM2EqvvCXk"
channel_id = "UCzIRxJYv0qY81cq1Ri-ylpA"
video_id = "sERW_Z2EO9U"
parts = ["snippet", "statistics", "contentDetails"]

client_id = "38484378170-1e8585s5evkh9s7m2vv1es0f47852svb.apps.googleusercontent.com"
client_secret = "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"

#yt = YTstats(API_KEY, channel_id, video_id)
#yt.get_channel_statistics()
#yt.get_video_statistics()
#yt.dump()
main()