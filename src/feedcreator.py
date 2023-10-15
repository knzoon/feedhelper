import json
from datetime import datetime
import time
import feedRepository
import turfapi

def readfeed():
    connection = feedRepository.getConnection()
    feeedReadInfo = feedRepository.getLatestReadInfo(connection)
    lastTime, lastZoneId, lastHighestOrder = feeedReadInfo

    feed = turfapi.fetchFeedFromDateOrderedLastFirst(lastTime)
    nrofFeedItems = len(feed)
    print("Number of feed items", nrofFeedItems)

    for feedItem in feed:
        lastHighestOrder += 1
        takeoverTime = datetime.strptime(feedItem["time"], "%Y-%m-%dT%H:%M:%S+0000")
        zoneId = feedItem["zone"]["id"]
        feedRepository.insertTakever(connection, lastHighestOrder, takeoverTime, json.dumps(feedItem, ensure_ascii=False))

    feedRepository.updateLatestReadInfo(connection, takeoverTime, zoneId, lastHighestOrder)
    connection.commit()
    connection.close()

def feedcreator(): 
    while True:
        readfeed()
        time.sleep(60)
        
if __name__ == '__main__':
    feedcreator()

