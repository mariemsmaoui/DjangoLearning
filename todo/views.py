from django.shortcuts import render
from rest_framework import viewsets
from .models import  ToDo
from .serializers import  ToDoSerializer
# Create your views here.
#@csrf_exempt
import csv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class ToDoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()


@csrf_exempt
def csv_upload(request):
    if request.method == 'POST' and request.FILES['file']:
        csv_file = request.FILES['file']

        # Check if the uploaded file is a CSV file
        if not csv_file.name.endswith('.csv'):
            return JsonResponse({'error': 'File is not a CSV file'}, status=400)

        # Decode and process the CSV file
        decoded_file = csv_file.read().decode('utf-8')
        csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')

        # Process the CSV data (example: print each row)
        for row in csv_data:
            print(row)

        return JsonResponse({'message': 'CSV file uploaded and processed successfully'}, status=200)

    return JsonResponse({'error': 'No file uploaded'}, status=400)
