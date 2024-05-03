from rest_framework.decorators import api_view
from django.http import JsonResponse
import pandas as pd


test_data = pd.read_csv('static/data/test_data.csv', encoding='cp949')
test_data_has_null = pd.read_csv('static/data/test_data_has_null.csv', encoding='cp949')

data_frame = pd.DataFrame(test_data)
df_has_null = pd.DataFrame(test_data_has_null)

# A. CSV 데이터를 DataFrame 으로 변환 후 반환
@api_view(['GET'])
def change_to_dataframe(request):
    df_dict = data_frame.to_dict('records')
    context = {
      'df_dict': df_dict
    }
    return JsonResponse(context)

# B. 결측치 처리 후 데이터 반환
@api_view(['GET'])
def processing_missing_value(request):
    # 결측치를 NULL로 변환
    df_dict = df_has_null.fillna('NULL').to_dict('records')
    context = {
      'df_dict': df_dict
    }
    return JsonResponse(context)

# C. 알고리즘 구현하기 (평균 나이와 가장 비슷한 10명)
# @api_view(['GET'])
# def calculate_avg_age(request):
#     # 결측치를 제거하고 나이 평균 계산
#     mean_age = df_has_null['나이'].mean()
#     # 나이 차이의 절대값을 계산하는 새로운 열 추가
#     df_has_null['나이 차이'] = df_has_null['나이'].apply(lambda x: abs(x - mean_age) if pd.notnull(x) else None)
#     # 나이 차이를 기준으로 정렬, 가장 작은 차이를 가진 상위 10개 행을 선택
#     closest_ages = df_has_null.sort_values(by='나이 차이').head(10)
#     # 딕셔너리 형태로 변환
#     df_dict = closest_ages.drop('나이 차이', axis=1).to_dict('records')
#     context = {
#       'df_dict': df_dict
#     }
#     return JsonResponse(context)

@api_view(['GET'])
def calculate_avg_age(request):
    avg_age = df_has_null['나이'].mean()

    df_has_null['나이_차이'] = abs(df_has_null['나이'] - avg_age)

    df_sorted = df_has_null.sort_values(by='나이_차이')

    similar_data = df_sorted.head(10).drop(columns='나이_차이')
    data = similar_data.to_dict('records')
    
    context = {
        'data': data,
    }
    return JsonResponse(context)