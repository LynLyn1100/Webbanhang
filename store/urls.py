from django.urls import path
from store import views
app_name='store'
urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('categories', views.CategoriesList.as_view(), name='categories_list'),
    path('product/<slug:slug>/', views.ProdcutDetails.as_view(),
         name='product_details'),
]
