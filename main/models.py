from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название курса")
    description = models.TextField(blank=True, verbose_name="Описание курса")
    image = models.ImageField(upload_to='courses/', blank=True, null=True,
                              verbose_name="Обложка курса")
    created_at = models.DateTimeField(auto_now_add=True)
    is_accessible = models.BooleanField(default=False,
                                        verbose_name="Доступен без авторизации")
    
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ['id']
    
    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='modules', verbose_name="Курс")
    title = models.CharField(max_length=200, verbose_name="Название раздела")
    description = models.TextField(blank=True, verbose_name="Описание раздела")
    order = models.PositiveIntegerField(default=1,
                                        verbose_name="Порядок отображения")
    
    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"
        ordering = ['order']
    
    def __str__(self):
        return f"{self.course.title} → {self.title}"


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE,
                               related_name='lessons', verbose_name="Раздел")
    title = models.CharField(max_length=200, verbose_name="Название урока")
    description = models.TextField(blank=True, verbose_name="Описание урока")
    order = models.PositiveIntegerField(default=1,
                                        verbose_name="Порядок отображения")
    
    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ['order']
    
    def __str__(self):
        return f"{self.module.title} → {self.title}"


class Slide(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,
                               related_name='slides', verbose_name="Урок")
    content = models.TextField(verbose_name="Контент слайда")
    order = models.PositiveIntegerField(default=1,
                                        verbose_name="Порядок отображения")
    
    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"
        ordering = ['order']
    
    def __str__(self):
        return f"{self.lesson.title} — Слайд {self.order}"
