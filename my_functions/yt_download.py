## video class
class video_class:
    '''
    To handle Video Metadata and download comments.
    '''

    instances = []
    def __init__(self, title : str, artist : str, year : int, video_id : str, status : int = None, genre : str = "default"):
        self.__class__.instances.append(self)

        self.title = title
        self.artist = artist
        self.year = year
        self.video_id = video_id
        self.status = status
        self.genre = genre
        self.id_name = f"{self.artist}-{self.title}"

    def __str__(self):
        return self.id_name
    
    def  __repr__(self):
        return self.id_name
        
    def get_comments(self, dev_key : str, len_output : int, order : str ="relevance"):
        print(f"*Beginning to download aprox. {len_output} comments in order of {order}, from {self.title}")        
        
        lst = download_comments(dev_key, self.video_id, order, len_output)
        
        print(f"{len(lst)} comments were extracted")
        
        xi = []
        for t in lst:
            t = t + (self.id_name, self.status)
            xi.append(t)
        df = pd.DataFrame(xi, columns =['author', 'comment', "origin", 'origin_status'])
        return df
    

## download_comments
import os
import googleapiclient
from googleapiclient.discovery import build
import pandas as pd
import time
import json


def download_comments(DEVELOPER_KEY, video_id, order="relevance", max_lenght_output=100):
    #config
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    youtube_api = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)
    #config 2 (preparation)
    is_first_page = True
    data_lst = []
    next_page_token = ''
    sleep = 0 #increase, if download-limit is reached to fast

    # main loop
    while is_first_page or next_page_token and len(data_lst) < max_lenght_output-1:
        time.sleep(sleep)
        print("MAIN LOOOP")

        #get page
        page = youtube_api.commentThreads().list(
            part="snippet",
            maxResults=100,
            videoId=video_id,
            textFormat="plainText",
            #is there a next page? If yes, get token:
            pageToken=next_page_token,
            order=order    #<- "time" or "relevance" (not the same as TOP-Comments on YT, but similar)
        ).execute()
                
        #get data from page into list
        page_list = []
        for item in page["items"]:
            comment = item["snippet"]["topLevelComment"]
            author = comment["snippet"]["authorDisplayName"]
            text = comment["snippet"]["textOriginal"]
            #print("Comment by {}: {}".format(author, text))
            item = (author, text)
            page_list.append(item)

        #combine data from all pages
        data_lst += page_list
        
        #get next page and repeat
        next_page_token = page.get('nextPageToken')
        is_first_page = False
        print(f"Status = {len(data_lst)}/{max_lenght_output}")
        print(10 * "-")
        
        if next_page_token == None:
            print("Function could not more comments, no next_page_token")
            return data_lst

    return data_lst