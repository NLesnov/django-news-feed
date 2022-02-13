class PublicPostFilter:
    """
    Фильтр только публичных записей для неавторизованного пользователя
    """
    def filter_queryset(self, request, queryset, view):
        if not (request.user and request.user.groups.filter(name='Subscriber')):
            queryset = queryset.filter(is_public=True)
        return queryset