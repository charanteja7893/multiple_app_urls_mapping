from django.test import TestCase

# Create your tests here.
def one(request):
    return render(request,'one.html')
def two(request):
    return render(request,'two.html')

