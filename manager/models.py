from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = "Книги"

    title = models.CharField(
        max_length=50,
        verbose_name="название",
        help_text="ну это типо погоняло книги"
    )

    date = models.DateTimeField(null=True)
    description = models.TextField(null=True)
    authors = models.ManyToManyField(User)


    def __str__(self):
        return f"{self.id} ~ {self.title}"



class Comment(models.Model):

    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

