from django.db import models

class PermissoesClientes(models.Model):

    class Meta:

        managed = False  # No database table creation or deletion operations \
                         # will be performed for this model.

        permissions = (
            ('clientes_permissoes', 'Permissão Global de Clientes'),
        )
