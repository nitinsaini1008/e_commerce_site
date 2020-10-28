from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('main_page',views.main_page,name='main_page'),
    path('search_name',views.search_name,name='search_name'),
    path('buy',views.buy,name='buy'),
    path('sign_in',views.sign_in,name='sign_in'),
    path('log_in',views.log_in,name='log_in'),
    path('log_out',views.log_out,name='log_out'),
    path('my_cart',views.my_cart,name='my_cart'),
    path('delete_cart',views.delete_cart,name='delete_cart'),
    path('about',views.about,name='about'),
    path('sub_page',views.sub_page,name='sub_page'),
    path('pre_buy',views.pre_buy,name='pre_buy'),
    path('account',views.account,name='account'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)