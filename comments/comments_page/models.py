from django.db import models


class Review(models.Model): #Mobel for book reviews
    my_email = models.CharField(max_length=40)
    books_name = models.CharField(max_length=80)
    rating = models.IntegerField(default=1)
    comment = models.TextField(max_length=1000)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.books_name
