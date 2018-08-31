from . import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Voter
        fields = ('name', 'mail', 'password', 'unique_code')


class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Candidate
        fields = ('name', 'party_symbol')
