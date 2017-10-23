import sys
from urllib.request import Request, urlopen
from datetime import *
import json


try:
    # url = 'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&key=AIzaSyBJe_ZQsSPD6R6X05fg_R6gZIif4Q-XttI&part=snippet&maxResults=10'
    # url = 'GET https://www.googleapis.com/youtube/v3/search'
    url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=UUKBGEFVPKHC5U_TfaSaHLgA&key=AIzaSyDFKSzOm9u58L71SE8PlFmS3aGf6CPXf-k'
    url = 'https://www.googleapis.com/youtube/v3/search?part=id&channelId=UCOmHUn--16B90oW2L6FRR3A&key=AIzaSyBJe_ZQsSPD6R6X05fg_R6gZIif4Q-XttI&maxResults=50'

    '''
    part = snippet # api 응답은 중첩된 속성도 모두 포함합니다.
    forMine = true // 지정한 콘텐츠 소유자가 소유한 리소스만 검색하도록 검색을 제한 
    
    eventType=completed
    maxResults=50 ( 0~50 )
    order=relevance
    q=검색어
    regionCode= ISO3166-1 alpha-2
    safeSearch=none
    topicID=Freebase 주제ID 
    
    '''

    request = Request(url)
    resp = urlopen(request)

    resp_body = resp.read().decode('utf-8')
    json_result = json.loads(resp_body)
    print(json_result, type(json_result))


    # items = json_result.get('items')
    # print(items, type(items))
    #
    # videos = items.get('id')
    # print(videos)

    items = json_result['items']
    print(items)

    video_result = []
    for item in items:
        video_info = item.get('id')
        video_Id = video_info.get('videoId')
        video_result.append(video_Id)

    print(video_result)

except Exception as e:
    print('%s : %s' % (e, datetime.now()), file=sys.stderr)