from django.http import Http404
from rest_framework.views import APIView

from api.models import Voter
from api.serializers import UserSerializer

from rest_framework import status
from rest_framework.response import Response


class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        voters = Voter.objects.all()
        serializer = UserSerializer(voters, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    def get_object(self, pk):
        try:
            return Voter.objects.get(pk=pk)
        except Voter.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        voter = self.get_object(pk)
        serializer = UserSerializer(voter)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        voter = self.get_object(pk)
        serializer = UserSerializer(voter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        voter = self.get_object(pk)
        voter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

