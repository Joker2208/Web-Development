from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.dashboard, name="dashboard"),
    path("products/", views.product_list, name="product_list"),
    path("products/new/", views.product_create, name="product_create"),
    path("products/<int:pk>/edit/", views.product_edit, name="product_edit"),
    path("products/<int:pk>/delete/", views.product_delete, name="product_delete"),
    path("categories/new/", views.category_create, name="category_create"),
    path("stock/move/", views.stock_move, name="stock_move"),
    path("stock/history/", views.transaction_list, name="transaction_list"),
    path("reports/", views.report, name="report"),
    path("reports/export.csv", views.report_csv, name="report_csv"),
]
