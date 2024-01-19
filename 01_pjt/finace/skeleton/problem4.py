import pprint
import requests


def get_deposit_products():
    api_key = "api_key"
    url = "http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?"
    params = {
        "auth": api_key,
        "topFinGrpNo": '020000',
        "pageNo": 1,
    }
    response = requests.get(url, params=params).json()

    prdt_list = response['result']['baseList'] # 상품 리스트
    opt_list = response['result']['optionList'] # 옵션 리스트
    new_list = []

    idx2 = 0
    for idx in range(len(prdt_list)):
        new_dict = {}
        new_dict['금리정보'] = []

        # for문 이용 시 탐색 시간이 길어져 while문으로 끊어서 탐색하도록 작성
        # 조건은 옵션리스트에서 상품 코드와 상품리스트에서 상품 코드가 같은지 파악
        # 이 때 index는 while문이 끝나도 유지시키기 위해 상위 for문 밖에서 선언
        while idx2 < len(opt_list) and opt_list[idx2]['fin_prdt_cd'] == prdt_list[idx]['fin_prdt_cd']:
            new2_dict = {}
            new2_dict['저축 금리'] = opt_list[idx2]['intr_rate']
            new2_dict['저축 기간'] = opt_list[idx2]['save_trm']
            new2_dict['저축금리유형'] = opt_list[idx2]['intr_rate_type']
            new2_dict['저축금리유형명'] = opt_list[idx2]['intr_rate_type_nm']
            new2_dict['최고 우대금리'] = opt_list[idx2]['intr_rate2']
            new_dict['금리정보'].append(new2_dict)
            idx2 += 1
        
        new_dict['금융회사명'] = prdt_list[idx]['kor_co_nm']
        new_dict['금융상품명'] = prdt_list[idx]['fin_prdt_nm']

        new_list.append(new_dict)

    return new_list


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)
