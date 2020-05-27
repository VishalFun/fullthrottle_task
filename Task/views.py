from rest_framework import viewsets
from . import models
from . import serializer
from django.http import JsonResponse




class UserView(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserSerializer

class ActivityPeriodView(viewsets.ModelViewSet):
    serializer_class = serializer.ActivityPeriodSerializer
    queryset = models.ActivityPeriod.objects.all()

class UserActivityDataView(viewsets.ModelViewSet):
    serializer_class = serializer.UserActivitySerializer
    queryset = models.User.objects.all()
