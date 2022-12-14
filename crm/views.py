from django.shortcuts import render, redirect
from crm.forms import ProjectForm,CustomerForm,ProfileForm,NewUserForm,TaskForm
from crm.models import Customer, Project,Profile,Task
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm ,UserChangeForm

def home(request):
    page_title = 'dashboard'
    all_projects = Project.objects.all()
    total_projects = all_projects.count()
    delivered = all_projects.filter(status='fait').count()
    pending = all_projects.filter(status='en attente').count()
    processing = all_projects.filter(status='en traitement').count()
    all_customers = Customer.objects.all()
    total_customers = all_customers.count()
    total_profiles = Customer.objects.all().count()

    context = {
        'title': page_title,
        'projects': all_projects,
        'total_projects': total_projects,
        'delivered': delivered,
        'pending': pending,
        'processing':processing,
        'customers': all_customers,
        'total_customers': total_customers,
        'total_profiles':total_profiles
    }
    template = 'crm/dashboard.html'
    return render(request, template, context)


def project(request):
    page_title = 'tous les Projets'
    all_projects = Project.objects.all()
    all_projects_count = Project.objects.all().count()

    context = {
        'title': page_title, 
        'data': all_projects, 
        'data_count':all_projects_count
    }
    template = 'crm/project_list.html'

    return render(request, template, context)

def createProject(request):
    page_title = 'Créer un projet'
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'title': page_title,
        'form': form
    }

    template = 'partials/form.html'
    return render(request, template, context)

def updateProject(request, pk):
    page_title = 'mise à jour projet'
    proj = Project.objects.get(id=pk)
    form = ProjectForm(instance=proj)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=proj)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'title': page_title,
        'form': form
    }

    template = 'partials/form.html'
    return render(request, template, context)

def deleteProject(request, pk):
    page_title = 'Supprimer le projet'
    Proj = Project.objects.get(id=pk)

    if request.method == 'POST':
        Proj.delete()
        return redirect('/')

    context = {
        'title': page_title,
        'item': Proj
    }

    template = 'partials/delete.html'
    return render(request, template, context)

def task(request):
    page_title = 'tous les Tâches'
    all_tasks = Task.objects.all()
    all_tasks_count = Task.objects.all().count()

    context = {
        'title': page_title, 
        'data': all_tasks, 
        'data_count':all_tasks_count
    }
    template = 'crm/task_list.html'

    return render(request, template, context)

def createTask(request):
    page_title = 'Créer un Tâche'
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'title': page_title,
        'form': form
    }

    template = 'partials/form.html'
    return render(request, template, context)

def updateTask(request, pk):
    page_title = 'mise à jour Tâche'
    tas = Task.objects.get(id=pk)
    form = TaskForm(instance=tas)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tas)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'title': page_title,
        'form': form
    }

    template = 'partials/form.html'
    return render(request, template, context)

def deleteTask(request, pk):
    page_title = 'Supprimer la Tâche'
    tas = Task.objects.get(id=pk)

    if request.method == 'POST':
        tas.delete()
        return redirect('/')

    context = {
        'title': page_title,
        'item': tas
    }

    template = 'partials/delete.html'
    return render(request, template, context)


def customer(request):
    page_title = 'tous les clients'
    customers = Customer.objects.all()
    customers_count = Customer.objects.all().count()
    context = {
        'title': page_title,
        'data': customers,
        'data_count':customers_count
    }
    template = 'crm/customer_list.html'
    return render(request, template, context)

def createCustomer(request):
    page_title = 'Créer un client'
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'title': page_title,
        'form': form
    }

    template = 'partials/form.html'
    return render(request, template, context)

def updateCustomer(request, pk):
    page_title = 'mise à jour client'
    Custom = Customer.objects.get(id=pk)
    form = CustomerForm(instance=Custom)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'title': page_title,
        'form': form
    }

    template = 'partials/form.html'
    return render(request, template, context)

def deleteCustomer(request, pk):
    page_title = 'Supprimer le client'
    Custom = Customer.objects.get(id=pk)

    if request.method == 'POST':
        Custom.delete()
        return redirect('/')

    context = {
        'title': page_title,
        'item': Custom
    }

    template = 'partials/delete.html'
    return render(request, template, context)


def profile(request):
    page_title = 'tous les Profils'
    profile = Profile.objects.all()
    profile_count = Profile.objects.all().count()

    context = {
        'title': page_title,
        'data': profile,
        'data_count':profile_count
    }
    template = 'crm/profile_list.html'
    return render(request, template, context)

def createProfile(request):
    page_title = 'Créer un Profil'
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'title': page_title,
        'form': form
    }

    template = 'partials/form.html'
    return render(request, template, context)

def updateProfile(request, pk):
    page_title = 'mise à jour le Profil'
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'title': page_title,
        'form': form
    }

    template = 'partials/form.html'
    return render(request, template, context)

def deleteProfile(request, pk):
    page_title = 'Supprimer le Profil'
    Profil = Profile.objects.get(id=pk)

    if request.method == 'POST':
        Profil.delete()
        return redirect('/')

    context = {
        'title': page_title,
        'item': Profil
    }

    template = 'partials/delete.html'
    return render(request, template, context)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('/')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="crm/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(email=email, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {email}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid email or password.")
		else:
			messages.error(request,"Invalid email or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="crm/login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    return redirect('/')
