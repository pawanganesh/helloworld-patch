from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from rest.models import Info
from rest.permissions import IsStaffUser
from rest.serializers import InfoModelSerializer


class InfoModelViewSet(ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoModelSerializer
    authentication_classes = [TokenAuthentication, ]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsStaffUser]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]


class InfoModelReadOnlyViewSet(ReadOnlyModelViewSet):
    serializer_class = InfoModelSerializer
    queryset = Info.objects.all()
