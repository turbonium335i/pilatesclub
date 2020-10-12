from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from django.contrib import messages
from . filters import memberFilter, UserFilter
from django.db.models import Sum
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer




def base(request):

    clients = client.objects.all().order_by('-registered')

    total = client.objects.all().count

    return render(request, 'members/base.html', {'clients': clients, 'total':total})

def newmember(request):

    form = addClient()

    if request.method == 'POST':
        form = addClient(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Member Added >>> {name} <<<')
            return redirect('base')

    context = {'form': form}

    return render(request, 'members/add_member.html', context)


def operations(request):

    sales = sale.objects.all().order_by('-timestamp')

    total = sale.objects.all().count

    x = sale.objects.all().aggregate(sum_order=Sum("paid"))

    totalsales = x['sum_order']

    return render(request, 'members/operations.html', {'sales': sales, 'total': total, 'totalsales': totalsales})

def lessons(request):

    clientlessons = lesson.objects.all()

    total = lesson.objects.all().count

    return render(request, 'members/lessons.html', {'clientlessons': clientlessons, 'total': total})


def memberinfo(request, pk):
    clients = client.objects.get(id=pk)

    clientlessons = clients.lesson_set.all()
    clientpayments = clients.sale_set.all()


    context = {'clients': clients, 'clientlessons':clientlessons, 'clientpayments':clientpayments}
    return render(request, 'members/memberinfo.html', context)

def searchfilter(request):

    searchedclient = client.objects.all().order_by('-registered')
    clientfilter = UserFilter(request.GET, queryset=searchedclient)
    searchedclient = clientfilter.qs

    return render(request, 'members/searchclient.html', {'searchedclient': searchedclient, 'clientfilter': clientfilter})





def generateWord(request, pk):

    wordbank = word.objects.get(id=pk)
    # vlist = random.choice(wordbank)

    # if request.method == 'POST':
    #     tput = request.POST['tname']
    #     if tput == wordbank.meaning:
    #         return redirect('vocab')

    return render(request, 'members/generateword.html', {'wordbank': wordbank})

def vocab(request):
    x = 'knavery'
    yy = word.objects.all()

    zzz = random.choice(yy)
    typed = 'cookie monster'

    if request.method == 'POST':

        typed = request.POST['tname']
        return redirect('generateword', typed)
        # if typed == zzz.meaning:
        #     messages.success(request, f'correct')
        #     return redirect('vocab')
        # check = lambda a, b: a * b
        # print('this is answer ', check(5, 6))


    return render(request, 'members/vtesting.html', {'x': x, 'typed': typed, 'zzz': zzz})

def wordput(request):
    print(request.POST['tname'])
    fromOtherPage = request.POST['tname']

    print(request.GET)

    return render(request, 'members/wordput.html', {'fromOtherPage': fromOtherPage})

def javacore(request):
    return render(request, 'members/xjavacore.html')

@api_view(['GET', 'POST'])
def apiOverview(request):
    api_urls= {
        'list': 'task-list',


    }

    return Response(api_urls)

@api_view(['GET', 'POST'])
def memberList(request):
    apimembers = client.objects.all()
    serializer = TaskSerializer(apimembers, many=True)
    return Response(serializer.data)
