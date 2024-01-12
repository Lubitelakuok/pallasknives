from django.contrib import admin
# Register your models here.
from .models import Video
admin.site.register(Video)
from .models import Task
admin.site.register(Task)