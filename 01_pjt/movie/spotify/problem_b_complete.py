import json
from pprint import pprint


def artist_info(artist, genres):
    new_dict = {}
    new_dict['genres_names'] = []
    # genres 리스트의 딕셔너리를 순회하다 ids가 맞는 값이 있으면 이름 추출
    for dict in genres:
        if dict['id'] in artist['genres_ids']:
            new_dict['genres_names'].append(dict['name'])

    new_dict['id'] = artist['id']
    new_dict['images'] = artist['images']
    new_dict['name'] = artist['name']
    new_dict['type'] = artist['type']
    
    return new_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))
