from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from PathBase.Serializers import SessionSerializer, UserSerializer, SessionFullSerializer, CharacterSerializer
from PathBase.models import User, Session, Character
from PathBase.permissions import IsStaffOrReadOnly, IsStaff


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SessionFullViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionFullSerializer

    @action(methods=['get'], detail=False, url_path='last-3')
    def get_last_3(self, request):
        set_emp = self.queryset.order_by('NameSession')[:3]
        data = self.serializer_class(set_emp, many=True).data
        return Response(data)

    # Выбирает последнюю бронь
    @action(methods=['get'], detail=False, url_path='PT-last')
    def PT_get_last(self, request):
        set_emp = self.queryset.order_by('NameSession')[:1]
        data = self.serializer_class(set_emp, many=True).data
        return Response(data)


class SessionViewSetPer(viewsets.ModelViewSet):
    permission_classes = (IsStaffOrReadOnly,)
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionFullViewSetPer(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Session.objects.all()
    serializer_class = SessionFullSerializer

    def get_my_info(self):
        user = self.request.user
        return Session.objects.filter(user=user)


class CharacterViewSetPer(viewsets.ModelViewSet):
    permission_classes = (IsStaff,)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
