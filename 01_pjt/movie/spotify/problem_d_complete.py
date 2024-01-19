import json


def max_polularity(artists):
    popularity_list = []

    # artists.json의 artist의 id를 이용해 파일 순회
    for i in range(len(artists)):
        id = artists[i]['id']
        id_json = open(f"data/artists/{id}.json", encoding="utf-8")
        artist_info = json.load(id_json)
        popularity_list.append(artist_info['popularity'])

    # 가장 인기도가 높은 수치의 인덱스를 이용해 artists.json에서 이름을 역추적
    max_value = max(popularity_list)
    famous_artist = artists[popularity_list.index(max_value)]['name']

    return famous_artist


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    print(max_polularity(artists_list))
