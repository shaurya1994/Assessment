from django.db import models

# Create your models here.

# Company Model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(
        max_length=100, 
        choices=
                (('IT', 'IT'), 
                ('Non IT', 'Non IT'), 
                ('Mobile Phones', 'Mobile Phones')), 
                default='IT'  # New Change
        )
    added_date = models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name + ' -- ' + self.location 


#Employee Model
class Employee(models.Model):
    # emp_id = models.AutoField(primary_key=True, default=1) # Doubt 1
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    # address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    # about = models.CharField(max_length=50)
    position = models.CharField(
        max_length=50,
        choices=(
            ('MNG', 'Manager'),
            ('SD', 'Software Developer'),
            ('PL', 'Project Leader')),
            default='Software Developer', 
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)



