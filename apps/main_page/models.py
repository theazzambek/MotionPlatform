from django.contrib.auth import get_user_model
from django.db import models
from apps.users.models import MyUser


User = get_user_model()


class HomePage(models.Model):
    other_course = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE
    )
    link = models.URLField(
        verbose_name="Ссылка на источник"
    )

    def __str__(self):
        return str(self.other_course.title)

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


class Event(models.Model):
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    address = models.CharField(
        max_length=255
    )
    time_field = models.TimeField()
    date_field = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'События'
        verbose_name_plural = 'События'


class MyLessons(models.Model):
    theme = models.CharField(
        max_length=255
    )
    theory = models.TextField()
    video = models.FileField(
        upload_to="videos/"
    )
    tasks = models.TextField()

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Темы'
        verbose_name_plural = 'Темы'


class Question(models.Model):
    profile = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE
    )
    comment = models.TextField()
    time = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    profile = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    comment = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    answer_comment = models.TextField()
    time = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.answer_comment

    class Meta:
        verbose_name = 'Ответы'
        verbose_name_plural = 'Ответы'


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
        related_name='likes',
        null=True,
        blank=True
    )
    answer = models.ForeignKey(
        'Answer',
        on_delete=models.CASCADE,
        related_name='likes',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = (('user', 'question'), ('user', 'answer'))
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return f"{self.user.firstname}{self.user.lastname} likes {'question' if self.question else 'answer'}"


class Course(models.Model):
    logo = models.ImageField(
        upload_to='logo/'
    )
    title = models.CharField(
        max_length=255
    )
    description = models.TextField()
    teacher = models.ForeignKey(
        MyUser,
        on_delete=models.PROTECT
    )
    start_date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'


class BlogTheme(models.Model):
    title = models.CharField(
       max_length=125
    )
    description = models.TextField()
    mediafile = models.FileField(
        upload_to='video_blog/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блоги'
        verbose_name_plural = 'Блоги'


