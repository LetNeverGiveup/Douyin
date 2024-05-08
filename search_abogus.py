import json
import urllib

import requests
from fake_useragent import UserAgent


url = 'http://124.223.166.207:80/ab/search'

ua = UserAgent().random
keywords = '上海'

params = {
    'device_platform': 'webapp',
    'aid': 6383,
    'channel': 'channel_pc_web',
    'search_channel': 'aweme_video_web',
    'enable_history': 1,
    'sort_type': 2,
    'publish_time': 0,
    'keyword': keywords,
    'search_source': 'tab_search',
    'query_correct_type': 1,
    'is_filter_search': 1,
    'offset': 0,
    'count': 20,
    'need_filter_settings': 1,
    'pc_client_type': 1,
    'version_code': '170400',
    'version_name': '17.4.0'
}

data = {
    'key': keywords,
    'ua': ua,
    'param': urllib.parse.urlencode(params)
}

headers = {
    "Referer": "https://www.douyin.com/search/{}?type=video".format(urllib.parse.quote(keywords, safe='')),
    "User-Agent": ua,
    "Cookie": "ttwid=1%7CtYAhi8uLyO22mV62abHWXP91MwL0mMuafJ6nb6GAFsI%7C1715139416%7Cad0636d8ce4f2224d9b71d1ad16c1672ba8b67430615a6f93a19482ce0dcebd5;"
}

response = requests.post(url, data=json.dumps(data), timeout=5)

if response.status_code == 200:
    json_data = json.loads(response.text)
    for key, value in json_data.items():
        params['a_bogus'] = value

        url = 'https://www.douyin.com/aweme/v1/web/search/item'
        response = requests.get(url, headers=headers, params=params, timeout=5)

        if response.status_code == 200:
            print(response.text)