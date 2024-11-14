# views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework.response import Response
from .models import Role, Appraiser, Client, LoanStatus, Loan, Collateral, Payment
from .forms import RoleForm, AppraiserForm, ClientForm, LoanStatusForm, LoanForm, CollateralForm, PaymentForm
from django.http import JsonResponse
from .models import Client
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .repositories import AppraiserRepository
from .serializers import AppraiserSerializer
# Role Views
class RoleListView(ListView):
    model = Role
    template_name = '../templates/role_list.html'

class RoleCreateView(CreateView):
    model = Role
    form_class = RoleForm
    template_name = '../templates/role_form.html'
    success_url = reverse_lazy('role-list')

class RoleUpdateView(UpdateView):
    model = Role
    form_class = RoleForm
    template_name = '../templates/role_form.html'
    success_url = reverse_lazy('role-list')

class RoleDeleteView(DeleteView):
    model = Role
    template_name = '../templates/role_confirm_delete.html'
    success_url = reverse_lazy('role-list')

# Appraiser Views
class AppraiserListView(ListView):
    model = Appraiser
    template_name = '../templates/appraiser_list.html'

class AppraiserCreateView(CreateView):
    model = Appraiser
    form_class = AppraiserForm
    template_name = '../templates/appraiser_form.html'
    success_url = reverse_lazy('appraiser-list')

class AppraiserUpdateView(UpdateView):
    model = Appraiser
    form_class = AppraiserForm
    template_name = '../templates/appraiser_form.html'
    success_url = reverse_lazy('appraiser-list')

class AppraiserDeleteView(DeleteView):
    model = Appraiser
    template_name = '../templates/appraiser_confirm_delete.html'
    success_url = reverse_lazy('appraiser-list')

# Client Views
class ClientListView(ListView):
    model = Client
    template_name = '../templates/client_list.html'

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = '../templates/client_form.html'
    success_url = reverse_lazy('client-list')

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = '../templates/client_form.html'
    success_url = reverse_lazy('client-list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = '../templates/client_confirm_delete.html'
    success_url = reverse_lazy('client-list')

def clients_list_api(request):
    clients = Client.objects.all().values("id", "first_name", "last_name", "email", "phone")
    # Convert QuerySet to a list of dictionaries
    clients_data = list(clients)
    return JsonResponse(clients_data, safe=False)


# API for listing clients
def clients_list_api(request):
    clients = Client.objects.all().values("id", "first_name", "last_name", "email", "phone")
    clients_data = list(clients)
    return JsonResponse(clients_data, safe=False)

# API for creating a new client
class AppraiserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        appraisers = AppraiserRepository.get_all()
        serializer = AppraiserSerializer(appraisers, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        appraiser = AppraiserRepository.get_by_id(pk)
        serializer = AppraiserSerializer(appraiser)
        return Response(serializer.data)

    def create(self, request):
        appraiser = AppraiserRepository.create(request.data)
        serializer = AppraiserSerializer(appraiser)
        return Response(serializer.data)

    def update(self, request, pk=None):
        appraiser = AppraiserRepository.update(pk, request.data)
        serializer = AppraiserSerializer(appraiser)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        AppraiserRepository.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)