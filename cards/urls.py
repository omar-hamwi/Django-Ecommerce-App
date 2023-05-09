from django.urls import path

from . import views
from django.conf.urls.static import static 
from django.conf import settings
urlpatterns = [
    path("",views.home),
    path("category/<slug:val>",views.CategoryView.as_view(), name="category"),
    # path("new", views.CardCreateView.as_view(), name="card-create"),
#     path("edit/<int:pk>", views.CardUpdateView.as_view(), name="card-update"),
#     path("box/<int:box_num>", views.BoxView.as_view(), name="box"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
