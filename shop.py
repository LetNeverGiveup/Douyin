import json

import requests

get_url = 'http://124.223.166.207:8185/dy/4aLRJG5U4cenNeVO/{}'


def get_shop(product_id):
    response = requests.get(get_url.format(product_id))

    if response.status_code == 200:
        json_data = json.loads(response.text)
        if json_data['state'] == '201':
            return get_shop(product_id)
        else:
            return json_data


if __name__ == '__main__':
    # 商品ID
    """
    3673831496810102867
    3673804416789643365
    3673804348288270377
    3673804090556678305
    3673804023816913093
    """
    product_id = '3673831496810102867'
    result = get_shop(product_id)
    print(result)