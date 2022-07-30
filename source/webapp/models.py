from django.db import models

from django.urls import reverse


class Poll(models.Model):
    question = models.TextField(max_length=500, verbose_name="Вопрос")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.id}. {self.question}: {self.created_at}"

    class Meta:
        db_table = "polls"
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"


class Choice(models.Model):
    text_var = models.TextField(max_length=100, verbose_name="Вариант")
    interview = models.ForeignKey("webapp.Poll", on_delete=models.CASCADE, related_name="interviews",
                                verbose_name='Опрос')

    def __str__(self):
        return f"{self.id}. {self.text_var}: {self.interview}"

    class Meta:
        db_table = "choice"
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
