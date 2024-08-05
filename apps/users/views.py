from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.views import Response, APIView
from .models import MyUser
from rest_framework import status
from .serializers import MyUserSerializer, UserLoginSerializer
from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAdminUser()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            tokens = self.get_tokens_for_user(user)
            user_data = serializer.data
            user_data['tokens'] = tokens  # Добавляем токены в данные пользователя
            return Response(user_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class CustomLoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if email and password:
            try:
                user = MyUser.objects.get(email=email, raw_password=password)
            except MyUser.DoesNotExist:
                return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({"detail": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

# class LoginAPIView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#
#         # Проверка учетных данных
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return Response({'success': 'Login successful'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


# class LoginAPIView(GenericAPIView):
#     serializer_class = UserLoginSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             password = serializer.validated_data['password']
#             user = authenticate(email=email, password=password)  # Аутентифицируем пользователя
#             if user is not None:
#                 refresh = RefreshToken.for_user(user)
#                 return Response({
#                     "refresh": str(refresh),
#                     "access": str(refresh.access_token),
#                     "message": "Вы успешно вошли в систему."
#                 }, status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": "Неверные учётные данные."}, status=status.HTTP_401_UNAUTHORIZED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def health_check(request):
    return JsonResponse({"status": "ok"}, status=200)
