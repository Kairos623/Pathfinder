from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from PathBase.Serializers import SessionSerializer, UserSerializer, SessionFullSerializer, CharacterSerializer, \
    WeaponSerializer, MagicSerializer
from PathBase.models import User, Session, Character, Weapon, Cell
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

    @action(methods=['get'], detail=False, url_path='Session-last')
    def Session_get_last(self, request):
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


class WeaponViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

    @action(methods=['get'], detail=False, url_path='Weapon')
    def Weapon_only_accountant(self, request):
        role = request.query_params.get('NameWeapon')
        set_acc = self.get_queryset().filter(NameWeapon=role)
        data = self.serializer_class(set_acc, many=True).data
        return Response(data)


class MagicViewSet(viewsets.ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = MagicSerializer
