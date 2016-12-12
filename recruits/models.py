from django.db import models

# Create your models here.

class Consultancy(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=50)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Consultancies'

    def __str__(self):
        return self.name


class Skillset(models.Model):
    skill = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.skill


class Profile(models.Model):
    consultancy = models.ForeignKey(Consultancy, related_name='profiles')
    skillset = models.ManyToManyField(Skillset, related_name='skills')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(default='user@gmail.com')
    gender = models.CharField(max_length=10, choices=(('M', 'Male'),
                                                      ('F', 'Female'),
                                                      ))
    resume = models.FileField(upload_to='doc_uploads/', blank=True)
    interview = models.FileField(upload_to='media_uploads/', blank=True)

    def __str__(self):
        return self.name

    @property
    def name(self):
        return ' '.join([str(self.first_name), str(self.last_name)])

    def get_absolute_url(self):
        return "/profiles/%i/" % self.id
