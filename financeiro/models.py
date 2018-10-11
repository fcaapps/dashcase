from django.db import models

class PermissoesFinanceiro(models.Model):

    class Meta:

        managed = False  # No database table creation or deletion operations \
                         # will be performed for this model.

        permissions = (
            ('financeiro_permissoes', 'Permissão Global do Financeiro'),
        )
