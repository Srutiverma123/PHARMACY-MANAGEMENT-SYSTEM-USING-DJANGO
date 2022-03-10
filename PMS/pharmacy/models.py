#Medicine structure

from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    exp = models.DateField()

    def __str__(self): #whenever a column is called return it's name
        return self.name

#Below commands are run in the terminal of PyCharm to make the structure of table in pgAdmin4 where database is present
'''
pip install psycopg2 #to connect django and postgresql
python manage.py makemigrations
python manage.py sqlmigrate pharmacy 0001
python manage.py migrate
'''

