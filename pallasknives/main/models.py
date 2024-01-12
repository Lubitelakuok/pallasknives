from django.db import models

class Task(models.Model):
    first_name = models.CharField(max_length=100,default=' ')
    last_name = models.CharField(max_length=100,default=' ')
    email = models.EmailField(default=' ')
    blade_type = models.CharField(max_length=50,default=' ',
                                  choices=[('Wharncliffe', 'Wharncliffe'), ('DropPoint', 'DropPoint'), ('Tanto', 'Tanto')])
    handle_type = models.CharField(max_length=50,default=' ',
                                  choices=[('1', '1'), ('2', '2')])
    color = models.CharField(max_length=50, default='Цвет',choices=[('Neobrabotan', 'Без обработки'), ('Blue', 'Синий'), ('Yellow', 'Желтый'), ('Marine', 'Бирюзовый'), ('Pink', 'Розовый')])
    message = models.TextField(default=' ')
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.blade_type} - {self.color}"

    class Meta:
        verbose_name ='Заявки'
        verbose_name_plural = 'Заявки'
class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to='main/%y')
    def __str__(self):
        return self.caption