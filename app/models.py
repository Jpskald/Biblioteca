from django.db import models

# Create your models here.

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name="Cidade"
        verbose_name_plural= "Cidades"


class Autor(models.Model):
    nome = models.CharField(max_length=100, verbose_name = "Nome do autor")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="CIDADE DO AUTOR")
    def __str__ (self):
        return self.nome
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class editora(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da editora")
    site = models.CharField(max_length=100, verbose_name="Site da editora")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da editora")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"

class leitor(models.Model):
    nome = models.CharField(max_length=100, verbose_name = "Nome do leitor")
    email = models.CharField(max_length=100, verbose_name = "Email do leitor" )
    cpf = models.CharField(max_length=11,unique=True, verbose_name = "CPF do leitor")
    def __str__ (self):
        return self.nome
    class Meta:
        verbose_name = "Leitor"
        verbose_name_plural = "Leitores"

class Genero(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Gênero")
    def __str__ (self):
        return self.nome
    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"

class livro(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do livro")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name = "Autor do livro")
    editora= models.ForeignKey(editora, on_delete=models.CASCADE, verbose_name = "Editora do livro")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name = "Gênero do livro")
    preco = models.IntegerField(verbose_name = "Preço do livro")
    data_plub = models.DateField(verbose_name = "Data de publicação do livro")
    status = models.BooleanField(verbose_name = "Status do livro")

    def __str__ (self):
        return f'{self.nome}, {self.autor}'
    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
