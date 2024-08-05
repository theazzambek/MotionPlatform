from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (HomePageViewSet, CourseViewSet, EventViewSet, MyLessonsViewSet, TeacherViewSet,
                    QuestionViewSet, AnswerViewSet, toggle_like_question, toggle_like_answer, BlogThemeViewSet,
                    StudentViewSet)

router = DefaultRouter()
router.register(r'homepages', HomePageViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'events', EventViewSet)
router.register(r'mylessons', MyLessonsViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'student', StudentViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'blogthemes', BlogThemeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('questions/<int:question_id>/toggle_like/', toggle_like_question, name='toggle-like-question'),
    path('answers/<int:answer_id>/toggle_like/', toggle_like_answer, name='toggle-like-answer'),
]
