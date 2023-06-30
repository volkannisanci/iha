from django.db import models

class IHA(models.Model):
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    agirlik = models.FloatField()
    kategori = models.CharField(max_length=100)
    # Diğer özellikleri buraya ekleyin

    def __str__(self):
        return self.marka

    class Meta:
        app_label = 'iha'

