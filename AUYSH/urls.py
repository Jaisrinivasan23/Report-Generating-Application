from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('admin-login/', views.admin_login, name='admin_login'),    
    path('admin-home/', views.admin_home, name='admin_home'),
    path('add-faculty/', views.add_faculty_view, name='add_faculty'),
    path('academic-performance/', views.academic_performance_view, name='academic_performance'),
    path('research-publications/', views.research_publications_view, name='research_publications'),
    path('financial-statements/', views.financial_statements_view, name='financial_statements'),
    path('infrastructure-developments/', views.infrastructure_developments_view, name='infrastructure_developments'),
    path('student-faculty-achievements/', views.student_faculty_achievements_view, name='student_faculty_achievements'),
    path('extracurricular-activities/', views.extracurricular_activities_view, name='extracurricular_activities'),
]
