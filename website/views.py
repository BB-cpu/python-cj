from django.shortcuts import render

def home(request):
    if request.method == "POST":
        appointment= request.POST['appointment']
        appointment_email= request.POST['appointment_email']
        #appointment_date = request.POST['appointment_date']
        #appointment_time = request.POST['appointment_time']
        message = request.POST['message']

        return render(request, 'home.html', {'appointment': appointment})

    else:
        return render(request, 'home.html', {})

def contact(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        message = request.POST['message']


        return render(request,'contact.html', {'fname': fname})

    else:
        return render(request,'contact.html', {})
def about(request):
    return render(request, 'about.html', {})
def doctors(request):
    return render(request, 'doctors.html', {})
def news(request):
    return render(request, 'news.html', {})
def services(request):
    return render(request, 'services.html', {})






