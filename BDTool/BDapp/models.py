from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, username,email, password, **extra_fields):
        user = self.model(username = username,email = email,password = password)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = False
        user.save(using=self._db)
        return user


    def create_superuser(self,username, email, password, **extra_fields):
        user = self.create_user(username = username,email = email,password = password)
        user.is_active = True
        user.is_staff  = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

    def get_by_natural_key(self,username_):
        print(username_)
        return self.get(username = username_)





class customUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=255,unique = True,null = False )
    email = models.EmailField(unique=True,blank = False,null = False)
    first_name = models.CharField( max_length=30, blank=True)
    last_name = models.CharField( max_length=30, blank=True)
    is_staff = models.BooleanField(default = True)
    is_active = models.BooleanField( default=True)
    is_superuser = models.BooleanField(default = False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def natural_key(self):
        return self.username

    def __str__(self):
        return self.username


# Create your models here.


class Technology(models.Model):
    technology_name=models.CharField(max_length=50)

    def __str__(self):
        return self.technology_name
class Client(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    skype_id=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    country=models.CharField(max_length=50)
    active =models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

class Project(models.Model):
    project_name = models.CharField(max_length=50)
    url_name = models.CharField(max_length=100)
    domain_name = models.CharField(max_length=100)
    project_desrciption = models.CharField(max_length=1000,blank = True)
    attachment = models.ImageField(blank=True, null=True)
    technology = models.CharField(max_length=100,default = "Python")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client', blank=True, null=True)
    # datend time we want to add
    def __str__(self):
        return self.project_name

    class Meta:
        ordering=('project_name',)




