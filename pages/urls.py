from django.urls import path

from . import views


app_name = 'pages'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('open-source/', views.OpenSourceView.as_view(), name='open_source'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('bootstrap-weekpicker/', views.BootstrapWeekpickerView.as_view(), name='bootstrap_weekpicker'),
]
