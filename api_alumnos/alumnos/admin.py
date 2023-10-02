from django.contrib import admin

# Register your models here.

from .models import Carrera, Curso, Alumno


admin.site.register(Carrera)
admin.site.register(Curso)
admin.site.register(Alumno)
