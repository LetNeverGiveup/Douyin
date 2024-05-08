import json
import urllib

import requests
from fake_useragent import UserAgent


url = 'http://124.223.166.207:80/ab/home'

ua = UserAgent().random
uid = 'MS4wLjABAAAAzzmS2TgIEvxGftMpWD13Ty8k5HmsjlGsLJ1yBUEm2Ew'

params = {
    'device_platform': 'webapp',
    'aid': 6383,
    'channel': 'channel_pc_web',
    'sec_user_id': uid,
    'max_cursor': 0,
    'locate_query': 'false',
    'show_live_replay_strategy': 1,
    'need_time_list': 1,
    'time_list_query': 0,
    'whale_cut_token': '',
    'cut_version': 1,
    'count': 18,
    'publish_video_strategy_type': 2,
    'pc_client_type': 1,
    'version_code': '290100',
    'version_name': '29.1.0'
}

data = {
    'uid': uid,
    'ua': ua,
    'param': urllib.parse.urlencode(params)
}

headers = {
    "Referer": "https://www.douyin.com/user/{}".format(uid),
    "User-Agent": ua,
    "Cookie": "s_v_web_id=verify_lp6jtw8q_ZRlgidAg_dyme_43Uq_A8LW_1ABBzH2mZiU9; ttwid=1%7CG50bROgzYQCYxuqnlj3CL7DmWRb0WT2z5JlTCsTy2mg%7C1700463120%7Cfafe4c99f5a63c11b10aa0a4accba77d3490c44d0d921a27095c979b5324b5a4; webcast_local_quality=null; passport_csrf_token=4498641a2affc25cac672d7e4627d058; passport_csrf_token_default=4498641a2affc25cac672d7e4627d058; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; strategyABtestKey=%221700463125.773%22; ttcid=26aacb2101ed444c89a26428d322b11e12; download_guide=%221%2F20231120%2F0%22; __ac_nonce=0655b2db20013f2c867de; __ac_signature=_02B4Z6wo00f01r2MLtgAAIDDlgZ1HaRgy069rCpAAMpEF3cfsO2JWYiVrsYzadstLPkMKo6kHd8lZNyXWvG-OWOm8SGpSVnHvFLi8N0AsvrVYSUJ8nzGRfRMipWmvMP6FYlGyH65DI8yu06Ja2; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQitqNFFkckdleHJJQ0FWZGFkNkJxb2V5NVdOY1BIb004UDBjUExwaVE3MWIwd0VSWmkwY1M3T2ZoTVRVZnlpMXJJKytKNlAxanpOVyt3anF3TW5aSkk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=RVJ5nNY-TmFqORWZEWgN7C-mYY0aW8xinAdmx0Plyuhzip45hC_arLsEjhkhjerFoGTCrgBLFrHe3S03cf9yiao_kSVmF0bRVxSFWsjtNeE7uXQEvim8xhiXADI7tbtPeg==; tt_scid=E9qoccsqk6KcPyM7SKQruu6HqB1qworOmdtr-2ZspF9eDlpDgwUlSD4hn52sIdStff92; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; msToken=PPrIM4D4h0kiIiJGKwsUzIDXL90saRbkntpmwm"
}

response = requests.post(url, data=json.dumps(data), timeout=5)

if response.status_code == 200:
    json_data = json.loads(response.text)
    for key, value in json_data.items():
        params['a_bogus'] = value

        url = 'https://www.douyin.com/aweme/v1/web/aweme/post'
        response = requests.get(url, headers=headers, params=params, timeout=5)

        if response.status_code == 200:
            print(response.text)