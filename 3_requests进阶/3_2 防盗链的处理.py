# -*- coding: utf-8 -*-
"""
1.拿到contId
2.拿到videostatus返回的json -> srcURL
3.修正内容
4.下载视频
作者：高振涵
日期：2022-09-12
"""
import requests


url = 'https://www.pearvideo.com/video_1032551'
contId = url.split("_")[-1]

vediostatus_url = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.5921952217590689'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
    # 防盗链：
    'Referer': url
}
resp = requests.get(vediostatus_url,headers=headers)
dic = resp.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']

# https://video.pearvideo.com/mp4/short/20170210/cont-1032551-10190652-hd.mp4   aim
# https://video.pearvideo.com/mp4/short/20170210/1662969714764-10190652-hd.mp4      now

srcUrl = srcUrl.replace(systemTime, f'cont-{contId}')

# 下载视频
with open('try.mp4','wb')as fin:
    fin.write(requests.get(srcUrl).content)

resp.close()