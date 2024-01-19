import json
import pprint as prt


def dec_artists(artists):
    popular_artists = []

    # artists.json의 artist의 id를 이용해 파일 순회
    for i in range(len(artists)):
        id = artists[i]['id']
        id_json = open(f"data/artists/{id}.json", encoding="utf-8")
        artist_info = json.load(id_json)
        follower = artist_info['followers']['total']

        # 팔로워수가 1000만명 이상일때 if문 실행
        if follower >= 10000000:
            new_dict = {}
            new_dict['name'] = artist_info['name']
            # ':'를 기준으로 split하여 uri-id 추출
            new_dict['uri-id'] = artist_info['uri'].split(':')[2]
            popular_artists.append(new_dict)
            
    return popular_artists


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    prt.pprint(dec_artists(artists_list))
