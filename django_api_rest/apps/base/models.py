from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """Model definition for BaseModel. """
    
    # TODO: Define fields here
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('Estado', default=True)
    created_at = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    updated_at = models.DateField('Fecha de  Actualizacion', auto_now=True, auto_now_add=False)
    deleted_at = models.DateField('Fecha de Eliminacion', auto_now=True, auto_now_add=False)
    
    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'
        