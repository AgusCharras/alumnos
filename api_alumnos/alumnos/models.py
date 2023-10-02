from django.db import models

class Carrera(models.Model):
    """
    Modelo que representa una carrera académica.

    Attributes:
        id (AutoField): Clave primaria única para la carrera.
        nombre (CharField): Nombre de la carrera.
        inicio (DateTimeField): Fecha y hora de inicio de la carrera.
        fin (DateTimeField): Fecha y hora de finalización de la carrera.
        duracion (IntegerField): Duración de la carrera en días.

    Meta:
        db_table (str): Nombre de la tabla en la base de datos.
        ordering (tuple): Orden predeterminado de los registros.
        verbose_name (str): Nombre singular legible de la carrera.
        verbose_name_plural (str): Nombre plural legible de las carreras.

    Methods:
        __str__(): Retorna una representación legible en cadena de la carrera.

    """

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    inicio = models.DateTimeField(auto_now_add=True)
    fin = models.DateTimeField(auto_now=True)
    duracion = models.IntegerField()

    class Meta:
        db_table = 'carreras'
        ordering = ('nombre',)
        verbose_name = 'carrera'
        verbose_name_plural = 'carreras'

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    """
    Modelo que representa un curso académico relacionado con una carrera.

    Attributes:
        id (AutoField): Clave primaria única para el curso.
        nombre (CharField): Nombre del curso.
        nivel (IntegerField): Nivel del curso.
        carreras_id (ForeignKey): Clave foránea que relaciona el curso con una carrera.

    Meta:
        db_table (str): Nombre de la tabla en la base de datos.
        ordering (tuple): Orden predeterminado de los registros.
        verbose_name (str): Nombre singular legible del curso.
        verbose_name_plural (str): Nombre plural legible de los cursos.

    Methods:
        __str__(): Retorna una representación legible en cadena del curso.

    """

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nivel = models.IntegerField()
    carreras_id = models.ForeignKey('Carrera', on_delete=models.CASCADE)

    class Meta:
        db_table = 'cursos'
        ordering = ('nombre',)
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    """
    Modelo que representa un alumno matriculado en un curso.

    Attributes:
        id (AutoField): Clave primaria única para el alumno.
        apellido (CharField): Apellido del alumno.
        nombre (CharField): Nombre del alumno.
        inscripcion (DateTimeField): Fecha y hora de inscripción del alumno en el curso.
        cursos_id (ForeignKey): Clave foránea que relaciona al alumno con un curso.

    Meta:
        db_table (str): Nombre de la tabla en la base de datos.
        ordering (tuple): Orden predeterminado de los registros.
        verbose_name (str): Nombre singular legible del alumno.
        verbose_name_plural (str): Nombre plural legible de los alumnos.

    Methods:
        __str__(): Retorna una representación legible en cadena del alumno.

    """

    id = models.AutoField(primary_key=True)
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    inscripcion = models.DateTimeField(auto_now_add=True)
    cursos_id = models.ForeignKey('Curso', on_delete=models.CASCADE)

    class Meta:
        db_table = 'alumnos'
        ordering = ('apellido', 'nombre')
        verbose_name = 'alumno'
        verbose_name_plural = 'alumnos'

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
