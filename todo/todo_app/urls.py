
from django.urls import path
from . import views

app_name="todoapp"

urlpatterns = [
    path('projectlist/',views.ProjectList,name='projectlist'),
    path('projectdetail/<str:title_p>/<int:id_p>',views.ProjectDetail,name='project_detail'),
    path('taskdetail/<str:title_t>/<int:id_t>',views.TaskDetail,name='task_detail'),
    path('projectform/',views.ViewProjectForm,name='projectform'),
    path('taskform/<int:project_id>',views.ViewTaskForm,name='taskform'),
    path('deletetask/<int:task_id>/<int:proj_id>/<str:name>/',views.DeleteTask,name='deletetask'),
    path('updatetask/<int:task_id>/',views.UpdateTask,name='updatetask'),


]