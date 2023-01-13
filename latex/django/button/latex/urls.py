from django.urls import path
from . import views

urlpatterns = [
    path('',views.Hello),
    path('conv',views.conv,name='conv'),
    path('store',views.store,name='store'),
    path('add',views.add,name='add'),
    path('final',views.final,name='final'),
]