from django.shortcuts import render, HttpResponse
import pandas as pd
from .models import Applicant,Connection,Status
from datetime import datetime

# Create your views here.

def index(request):
    return render(request,"index.html") 

def login(request):
     return render(request,"login.html")
def uploaddata(request):
    try:
      filepath='electricity_board_case_study.csv'
      df=pd.read_csv(filepath,encoding='Latin-1')
     
      for index, row in df.iterrows():
               # create or update dont duplicates
               applicant,created = Applicant.objects.get_or_create(
                    Applicant_Name=row ['Applicant_Name'],
                    Gender=row ['Gender'],
                    District=row ['District'],
                    State=row ['State'],
                    Pincode=row ['Pincode'],
                    Ownership=row ['Ownership'],
                    GovtID_Type=row ['GovtID_Type'],
                    ID_Number=row ['ID_Number'],
                    Category=row ['Category'],
               )
     
               # create or get the status object
               status, created=Status.objects.get_or_create(Status_Name=row['Status'])
               Date_of_Application = datetime.strptime(row['Date_of_Application'], "%d-%m-%Y")
               Date_of_Approval=None
               if (not pd.isna(row['Date_of_Approval'])):
                    Date_of_Approval =datetime.strptime(row['Date_of_Approval'], "%d-%m-%Y")
               Modified_Date = datetime.strptime(row['Modified_Date'],"%d-%m-%Y")
     
               Connection.objects.get_or_create(
                    Applicant=applicant,
                    Load_Applied=row['Load_Applied'],
                    Date_of_Application=Date_of_Application,
                    Date_of_Approval=Date_of_Approval,
                    Modified_Date=Modified_Date,
                    Status=Status,
                    Reviewer_ID=row['Reviewer_ID'],
                    Reviewer_Name=row['Reviewer_Name'],
                    Reviewer_Comment=row['Reviewer_Comments'],
               )
               print(row['ID'])
      
    except Exception as e:
        return HttpResponse(f"Error: {e}")
     
    return HttpResponse("File data Uploaded Successfully")
