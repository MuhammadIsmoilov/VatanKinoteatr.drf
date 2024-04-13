from rest_framework import serializers
from .models import Actor, Director, Genre, Rating, Movie,Payment


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"



class MovieCreateSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many = True)
    director = serializers.StringRelatedField(many = True)
    actor = serializers.StringRelatedField(many = True)
    rating = serializers.StringRelatedField(many = True)
    class Meta:
        model = Movie
        fields = ['movie_name','movie_img','age_limit','movie_date','genre','movie_year','movie_country','director','duration','actor','descrition','rating']



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'