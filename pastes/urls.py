from django.urls import path
from .views import PasteCreateView, PasteDetailView

urlpatterns = [
    path('pastes/', PasteCreateView.as_view()),
    path('pastes/<uuid:paste_id>/', PasteDetailView.as_view()),
]
