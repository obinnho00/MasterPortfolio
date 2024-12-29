from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator,EmailValidator


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
    picture = models.ImageField(upload_to='skill_pictures/', blank=True, null=True)  
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
    name = models.CharField(max_length=100, default="Isaac Obi Cv") 
    file = models.BinaryField() 
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "cv"
        managed = True

    def __str__(self):
        return f"CV ({self.file})"


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

    class Meta:
        db_table = "about_me"
        managed = True

    def __str__(self):
        return "About Me"



class Reference(models.Model):
    name = models.CharField(max_length=100)  # Name of the reference
    email = models.EmailField(blank=True, null=True)  # Email address
    role = models.CharField(max_length=100, blank=True, null=True)  # Role of the reference
    company = models.CharField(max_length=150, blank=True, null=True)  # Company name
    picture = models.ImageField(upload_to="references_pictures/", blank=True, null=True)  # Picture associated with the reference

    class Meta:
        db_table = "references_table"
        managed = True

    def __str__(self):
        return f"{self.name} - {self.role} at {self.company}"


class TechnicalSkill(models.Model):
    """
    Represents an individual technical skill with predefined categories and a skill level scale.
    """
    LIBRARIES_AND_FRAMEWORKS = 'Libraries and Frameworks'
    DATA_SCIENCE_ANALYSIS = 'Data Science & Analysis'
    PROGRAMMING_LANGUAGES = 'Programming Languages'
    BACKEND_DEVELOPMENT = 'Backend Development'
    FRONTEND_DEVELOPMENT = 'Frontend Development'
    VERSION_CONTROL_TOOLS = 'Version Control & Tools'
    DEVELOPMENT_PRACTICES = 'Development Practices'
    OTHER = 'Other'

    CATEGORY_CHOICES = [
        (LIBRARIES_AND_FRAMEWORKS, LIBRARIES_AND_FRAMEWORKS),
        (DATA_SCIENCE_ANALYSIS, DATA_SCIENCE_ANALYSIS),
        (PROGRAMMING_LANGUAGES, PROGRAMMING_LANGUAGES),
        (BACKEND_DEVELOPMENT, BACKEND_DEVELOPMENT),
        (FRONTEND_DEVELOPMENT, FRONTEND_DEVELOPMENT),
        (VERSION_CONTROL_TOOLS, VERSION_CONTROL_TOOLS),
        (DEVELOPMENT_PRACTICES, DEVELOPMENT_PRACTICES),
        (OTHER, OTHER),
    ]

    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    skill_level = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        default=5,  # Default value for skill level
        help_text="Skill level on a scale of 1 to 10"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "technical_skill"
        managed = True
        unique_together = ('category', 'name')  # Prevent duplicate skills in the same category

    def __str__(self):
        return f"{self.name} ({self.category}) - Level: {self.skill_level}"
    



# need attention 
class WebsitePolicy(models.Model):
    """
    Represents the terms of use and policies for the website.
    """
    terms_of_use = models.TextField()  # Field for the terms of use
    policy_statement = models.TextField()  # Field for the policy statement
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the policy is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the policy is updated

    class Meta:
        db_table = "website_policy"
        managed = True

    def __str__(self):
        return f"Website Policy (Created: {self.created_at})"



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()], unique=True)

    class Meta:
        db_table = 'user'
        managed = True
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name


class BugReport(models.Model):
    posted_date = models.DateTimeField(auto_now_add=True)
    bug_type = models.CharField(max_length=50)
    report = models.TextField()
    solution = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bug_reports'
    )

    class Meta:
        db_table = 'bug_report'
        managed = True
        verbose_name = "Bug Report"
        verbose_name_plural = "Bug Reports"

    def __str__(self):
        return f"{self.bug_type} reported by {self.user.email}, {self.solution} on {self.posted_date}"


class Comment(models.Model):
    bug_report = models.ForeignKey(BugReport, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    #comment_posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comment'
        managed = True
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Comment by {self.user.email} on {self.bug_report}"