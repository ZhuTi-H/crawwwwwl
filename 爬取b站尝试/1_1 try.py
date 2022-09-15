# -*- coding: utf-8 -*-
"""
作者：高振涵
日期：2022-09-12
"""
# import requests
#
#
#
# vedio_url = 'https://cn-sh-fx-01-01.bilivideo.com/upgcxcode/94/29/828222994/828222994-1-30077.m4s?e=ig8euxZM2rNcNbdl' \
#             'hoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_' \
#             'g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1663061' \
#             '450&gen=playurlv2&os=bcache&oi=3030957307&trid=0000698b81b089094d7182bceab7ab02a129u&mid=412710361&plat' \
#             'form=pc&upsig=39916026392a3dc047bca410f5114f14&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&' \
#             'cdnid=3740&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=231521&logo=80000000'
#
# audio_url = 'https://cn-sh-fx-01-06.bilivideo.com/upgcxcode/94/29/828222994/828222994_nb3-1-30232.m4s?e=ig8euxZ' \
#             'M2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8B' \
#             'TrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&n' \
#             'bs=1&deadline=1663061450&gen=playurlv2&os=bcache&oi=3030957307&trid=0000698b81b089094d7182bceab7ab' \
#             '02a129u&mid=412710361&platform=pc&upsig=99315b4b39ee751a1b66606d67768f7d&uparams=e,uipk,nbs,deadl' \
#             'ine,gen,os,oi,trid,mid,platform&cdnid=3745&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=16632&logo=80000000'
#
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
#     'referer': 'https://www.bilibili.com/video/BV1Ud4y1X7VV?spm_id_from=333.1007.tianma.2-2-5.click&vd_source=67c8f89b8798b291350a302084137062'
# }
#
# resp1 = requests.get(audio_url, headers=headers)
# resp2 = requests.get(vedio_url, headers=headers)
#
# data_audio = resp1.content
# data_vedio = resp2.content
#
# with open('csgo_audio.mp4', 'wb')as fin:
#     fin.write(data_audio)
# with open('csgo_vedio.mp4', 'wb')as fin:
#     fin.write(data_vedio)
#
# os.system('ffmpeg -i "csgo_vedio.mp4" -i "csgo_audio.mp4" -c copy "csgo.mp4"')
#
# print('over!')
# resp1.close()
# resp2.close()


import requests
from lxml import etree
import re
import os

url = input("input the url:")
style_number = input("input the style(番剧：1 , 短视频：2 , 电影：3): ")

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
    'referer': 'https://search.bilibili.com/',
    'cookie': "buvid3=86E677D7-47EB-A6EC-5A67-061EE7DE1B3C88940infoc; i-wanna-go-back=-1; _uuid=210110109D7-7188-EB74-D13D-3984B87855C189120i"
              "nfoc; buvid4=1F6D457B-FEFE-0EE8-A61E-8BB34FB1B36492153-022061020-+D7oKDig4xwbeW2qqRLmUA%3D%3D; buvid_fp_plain=undefined; SESSD"
              "ATA=3476609d%2C1670427520%2Cc312d%2A61; bili_jct=eee2345f94d13237f67a1e61c3b9c1cb; DedeUserID=412710361; DedeUserID__ckMd5=321"
              "ca0b633cebc21; sid=jx34zfhz; buvid_fp=d9c9825b8ba8eae0f5426fef4bb64b4b; CURRENT_BLACKGAP=0; blackside_state=0; rpdid=|(m~lYYll"
              "||0J'uYlR)~llR|; LIVE_BUVID=AUTO2916548772318916; b_ut=5; nostalgia_conf=-1; fingerprint3=32b6cff0fe765c08da24f815425faa16; is"
              "-2022-channel=1; hit-dyn-v2=1; fingerprint=9571a7880b19e4ffff73e2b5da10424f; b_nut=100; CURRENT_QUALITY=80; bp_video_offset_412"
              "710361=703855881938272400; CURRENT_FNVAL=4048; b_lsid=55A96B55_18335DD9E86; PVID=2"
}

resp = requests.get(url, headers=headers)
style = int(style_number)

# if style == 1:
#     number_first = url.split('?')[0]
#     number_mid = number_first.split('/')[-1]
#     number_last = number_mid.split('p')[-1]

page_content = resp.text

# 转换类型
html_obj = etree.HTML(page_content)
title = html_obj.xpath('//title/text()')[0]

if style == 1 : title = re.findall(r'(.*?)-番剧', title)[0]   # 番剧
if style == 2 : title = re.findall(r'(.*?)_哔哩哔哩_bilibili', title)[0]     # 短视频
if style == 3 : title = re.findall(r'(.*?)-电影', title)[0]   # 电影

url_content = html_obj.xpath('//script[contains(text(),"window.__playinfo__")]/text()')

if style == 1: obj1 = re.compile(r'"video":.*?"backupUrl":\["(?P<video_url>.*?)","', re.S)  # 番剧
if style == 2: obj1 = re.compile(r'"video":.*?:"(?P<video_url>.*?)","base', re.S)     # 短视频
if style == 3: obj1 = re.compile(r'"video":.*?"backupUrl":\["(?P<video_url>.*?)","', re.S)  # 电影

result1 = obj1.finditer(page_content)
for it in result1:
    video_url = it.group('video_url')

if style == 1: obj2 = re.compile(r'"audio":.*?"backupUrl":\["(?P<audio_url>.*?)","', re.S)  # 番剧
if style == 2: obj2 = re.compile(r'"audio".*?:"(?P<audio_url>.*?)","base', re.S)   # 短视频
if style == 3: obj2 = re.compile(r'"audio":.*?"backupUrl":\["(?P<audio_url>.*?)","', re.S)  # 电影

result2 = obj2.finditer(page_content)
for it in result2:
    audio_url = it.group("audio_url")

resp1 = requests.get(audio_url, headers=headers)
resp2 = requests.get(video_url, headers=headers)

data_audio = resp1.content
data_video = resp2.content

title_new = title + 'no use'

with open(f'{title_new}.mp3', 'wb')as fin:
    fin.write(data_audio)
with open(f'{title_new}.mp4', 'wb')as fin:
    fin.write(data_video)


os.system(f'ffmpeg -i "{title_new}.mp4" -i "{title_new}.mp3" -c copy "{title}.mp4"')

os.remove(f'{title_new}.mp4')
os.remove(f'{title_new}.mp3')

print('over!')
resp.close()
resp1.close()
resp2.close()
# https://www.bilibili.com/video/BV1ZT4y1d7JM?p=45&spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=67c8f89b8798b291350a302084137062







