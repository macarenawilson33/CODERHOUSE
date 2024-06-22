from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')
    , path('about/', views.about, name='about')
    , path('login/', views.login_user, name='login')
    , path('logout/', views.logout_user, name='logout')
    , path('register/', views.register_user, name='register')
    , path('update_user/', views.update_user, name='update_user')
    , path('update_password/', views.update_password, name='update_password')
    , path('product/<int:pk>', views.product, name='product')
    , path('category/<str:var>', views.category, name='category')
    , path('new_product/', views.new_product, name='new_product')
    , path('delete_product/<int:pk>', views.delete_product, name='delete_product')
    , path('update_product/<int:pk>', views.update_product, name='update_product')
    , path('new_comment/<int:product_id>', views.new_comment, name='new_comment')
    , path('remove_comment/<int:comment_id>', views.remove_comment, name='remove_comment')
]
