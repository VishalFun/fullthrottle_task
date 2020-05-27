from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ActivityPeriod
        fields = "__all__"

class APSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ActivityPeriod
        fields = ["start_time","end_time"]



class UserActivitySerializer(serializers.ModelSerializer):
    activity_periods = APSerializer(many=True,read_only=True)

    class Meta:
        model = models.User
        fields = ["id","real_name","tz","activity_periods"]


