from django.contrib import admin

# Register your models here.

from .models import Category,Client,Fournisseur,Commande,Vente,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","libelle")

class VenteAdmin(admin.ModelAdmin):
    list_display = ("id","code","prix","quantite","datevente")

class FournisseurAdmin(admin.ModelAdmin):
    list_display = ("nom","prenom","telephone","adresse")

class ClientAdmin(admin.ModelAdmin):
    list_display = ("nom","prenom","telephone","adresse")

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","prixunitaire","quantite","dateexpiration")

class CommandeAdmin(admin.ModelAdmin):
    list_display = ("id","code","prix","quantite","datecommande")

admin.site.register(Commande,CommandeAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(Vente,VenteAdmin)
admin.site.register(Fournisseur,FournisseurAdmin)
admin.site.register(Product,ProductAdmin)


