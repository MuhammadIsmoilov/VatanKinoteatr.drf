from rest_framework.generics import RetrieveAPIView,ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from .models import Actor, Director, Genre, Rating, Movie,Payment
from .serializer import ActorSerializer, DirectorSerializer, GenreSerializer, RatingSerializer, MovieCreateSerializer,MovieSerializer,PaymentSerializer
from rest_framework.permissions import AllowAny, IsAdminUser,IsAuthenticated

# 1
class ActorApiView(ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [AllowAny]



class ActorDetailApiView(RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [AllowAny]



class ActorCreateApiView(CreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticated]


class ActorUpdateApiView(UpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticated]



class ActorDeleteApiView(DestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticated]


# 2


class DirectorApiView(ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [AllowAny]



class DirectorDetailApiView(RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [AllowAny]



class DirectorCreateApiView(CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]


class DirectorUpdateApiView(UpdateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]



class DirectorDeleteApiView(DestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]

# 3


class GenreApiView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]



class GenreDetailApiView(RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]



class GenreCreateApiView(CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]


class GenreUpdateApiView(UpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]



class GenreDeleteApiView(DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]

# 4


class MovieApiView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateSerializer
    permission_classes = [AllowAny]



class MovieDetailApiView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]



class MovieCreateApiView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]


class MovieUpdateApiView(UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]



class MovieDeleteApiView(DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]


# 5


class RatingApiView(ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [AllowAny]



class RatingDetailApiView(RetrieveAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [AllowAny]



class RatingCreateApiView(CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]


class RatingUpdateApiView(UpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]



class RatingDeleteApiView(DestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]


# 6


class PaymentApiView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [AllowAny]



class PaymentDetailApiView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [AllowAny]



class PaymentCreateApiView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class PaymentUpdateApiView(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]



class PaymentDeleteApiView(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]