"""
    팔로워가 5,000,000이상, 10,000,000미만인 아티스트들을 
    아티스트 이름과 팔로워를 목록으로 출력하기
"""

import json
from pprint import pprint


def get_popular():
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    famous_artists = []

    # artists.json의 artist의 id를 이용해 파일 순회
    for i in range(len(artists_list)):
        id = artists_list[i]['id']
        id_json = open(f"data/artists/{id}.json", encoding="utf-8")
        artist_info = json.load(id_json)
        follower = artist_info['followers']['total']

        # 팔로워수가 500만명 이상, 1000만명 이하일때 if문 실행
        if 5000000 <= follower and follower <= 10000000:
            new_dict = {}
            new_dict['followers'] = artist_info['followers']['total']
            new_dict['name'] = artist_info['name']
            famous_artists.append(new_dict)
            
    return famous_artists


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(get_popular())
