from django.shortcuts import render
def home_view(request):
    return render(request, 'insurance/index.html')

#renders to the insurance/index.html page
