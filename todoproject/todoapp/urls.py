from . import views
from django.urls import path

urlpatterns = [
path('',views.index,name='index'),
path('delete/<int:id>/',views.delete,name='delete'),
path('update/<int:id>/',views.update,name='update'),
path('cbvindex',views.Todolistview.as_view(),name='cbvindex'),
path('cbvdetail/<int:pk>/',views.Tododetailview.as_view(),name='cbvdetail'),
path('cbvedit/<int:pk>/',views.Todoupdateview.as_view(),name='cbvedit'),
path('cbvdelete/<int:pk>/',views.Tododeleteview.as_view(),name='cbvdelete'),
]