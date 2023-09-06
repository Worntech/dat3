from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name = "signup"),
    path('signin', views.signin, name = "signin"),
	path('logout/', views.logout, name="logout"),
 
    path("",views.home,name = "home"),
    path("aboutus",views.aboutus,name = "aboutus"),
    path("base",views.base,name = "base"),
    path("project",views.project,name = "project"),
    path("strategic",views.strategic,name = "strategic"),
    path("contactus",views.contactus,name = "contactus"),
    path("contactpost/",views.contactpost,name = "contactpost"),
    path("contactlist/",views.contactlist,name = "contactlist"),
    path("viewcontact/<int:id>/",views.viewcontact,name = "viewcontact"),
    path('deletecontact/<int:id>/', views.deletecontact, name = "deletecontact"),
    path("files/",views.files,name = "files"),
    path("filesdisplay/",views.filesdisplay,name = "filesdisplay"),
    path('deletefiles/<int:id>/', views.deletefiles, name = "deletefiles"),
    path('viewfiles/<int:id>/', views.viewfiles, name = "viewfiles"),
    path("dashboard/",views.dashboard,name = "dashboard"),
    path("governance/",views.governance,name = "governance"),
    # path("viewleader/<int:id>/",views.viewleader,name = "viewleader"),
    path('deleteleader/<int:id>/', views.deleteleader, name = "deleteleader"),
    path("leaderdisplay/",views.leaderdisplay,name = "leaderdisplay"),
]