from django import forms

from ecommerce.models import Category, Client, Commande, Fournisseur, Product, Vente


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Category
        fields = ('libelle',)

class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Client
        fields = ('nom','prenom','telephone','adresse',)


class FournisseurForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FournisseurForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Fournisseur
        fields = ('nom','prenom','telephone','adresse',)

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    dateexpiration = forms.CharField(label="Date d'expiration",widget=forms.TextInput(attrs={
        'type': 'datetime-local',
        }))
    class Meta:
        model = Product
        fields = ('libelle','category','quantite','image','prixunitaire','dateexpiration',)

class VenteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VenteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Vente
        fields = ('status','product','client','quantite','prix',)

class CommandeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommandeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Commande
        fields = ('status','product','fournisseur','quantite','prix',)