from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Product
from django.views.generic import TemplateView,ListView,DetailView,View,UpdateView,DeleteView,CreateView
from .forms import ProductForm
from django.urls import reverse_lazy
# Create your views here.

class HomeView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        categories = Category.objects.all()
        context = {'products': products, 'categories': categories}
        return render(request, self.template_name, context)

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'create_category.html'
    success_url = reverse_lazy('home')


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'category']
    template_name = 'product_create.html'
    success_url = reverse_lazy('home')



class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'  
    context_object_name = 'p'

		

class CategoryDetailView(View):
    def get(self, request, *args, **kwargs,):
        id=kwargs.get('pk')
        category = Category.objects.get(id=id)
        products = Product.objects.filter(category=category)

        return render(request, 'category.html', {'products':products, 'category':category})

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('home')  

class ProductDeleteView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)        
        product.delete()
        return redirect('home')

