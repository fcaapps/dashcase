from django.db import models

class PermissoesOutrasAreas(models.Model):

    class Meta:

        managed = False  # No database table creation or deletion operations \
                         # will be performed for this model.

        permissions = (
            ('outrasareas_permissoes', 'Permissão Global de Outras Areas'),
        )
