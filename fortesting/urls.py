from django.contrib import admin
from django.urls import path, include
from seri.views import TestView
from rest_framework.routers import DefaultRouter

from tranmodel.views import *



router = DefaultRouter()
router.register('person', PersonViewSet, basename='person')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('test/', TestView.as_view()),
    path("stripe/", include("djstripe.urls", namespace="djstripe")),
    
    path('', include(router.urls)),
]
