from celery import shared_task
import csv
from django.http import HttpResponse
from .models import Book
from time import sleep


#app = Celery('tasks', broker='redis://localhost:6379')
#@app.task

@shared_task
def add(x, y):
    sleep(5)
    return x + y

#file = 'books.csv'
@shared_task
def exporttocsv(*args, **kwargs):
    print("create csv file")
    file = open("books.csv", "w")
    writer = csv.writer(file)
    writer.writerow(['Title', 'Author', 'Category', 'Price','Quantity'])
    print("writing books info ...")
    for book in Book.objects.all().values_list('title', 'author', 'category', 'price','quantity'):
        writer.writerow(book)
    
    
    return 'Done'