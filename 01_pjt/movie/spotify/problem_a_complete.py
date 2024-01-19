import json
from pprint import pprint


# 새로운 딕셔너리를 함수 내부에서 만든 후 키-값 추가 마지막으로 리턴
def artist_info(artist):
    new_dict = {}
    new_dict['genres_ids'] = artist['genres_ids']
    new_dict['id'] = artist['id']
    new_dict['images'] = artist['images']
    new_dict['name'] = artist['name']
    new_dict['type'] = artist['type']
    return new_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    pprint(artist_info(artist_dict))
