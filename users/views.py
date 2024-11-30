from datetime import datetime

from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


from users.models import User
from users.serilayzer import UserSerializer, ConfSerializer, LoginSerializer


# Create your views here.


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserConfirmationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=ConfSerializer
    )
    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = ConfSerializer(data=request.data)
        if serializer.is_valid():
            self.verify_codee(user, serializer.validated_data.get("code"))
            data = {
                'status': 'Success',
                'message': f'Confirmation code {serializer.validated_data["code"]}',
            }
        else:
            data = {
                'status': 'Fail',
                'message': serializer.errors
            }
        return Response(data)

    @staticmethod
    def verify_codee(user, code):
        verification = user.code.filter(
            code=code,
            is_confirmed=False,
            expire_time__gte=datetime.now()
        )
        if not verification.exists():
            data = {
                'status': 'Fail',
                'message': 'Code xato yokida eskirgan'
            }
            raise ValidationError(data)
        verification.update(is_confirmed=True)
        user.is_verified = True
        user.save()

        return True


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        request=LoginSerializer
    )

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            return Response({
                'access_token': user.token()['access_token'],
                'refresh_token': user.token()['refresh_token']
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

