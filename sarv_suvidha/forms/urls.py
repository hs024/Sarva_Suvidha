from django.urls import path
from .views import BogieChecksheetFormCreateView, WheelSpecificationView

urlpatterns = [
    path('api/forms/bogie-checksheet', BogieChecksheetFormCreateView.as_view()),
    path('api/forms/wheel-specifications', WheelSpecificationView.as_view()),  # ✅ combined GET and POST
]
