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

    opt_list = response['result']['optionList']
    new_opt_list = []

    for idx in range(len(opt_list)):
        new_dict = {}
        new_dict['금융상품코드'] = opt_list[idx]['fin_prdt_cd']
        new_dict['저축 금리'] = opt_list[idx]['intr_rate']
        new_dict['저축 기간'] = opt_list[idx]['save_trm']
        new_dict['저축금리유형'] = opt_list[idx]['intr_rate_type']
        new_dict['저축금리유형명'] = opt_list[idx]['intr_rate_type_nm']
        new_dict['최고우대금리'] = opt_list[idx]['intr_rate2']
        new_opt_list.append(new_dict)

    return new_opt_list


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)
