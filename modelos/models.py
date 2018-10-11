from django.db import models

class PermissoesModelos(models.Model):

    class Meta:

        managed = False  # No database table creation or deletion operations \
                         # will be performed for this model.

        permissions = (
            ('modelos_permissoes', 'Permissão Global de Modelos'),
        )
