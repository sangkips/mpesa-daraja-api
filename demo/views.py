from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        cl = MpesaClient()
        phone_number = request.POST['phone_number']
        amount = int(request.POST['amount'])
        account_reference = 'reference'
        transaction_desc = request.POST['transaction_desc']
        callback_url = 'https://darajambili.herokuapp.com/express-payment'
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        
        if isinstance(response, dict):
            response_data = response  # Assuming response is already in the correct format
        else:
            response_data = {
                "message": "Success"  # Adjust according to your actual response structure
            }
        
        return JsonResponse(response_data)
    return render(request, 'index.html')

def stk_push_callback(request):
        data = request.body
        
        return HttpResponse(data)
