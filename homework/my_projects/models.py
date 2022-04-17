from django.db import models
from my_users.models import MyUser


class Project(models.Model):
    date_create = models.DateTimeField(verbose_name='Дата создания проекта',
                                       auto_now_add=True, null=True)
    name = models.CharField(verbose_name='Название проекта', max_length=100)
    link_rep = models.URLField(verbose_name='Ссылка на репозиторий', max_length=255, blank=True, null=True)
    users = models.ManyToManyField(MyUser, verbose_name='Пользователи')
    creator = models.ForeignKey(MyUser, verbose_name='Создатель проекта',
                                on_delete=models.CASCADE, related_name='creator_project',
                                blank=True, null=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проект'
        ordering = ['-date_create']

    def __str__(self):
        return f"{self.pk}"


class ToDo(models.Model):
    project = models.ForeignKey(Project, verbose_name='Проект',
                                on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(verbose_name='Текст заметки', blank=False)
    date_create = models.DateTimeField(verbose_name='Дата создания',
                                       auto_now_add=True, null=True)
    date_update = models.DateTimeField(verbose_name='Дата обновления',
                                       auto_now_add=True, null=True)
    creator = models.ForeignKey(MyUser, verbose_name='Автор заметки',
                                on_delete=models.CASCADE,
                                related_name='todo_creator', blank=True,
                                null=True)
    status = (('активно', 'активно'), ('закрыто', 'закрыто'))

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметка'
        ordering =['-date_create']

    def __str__(self):
        return f"{self.pk}"
