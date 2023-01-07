import uuid
from django.db import models

# Create your models here.

class Category(models.Model):
    libelle = models.CharField(max_length=50)

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')

    def __str__(self):
        return self.libelle

class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Fournisseur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Product(models.Model):
    libelle = models.CharField(max_length=50)
    quantite = models.IntegerField()
    prixunitaire = models.FloatField()
    datefabrication = models.DateTimeField(auto_now_add=True)
    dateexpiration = models.DateTimeField()
    image = models.ImageField(upload_to="photo_products/",blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle

class Vente(models.Model):
    STATUS = (
        ("Pending","Pending"),
        ("Out for delivery","Out for delivery"),
        ("Delivered","Delivered"),
    )
    code = models.UUIDField(default = uuid.uuid4, editable = False)
    quantite = models.IntegerField()
    prix = models.FloatField()
    datevente = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,null=True,choices=STATUS)

    def __str__(self):
        return f'{self.code}'

class Commande(models.Model):
    STATUS = (
        ("Pending","Pending"),
        ("Out for delivery","Out for delivery"),
        ("Delivered","Delivered"),
    )
    code = models.UUIDField(default = uuid.uuid4, editable = False)
    quantite = models.IntegerField()
    prix = models.FloatField()
    datecommande = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,null=True,choices=STATUS)

    def __str__(self):
        return f'{self.code}'

