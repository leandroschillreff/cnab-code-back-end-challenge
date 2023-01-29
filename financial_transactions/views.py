from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView, Request

from utils.utils import handle_uploaded_file

from .forms import UploadFileForm
from .models import FinancialTransaction
from .serializers import (FinancialTransactionSerializer,
                          FinancialTransactionStoreSerializer)
from django.contrib import messages


class FinancialTransactionUploadCreateView(APIView):
    serializer_class = FinancialTransactionSerializer

    def get(self, request: Request):
        form = UploadFileForm()
        return render(request, 'files/model_form_upload.html', {'form': form})

    def post(self, request: Request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            messages.info(
                request, 'Your CNAB file was successfully submitted!')
            return HttpResponseRedirect('/api/cnab/upload/')


class FinancialTransactionListView(ListAPIView):
    serializer_class = FinancialTransactionSerializer
    queryset = FinancialTransaction.objects.all().order_by('id')


class FinancialTransactionListStoreView(ListAPIView):
    serializer_class = FinancialTransactionStoreSerializer
    queryset = FinancialTransaction.objects.values('store_name', 'store_owner').annotate(
        total_balance=Sum('value')).order_by('store_name')
