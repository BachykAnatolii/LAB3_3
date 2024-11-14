from rest_framework import viewsets
from myapp.models import Role, Appraiser, Client, LoanStatus, Loan, Collateral, Payment
from .serializers import RoleSerializer, AppraiserSerializer, ClientSerializer, LoanStatusSerializer, LoanSerializer, CollateralSerializer, PaymentSerializer
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .NetworkHelper import NetworkHelper
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class AppraiserViewSet(viewsets.ModelViewSet):
    queryset = Appraiser.objects.all()
    serializer_class = AppraiserSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class LoanStatusViewSet(viewsets.ModelViewSet):
    queryset = LoanStatus.objects.all()
    serializer_class = LoanStatusSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class CollateralViewSet(viewsets.ModelViewSet):
    queryset = Collateral.objects.all()
    serializer_class = CollateralSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
def position_list_view(request):
    positions = NetworkHelper.get_positions()
    return render(request, 'position_list.html', {'positions': positions})

def position_detail_view(request, position_id):
    position = NetworkHelper.get_position_by_id(position_id)
    return render(request, 'position_detail.html', {'position': position})

def add_position_view(request):
    if request.method == 'POST':
        data = {
            'position_title': request.POST['position_title'],
            'base_salary': request.POST['base_salary'],
        }
        NetworkHelper.create_position(data)
        return redirect(reverse('position_list'))
    return render(request, 'add_position.html')

def edit_position_view(request, position_id):
    position = NetworkHelper.get_position_by_id(position_id)
    if request.method == 'POST':
        data = {
            'position_title': request.POST['position_title'],
            'base_salary': request.POST['base_salary'],
        }
        NetworkHelper.update_position(position_id, data)
        return redirect(reverse('position_list'))
    return render(request, 'edit_position.html', {'position': position})

def delete_position_view(request, position_id):
    if request.method == 'POST':
        NetworkHelper.delete_position(position_id)
        return redirect(reverse('position_list'))
    position = NetworkHelper.get_position_by_id(position_id)
    return render(request, 'delete_position.html', {'position': position})