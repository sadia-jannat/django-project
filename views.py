from django.shortcuts import render,redirect




# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]
# oper ar part katbana..ata katly kiso ase na


def home(request):
    context={
        'posts': posts
    }
    return render(request,'food/home.html',context)

def about(request):
    return render(request, 'food/about.html')




def chart(request):
    return render(request,'food/chart.html')

def bmi(request):
    return render(request,'food/bmi.html' )



def add(request):

    return render(request, 'food/add.html')


def other(request):


    return render(request, 'food/other.html')

def cal(request):
    a=int(request.GET['a1'])
    b=int(request.GET['a2'])
    c=a+b

    return render(request,'../other/',{'result':c})



def res(request):

    return render(request, 'food/res.html')


def math(request):
    return render(request,'food/math.html')

def teatment(request):
    return render(request,'food/teatment.html')


def brain(request):
    return render(request,'food/brain.html')

def health(request):
    return render(request,'food/health.html')

def food(request):
    return render(request,'food/food.html')


def women(request):
    return render(request,'food/women.html')


#practis 2

def welcome(request):
    try:
        ans=0
        n1=int(request.GET.get('num1'))
        n2 = int(request.GET.get('num2'))
        ans=n1+n2

    except:
        pass
    return render(request, 'food/welcome.html', {'output':ans})






