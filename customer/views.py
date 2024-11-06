from django.shortcuts import render,redirect

def customerclicked_view(request):
    return render(request,'customer/customerclicked.html')