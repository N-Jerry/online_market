from django.urls import path

from . import views

app_name = 'item'
urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete', views.delete, name='delete'),
    #path('<int:pk>/edit', views.edit, name='edit'),
    path('', views.browse, name='browse'),
    path("<int:pk>/edit", views.edit.as_view(template_name = 'item/form.html'), name="edit"),
]
