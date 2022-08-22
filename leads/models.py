from django.db import models
from django.conf import settings
from django.urls import reverse

from datetime import datetime 



class Prospect(models.Model):
    PasContacte= 'Pas contacté'
    ARelancer = 'A relancer'
    EnCours = 'En cours'
    PasInteresse= 'Pas intéressé'
    DossierAnnule = 'Dossier Annulé'
    Signe = 'Signé'

    STATUS = (
        (PasContacte, 'Pas contacté'),
        (ARelancer, 'A relancer'),
        (EnCours, 'En cours'),
        (PasInteresse, 'Pas intéressé'),
        (DossierAnnule,'Dossier Annulé'),
        (Signe,'Signé'),
    )

    Nom = models.CharField(max_length=20)
    Prénom = models.CharField(max_length=20)
    Email = models.EmailField()
    NumeroDeTelephone = models.CharField(max_length=20)
    Age = models.IntegerField(default=0)
    Marié = models.BooleanField(default=False)
    NBEnfants = models.IntegerField(default=0)
    Agent = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.SET_NULL)
    Profession = models.CharField(max_length=20)
    RevenuAnnuel = models.FloatField(default=0)
    Adresse = models.CharField(max_length=20)
    
    créeLe = models.DateField(auto_now_add=True)
    
    status = models.CharField(max_length=25, choices=STATUS, default=PasContacte)

    def __str__(self):
        return f"{self.Nom} {self.Prénom}"
