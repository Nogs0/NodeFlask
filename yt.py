from googleapiclient.discovery import build
from config import API_KEY

youtube = build('youtube', 'v3', developerKey=API_KEY)

def Get_Comments(video_id) -> list:
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText"
    )
    
    response = request.execute()
    
    while response:
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        
        if 'nextPageToken' in response:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                pageToken=response['nextPageToken'],
                textFormat="plainText"
            )
            response = request.execute()
        else:
            break
    
    return comments
