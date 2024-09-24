from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True) # Auto incrementa um ID
    name = models.CharField(max_length=200) # Campo modelo, tipo Char

    def __str__(self):
        return self.name
   
    
# Criação da Tabela de Cadastro de Veiculos
class Car(models.Model):
    id = models.AutoField(primary_key=True) # Auto incrementa um ID
    model = models.CharField(max_length=200) # Campo modelo, tipo Char
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # Reecebe chave estrangeria da tabale Brand
    factory_year = models.IntegerField(blank=True, null=True) # Ano de fabricação, tipo Int, nos parametros informados, blank=true, permite deixar o campo em branco e null=true permite deixar null, ou seja , não é obrigado a informar dados
    model_year = models.IntegerField(blank=True, null=True) # Ano do modelo, tipo Int
    plate = models.CharField(max_length=10, blank=True, null=True) # Placa, tipo Char 
    photo = models.ImageField(upload_to='cars/', blank=True, null=True) # Foto, tipo Image
    value = models.FloatField(blank=True, null=True) # Campo valor, tipo float

    def __str__(self):
        return self.model
    