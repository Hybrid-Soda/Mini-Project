import pprint
import requests


def get_deposit_products():
    api_key = "api_key"
    url = "http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json"
    params = {
        "auth": api_key,
        "topFinGrpNo": '020000',
        "pageNo": 1,
    }
    response = requests.get(url, params=params).json()
    prdt_list = response['result']['baseList']

    return prdt_list


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)