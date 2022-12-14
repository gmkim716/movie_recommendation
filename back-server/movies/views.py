from django.shortcuts import render
from rest_framework.decorators import api_view
# from django.http.response import JsonResponse 		# JsonResponse 불러오기
from .models import Movie, Review, Genre
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from .serializer import MovieListSerializer, ReviewSerializer, Movieserializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth import get_user_model

TMDB_API_KEY = "1894a2923867c8d04cf110591f18e4c0"

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_list(request):
	if request.method == 'GET':
		movies = get_list_or_404(Movie)
		serializer = MovieListSerializer(movies, many=True)
		return Response(serializer.data)

@api_view(['GET',])
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_detail(request, movie_pk):
	movie = get_object_or_404(Movie, pk=movie_pk)
	print(movie)
	if request.method == 'GET':
		serializer = Movieserializer(movie)
		return Response(serializer.data)

@api_view(['GET',])
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_genres(request, movie_pk):
	movie = get_object_or_404(Movie, pk=movie_pk)

	if request.method == 'GET':
		serializer = Movieserializer(movie)
		return Response(serializer.data)

@api_view(['GET',])
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_actors(request, movie_pk):
	movie = get_list_or_404(Movie, pk=movie_pk)

	if request.method == 'GET':
		serializer = Movieserializer(movie)
		return Response(serializer.data)


@api_view(['POST',])
@permission_classes([IsAuthenticated])
def like(request, movie_pk):					# 요청한 유저가 권한이 있을 때 (로그인 되어 있을 때)
	movie = get_object_or_404(Movie, pk=movie_pk)  # 영화 객체 선택
	user = get_object_or_404(get_user_model(), pk=request.user.pk)
	# 영화의 장르에 대해 좋아요 표기를 원한다면 
	# genres = movie.genres.all()				
    # for g in genres:
    #     genre = Genre.objects.get(pk=g.pk)
    #     genre.like_users.add(request.user)
	# is_liked 데이터 변화
	if movie.like_users.filter(pk=request.user.pk).exists():		# 요청한 유저의 pk가 영화를 좋아한 사람들의 pk에 존재할 때: 이미 좋아요를 누른 경우, 클릭
		movie.like_users.remove(request.user)
		user.like_movies.remove(movie_pk)
	else:										# 좋아요를 누른 적이 없는 유저가 좋아요를 누를 경우
		movie.like_users.add(request.user)
		user.like_movies.add(movie_pk)
	movie = get_object_or_404(Movie, pk=movie_pk)
	# serializer = Movieserializer(movie)
	return Response(movie.pk)

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def watched(request, movie_pk):					# 요청한 유저가 권한이 있을 때 (로그인 되어 있을 때)
	movie = get_object_or_404(Movie, pk=movie_pk)  # 영화 객체 선택
	user = get_object_or_404(get_user_model(), pk=request.user.pk)
	if movie.watched_users.filter(pk=request.user.pk).exists():		# 요청한 유저의 pk가 영화를 좋아한 사람들의 pk에 존재할 때: 이미 좋아요를 누른 경우, 클릭
		movie.watched_users.remove(request.user)
		user.watched_movies.remove(movie_pk)

	else:										# 시청 여부를 누른 적이 없는 유저가 좋아요를 누를 경우
		movie.watched_users.add(request.user)
		user.watched_movies.add(movie_pk)
	movie = get_object_or_404(Movie, pk=movie_pk)
	serializer = Movieserializer(movie)
	return Response(serializer.data)

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def bookmarked(request, movie_pk):					# 요청한 유저가 권한이 있을 때 (로그인 되어 있을 때)
	movie = get_object_or_404(Movie, pk=movie_pk)  # 영화 객체 선택
	user = get_object_or_404(get_user_model(), pk=request.user.pk)
	if movie.bookmarked_users.filter(pk=request.user.pk).exists():		# 요청한 유저의 pk가 영화를 좋아한 사람들의 pk에 존재할 때: 이미 좋아요를 누른 경우, 클릭
		movie.bookmarked_users.remove(request.user)
		user.bookmarked_movies.remove(movie_pk)
	else:										# 북마크를 누른 적이 없는 유저가 좋아요를 누를 경우
		movie.bookmarked_users.add(request.user)
		user.bookmarked_movies.add(movie_pk)
	movie = get_object_or_404(Movie, pk=movie_pk)
	serializer = Movieserializer(movie)
	return Response(serializer.data)



@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_reviews(request, movie_pk):
	if request.method == 'GET':
		reviews = get_list_or_404(Review.objects.order_by('-pk'))
		serializer = ReviewSerializer(reviews, many=True)
		return Response(serializer.data)
	else:
		movie = get_object_or_404(Movie, pk=movie_pk)
		serializer = ReviewSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save(movie=movie, user=request.user)
			return Response(serializer.data)


@api_view(['POST',])
@permission_classes([IsAuthenticated])
def like_review(request, review_pk):
	review = get_object_or_404(Review, pk=review_pk)
	if review.like_users.filter(pk=request.user.pk).exists():		# 요청한 유저의 pk가 영화를 좋아한 사람들의 pk에 존재할 때: 이미 좋아요를 누른 경우, 클릭
		review.like_users.remove(request.user)
	else:										
		review.like_users.add(request.user)
	context = {
		'pk':request.user.pk,
		'review_pk':review_pk,
		'like_user_count': review.like_users.count()
	}
	return Response(context)

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def hate_review(request, review_pk):
	review = get_object_or_404(Review, pk=review_pk)
	if review.hate_users.filter(pk=request.user.pk).exists():
		review.hate_users.remove(request.user)
	else:
		review.hate_users.add(request.user)
	context = {
		'pk': request.user.pk,
		'review_pk': review_pk,
		'hate_users_count': review.hate_users.count()
	}
	return Response(context)

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def delete_review(request, movie_id, review_id):
	review = get_object_or_404(Review, pk=review_id)
	review.delete()
	movie = get_object_or_404(Movie, pk=movie_id)
	serializer = Movieserializer(movie)
	return Response(serializer.data)

# 검색어 입력시 아래에 나오는 목록 
@api_view(['GET',])
@permission_classes([IsAuthenticatedOrReadOnly])
def search(request, query):
	movies = Movie.objects.filter(title__startswith=query)
	serializer = MovieListSerializer(movies, many=True)
	return Response(serializer.data)

# 검색어 입력 후 엔터
@api_view(['GET',])
@permission_classes([IsAuthenticatedOrReadOnly])
def searchEnter(request, query):
	movies = Movie.objects.filter(title__contains=query)
	serializer = MovieListSerializer(movies, many=True)
	return Response(serializer.data)

	