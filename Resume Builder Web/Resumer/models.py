from django.db import models

# --------------------------------------------Project Tables--------------------------------------------


class Project(models.Model):
    name = models.CharField('Project name', max_length=100)
    duration = models.IntegerField("Duration (yrs)")
    version = models.CharField('Version', max_length=15)

    def __str__(self):
        s = self.name
        return s


class Achievement(models.Model):
    achievement = models.TextField('Achievement')

    def __str__(self):
        s = self.achievement
        return s


class Skill(models.Model):
    name = models.CharField("Skill", max_length=20)
    type = models.CharField("type", max_length=20)

    def __str__(self):
        return self.name

# ----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------Education Tables-------------------------------------------------


class Organization(models.Model):
    name = models.CharField('Name', max_length=20)
    type = models.CharField('Industry', max_length=200)

    def __str__(self):
        s = self.name
        return s


class Experience(models.Model):
    job = models.CharField("Job Name", max_length=20)
    company = models.ForeignKey(Organization, on_delete=models.CASCADE)
    yrs = [(x, x) for x in range(1975, 2022)]
    start_yr = models.IntegerField('Starting Year', choices=yrs)
    designation = models.CharField('Designation', max_length=20)
    project = models.ManyToManyField(Project)
    add = models.TextField('Additional', blank=True)

    def __str__(self):
        s = self.job
        return s


class Education(models.Model):
    course_name = models.CharField('Course Name', max_length=20)
    institute = models.ManyToManyField(Organization)
    score = models.DecimalField('Score', max_digits=3, decimal_places=2)
    yrs = [(x, x) for x in range(1975, 2022)]
    pass_yr = models.IntegerField('Passing Year', choices=yrs)

    def __str__(self):
        return self.course_name

# ----------------------------------------------------------------------------------------------------------------
# --------------------------------------------Basic Information Tables--------------------------------------------


class Contact(models.Model):
    cont1 = models.IntegerField('Contact 1')
    cont2 = models.IntegerField('Contact 2', blank=True, null=True)

    def __str__(self):
        s = str(self.cont1)
        return s


class Addresse(models.Model):
    Address1 = models.TextField()
    Address2 = models.TextField(blank=True, null=True)

    def __str__(self):
        s = self.Address1
        # if self.Address2 is not None:
        #     s += '\n' + 'Secondary Address: ' + self.Address1
        return s


class Information(models.Model):
    first_name = models.CharField('First Name', max_length=20)
    last_name = models.CharField('Last Name', max_length=20)
    Email = models.EmailField('Email')
    LinkedIn = models.URLField('LinkedIn')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    address = models.ManyToManyField(Addresse)
    education = models.ManyToManyField(Education)
    exp = models.ManyToManyField(Experience)
    Ach = models.ManyToManyField(Achievement)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.first_name+" "+self.last_name

# ----------------------------------------------------------------------------------------------------------------
