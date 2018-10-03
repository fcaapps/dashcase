from django.db import models

class DadosPerfil(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, blank=True)
    nome_fantasia = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to='clientes_fotos', null=True, blank=True)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nome + ' ' + self.email

