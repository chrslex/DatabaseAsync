from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from PIL import Image

SEXES = (('PEREMPUAN', 'Perempuan'), ('LAKI-LAKI', 'Laki-laki'))
MAJOR = (('IF', 'Teknik Informatika'), ('STI', 'Sistem Teknologi Informasi'))

class Person(models.Model):

    text_regex = RegexValidator(r'^[a-z A-Z]*$', 'Only letters are allowed.')
    nama = models.CharField(validators=[text_regex], max_length=75)
    nim_tpb = models.IntegerField(default=16519599, validators=[MaxValueValidator(16519600), MinValueValidator(16519000)])
    nim_jurusan = models.IntegerField(default=13519999)
    panggilan = models.CharField(validators=[text_regex], max_length=30)
    jenis_kelamin = models.CharField(max_length=9,choices=SEXES)
    jurusan = models.CharField(max_length=3, choices=MAJOR)
    image = models.ImageField(default = 'default.png', upload_to='async')
    kelompok = models.IntegerField(default=0, validators=[MaxValueValidator(12), MinValueValidator(0)])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 256 or img.width > 256:
            output_size = (256, 256)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def update(self):
        self.save()

    def __str__(self):
        return '{0} {1} ({2})'.format(self.nama, self.panggilan, self.jenis_kelamin)