from django.db import models

class PersonalInformation(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "personal_information"
        managed = True

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    name = models.CharField(max_length=100)  
    proficiency = models.IntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        db_table = "skills"
        managed = True  

    def __str__(self):
        return self.name


class Education(models.Model):
    school_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    gpa = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "education"
        managed = True

    def __str__(self):
        return f"{self.degree} at {self.school_name}"


class CV(models.Model):
    pdf = models.FileField(upload_to='cv_files/')  

    class Meta:
        db_table = "cvs"
        managed = True

    def __str__(self):
        return f"CV ({self.pdf.name})"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    technologies_used = models.TextField(blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    repository_url = models.URLField(blank=True, null=True)

    class Meta:
        db_table = "projects"
        managed = True

    def __str__(self):
        return self.title


class AboutMe(models.Model):
    introduction = models.TextField()  
    fun_interests = models.TextField()  

    class Meta:
        db_table = "about_me"
        managed = True

    def __str__(self):
        return "About Me"


class Reference(models.Model):
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    organization = models.CharField(max_length=150, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "references"
        managed = True

    def __str__(self):
        return f"{self.name} - {self.relationship}"
    



class ProfolioPolicy(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    url = models.URLField(max_length=200)  

    class Meta:
        managed = True  
        db_table = 'profolio_policy' 
        verbose_name = 'Profolio Policy'
        verbose_name_plural = 'Profolio Policies'

    def __str__(self):
        return self.name
