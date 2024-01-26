import requests
from pprint import pprint


def bestseller_book():
    api_key = 'api_key'
    url = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    params = {
        'ttbkey': api_key,
        'Query': '파울로 코엘료',
        'QueryType': 'Author',
        'MaxResults' : 20,
        'start' : 1,
        'SearchTarget' : 'Book',
        'output' : 'js',
        'Version' : '20131101'
    }
    response = requests.get(url, params=params).json()

    top_5_sales_list = []

    # sorted() 사용하여 salespoint 기준으로 내림차순 정렬
    sorted_list = sorted(response['item'], key=lambda item: item['salesPoint'], reverse = True)

    # sorted_list 순회하며 item 5개만 추가
    for i in range(5):
            top_5_sales_list.append(sorted_list[i]['title'])

    return top_5_sales_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(bestseller_book())
