from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView, Request

from utils.utils import handle_uploaded_file

from .forms import UploadFileForm
from .models import FinancialTransaction
from .serializers import FinancialTransactionSerializer


class FinancialTransactionUploadCreateView(APIView):
    def get(self, request: Request):
        form = UploadFileForm()
        return render(request, 'files/model_form_upload.html', {'form': form})

    def post(self, request: Request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/api/cnab/upload/')


class FinancialTransactionListView(ListAPIView):
    serializer_class = FinancialTransactionSerializer
    queryset = FinancialTransaction.objects.all()
