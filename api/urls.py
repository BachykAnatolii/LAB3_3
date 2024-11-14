from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'roles', views.RoleViewSet)
router.register(r'appraisers', views.AppraiserViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'loan-statuses', views.LoanStatusViewSet)
router.register(r'loans', views.LoanViewSet)
router.register(r'collaterals', views.CollateralViewSet)
router.register(r'payments', views.PaymentViewSet)

urlpatterns = [
    path('positions/', views.position_list_view, name='position_list'),
    path('positions/add/', views.add_position_view, name='add_position'),
    path('positions/edit/<int:position_id>/', views.edit_position_view, name='edit_position'),
    path('positions/delete/<int:position_id>/', views.delete_position_view, name='delete_position'),
]
