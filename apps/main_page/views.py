from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Like, MyUser, Course, Question, Event, Answer, HomePage, MyLessons, BlogTheme
from rest_framework import viewsets
from .serializers import (
    QuestionSerializer, AnswerSerializer,
    TeacherSerializer, HomePageSerializers, CoursesSerializer, EventsSerializer, MyLessonsSerializer,
    BlogThemeSerializer, StudentSerializer)
from ..users.models import UserType


class HomePageViewSet(viewsets.ModelViewSet):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializers

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:  # create, update, destroy
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:  # actions like 'create', 'update', 'destroy'
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:  # actions like 'create', 'update', 'destroy'
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class MyLessonsViewSet(viewsets.ModelViewSet):
    queryset = MyLessons.objects.all()
    serializer_class = MyLessonsSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:  # actions like 'create', 'update', 'destroy'
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class TeacherViewSet(ReadOnlyModelViewSet):
    queryset = MyUser.objects.filter(role=UserType.TEACHER)
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return MyUser.objects.get_teachers()


class StudentViewSet(ReadOnlyModelViewSet):
    queryset = MyUser.objects.filter(role=UserType.STUDENT)
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return MyUser.objects.get_student()


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user)


@api_view(['POST'])
def toggle_like_question(request, question_id):
    user = request.user
    question = Question.objects.get(id=question_id)
    like, created = Like.objects.get_or_create(user=user, question=question)
    if not created:
        like.delete()
        return Response({'status': 'like removed'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'status': 'like added'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def toggle_like_answer(request, answer_id):
    user = request.user
    answer = Answer.objects.get(id=answer_id)
    like, created = Like.objects.get_or_create(user=user, answer=answer)
    if not created:
        like.delete()
        return Response({'status': 'like removed'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'status': 'like added'}, status=status.HTTP_201_CREATED)


class BlogThemeViewSet(viewsets.ModelViewSet):
    queryset = BlogTheme.objects.all()
    serializer_class = BlogThemeSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:  # create, update, destroy
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]