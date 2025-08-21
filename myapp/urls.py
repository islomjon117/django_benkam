from django.urls import path
from . import views
from .views import certificates, team_view

urlpatterns = [
    path('', views.home, name='home-1'),
    path('', views.home2, name='home-2'),
    path('contact', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog-inner/', views.blog2, name='blog2'),
    path('', views.not_found, name='not_found'),
    path('portfolio/', views.portfolio1, name='portfolio1'),
    path('portfolio-2/', views.die_shop_list, name='portfolio2_list'),
    path('portfolio-3', views.offer_list, name='portfolio3_list'),
    path('portfolio-2/<int:id>/', views.die_shop_detail, name='project1'),
    path('project-2', views.project2, name='project2'),
    path('project-3/<int:id>/', views.portfolio_detail, name='die_shop_detail'),
    path('project-4/', views.project4, name='project4'),
    path('project-5/<int:id>/', views.project5, name='project5'),
    # path('', views.project2, name='project6'),
    path('portfolio/<int:id>/', views.portfolio_detail, name='project-3'),
    path('publication/', views.publication, name='publication'),
    path('service/', views.service, name='service'),
    path('services/', views.services, name='services'),
    # path('', views.team, name='team'),
    path('team/', team_view, name='team'),
    path('team/<int:pk>/', views.team_detail, name='team_detail'),
    path('certificates/', views.certificates, name='certificates'),
    
]
