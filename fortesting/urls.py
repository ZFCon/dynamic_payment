from django.contrib import admin
from django.urls import path, include
from seri.views import TestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('test/', TestView.as_view()),
    path("stripe/", include("djstripe.urls", namespace="djstripe")),
]
