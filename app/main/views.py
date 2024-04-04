from rest_framework import generics

from .serializers import (
    ProfessionSerializer,
    AboutMeSerializer,
    PartnerSerializer,
    EducationSerializer,
    ExperienceSerializer,
    AwardSerializer,
    SkillsSerializer,
    ServicesSerializer,
    ProjectsSerializer,
    DoneSerializer,
    MeContactSerializer
    )
from .models import (
    Profession,
    AboutMe,
    Partner,
    Education,
    Experience,
    Award,
    Skills,
    Services,
    Projects,
    Done,
    MeContact
    )


class ProfessionAPIView(generics.ListAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    pagination_class = None


class AboutMeAPIView(generics.ListAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer
    pagination_class = None


class PartnerAPIView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    pagination_class = None


class EducationAPIView(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    pagination_class = None


class ExperienceAPIView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    pagination_class = None


class AwardAPIView(generics.ListAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    pagination_class = None


class SkillsAPIView(generics.ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    pagination_class = None


class ServicesAPIView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    pagination_class = None


class ProjectsAPIView(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    pagination_class = None


class DoneAPIView(generics.ListAPIView):
    queryset = Done.objects.all()
    serializer_class = DoneSerializer
    pagination_class = None


class MeContactsAPIView(generics.ListAPIView):
    queryset = MeContact.objects.all()
    serializer_class = MeContactSerializer
    pagination_class = None

