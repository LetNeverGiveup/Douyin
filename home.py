import json
import requests
from fake_useragent import UserAgent


url = 'http://124.223.166.207:80/xb/home'

ua = UserAgent().random
param ='device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id={}&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1200&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=109.0.0.0&browser_online=true&engine_name=Blink&engine_version=109.0.0.0&os_name=Windows&os_version=10&cpu_core_num=4&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7303433435736639027&msToken=v8MvT8Xg5vvMAKjndmJWZUhG-2Qhz1DIhBnuEmmhCMPgPJSATPMZvjvK9h2Z4DukWpM40OkKnLqWrXeqU0fVGbEPV22iHUB8DRsi-XlrKFOVYHqShYA0txlbCWZd_5A='

uid = 'MS4wLjABAAAAzzmS2TgIEvxGftMpWD13Ty8k5HmsjlGsLJ1yBUEm2Ew'
data = {
    'uid': uid,
    'ua': ua,
    'param': param
}

headers = {
    "Referer": "https://www.douyin.com/user/{}",
    "User-Agent": ua,
    "Cookie": "s_v_web_id=verify_lp6jtw8q_ZRlgidAg_dyme_43Uq_A8LW_1ABBzH2mZiU9; __ac_nonce=0655b0210002170b5cb09; __ac_signature=_02B4Z6wo00f01m3wYxgAAIDDRno43VYp..5t0GeAAP42cc; ttwid=1%7CG50bROgzYQCYxuqnlj3CL7DmWRb0WT2z5JlTCsTy2mg%7C1700463120%7Cfafe4c99f5a63c11b10aa0a4accba77d3490c44d0d921a27095c979b5324b5a4; webcast_local_quality=null; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1200%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; msToken=v8MvT8Xg5vvMAKjndmJWZUhG-2Qhz1DIhBnuEmmhCMPgPJSATPMZvjvK9h2Z4DukWpM40OkKnLqWrXeqU0fVGbEPV22iHUB8DRsi-XlrKFOVYHqShYA0txlbCWZd_5A=; passport_csrf_token=4498641a2affc25cac672d7e4627d058; passport_csrf_token_default=4498641a2affc25cac672d7e4627d058; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; strategyABtestKey=%221700463125.773%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQitqNFFkckdleHJJQ0FWZGFkNkJxb2V5NVdOY1BIb004UDBjUExwaVE3MWIwd0VSWmkwY1M3T2ZoTVRVZnlpMXJJKytKNlAxanpOVyt3anF3TW5aSkk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; ttcid=26aacb2101ed444c89a26428d322b11e12; tt_scid=-Zcb4aK3BEMQNUh7JWYTXEOqmFoeHHBKAG93ZMzNPdQpN3OMTCOxTTRbc68W6VrNb3aa; msToken=WsxOpni__vKqgzXvy1PEF7eEOVHmKTvTYbzRvZjCNVtZOFYP3ZpV394TcDqncq3vZGdNeJmpy2ceIzm0aPS9nohcA3dDTsXnaHQYI0nI2xt775bRTvIcXQ4cke1cQsM=; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22"
}

response = requests.post(url, data=json.dumps(data), timeout=5)

if response.status_code == 200:
    print(response.text)
    json_data = json.loads(response.text)
    for key, value in json_data.items():
        url = 'https://www.douyin.com/aweme/v1/web/aweme/post/?'+param.format(key)+"&X-Bogus={}".format(value)

        headers['Referer'] = headers['Referer'].format(key)
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code == 200:
            print(response.text)
