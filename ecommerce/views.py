from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

from ecommerce.forms import CategoryForm, ClientForm, FournisseurForm, ProductForm
from .models import Category, Client, Fournisseur, Product

# Create your views here.
'''
Accueil
'''
def index(request):
    products = Product.objects.all().order_by('-id')
    context = {'products': products}
    return render(request, 'index.html', context)


'''
Debut
Partie des products
'''

def liste_product(request):
    products = Product.objects.all().order_by('-id')
    context = {'products': products}
    return render(request, 'product/liste.html', context)

def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            libelle = form.cleaned_data.get('libelle')
            form.save()
            form = ProductForm()
            messages.success(request,f'{libelle} has been saved successfully')
            return redirect('liste_product')
    context = {'form': form}
    return render(request, 'product/add.html', context)

def update_product(request,id):
    product = get_object_or_404(Product, id=id)
    # product = Product.objects.get(id=id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('liste_product')
    context = {'form': form}
    return render(request, 'product/update.html', context)

def detail_product(request,id):
    product = get_object_or_404(Product, id=id)
    context = {'product': product}
    return render(request, 'product/detail.html', context)

def delete_product(request,id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request,f'product has been saved successfully')
    return redirect('liste_product')

'''
fin
Partie des products
'''

'''
Debut
Partie des categorie
'''

def liste_category(request):
    categories = Category.objects.all().order_by('-id')
    paginator = Paginator(categories, 5)
    page_number = request.GET.get('page')
    page_categories = paginator.get_page(page_number)
    context = {'categories': page_categories}
    return render(request, 'category/liste.html', context)


def search_categorie(request):
	search = request.GET.get('search')
	categories = Category.objects.filter(Q(libelle__icontains = search))
	post_number = categories.count()
   

	message = f'{post_number} categories '
	if post_number <= 1:
		message = f'{post_number} categorie '
	context = {
		'categories':categories,
		'message':message
	}
	return render(request,  'category/search.html' , context)


def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            libelle = form.cleaned_data['libelle']
            form.save()
            form = CategoryForm()
            messages.success(request,f'{libelle} has been saved successfully')
            return redirect('liste_category')
    context = {'form': form}
    return render(request, 'category/add.html', context)

def update_category(request,id):
    category = Category.objects.get(id=id)
    form = CategoryForm(request.POST or None ,instance=category)
    if form.is_valid():
        form.save()
        return redirect('liste_category')
    context = {'form': form}
    return render(request, 'category/update.html', context)


def detail_category(request, id):
    category = get_object_or_404(Category, id=id)
    context = {'category': category}
    return render(request, 'category/detail.html', context)

def delete_category(request,id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('liste_category')

'''
fin
Partie des categories
'''

'''
Debut
Partie des clients
'''

def liste_client(request):
    clients = Client.objects.all().order_by('-id')
    context = {'clients': clients}
    return render(request, 'client/liste.html', context)


def add_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            form = ClientForm()
            return redirect('liste_client')
    context = {'form': form}
    return render(request, 'client/add.html', context)

def update_client(request,id):
    client = Client.objects.get(id=id)
    form = ClientForm(request.POST or None ,instance=client)
    if form.is_valid():
        form.save()
        return redirect('liste_client')
    context = {'form': form}
    return render(request, 'client/update.html', context)


def detail_client(request, id):
    client = get_object_or_404(Client, id=id)
    context = {'client': client}
    return render(request, 'client/detail.html', context)

def delete_client(request,id):
    client = get_object_or_404(client, id=id)
    client.delete()
    return redirect('liste_client')



'''
fin
Partie des clients
'''


'''
Debut
Partie des fournisseurs
'''

def liste_fournisseur(request):
    fournisseurs = Fournisseur.objects.all().order_by('-id')
    context = {'fournisseurs': fournisseurs}
    return render(request, 'fournisseur/liste.html', context)


def add_fournisseur(request):
    form = FournisseurForm()
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            form = FournisseurForm()
            return redirect('liste_fournisseur')
    context = {'form': form}
    return render(request, 'fournisseur/add.html', context)

def update_fournisseur(request,id):
    fournisseur = Fournisseur.objects.get(id=id)
    form = FournisseurForm(request.POST or None ,instance=fournisseur)
    if form.is_valid():
        form.save()
        return redirect('liste_fournisseur')
    context = {'form': form}
    return render(request, 'fournisseur/update.html', context)


def detail_fournisseur(request, id):
    fournisseur = get_object_or_404(Fournisseur, id=id)
    context = {'fournisseur': fournisseur}
    return render(request, 'fournisseur/detail.html', context)

def delete_fournisseur(request,id):
    fournisseur = get_object_or_404(Fournisseur, id=id)
    fournisseur.delete()
    return redirect('liste_fournisseur')


'''
fin
Partie des fournisseurs
'''

'''
Debut
Partie des ventes
'''

'''
fin
Partie des ventes
'''

'''
Debut
Partie des commandes
'''

'''
fin
Partie des commandes
'''