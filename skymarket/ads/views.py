from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from ads.models import Ad, Comment
from ads.serializers import * 
from ads.permissions import UserPermission




class AdPagination(pagination.PageNumberPagination):
    page_size = 4
    page_query_param = "page"
    max_page_size = 100000


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    serializer_action_classes = {
        'list': AdListSerializer,
        'retrieve': AdRetrieveSerializer,
        'create': AdCreateSerializer,
        'update': AdCreateSerializer,
    }
    #permission_classes = [UserPermission]

    @action(detail=False, methods=['get'], url_path=r'me', serializer_class=AdListSerializer)
    def user_ads(self, request, *args, **kwargs):
        current_user = self.request.user
        users_ads = Ad.objects.filter(author=current_user)
        page = self.paginate_queryset(users_ads)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(users_ads, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    serializer_action_classes = {
        'list': CommentListSerializer,
        'retrieve': CommentListSerializer,
        'create': CommentCreateSerializer,
        'update': CommentCreateSerializer,
    }

    #permission_classes = (UserPermission)

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.kwargs['ad_id'])

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def perform_create(self, serializer):
        ad = Ad.objects.get(pk=self.kwargs['ad_id'])
        serializer.save(author=self.request.user, ad=ad)

