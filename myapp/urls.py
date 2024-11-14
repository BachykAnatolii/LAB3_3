# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (RoleListView, RoleCreateView, RoleUpdateView, RoleDeleteView,
                    AppraiserListView, AppraiserCreateView, AppraiserUpdateView, AppraiserDeleteView,
                    ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, AppraiserViewSet)
from . import views


router = DefaultRouter()
router.register(r'appraisers', AppraiserViewSet, basename='appraiser')

urlpatterns = [
    path('', include(router.urls)),
    # Role URLs
    path('roles/', RoleListView.as_view(), name='role-list'),
    path('roles/add/', RoleCreateView.as_view(), name='role-add'),
    path('roles/<int:pk>/edit/', RoleUpdateView.as_view(), name='role-edit'),
    path('roles/<int:pk>/delete/', RoleDeleteView.as_view(), name='role-delete'),

    # Appraiser URLs
    path('appraisers/', AppraiserListView.as_view(), name='appraiser-list'),
    path('appraisers/add/', AppraiserCreateView.as_view(), name='appraiser-add'),
    path('appraisers/<int:pk>/edit/', AppraiserUpdateView.as_view(), name='appraiser-edit'),
    path('appraisers/<int:pk>/delete/', AppraiserDeleteView.as_view(), name='appraiser-delete'),

    # Client URLs
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/add/', ClientCreateView.as_view(), name='client-add'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='client-edit'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),

]
