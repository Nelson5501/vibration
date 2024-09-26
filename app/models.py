from django.db import models

class Evenement(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()

    def __str__(self):
        return self.titre
    

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    path = models.CharField(max_length=200)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.ip_address} visited {self.path} on {self.timestamp}"


class PlayedTrack(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    played_at = models.DateTimeField(auto_now_add=True)



class Sale(models.Model):
    date = models.DateField()
    amount = models.FloatField()




    def __str__(self):
        return f"{self.title} by {self.artist} played on {self.played_at}"
