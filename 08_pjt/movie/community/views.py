from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import (
    require_safe,
    require_POST,
    require_http_methods,
)
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.http import JsonResponse


# 전체 리뷰 목록 페이지 조회
@require_safe
def index(request):
    reviews = Review.objects.order_by("-pk")
    context = {
        "reviews": reviews,
    }
    return render(request, "community/index.html", context)


# 새로운 리뷰 생성 페이지 조회 & 단일 리뷰 데이터 저장
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("community:detail", review.pk)
    else:
        form = ReviewForm()
    context = {
        "form": form,
    }
    return render(request, "community/create.html", context)


# 단일 리뷰 상세 페이지 조회
@require_safe
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        "review": review,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "community/detail.html", context)


# 단일 댓글 데이터 저장
@require_POST
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect("community:detail", review.pk)
    context = {
        "comment_form": comment_form,
        "review": review,
        "comments": review.comment_set.all(),
    }
    return render(request, "community/detail.html", context)


# 단일 리뷰 좋아요 기능
@login_required
def like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user in review.like_users.all():
        review.like_users.remove(request.user)
        is_liked = False
    else:
        review.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
        'likes_count': review.like_users.count(),
    }
    return JsonResponse(context)

