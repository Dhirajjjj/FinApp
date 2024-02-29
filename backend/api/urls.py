from django.urls import path

from . import views

urlpatterns = [
    path("account/", views.AccountMixinView.as_view()),
    path("transactions/", views.TransactionMixinView.as_view()),

    path("account/investments/deposits", views.FixedDepositMixinView.as_view()),
    path("account/investments/stocks", views.StockMixinView.as_view()),
    path("account/investments/bonds", views.BondMixinView.as_view()),
    path("account/investments/mutualfunds", views.MutualFundMixinView.as_view()),
    
    path("account/payments/loans", views.LoanMixinView.as_view()),
    path("account/payments/pf", views.ProvidentFundMixinView.as_view()),
    path("account/payments/insurance", views.InsuranceMixinView.as_view()),
]