"""controleEstoque URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/login/$', auth_views.login),
    url(r'^$', views.lst_safra, name='lst_safra'),
    url(r'^add-product', views.add_product, name='add_product'),
    url(r'^lst-safra', views.lst_safra, name='lst_safra'),
    url(r'^lst-produtos', views.lst_produtos, name='lst_produtos'),
    url(r'^lst-servicos', views.lst_servicos, name='lst_servicos'),
    url(r'^add-safra', views.add_safra, name='add_safra'),
    url(r'^add-produtos', views.add_produtos, name='add_produtos'),
    url(r'^add-servicos', views.add_servicos, name='add_servicos'),
    url(r'^logout', views.log_out, name='logout'),
    url(r'^remove-product/(?P<id>[^\.]+)', views.remove_product, name='remove_product'),
    url(r'^remove-safra/(?P<id>[^\.]+)', views.remove_safra, name='remove_safra'),
    url(r'^edit-safra/(?P<id>[^\.]+)', views.edit_safra, name='edit_safra'),
    url(r'^remove-produtos/(?P<id>[^\.]+)', views.remove_produtos, name='remove_produtos'),
    url(r'^edit-produtos/(?P<id>[^\.]+)', views.edit_produtos, name='edit_produtos'),
    url(r'^remove-servicos/(?P<id>[^\.]+)', views.remove_servicos, name='remove_servicos'),
    url(r'^edit-servicos/(?P<id>[^\.]+)', views.edit_servicos, name='edit_servicos'),

]
