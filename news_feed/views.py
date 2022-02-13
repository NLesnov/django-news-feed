from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .filters import PublicPostFilter
from .models import Post
from .permissions import IsAuthor
from .serializers import PostSerializer


class NewsFeedViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = (PublicPostFilter,)

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthor,)
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)




