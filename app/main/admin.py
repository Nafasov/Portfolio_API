from django.contrib import admin

# Register your models here.

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


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'created_date')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'created_date')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')


@admin.register(Award)
class AwdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link', 'created_date')


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')


@admin.register(Done)
class DoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'number')


@admin.register(MeContact)
class MeContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone')
