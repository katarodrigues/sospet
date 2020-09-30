from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    CATEGORY = (
        ("PROCURA-SE","Procura-se"),
        ("POCRIAÇÃO", "Pocriação"),
        ("ADOÇÃO", "Adoção"),
    )
    city = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    begin_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='pet')
    category = models.CharField (max_length=11, choices=CATEGORY, default="PROCURA-SE")
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.id)

    class Meta:
        db_table = 'pet'