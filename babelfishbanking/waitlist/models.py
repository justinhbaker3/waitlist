from django.db import models
from django.db.models import Q
from django.utils import timezone

class Waiter(models.Model):
    username = models.CharField(max_length=200)
    referrer = models.ForeignKey('self', on_delete=models.RESTRICT, blank=True, null=True)
    signup_date = models.DateTimeField('signup_date')
    score = models.IntegerField(default=0)
    waiting = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    def create(username, referrer=None):
        return Waiter(
            username=username,
            referrer=referrer,
            signup_date=timezone.now(),
        )

    def rank(self):
        rank = Waiter.objects.filter(
            Q(waiting=True) &
            (
                Q(score__gt=self.score) |
                Q(score=self.score, signup_date__lte=self.signup_date)
            ),
            ).count()
        return rank

    def increment_score(self):
        self.score += 1
        