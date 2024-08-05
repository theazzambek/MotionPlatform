from django.utils import timezone

from .models import Question, Event, Course, Answer, Like, MyUser, HomePage, MyLessons, BlogTheme
from rest_framework import serializers


class HomePageSerializers(serializers.ModelSerializer):

    class Meta:
        model = HomePage
        fields = ('id', 'other_course', 'link')


class CoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'logo', 'title', 'description', 'teacher', 'start_date')


class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'time_field', 'date_field')


class MyLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyLessons
        fields = ('id', 'theme', 'theory', 'video', 'tasks')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'firstname', 'lastname', 'speciality', 'experience']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'firstname', 'lastname', 'speciality']


class QuestionSerializer(serializers.ModelSerializer):
    time_since_added = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id', 'comment', 'profile', 'time', 'time_since_added']
        read_only_fields = ['profile', 'time_since_added']

    def get_time_since_added(self, obj):
        current_time = timezone.now()
        time_difference = current_time - obj.time
        return {
            'Дни': time_difference.days,
            'Часы': time_difference.seconds // 3600,
            'Минуты': (time_difference.seconds // 60) % 60,
            'секунды': time_difference.seconds % 60
        }


class AnswerSerializer(serializers.ModelSerializer):
    time_since_added = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = ['id', 'comment', 'answer_comment', 'profile', 'time', 'time_since_added']
        read_only_fields = ['profile', 'time_since_added']

    def get_time_since_added(self, obj):
        current_time = timezone.now()
        time_difference = current_time - obj.time
        return {
            'Дни': time_difference.days,
            'Часы': time_difference.seconds // 3600,
            'Минуты': (time_difference.seconds // 60) % 60,
            'секунды': time_difference.seconds % 60
        }

# class LikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Like
#         fields = ['id', 'user', 'question', 'answer', 'created_at']
#


class BlogThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTheme
        fields = ('id', 'title', 'description', 'mediafile')
