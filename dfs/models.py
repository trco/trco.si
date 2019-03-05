from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=16, null=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    # string fields
    title = models.CharField(max_length=64, null=True)
    imdb_link = models.URLField(null=True)
    # number field
    imdb_rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    # boolean field
    parents_guide = models.BooleanField(default=False, null=True)
    # date field
    release_date = models.DateField(null=True)
    # relationship fields
    director = models.ForeignKey(Director, null=True, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
