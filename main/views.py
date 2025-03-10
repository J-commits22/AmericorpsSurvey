from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from . forms import CreateUserForm, LoginForm
from . forms import StudentForm
from . models import Student
from django.contrib.auth.models import auth # type: ignore
from django.contrib.auth import authenticate # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib import messages # type: ignore



def index(request):
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():

            password = request.POST.get('password')

            username = request.POST.get('username')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect('home')
            
        else:

            for error in form.errors.values():

                messages.error(request, error)
            
            
    context = {'loginform':form}

    return render(request, "index.html", context=context) 


def successpage(request):
    return render(request, "successPage.html")


def successpagetwo(request):
    return render(request, "successPageTwo.html")


def signup(request):

    form = CreateUserForm()

    if request.method == "POST": 

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('successpage')
        else:
            for error in form.errors.values():

                messages.error(request, error)

    context = {'registerform':form}

    return render(request, 'signup.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('successpagetwo')
        else:
            return HttpResponse(print(form.errors))
    else:
        form = StudentForm()
    return render(request, 'registration.html', {'form': form})


@login_required(login_url='index')
def home(request):
    error_message = None

    if 'student_id' in request.GET:
        student_id = request.GET['student_id']

        # Check if the input is a valid number
        try:
            student_id = int(student_id)  # Try to convert input to an integer
        except ValueError:
            error_message = "Invalid input. Please enter a valid student ID."
            return render(request, 'home.html', {'error_message': error_message})

        try:
            student = Student.objects.get(student_id=student_id)
            return render(request, 'home.html', {'student': student})
        except Student.DoesNotExist:
            error_message = "Student ID Not Found"
    else:
        error_message = " "

    return render(request, 'home.html', {'error_message': error_message})


def student_list(request):
    student = Student.objects.all()
    return render(request, 'home.html', {'student': student})

def logout(request):

    auth.logout(request)

    return redirect('index')



