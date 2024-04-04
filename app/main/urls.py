from django.urls import path

from .views import (
    ProfessionAPIView,
    AboutMeAPIView,
    PartnerAPIView,
    EducationAPIView,
    ExperienceAPIView,
    AwardAPIView,
    SkillsAPIView,
    ServicesAPIView,
    ProjectsAPIView,
    DoneAPIView,
    MeContactsAPIView
    )

app_name = 'main'


urlpatterns = [
    path('professions/', ProfessionAPIView.as_view()),
    path('aboutme/', AboutMeAPIView.as_view()),
    path('partner/', PartnerAPIView.as_view()),
    path('education/', EducationAPIView.as_view()),
    path('experience/', ExperienceAPIView.as_view()),
    path('award/', AwardAPIView.as_view()),
    path('skills/', SkillsAPIView.as_view()),
    path('services/', ServicesAPIView.as_view()),
    path('projects/', ProjectsAPIView.as_view()),
    path('done/', DoneAPIView.as_view()),
    path('mecontacts/', MeContactsAPIView)

]


"""
    Profession
        -list
    AboutMe
        -list
    Partner
        -list
    Education
        -list
    Experience
        -list
    Award
        -list
    Skills
        -list
    Services
        -list
    Projects
        -list
    Done
        -list
    MeContact
        -list
     
"""