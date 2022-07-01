import email
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Project,Task
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods
from .forms import *
from user_app.models import CustomUser
# Create your views here.

User = get_user_model()

def ProjectList(request):
    user=request.user
    all_p = user.project_member.all()
    context={'all_p' : all_p}
    return render(request,'project.html',context)


def ProjectDetail(request,title_p,id_p):
    user=request.user
    detail_p = user.project_member.get(title=title_p,id=id_p)
    all_task = user.task_member.filter(project_id=id_p)
    context= {'detail_p' : detail_p,'all_task' : all_task, 'project_id': id_p}
    return render(request,'task.html',context)

def TaskDetail(request,title_t,id_t):
    user=request.user
    detail_T = User.team_member.get(title=title_t,id=id_t)
    return render(request,'task.html',{'detail_T' : detail_T})

@require_http_methods(["GET", "POST"])
def ViewProjectForm(request):
    user=request.user
    users=User.objects.all()
    if request.method == "POST":
        admin=User.objects.get(email=request.POST.get('admin_todo'))
        new_request=request.POST.copy()
        new_request['admin_todo']=admin.id
        form = ProjectForm(new_request)
        if form.is_valid():
            form.save() 
            project=form.instance
            project.team_member.add(User.objects.get(email=request.POST.get('team_member')))
            project.team_member.add(User.objects.get(email=request.POST.get('admin_todo')))
            return redirect("todoapp:projectlist")
        else:
            return render(request, 'add_project.html', {'form': form, 'errors':'error.'})
    
    else:
        
        form = ProjectForm()
    
    return render(request,'add_project.html',{'form' : form,'users' : users})

@require_http_methods(["GET", "POST"])
def ViewTaskForm(request, project_id):
    user=request.user
    users = Project.objects.get(id=project_id).team_member.all()

    if request.method == "POST":
        new_req = request.POST.copy()
        new_req.update({"project":project_id})
        form =  TaskForm(new_req)
        if form.is_valid():
            form.save() 
            task=form.instance
            task.team_member.add(User.objects.get(email=request.POST.get('team_member')))
            task.team_member.add(user)
            task.project_id = project_id
            task.save()

            return redirect('todoapp:project_detail' ,task.project.title ,task.project_id)
        else:
            return render(request, 'add_task.html', {'form': form,'errors':'error.','users': users})
    else:
        form = TaskForm()
    
    return render(request,'add_task.html',{'form' : form,'users': users})



@require_http_methods(["GET", "POST"])
def UpdateTask(request , task_id):
    task_obj = Task.objects.get(id=task_id)
    users = task_obj.project.team_member.all()
    if request.method == "GET":
        return render(request , "update_task.html" , {"task_obj":task_obj , 'users':users})
    
    if request.method == "POST":
        
        data = request.POST
        if data.get("title",""):
            task_obj.title = data["title"]
        if data.get('status',""):
            task_obj.status = data["status"]
        if data.get("text_todo",""):
            task_obj.text_todo = data["text_todo"]
        if data.get("end_date",""):
            task_obj.end_date=data["end_date"]
        if data.get("team_member",""):
            task_obj.team_member.add(User.objects.get(email=request.POST.get('team_member')))

        task_obj.save()
        return redirect('todoapp:project_detail' ,task_obj.project.title ,task_obj.project_id)
    else:
            
            return render(request, 'update_task.html', {'form': "form",'errors':'error'})

def DeleteTask(request,task_id,proj_id,name):

    Task.objects.filter(id=task_id).delete()
    return redirect('todoapp:project_detail',name,proj_id)



