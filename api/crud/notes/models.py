from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=250)
    email = models.EmailField(max_length=255, unique=True)
    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class Tag(models.Model):
    """Tag for data. Every tag has unique text.
    """
    text = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return 'Tag[id: {id}, text: {text}]'.format(
            id=self.id, text=self.text)


class Note(models.Model):
    TYPE_CHOICES = (
        ("1", "TIPO 1"),
        ("2", "TIPO 2"),
        ("3", "TIPO 3")
    )
    date = models.DateTimeField(auto_now=True) #actualiza la fecha en CREATE y en UPDATE
    end_date = models.DateField(verbose_name="Fecha de finalización")
    note = models.TextField(verbose_name="Nota", max_length=250)
    adjunto = models.FileField(blank=True, null=True)
    user = models.ManyToManyField(User, related_name='notes', blank=True)
    task = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    tipo = models.CharField(max_length=7, choices=TYPE_CHOICES,)

    def __str__(self):
        return self.note

