from django.shortcuts import render, redirect
from .forms import KeywordForm
from .models import Keyword, Trend

import matplotlib.pyplot as plt
from selenium import webdriver
from bs4 import BeautifulSoup
from io import BytesIO
import base64
import re


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


def keyword(request):
    keywords = Keyword.objects.all()
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trends:keyword')
    else:
        form = KeywordForm()
    context = {
        'keywords': keywords,
        'form': form,
    }
    return render(request, 'trends/keyword.html', context)


def keyword_detail(request, pk):
    if request.method == 'POST':
        keyword = Keyword.objects.get(pk=pk)
        keyword.delete()
    return redirect('trends:keyword')


def crawling(request):
    keywords = Keyword.objects.all()

    for keyword in keywords:
        url = f'https://www.google.com/search?q={keyword.name}'
        driver = webdriver.Chrome()
        driver.get(url)

        # 열린 페이지 소스 가져오기
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        result_stats = soup.select_one("#result-stats").get_text()

        # 숫자 부분만 추출
        number = int(re.findall(r'\d+', result_stats.replace(',', ''))[0])

        # 저장되어 있는 키워드라면 검색 결과 개수만 변경
        if Trend.objects.filter(name=keyword.name).exists():
            trend = Trend.objects.get(name=keyword.name, search_period='all')
            trend.result = number
            trend.save()
        # 저장되지 않은 키워드라면 새로 생성
        else:
            Trend.objects.create(name=keyword.name, result=number, search_period='all')

    trends = Trend.objects.filter(search_period='all')
    context = {
        'trends': trends,
    }
    return render(request, 'trends/crawling.html', context)


def crawling_histogram(request):
    # 데이터 준비
    trends = Trend.objects.all()
    name = [trend.name for trend in trends]
    result = [trend.result for trend in trends]

    # 히스토그램에 데이터 입력
    plt.figure(figsize=(10, 6))
    plt.bar(name, result, label="Trend")

    # 그래프 출력 조정
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()

    context = {
        'image': f'data:image/png;base64, {export_pic()}',
    }
    return render(request, 'trends/crawling_histogram.html', context)


def crawling_advanced(request):
    keywords = Keyword.objects.all()

    for keyword in keywords:
        url = f'https://www.google.com/search?q={keyword.name}&tbs=qdr:y'
        driver = webdriver.Chrome()
        driver.get(url)

        # 열린 페이지 소스 가져오기
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        result_stats = soup.select_one("#result-stats").get_text()

        # 숫자 부분만 추출
        number = int(re.findall(r'\d+', result_stats.replace(',', ''))[0])

        # 저장되어 있는 키워드라면 검색 결과 개수만 변경
        if Trend.objects.filter(name=keyword.name, search_period='year').exists():
            trend = Trend.objects.get(name=keyword.name, search_period='year')
            trend.result = number
            trend.save()
        # 저장되지 않은 키워드라면 새로 생성
        else:
            Trend.objects.create(name=keyword.name, result=number, search_period='year')

    # 데이터 준비
    trends = Trend.objects.filter(search_period='year')
    name = [trend.name for trend in trends]
    result = [trend.result for trend in trends]

    # 히스토그램에 데이터 입력
    plt.figure(figsize=(10, 6))
    plt.bar(name, result, label="Trend")

    # 그래프 출력 조정
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()

    context = {
        'image': f'data:image/png;base64, {export_pic()}',
    }
    return render(request, 'trends/crawling_advanced.html', context)


'''
# 데이터 크롤링 
url = 'https://quotes.toscrape.com/tag/love/'
response = requests.get(url)
html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')

# 1. find : 첫번째 태그를 가진 요소 검색
main = soup.find('title')
print(main)

# 2. find_all : 해당 태그를 가진 모든 요소 검색
# 리스트로 반환
test = soup.find_all('a')

# 3. CSS 선택자로 하나를 선택 - 선택자가 일치하는 첫 번째 글
# span 태그로도 검색이 가능하지만 인용구라는 내용은 text class로 지정
# 따라서 class를 통한 검색이 더 옳다
word = soup.select_one('.text')
# word = soup.select_one('span')
print(f'첫번째 글 = {word.text}')

# 4. CSS 선택자로 여러개를 선택
words = soup.select('.text')
for w in words: print(f'글 : {w.text}')
'''
'''
url = f'https://www.google.com/search?q={keyword.name}'
driver = webdriver.Chrome()
driver.get(url)

# 열린 페이지 소스 가져오기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
result_stats = soup.select_one("#result-stats")
print(result_stats)

print(soup.prettify())
with open("soup.txt", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
'''