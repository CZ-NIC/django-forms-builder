from django.urls import path

from forms_builder.forms import views

urlpatterns = [
    path("<slug:slug>/sent/", views.form_sent, name="form_sent"),
    path("<slug:slug>/", views.form_detail, name="form_detail"),
]
