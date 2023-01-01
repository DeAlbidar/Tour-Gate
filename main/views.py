from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, Folder
from .forms import CreateNewList, NewFolderForm, NewFolderFileForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.conf import settings


def index(response):
	return render(response, "main/index.html", {})

def about(response):
	return render(response, "main/about.html", {})

def contact(response):
	return render(response, "main/contact.html", {})

def gallery(response):
	return render(response, "main/gallery.html", {})

@login_required
def drive(response):
	user_folder = None
	if response.method == 'POST':
		form = NewFolderForm(response.POST)
		if form.is_valid():
			user_folder = form.save(commit=False)
			user_folder.save()
			response.user.folder.add(user_folder)
	else:
		form = NewFolderForm()
	return render(response, "main/drive.html", {"form":form})

@login_required
def folder(response):
	user_folder = None
	if response.method == 'POST':
		form = NewFolderForm(response.POST)
		if form.is_valid():
			user_folder = form.save(commit=False)
			user_folder.save()
			response.user.folder.add(user_folder)
			next = response.POST.get('next', '/')
			return HttpResponseRedirect(next)
	else:
		form = NewFolderForm()
	return render(response, "main/folder_details.html", {"form":form})

@login_required
def folder_details(response, id):
	form = NewFolderForm(response.POST or None)
	if Folder.objects.filter(parent=id).exists():
		ls = Folder.objects.filter(parent=id)
		user_folder = None
		if response.method == 'POST':
			if form.is_valid():
				user_folder = form.save(commit=False)
				user_folder.save()
				response.user.folder.add(user_folder)
		return render(response, "main/folder_details.html", {"form":form,"ls":ls,"id":id})
	else:
		form = NewFolderForm()
		return render(response, "main/folder_details.html", {"form":form,"id":id})
	return render(response, "main/drive.html", {"id":id})


def faq(response):
	return render(response, "main/faq.html", {})

def view(response):
	return render(response, "main/view.html", {})

@login_required
def view_details(response, id):
	if ToDoList.objects.filter(id=id).exists():
		ls = ToDoList.objects.get(id=id)
		if ls in response.user.todolist.all():
			if response.method == "POST":
				if response.POST.get("save"):
					for item in ls.item_set.all():
						if response.POST.get("c" + str(item.id)) == "clicked":
							item.complete = True
						else:
							item.complete = False
						item.save()
				elif response.POST.get("newItem"):
					txt = response.POST.get("new")
					if len(txt) > 2:
						ls.item_set.create(text=txt, complete = False)
					else:
						print("Invalid Input")

			return render(response, "main/view_details.html", {"ls":ls})
		return render(response, "main/view.html", {})
	return render(response, "main/view.html", {})
	
@login_required
def create(response):
	if response.method == "POST":
		form = CreateNewList(response.POST)
		if  form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()
			response.user.todolist.add(t)
		return HttpResponseRedirect("/view/%i" %t.id)
	else:
		form = CreateNewList()
	return render(response, "main/create.html", {"form":form})

@login_required
def upload_file(response, id):
	user_folder = None
	if response.method == 'POST':
		form = NewFolderFileForm(response.POST, response.FILES)
		if form.is_valid():
			user_folder = form.save(commit=False)
			user_folder.save()
			response.user.folder.add(user_folder)
			next = response.POST.get('next', '/')
			return HttpResponseRedirect(next)
	else:
		form = NewFolderFileForm()
	return render(response, "main/upload_file.html", {'form': form, 'id':id})