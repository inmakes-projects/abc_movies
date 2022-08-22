from django.db import models

# Create your models here.

class Movie(models.Model):

    MOVIE_GENRE = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Crime and mystery', 'Crime and mystery'),
        ('Fantasy', 'Fantasy'),
        ('Historical', 'Historical'),
        ('Romance', 'Romance'),
        ('Satire', 'Satire'),
        ('Science fiction', 'Science fiction'),
        ('Thriller', 'Thriller'),
        ('Western', 'Western'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=200)
    desc = models.TextField()
    release_year = models.IntegerField()
    poster = models.ImageField(upload_to='movies')
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    actors = models.TextField()
    genre = models.TextField(choices=MOVIE_GENRE) 

    def __str__(self):
        return self.name
    
