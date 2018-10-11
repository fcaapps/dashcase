from django.db import models

class PermissoesVendas(models.Model):

    class Meta:

        managed = False  # No database table creation or deletion operations \
                         # will be performed for this model.

        permissions = (
            ('vendas_permissoes', 'Permissão Global de Vendas'),
        )
