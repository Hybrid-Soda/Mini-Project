# base64 :텍스트 <-> 이진 데이터 변환 모듈
# io : 입출력 연산을 위한 Python 표준 라이브러리
# BytesIO : 이진 데이터를 다루기 위한 버퍼 제공
import base64
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt
from django.shortcuts import render

# 그래프 처리
def export_pic():
    # BytesIO 객체를 생성하고, buffer라는 변수에 할당
    buffer = BytesIO()
    # buffer에 그래프를 png 형태로 저장
    plt.savefig(buffer, format='png')
    # buffer의 내용을 인코딩
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()
    return img_base64

# 데이터 읽어오기
def problem1(request):
    df = pd.DataFrame(pd.read_csv('static/weathers/austin_weather.csv'))
    df_html = df.to_html(index=False)
    context = {
        'df_html': df_html,
    }
    return render(request, "weathers/problem1.html", context)

# 일 별 온도 비교
def problem2(request):
    # CSV 파일 읽기 - DataFrame으로 변환
    df = pd.DataFrame(pd.read_csv('static/weathers/austin_weather.csv'))
    # 'Date' 열을 날짜 형식으로 변환
    df['Date'] = pd.to_datetime(df['Date'])

    # 그래프에 데이터 입력
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['TempHighF'], label='High Temperature')
    plt.plot(df['Date'], df['TempAvgF'], label='Average Temperature')
    plt.plot(df['Date'], df['TempLowF'], label='Low Temperature')

    # 그래프 출력 조정
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.grid(True)
    plt.legend()

    context = {
        'image': f'data:image/png;base64, {export_pic()}',
    }
    return render(request, "weathers/problem2.html", context)

# 월 별 온도 비교
def problem3(request):
    # CSV 파일 읽기 (필요한 데이터만 들여옴)
    df = pd.read_csv('static/weathers/austin_weather.csv', usecols=['Date', 'TempHighF', 'TempAvgF', 'TempLowF'])
    # DataFrame으로 변환
    df = pd.DataFrame(df)
    # 'Date' 열을 날짜 형식으로 변환
    df['Date'] = pd.to_datetime(df['Date'])
    # 년-월을 고려하여 월별 데이터 그룹화
    month_group = df.groupby([df['Date'].dt.year, df['Date'].dt.month]).mean()

    # 그래프에 데이터 입력
    plt.figure(figsize=(10, 6))
    plt.plot(month_group['Date'], month_group['TempHighF'], label='High Temperature')
    plt.plot(month_group['Date'], month_group['TempAvgF'], label='Average Temperature')
    plt.plot(month_group['Date'], month_group['TempLowF'], label='Low Temperature')

    # 그래프 출력 조정
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.grid(True)
    plt.legend()

    context = {
        'image': f'data:image/png;base64, {export_pic()}',
    }
    return render(request, "weathers/problem3.html", context)

# 날씨 이벤트
def problem4(request):
    from collections import Counter
    # CSV 파일 읽기 (필요한 데이터만 들여옴)
    df = pd.DataFrame(pd.read_csv('static/weathers/austin_weather.csv', usecols=['Events']))
    # 각 이벤트를 분리하고 카운트
    event_counts = Counter()
    # 빈 리스트 초기화
    events_list = []

    # 이벤트 이름 정제
    for event_group in df['Events'].dropna():
        # 각 행을 쉼표로 분리
        split_events = event_group.split(',')

        # 생성된 리스트의 각 원소에 대해 공백 제거
        cleaned_events = [event.strip() if event.strip() else 'No Events' for event in split_events]

        # 공백이 제거된 이벤트 이름들을 cleaned_events_list에 추가
        events_list.append(cleaned_events)

    # events_list 내의 각 이벤트에 대해 카운트 수행
    for event_group in events_list:
        for event in event_group:
            event_counts[event] += 1
    
    # 내림차순 정렬
    event_counts = dict(sorted(event_counts.items(), key=lambda item: -item[1]))

    # 히스토그램 데이터 준비
    events = list(event_counts.keys())
    counts = list(event_counts.values())

    # 히스토그램에 데이터 입력
    plt.figure(figsize=(10, 6))
    plt.bar(events, counts)

    # 그래프 출력 조정
    plt.title('Event Counts')
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.grid(True)

    context = {
        'image': f'data:image/png;base64, {export_pic()}',
    }
    return render(request, "weathers/problem4.html", context)
