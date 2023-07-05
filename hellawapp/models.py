from django import models


class Board(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#로그인
class Blog(models.Model):
    text = models.TextField()