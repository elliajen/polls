from django.urls import path

from poll import views

app_name = 'poll'

urlpatterns = [
    # poll/
    path('', views.index, name='index'),
    # poll/<int:question_id>/
    path('poll/<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/result/', views.result, name='result')
]