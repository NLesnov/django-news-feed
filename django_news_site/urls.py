from django.contrib import admin
from django.urls import path, include

from news_feed.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('account/sign_up/', include('users.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('feed/', include('news_feed.urls')),
]
