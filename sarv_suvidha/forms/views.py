from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *

class BogieChecksheetFormCreateView(generics.CreateAPIView):
    serializer_class = BogieChecksheetFormSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        form = serializer.save()
        return Response({
            "success": True,
            "message": "Bogie checksheet submitted successfully.",
            "data": {
                "formNumber": form.formNumber,
                "inspectionBy": form.inspectionBy,
                "inspectionDate": str(form.inspectionDate),
                "status": form.status
            }
        }, status=status.HTTP_201_CREATED)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class WheelSpecificationView(APIView):
    def get(self, request):
        queryset = WheelSpecification.objects.all()
        form_number = request.GET.get('formNumber')
        submitted_by = request.GET.get('submittedBy')
        submitted_date = request.GET.get('submittedDate')

        if form_number:
            queryset = queryset.filter(formNumber=form_number)
        if submitted_by:
            queryset = queryset.filter(submittedBy=submitted_by)
        if submitted_date:
            queryset = queryset.filter(submittedDate=submitted_date)

        serializer = WheelSpecificationSerializer(queryset, many=True)
        return Response({
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": serializer.data
        })

    def post(self, request):
        serializer = WheelSpecificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        spec = serializer.save()
        return Response({
            "success": True,
            "message": "Wheel specification submitted successfully.",
            "data": {
                "formNumber": spec.formNumber,
                "submittedBy": spec.submittedBy,
                "submittedDate": str(spec.submittedDate),
                "status": spec.status
            }
        }, status=status.HTTP_201_CREATED)
