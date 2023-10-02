from django.conf import settings
from rest_framework import serializers
from .models import Carrera, Curso, Alumno

class CarreraSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Carrera.

    Utilizado para convertir objetos Carrera en datos JSON y viceversa.

    Attributes:
        inicio (DateTimeField): Campo de fecha y hora de inicio de la carrera.
        fin (DateTimeField): Campo de fecha y hora de finalización de la carrera.

    Meta:
        model (Carrera): Modelo de origen para el serializador.
        fields (str): Todos los campos del modelo se incluyen en la representación JSON.

    """
    inicio = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False, allow_null=True)
    fin = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False, allow_null=True)

    class Meta:
        model = Carrera
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Curso.

    Utilizado para convertir objetos Curso en datos JSON y viceversa.

    Meta:
        model (Curso): Modelo de origen para el serializador.
        fields (str): Todos los campos del modelo se incluyen en la representación JSON.

    """
    class Meta:
        model = Curso
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Alumno.

    Utilizado para convertir objetos Alumno en datos JSON y viceversa.

    Meta:
        model (Alumno): Modelo de origen para el serializador.
        fields (str): Todos los campos del modelo se incluyen en la representación JSON.

    """
    class Meta:
        model = Alumno
        fields = '__all__'
