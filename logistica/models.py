from django.db import models

class PermissoesLogistica(models.Model):

    class Meta:

        managed = False  # No database table creation or deletion operations \
                         # will be performed for this model.

        permissions = (
            ('logistica_permissoes', 'Permissão Global de Logistica'),
        )
