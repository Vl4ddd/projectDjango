from django.db import models

class SalaryAllYear(models.Model):
    year = models.TextField()
    salary = models.DecimalField(decimal_places=10, max_digits=19)

    class Meta:
        db_table = 'salary_by_year'


class SalaryVacYear(models.Model):
    year = models.TextField()
    salary = models.DecimalField(decimal_places=10, max_digits=19)

    class Meta:
        db_table = 'salary_by_year_vac'

class CountAllYear(models.Model):
    year = models.TextField()
    count = models.IntegerField()

    class Meta:
        db_table = 'count_by_year_all'

class CountVacYear(models.Model):
    year = models.TextField()
    count = models.IntegerField()

    class Meta:
        db_table = 'count_by_year_vac'

class AreaAllSalary(models.Model):
    year = models.TextField()
    salary = models.DecimalField(decimal_places=10, max_digits=19)


    class Meta:
        db_table = 'area_all_salary'
    
class AreaAllCount(models.Model):
    year = models.TextField()
    count = models.IntegerField()

    class Meta:
        db_table = 'area_all_count'

class AreaVacSalary(models.Model):
    year = models.TextField()
    salary = models.DecimalField(decimal_places=10, max_digits=19)


    class Meta:
        db_table = 'area_vac_salary'

class AreaVacCount(models.Model):
    year = models.TextField()
    count = models.IntegerField()

    class Meta:
        db_table = 'area_vac_count'

