from django.db import models

class Website(models.Model):
    first_service_detail = models.TextField()
    second_service_detail = models.TextField()
    third_service_detail = models.TextField()
    website_name = models.CharField(max_length=20, default="Say my name")
    has_won = models.CharField(default="lets play some TICTACTOE", max_length=40)
    round = models.IntegerField(default=1)

    def __str__(self):
        return self.website_name