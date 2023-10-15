import requests
import urllib.parse
import json

def fetchFeedFromDateOrderedLastFirst(lastDatetime):
    datetimeString = lastDatetime.strftime("%Y-%m-%dT%H:%M:%S+0000")
    encodedRequestStr = 'https://api.turfgame.com/unstable/feeds/takeover?afterDate=' + urllib.parse.quote(datetimeString)
    response = requests.get(encodedRequestStr)
    #feedFromApi = json.loads(response.text, encoding='utf-8')
    feedFromApi = response.json()
    sortedFeed = sorted(feedFromApi, key=lambda fi: fi["time"])
    return sortedFeed


    