from django.db import models


class Usuario(models.Model):
    matricula = models.CharField(primary_key=True, max_length=14)
    nome_completo = models.CharField(max_length=200)
    cpf = models.CharField(unique=True, max_length=14)
    campus = models.CharField(max_length=4, blank=False, null=False)
    curso = models.CharField(max_length=75, blank=False, null=False)
    email_pessoal = models.EmailField(unique=True, max_length=250)
    email_escolar = models.EmailField(unique=True, max_length=250)
    email_academico = models.EmailField(unique=True, max_length=250)
    tipo_vinculo = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)
    data_nascimento = models.DateField()
    url_foto = models.URLField(max_length=600)

    @property
    def primeiro_nome(self) -> str:
        return self.nome_completo.split()[0]

    @property
    def ultimo_nome(self) -> str:
        return self.nome_completo.split()[-1]

    @property
    def nome(self) -> str:
        return f"{self.primeiro_nome} {self.ultimo_nome}"

    def __str__(self) -> str:
        return self.nome_completo
