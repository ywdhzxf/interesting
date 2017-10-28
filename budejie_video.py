#coding:utf8
import requests
import re

#获取当前页的所有视频地址
def parse(url):
    html = requests.get(url)
    html = html.content
    pattern = re.compile(r'data-mp4="(.*?)"')
    video_list = pattern.findall(html)
    print video_list
    return video_list

#下载视频
def video_down(video_list):
    a = 1
    for video_url in video_list:
        response = requests.get(video_url)
        if response.status_code == 200:
            fname = video_url.split('/')[-1]
            print response.url
            with open('./budejie/'+fname,'wb') as f:
                f.write(response.content)
                print '下载完成%d' % a
                a += 1
        else:
            pass

if __name__ == '__main__':
    base_url = 'http://www.budejie.com/%d'
    page = int(raw_input('请输入下载几页视频'))+1
    for x in range(1,page):
        print x
        url = base_url % x
        res = parse(url)
        video_down(res)
        print '下载完成%d页' % x
