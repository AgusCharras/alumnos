from django.shortcuts import render
from rest_framework import viewsets
from .models import Carrera, Curso, Alumno
from .serializers import CarreraSerializer, CursoSerializer, AlumnoSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    """
    Vista de conjunto (viewset) para el modelo Carrera.

    Attributes:
        queryset: Consulta que devuelve todos los objetos Carrera.
        serializer_class: Serializador utilizado para convertir objetos Carrera en datos JSON y viceversa.

    """
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """
    Vista de conjunto (viewset) para el modelo Curso.

    Attributes:
        queryset: Consulta que devuelve todos los objetos Curso.
        serializer_class: Serializador utilizado para convertir objetos Curso en datos JSON y viceversa.

    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    """
    Vista de conjunto (viewset) para el modelo Alumno.

    Attributes:
        queryset: Consulta que devuelve todos los objetos Alumno.
        serializer_class: Serializador utilizado para convertir objetos Alumno en datos JSON y viceversa.

    """
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
