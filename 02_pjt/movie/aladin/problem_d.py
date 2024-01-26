import requests
from pprint import pprint


def author_other_works(title):

    # 검색을 두 번(제목으로 검색, 작품으로 검색) 해야 하므로 함수 선언
    def search_func(query, query_type):
        api_key = 'api_key'
        url = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
        params = {
            'ttbkey': api_key,
            'Query': query,
            'QueryType': query_type,
            'MaxResults' : 5,
            'start' : 1,
            'SearchTarget' : 'Book',
            'output' : 'js',
            'Version' : '20131101'
        }
        response = requests.get(url, params=params).json()
        return response
    
    # 제목으로 검색
    response = search_func(title, 'Title')

    # 검색 결과가 있다면 loop 진행
    if response['totalResults'] > 0:
        # (지은이) 앞에서 잘라서 작가 이름만 추출
        author = response['item'][0]['author'].split('(')[0].strip()
        # 작가로 검색
        new_response = search_func(author, 'Author')
        search_list = []

        # 결과 리스트 순회하며 아이템 제목만 추출
        for item in new_response['item']:
            search_list.append(item['title'])
        return search_list
    # 검색 결과가 없다면 None 반환
    else:
        return None


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(author_other_works('베니스의 상인'))

    pprint(author_other_works('개미'))

    pprint(author_other_works('*'))
