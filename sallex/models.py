from django.db import models
from Salle.models import Salle
from Examen.models import Examen

class Sallex(models.Model):
    idse = models.AutoField(primary_key=True)
    id_salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    id_examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id_salle} - {self.id_examen}'
