from django.shortcuts import render
from django.views import generic
from store.models import Product, Category
from django_filters.views import FilterView
from store.filters import ProductFilter
from cart.forms import CartForm
from django.db.models import Count
from django import forms
import django_filters

class ProductFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(
        label='Danh mục',
        queryset=Category.objects.all()
    )
    price = django_filters.RangeFilter(label='Giá')

    class Meta:
        model = Product
        fields = ['category', 'price']

class ProductList(FilterView):
    model = Product
    queryset = Product.objects.all()
    paginate_by = 20
    filterset_class = ProductFilter
    context_object_name = 'products'
    template_name = 'store/product_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if 'category_slug' in self.kwargs:
            qs = qs.filter(category__slug=self.kwargs['category_slug'])
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def get_queryset(self):
        product = super().get_queryset()
        return product.select_related('category').annotate(
            total_purchases=Count('ordered')) #biến để đếm số lượng khách đã mua hàng (đếm hành động 'ordered')

class ProdcutDetails(generic.DetailView):
    model = Product
    template_name = 'store/product_details.html'
    context_object_name = 'product'

    def get_queryset(self):
        product = super().get_queryset()
        return product.select_related('category').annotate(
            total_purchases=Count('ordered')) #biến để đếm số lượng khách đã mua hàng (đếm hành động 'ordered')


class CategoriesList(generic.ListView):
    template_name = 'store/categories_list.html'
    context_object_name = 'categories'
    queryset = Category.objects.all().annotate(num_products=Count('products'))
'''
def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "store/post.html", {"post": post, "form": form})'''
