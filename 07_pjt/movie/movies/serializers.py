from rest_framework import serializers
from .models import Actor, Movie, Review


# 전체 배우 목록 제공
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

# 단일 배우 정보 제공
class ActorSerializer(serializers.ModelSerializer):
    class MovieDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movie = MovieDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('id', 'name', 'movie')

# 전체 영화 목록 제공
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview')

# 단일 영화 목록 제공
class MovieSerializer(serializers.ModelSerializer):
    class ActorDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    class ReviewDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'content')

    actor = ActorDetailSerializer(many=True, read_only=True)
    review_set = ReviewDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'actor', 'review_set', 'title', 'overview', 'release_date', 'poster_path')

# 전체 리뷰 목록 제공
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content')
        read_only_fields = ('movie',)

#  단일 리뷰 목록 제공
class ReviewSerializer(serializers.ModelSerializer):
    class MovieDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movie = MovieDetailSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'movie', 'title', 'content')