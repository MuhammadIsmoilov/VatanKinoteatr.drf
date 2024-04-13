from django.db import models
from django.urls import reverse

class Actor(models.Model):
    Gender = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )

    actor_fname = models.CharField(max_length=50)
    actor_lname = models.CharField(max_length=50)
    actor_gender = models.CharField(max_length=10,choices=Gender)
    

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"

    def __str__(self):
        return self.actor_fname + " " + self.actor_lname

    def get_absolute_url(self):
        return reverse("Actor_detail", kwargs={"pk": self.pk})
    


class Director(models.Model):
     
    director_fname = models.CharField(max_length=50)
    director_lname = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directors"

    def __str__(self):
        return self.director_fname + " " + self.director_lname

    def get_absolute_url(self):
        return reverse("Director_detail", kwargs={"pk": self.pk})


class Genre(models.Model):
    genre_name = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.genre_name

    def get_absolute_url(self):
        return reverse("Genre_detail", kwargs={"pk": self.pk})


class Rating(models.Model):
    number_of_rating = models.FloatField(max_length=5,default=0)

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"
    
    def __str__(self):
        return str(self.number_of_rating)
    
    def get_absolute_url(self):
        return reverse("Rating_detail", kwargs={"pk": self.pk})
    
class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    movie_img = models.ImageField(max_length=None, upload_to='images', default='/media')
    age_limit = models.CharField(max_length=5)
    movie_date = models.DateField(auto_now=False, auto_now_add=False)
    genre = models.ManyToManyField(Genre,related_name='movie')
    movie_year = models.CharField(max_length=5)
    movie_country = models.CharField(max_length=50)
    director = models.ManyToManyField(Director,related_name='movie')
    duration = models.DurationField()
    actor = models.ManyToManyField(Actor,related_name='movie')
    description = models.CharField(max_length=250)
    rating = models.ManyToManyField(Rating, related_name='movie')

    

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.movie_name

    def get_absolute_url(self):
        return reverse("Movie_detail", kwargs={"pk": self.pk})

    
class Payment(models.Model):
    Type = (
        ('CASH', 'CASH'),
        ('CARD', 'CARD'),
    )
    fname_lname_of_user = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField(max_length=13)
    type_of_payment = models.CharField(max_length=20,choices=Type)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return self.fname_lname_of_user

    def get_absolute_url(self):
        return reverse("Payment_detail", kwargs={"pk": self.pk})