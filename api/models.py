from django.db import models
from django.utils import timezone


class Voter(models.Model):
    name = models.CharField(max_length=20)
    mail = models.EmailField()
    password = models.CharField(max_length=50)
    unique_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=20)
    party_symbol = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Election(models.Model):
    titre = models.CharField(max_length=100)
    public_key = models.CharField(max_length=20)
    duration = models.DurationField()
    date = models.DateTimeField(default=timezone.now)
    voters = models.ManyToManyField(Voter, related_name='Elections', blank=True)
    candidates = models.ManyToManyField(Candidate, related_name='Elections', blank=True)

    def __str__(self):
        return self.titre


class Vote(models.Model):
    date = models.DateTimeField(default=timezone.now)
    voter = models.OneToOneField(Voter, on_delete=models.CASCADE)
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    election = models.OneToOneField(Election, on_delete=models.CASCADE)


class Result(models.Model):
    details = models.TextField()
    election = models.OneToOneField(Election, on_delete=models.CASCADE)

    def __str__(self):
        return self.details
