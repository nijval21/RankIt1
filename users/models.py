from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email
    
class josaa2023(models.Model):
    round_no = models.CharField(max_length=128)
    institute_type = models.CharField(max_length=128)
    institute_name = models.CharField(max_length=128)
    academic_program = models.CharField(max_length=128)
    seat_type = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    open_rank = models.CharField(max_length=128)
    close_rank = models.CharField(max_length=128)
class josaa2022(models.Model):
    round_no = models.CharField(max_length=128)
    institute_type = models.CharField(max_length=128)
    institute_name = models.CharField(max_length=128)
    academic_program = models.CharField(max_length=128)
    seat_type = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    open_rank = models.CharField(max_length=128)
    close_rank = models.CharField(max_length=128)
class josaa2021(models.Model):
    round_no = models.CharField(max_length=128)
    institute_type = models.CharField(max_length=128)
    institute_name = models.CharField(max_length=128)
    academic_program = models.CharField(max_length=128)
    seat_type = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    open_rank = models.CharField(max_length=128)
    close_rank = models.CharField(max_length=128)
class josaa2020(models.Model):
    round_no = models.CharField(max_length=128)
    institute_type = models.CharField(max_length=128)
    institute_name = models.CharField(max_length=128)
    academic_program = models.CharField(max_length=128)
    seat_type = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    open_rank = models.CharField(max_length=128)
    close_rank = models.CharField(max_length=128)
class josaa2019(models.Model):
    round_no = models.CharField(max_length=128)
    institute_type = models.CharField(max_length=128)
    institute_name = models.CharField(max_length=128)
    academic_program = models.CharField(max_length=128)
    seat_type = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    open_rank = models.CharField(max_length=128)
    close_rank = models.CharField(max_length=128)
class josaa2018(models.Model):
    round_no = models.CharField(max_length=128)
    institute_type = models.CharField(max_length=128)
    institute_name = models.CharField(max_length=128)
    academic_program = models.CharField(max_length=128)
    seat_type = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    open_rank = models.CharField(max_length=128)
    close_rank = models.CharField(max_length=128)
class josaa2017(models.Model):
    round_no = models.CharField(max_length=128)
    institute_type = models.CharField(max_length=128)
    institute_name = models.CharField(max_length=128)
    academic_program = models.CharField(max_length=128)
    seat_type = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    open_rank = models.CharField(max_length=128)
    close_rank = models.CharField(max_length=128)
class josaa2016(models.Model):
    round_no = models.CharField(max_length=128)
    institute_type = models.CharField(max_length=128)
    institute_name = models.CharField(max_length=128)
    academic_program = models.CharField(max_length=128)
    seat_type = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    open_rank = models.CharField(max_length=128)
    close_rank = models.CharField(max_length=128)