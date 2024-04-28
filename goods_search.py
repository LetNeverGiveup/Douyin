import requests

get_url = 'http://124.223.166.207/dys/4aLRJG5U4cenNeVO/{}/{}'

keywords = '夹克'     # 搜索商品关键词
page = 1             # 第几页

get_url = get_url.format(keywords, page)

response = requests.get(get_url)
if response.status_code == 200:
   print(response.text)
