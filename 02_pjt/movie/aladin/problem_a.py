import requests


def author_works():
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
    
    title_list = []

    # response dict 내부의 'item' 키의 리스트 순회
    for item in response['item']:
        # 리스트 내부의 item들의 딕셔너리 속 'title'에 관한 값을 title_list 에 추가
        title_list.append(item['title'])

    return title_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(author_works())
