from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    # User Input
    number_list = list()

    for i in range(6):
        number = request.GET['number'+str(i+1)]
        number_list.append(int(number))

    # Random Output
    random_list = list()
    
    for j in range(7):
        number = random.randrange(1,46)
        random_list.append(number)

    return render(request, 'result.html', {'number_list':number_list, 'random_list':random_list})