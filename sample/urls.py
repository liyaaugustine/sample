from django.urls import path,include
from django.conf.urls import url
from . import views
urlpatterns = [
    path('',views.index),
    path('home', views.home),
    path('first',views.first, name='first'),
    path('facebook',views.facebook, name='facebook'),
    path('calculater',views.calculater, name='calculater'),
    path('form', views.form, name='form'),
    path('add', views.add, name='add'),
    path('result', views.result, name='result'),
    path('ajaxadd', views.ajaxadd, name='ajaxadd'),
    path('ajaxsum', views.ajaxsum, name='ajaxsum'),
    path('parent',views.parent,name='parent'),
    path('child',views.child,name='child'),
    path('foreign',views.foreign,name='foreign'),
    path('sampleform',views.sampleform,name='sampleform'),
    path('logauth',views.logauth,name='logauth'),
    path('home2',views.home2,name='home2'),
    path('signout',views.signout,name='signout'),
    path('vprofile',views.vprofile,name='vprofile'),
    path('upvprofile',views.upvprofile,name='upvprofile'),
    path('checking',views.checking,name='checking'),
    path('vsingle/<int:userid>',views.vsingle,name='vsingle'),
    path('delete/<int:delid>',views.delete,name='delete'),
    path('deleteacc',views.deleteacc,name='deleteacc'),
    path('uparticle/<int:itmid>',views.uparticle,name='uparticle'),
    path('ajaxmthd',views.ajaxmthd, name='ajaxmthd'),
    path('myform',views.myform, name='myform'),
    path('display',views.display, name='display'),
    path('datadel',views.datadel, name='datadel'),
    path('dataedit',views.dataedit, name='dataedit'),
    path('updtdata',views.updtdata, name='updtdata'),
    #path('selectdata',views.selectdata, name='selectdata'),
    #path('selectdata/<int:id>',views.selectdata, name='selectdata'),
    url(r'^selectdata/$',views.selectdata),
    url(r'^selectdata/([0-9]+)$',views.selectdata),
    path('dashboard',views.dashboard, name='dashboard'),
    path('adregister', views.adregister, name='adregister'),
]