from django.shortcuts import render,redirect
# from django.http import HttpResponseRedirect
from .forms import *
global prevptr, present, nextptr


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        var = Information.objects.filter(name__contains=searched)
        return render(request, 'Resumer/search.html', {'searched':searched,'var':var})
    else:
        return render(request, 'Resumer/home.html', {})


def inform(request, key="1"):
    submitted, add_feature = False, False
    name, next = "", ""
    if key == "1":
        name = "Information"
        next = "2"
        add_feature = False
    elif key == "2":
        name = "Education"
        add_feature = True
    elif key == "3":
        name = "Experience"
        add_feature = True
    elif key == "4":
        name = "Organization"
        add_feature = True
    elif key == "5":
        name = "Contacts"
        add_feature = True
    else:
        name = "Addresses"
        add_feature = True
    if request.method == 'POST':
        if key == "1":
            form = Inform(request.POST)
        elif key == "2": # edu
            form = EduForm(request.POST)
        elif key == "3": # exp
            form = ExpForm(request.POST)
        elif key == "4": # organizatin
            form = OrgForm(request.POST)
        elif key == "5": # contacts
            form = ContForm(request.POST)
        else: # addresses
            form = AddrsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/infrom/{key}?submitted=True')
    else:
        if key == "1":
            form = Inform
        elif key == "2": # edu
            form = EduForm
        elif key == "3": # exp
            form = ExpForm
        elif key == "4": # organizatin
            form = OrgForm
        elif key == "5": # contacts
            form = ContForm
        else: # addresses
            form = AddrsForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "Resumer/infrom.html",
                  {'name': name, 'form': form, 'add_feature': add_feature, 'submitted': submitted, 'next': next})


def eduform(request):
    submitted = False
    add_feature = True
    form = EduForm
    name = "Education"
    if submitted:
        pass
    else:
        pass
    return render(request, "Resumer/infrom.html", {'name': name, 'form': form, 'add_feature': add_feature})


def expform(request):
    submitted = False
    add_feature = True
    form = ExpForm
    name = "Experience"
    if submitted:
        pass
    else:
        pass
    return render(request, "Resumer/infrom.html", {'name': name, 'form': form, 'add_feature': add_feature})


def orgform(request):
    add_feature = True
    form = OrgForm
    name = "Organization"
    return render(request, "Resumer/infrom.html", {'name': name, 'form': form, 'add_feature': add_feature})


def home(request):
    return render(request, 'Resumer/home.html', {})


def resume(request):
    style = '1'
    name = "Gaurav Bhardwaj"
    desc = "This is Gaurav Bhardwaj, from Jalandhar, Punjab, India, 19 years old Student currently pursuing Bachelor’s Degree in Computer Science and Engineering from Dr. B. R. Ambedkar National Institute of Technology, Jalandhar. I was born on 24th November, 2000, in Jalandhar."
    email = "bhardwajg2411@gmail.com"
    linkedin = "linkedin.com/in/gaurav-bhardwaj-666945177"
    contacts = "628-391-3449"
    body_headers = {'1': 'Education', '2': 'Acheievements', '3': 'Experience', '4': 'Key Skills'}
    edu = ["MARCH’2016 | MATRIC QUALIFICATION, APEE JAY SCHOOL, MAHAVIR MARG, JALANDHAR, PUNJAB, INDIA | CGPA: 8.8",
            "MARCH’2018 | HIGHER EDUCATION, APEE JAY SCHOOL, MAHAVIR MARG, JALANDHAR, PUNJAB, INDIA | percentage : 88.87%",
            "JULY'2018-22 | PERSUING BACHELOR DEGREE, DR. B. R. AMEDKAR NATIONAL INSTITUTE OF TECHNOLOGY, JALANDHAR,"
            " PUNJAB, INDIA | First year CGPA : 6.93 , Second year CGPA: 6.97"]
    ach = ['Experience in programming languages – C, C++, Python.', 'Knowledge of Data Structures and Algorithms,'
           ' Database Management system, Networking, Machine Learning.',
           'Experience with Competitive programming.']
    exp = ['Record Keeping project with python and Sql',
              'COVID Patient Identification software using Decision tree Classifier, Python GUI, Jupyter Notebook.',
              'List Recommender System using machine learning.',
              'Project software for searching elements in a List using various searching algorithms like '
              'Binary Search, graph searching, hashing technique, etc.',
              'CV maker application in GUI, Web-App using tkinter, Django']
    skills = ['Creativity', 'Punctuality', 'Communication', 'Team Work']
    body = {'education': edu,'ach': ach, 'experience': exp, "skill": skills}
    form = {'name': name, 'desc': desc, 'email': email, 'linkedin': linkedin,'contacts': contacts, 'body_header': body_headers, 'body': body}

    return render(request, 'Resumer/Resume.html', {'style': style,'form': form})