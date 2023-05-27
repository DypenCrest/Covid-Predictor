from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserCreationForm
from django.contrib import messages
import pandas as pd
from .models import CovidPrediction
# Create your views here.
def home_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request,("Login Failed!"))
            return redirect('/')
    else:
        return render(request,'home.html',{})

#Dashboard
def dashboard_view(request):
    return render(request,'dashboard.html')

#register user
def reg(request):
    form=CustomUserCreationForm()
    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,("Registration Successful!"))
            return redirect('/')

    return render(request, 'account/register.html', {'form':form})

def log_out(request):
    logout(request)
    messages.success(request,("You were logged out!"))
    return redirect('/')

#Main prediction function reads the pickle file data
def predictor(request):
    model = pd.read_pickle('covid_model.pickle')

    sex = request.GET['sex']
    intubed = request.GET['intubed']
    pneumonia = request.GET['pneumonia']
    age = request.GET['age']
    diabetes = request.GET['diabetes']
    copd = request.GET['copd']
    asthma = request.GET['asthma']
    hypertension = request.GET['hypertension']
    cardiovascular = request.GET['cardiovascular']
    obesity = request.GET['obesity']
    renal_chronic = request.GET['renal_chronic']
    tobacco = request.GET['tobacco']
    contact_other_covid = request.GET['contact_other_covid']
    icu = request.GET['icu']




    lis = []

    lis.append(sex)
    lis.append(intubed)
    lis.append(pneumonia)
    lis.append(age)
    lis.append(diabetes)
    lis.append(copd)
    lis.append(asthma)
    lis.append(hypertension)
    lis.append(cardiovascular)
    lis.append(obesity)
    lis.append(renal_chronic)
    lis.append(tobacco)
    lis.append(contact_other_covid)
    lis.append(icu)

    print(lis)

    classification = model.predict([lis])

    CovidPrediction.objects.create(
        sex=sex,
        intubed=intubed,
        pneumonia=pneumonia,
        age=age,
        diabetes=diabetes,
        copd=copd,
        asthma=asthma,
        hypertension=hypertension,
        cardiovascular=cardiovascular,
        obesity=obesity,
        renal_chronic=renal_chronic,
        tobacco=tobacco,
        contact_other_covid=contact_other_covid,
        icu=icu,
        classification=classification[0]
    )

    return render(request, 'predict.html', {'classification_result': classification[0]})



def db_record(request):
    covid_predictions = CovidPrediction.objects.all()

    context = {
        'covid_records': covid_predictions
    }

    return render(request, 'database/db.html', context)

       


def delete(request, pk):
    covid_data = CovidPrediction.objects.get(id=pk)
    covid_data.delete()
    return redirect('records')