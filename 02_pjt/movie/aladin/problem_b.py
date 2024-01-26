import requests
from pprint import pprint


def best_review_books():
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

    rank_up_to_9_list = []

    # response dict 내부의 'item' 키의 리스트 순회
    for item in response['item']:
        # 평점이 9점 이상이라면 리스트에 추가
        if item['customerReviewRank'] >= 9:
            rank_up_to_9_list.append(item)

    return rank_up_to_9_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(best_review_books())
