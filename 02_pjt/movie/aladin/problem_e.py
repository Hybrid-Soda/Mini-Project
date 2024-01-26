import requests
from pprint import pprint


def ebook_list(title):

    # 검색을 두 번(제목으로 검색, 작품으로 검색) 해야 하므로 함수 선언
    def search_func(query, search_target):
        api_key = 'api_key'
        url = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
        params = {
            'ttbkey': api_key,
            'Query': query,
            'QueryType': 'Title',
            'MaxResults' : 5,
            'start' : 1,
            'SearchTarget' : search_target,
            'output' : 'js',
            'Version' : '20131101'
        }
        response = requests.get(url, params=params).json()
        return response

    # 종이서적 검색
    response = search_func(title, 'Book')

    # 검색 결과가 있다면 loop 진행
    if response['totalResults'] > 0:
        # 종이 서적의 판매가
        book_price = response['item'][0]['priceSales']
        # 전자 서적 검색
        new_response = search_func(title, 'eBook')
        ebook_info_list = []

        # 전자 서적 순회
        for item in new_response['item']:
            # 10 % 이상 저렴하다면 필요 정보 딕셔너리 생성
            if item['priceSales'] <= book_price * 0.9:
                ebook_info = {}
                ebook_info['isbn'] = item['isbn']
                ebook_info['itemId'] = item['itemId']
                ebook_info['link'] = item['link']
                ebook_info['priceSales'] = item['priceSales']
                ebook_info_list.append(ebook_info)
        return ebook_info_list
    # 검색 결과가 없다면 None 반환
    else:
        return None


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(ebook_list('베니스의 상인'))

    pprint(ebook_list('*'))
