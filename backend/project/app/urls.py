from django.urls import path
from app import views
from .views import ConnectionListView

urlpatterns = [
   path("",views.index,name="index"),
   path("login/",views.login,name="login"),
   path("uploaddata",views.uploaddata,name="uploaddata"),
   path("getApplicantData/",ConnectionListView.as_view(),name="connection_list"),
   path("update_applicant/<int:id>",views.update_applicant,name='update_applicant'),
   path("connectionvisualization/",views.connectionvisualization,name="connectionvisualization"),
   path("connectionrequestdata/",views.connectionrequestdata,name="connectionrequestdata"),
]

#""=="/"=="localhost"==http://127.0.0.1:8000/