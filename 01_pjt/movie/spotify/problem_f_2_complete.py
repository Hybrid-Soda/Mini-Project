"""
    장르에 acoustic이 포함된 아티스트 이름 목록 출력하기
"""

import json
from pprint import pprint


def acoustic_artists():
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    artist_acoustic = []

    # genres 리스트의 딕셔너리를 순회하다 ids가 맞는 값이 있으면 이름 추출
    for dict1 in artists_list:
        for dict2 in genres_list:
            if dict2['id'] in dict1['genres_ids'] and dict2['name'] == "acoustic":
                artist_acoustic.append(dict1['name'])
    return artist_acoustic

# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(acoustic_artists())
