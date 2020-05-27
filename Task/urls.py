from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'UserActivityData',views.UserActivityDataView,basename='UserActivityData')
router.register(r'UserAdd',views.UserView, basename='UserAdd')
router.register(r'ActivityPeriod',views.ActivityPeriodView,basename='ActivityPeriod')

urlpatterns = [
    path('',include(router.urls)),
    ]
