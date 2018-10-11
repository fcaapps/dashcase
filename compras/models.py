from django.db import models

class PermissoesCompras(models.Model):

    class Meta:

        managed = False  # No database table creation or deletion operations \
                         # will be performed for this model.

        permissions = (
            ('compras_permissoes', 'Permissão Global de Compras'),
        )
