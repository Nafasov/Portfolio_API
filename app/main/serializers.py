from rest_framework import serializers

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


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'title']


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = ['id', 'name', 'image', 'birthday', 'address', 'zip_code', 'phone', 'email', 'project_complete', 'cvv', 'created_date']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'image', 'link', 'created_date']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'years', 'title', 'position', 'content', 'created_date']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'years', 'title', 'position', 'content', 'created_date']


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ['id', 'years', 'title', 'position', 'content', 'created_date']


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['id', 'title', 'percentage', 'Last_week', 'Last_month', 'created_date']


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'title', 'icon', 'link', 'description', 'created_date']


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'title', 'category', 'image', 'link', 'created_date']


class DoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Done
        fields = ['id', 'title', 'number', 'modified_date']


class MeContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeContact
        fields = ['id', 'address', 'image', 'phone', 'li_me', 'email', 'web_site', 'website']
