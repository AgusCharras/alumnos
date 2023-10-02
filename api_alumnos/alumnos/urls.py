from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarreraViewSet, CursoViewSet, AlumnoViewSet


router = DefaultRouter()
router.register(r'carreras', CarreraViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'alumnos', AlumnoViewSet)


urlpatterns = [
    # Otras URL de la aplicación
    path('', include(router.urls)),
]
