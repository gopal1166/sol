# Session 7 : Django: Models, ORM

Date: 31/5/2019

model:
```
To create tables 
```

syntax:
```
class ModelName(models.Model):
    create fields: columns

    create functions as well
```

migration: to create the tables in db
```
    1. create migration files
    2. migrate the files to the database

    1. migration file:
        infomation about the table: table name, columns and data types of columns
    
        $ python manage.py makemigrations

    2. to migrate: 
        $ python manage.py migrate

    **id will be added automatically to each table if we don't define explicity
```

amdin panel:
```
createsuper: `python manage.py createsuperuser`
```

To do anything 
like creating, updating, retrieving and deleting the data

we've register the model in admin
```

django ORM:
```
crud:

create: ModelName.objects.create(fieldname='value')

retrieve: ModelName.objects.all()

to retrive/get only record: ModelName.objects.get(id=)

updating:
    1. get the record instance:
        instance = ModelName.objects.get(id=)
    2. instance.field_name = "new value"
    3. instance.save()    # to reflect the update in database

delete: 
    1. get the record instance:
        instance = ModelName.objects.get(id=)
    2. delete the install:
        instance.delete

quick recap:
```
created models, migrations, migrate, 
CRUD table records using django ORM in django shell

To acces sthe django shell:
    $ python manage.py shell

created super user
```

Task:
```
create a table and play around using django ORM
```

filter
lookup
admin panel usage














