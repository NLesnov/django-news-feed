
from rest_framework import routers
from .views import NewsFeedViewSet

news_post_router = routers.SimpleRouter()

news_post_router.register(r'', NewsFeedViewSet)

urlpatterns = news_post_router.urls
