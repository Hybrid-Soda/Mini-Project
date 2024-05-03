from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_safe
from .models import Movie, Genre
from django.http import JsonResponse


# 전체 영화 목록 페이지 조회
@require_safe
def index(request):
    genres = get_list_or_404(Genre)
    movies = get_list_or_404(Movie)
    context = {
        'genres': genres,
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


# 필터링 된 영화 데이터 제공
def filter_genre(request):
    genre_id = request.GET['genreId']
    movies = get_list_or_404(Movie, genres__id=genre_id)
    data = [{'title': movie.title} for movie in movies]
    return JsonResponse(data, safe=False)

# 영화 추천 페이지 조회
@require_safe
def recommended(request):
    # 콘텐츠 기반 필터링
    # 영화의 'overview', 'genres 메타데이터를 분석하여 사용자가 과거에 평가한 영화와 비슷한 영화를 추천

    # 인기도 기반 필터링
    # 'popularity', 'vote_average'를 활용하여 가장 인기 있는, 또는 평점이 높은 영화를 추천

    # 데모그래픽 필터링
    # 사용자의 인구통계학적 정보(예: 연령, 성별 등)를 사용하여 특정 그룹에게 인기 있는 영화를 추천
    pass
