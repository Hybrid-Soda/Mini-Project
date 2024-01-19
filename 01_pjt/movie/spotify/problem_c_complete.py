import json
from pprint import pprint


def artist_info(artists, genres):
    new_list = []
    
    # list 내부에 append할 dict를 만들기 위한 for문
    for dict1 in artists:
        new_dict = {}
        new_dict['genres_names'] = []

        # ids의 id를 통해 name을 매칭하기 위한 for문
        for dict2 in genres:
            if dict2['id'] in dict1['genres_ids']:
                new_dict['genres_names'].append(dict2['name'])

        # artists의 요소 새로운 딕셔너리에 추가
        new_dict['id'] = dict1['id']
        new_dict['images'] = dict1['images']
        new_dict['name'] = dict1['name']
        new_dict['type'] = dict1['type']
        new_list.append(new_dict)
    
    return new_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
