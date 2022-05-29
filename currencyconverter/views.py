from django.shortcuts import render
from .models import Currency
from .forms import CurrencyForm
# from django.shortcuts import redirect

from .serializers import CurrencySerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
# def converter(request):
#     # dollar_value = int(request.GET.get("dollar", 0))
#     # result = dollar_value / 400
#     result = ""
#     if request.method == "POST":
#         # dollar_value = int(request.POST["dollar"])
#         # b = Currency(currency_value=dollar_value)
#         # b.save()
#         currencyform = CurrencyForm(request.POST)
#         if currencyform.is_valid():
#             dollar_value = currencyform.cleaned_data["currency_value"]
#             result = int(dollar_value) * 400
#             b = Currency(currency_value=dollar_value)
#             b.save()
#             # return redirect('converter')
#     else:
#         currencyform = CurrencyForm
#     context = {
#         "result": result,
#         "currencyform": currencyform
#     }
#     return render(request, 'currencyconverter/index.html', context)


@api_view(['GET','POST'])
def converter(request):
    if request.method == 'GET':
        currency = Currency.objects.all()
        serializers = CurrencySerializers(currency,many=True)
        return Response(serializers.data)

    elif(request.method == 'POST'):
        serializers = CurrencySerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)