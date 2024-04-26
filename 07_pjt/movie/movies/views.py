from .serializers import ActorSerializer, MovieSerializer, ReviewSerializer
from .serializers import ActorListSerializer, MovieListSerializer, ReviewListSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Actor, Movie, Review
from rest_framework import status


# 전체 배우 목록 제공
@api_view(['GET'])
def actor_list(request):
    actors = get_list_or_404(Actor)
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)


# 단일 배우 정보 제공 (출연 영화 제목 포함)
@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)


# 전체 영화 목록 제공
@api_view(['GET'])
def movie_list(request):
    actors = get_list_or_404(Movie)
    serializer = MovieListSerializer(actors, many=True)
    return Response(serializer.data)


# 단일 영화 정보 제공 (출연 배우 이름과 리뷰 목록 포함)
@api_view(['GET'])
def movie_detail(request, movie_pk):
    actor = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(actor)
    return Response(serializer.data)


# 전체 리뷰 목록 제공
@api_view(['GET'])
def review_list(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


# 단일 리뷰 조회 & 수정 & 삭제 (출연 영화 제목 포함)
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 리뷰 생성
@api_view(['POST'])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)