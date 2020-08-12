from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

SEXES = (('FEMALE', 'Female'), ('MALE', 'Male'))

class Person(models.Model):

    text_regex = RegexValidator(r'^[a-z A-Z]*$', 'Only letters are allowed.')
    nama = models.CharField(validators=[text_regex], max_length=75)
    nim_tpb = models.IntegerField(default=16519599, validators=[MaxValueValidator(16519600), MinValueValidator(16519000)])
    nim_jurusan = models.IntegerField(default=13519999)
    panggilan = models.CharField(validators=[text_regex], max_length=30)
    jenis_kelamin = models.CharField(max_length=6,choices=SEXES)

    def update(self):
        self.save()

    def __str__(self):
        return '{0} {1} ({2})'.format(self.nama, self.panggilan, self.jenis_kelamin)