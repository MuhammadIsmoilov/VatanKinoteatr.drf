from django.urls import path
from .views import (ActorApiView,ActorDetailApiView,ActorCreateApiView,ActorUpdateApiView,ActorDeleteApiView,
                    RatingApiView,RatingDetailApiView,RatingCreateApiView,RatingUpdateApiView,RatingDeleteApiView,
                    GenreApiView,GenreDetailApiView,GenreCreateApiView,GenreUpdateApiView,GenreDeleteApiView,
                    DirectorApiView,DirectorDetailApiView,DirectorCreateApiView,DirectorUpdateApiView,DirectorDeleteApiView,
                    MovieApiView,MovieDetailApiView,MovieCreateApiView,MovieUpdateApiView,MovieDeleteApiView,
                    PaymentApiView,PaymentCreateApiView,PaymentUpdateApiView,PaymentDetailApiView,PaymentDeleteApiView
                    )


urlpatterns = [
    path("actor-list/",ActorApiView.as_view(),),
    path("actor-detail/<int:pk>/",ActorDetailApiView.as_view(),),
    path("create-actor/",ActorCreateApiView.as_view(),),
    path("update-actor/<int:pk>/",ActorUpdateApiView.as_view(),),
    path("delete-actor/<int:pk>/",ActorDeleteApiView.as_view(),),


    path("rating-list/",RatingApiView.as_view(),),
    path("rating-detail/<int:pk>/",RatingDetailApiView.as_view(),),
    path("create-rating/",RatingCreateApiView.as_view(),),
    path("update-rating/<int:pk>/",RatingUpdateApiView.as_view(),),
    path("delete-rating/<int:pk>/",RatingDeleteApiView.as_view(),),


    path("director-list/",DirectorApiView.as_view(),),
    path("director-detail/<int:pk>/",DirectorDetailApiView.as_view(),),
    path("create-director/",DirectorCreateApiView.as_view(),),
    path("update-director/<int:pk>/",DirectorDetailApiView.as_view(),),
    path("delete-director/<int:pk>/",DirectorDeleteApiView.as_view(),),


    path("genre-list/",GenreApiView.as_view(),),
    path("genre-detail/<int:pk>/",GenreDetailApiView.as_view(),),
    path("create-genre/",GenreCreateApiView.as_view(),),
    path("update-genre/<int:pk>/",GenreUpdateApiView.as_view(),),
    path("delete-genre/<int:pk>/",GenreDeleteApiView.as_view(),),


    path("movie-list/",MovieApiView.as_view(),),
    path("movie-detail/<int:pk>/",MovieDetailApiView.as_view(),),
    path("create-movie/",MovieCreateApiView.as_view(),),
    path("update-movie/<int:pk>/",MovieUpdateApiView.as_view(),),
    path("delete-movie/<int:pk>/",MovieDeleteApiView.as_view(),),


    path("payment-list/",PaymentApiView.as_view(),),
    path("payment-detail/<int:pk>/",PaymentDetailApiView.as_view(),),
    path("create-payment/",PaymentCreateApiView.as_view(),),
    path("update-payment/<int:pk>/",PaymentUpdateApiView.as_view(),),
    path("delete-payment/<int:pk>/",PaymentDeleteApiView.as_view(),),
]
