from django.urls import path
from .views import job_list, create_job, job_detail, apply_for_job, application_details

urlpatterns = [
    path('', job_list, name='job_list'),
    path('create/', create_job, name='create_job'),
    path('jobs/<int:pk>/', job_detail, name='job_detail'),
    path('jobs/<int:pk>/apply/', apply_for_job, name='apply_for_job'),path('applications/<int:id>/', application_details, name='application_details')
]
