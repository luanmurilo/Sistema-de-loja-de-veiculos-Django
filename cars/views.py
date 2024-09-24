from django.shortcuts import render

# Função de teste de response
def testResponse(request):
    return render(request, 'cars.html')

