from django.shortcuts import render,HttpResponse
from math import factorial
# Create your views here.
def square(request):
    n=5
    sq=n*n
    return render(request,'index1.html',{'p1':sq,'p2':n})
def fact(request):
    n=6
    fact1=1
    for i in range(1,n+1,1):
        fact1=fact1*i
    return render(request,'index.html',{'param1':fact1,'param2':n})

def factorial(request):

    fact_list = []
    for num in range(3, 9):
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        fact_list.append((num, fact))
    return render(request,'index3.html',{'fact_list':fact_list})


def factorial_input(request):
    if request.method == 'POST':
        num = int(request.POST.get('num'))
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return HttpResponse(f"The factorial of {num} is {fact}")
    return render(request, 'factorial_input.html')

def get_possibilities(s):
    if len(s) == 1:
        return [s]
    possibilities = []
    for i in range(len(s)):
        char = s[i]
        remaining_str = s[:i] + s[i+1:]
        for p in get_possibilities(remaining_str):
            possibilities.append(char + p)
    return possibilities

def index(request):
    if request.method == 'POST':
        input_string = request.POST.get('input_string')
        permutations = get_possibilities(input_string)
        return render(request, 'combinations.html', {'permutations': permutations, 'input_string': input_string})
    return render(request, 'combinations.html')


