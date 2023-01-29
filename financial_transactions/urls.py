from django.urls import path
from . import views

urlpatterns = [
    path("cnab/upload/", views.FinancialTransactionUploadCreateView.as_view()),
    path("cnab/list/", views.FinancialTransactionListView.as_view()),
    path("cnab/balance/", views.FinancialTransactionListStoreView.as_view()),
]
