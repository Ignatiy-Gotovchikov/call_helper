from django.urls import path, include
from rest_framework.routers import DefaultRouter

from organizations.views import dicts

router = DefaultRouter()

router.register(r'dicts/positions', dicts.PositionView, 'req')

urlpatterns = [

]

urlpatterns += path('organizations/', include(router.urls)),