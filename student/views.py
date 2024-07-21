from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q

##translate teh query by orm to sql ######
# def student_list_(request):
#
#     #equivalent to sql statement
#     posts = Student.objects.all()
#
#     print(posts)
#     print(posts.query)
#     print(connection.queries)
#
#     return render(request, 'output.html',{'posts':posts})
#OR
# def student_list_(request):
#     posts = Student.objects.filter(surname__startswith='mariam') | Student.objects.filter(firstname__startswith='abid')
#
#     print(posts)
#     print(connection.queries)
#
#     return render(request, 'output.html',{'posts':posts})

# def student_list_(request):
#     posts = Student.objects.filter(Q(firstname__startswith='smaoui') | ~Q (firstname__startswith='snen') | Q (firstname__startswith='yangui'))
#     print(posts)
#     print(connection.queries)
#
#     return render(request, 'output.html',{'posts':posts})

# #ANd
# def student_list_(request):
#     posts = Student.objects.filter(classroom=3) & (Student.objects.filter(surname__startswith='mariam'))
#     print(posts)
#     print(connection.queries)
#
#     return render(request, 'output.html',{'posts':posts})

# #UNION
# def student_list_(request):
#     posts = Student.objects.all().values_list("surname").union(Teacher.objects.all().values_list("firstname"))
#     print(posts)
#     print(connection.queries)
#
#     return render(request, 'output.html',{'posts':posts})

#EXCLUDE : NOT
def teachers_list_(request):
    posts = Teacher.objects.all()

    print(posts)
    print(connection.queries)
    teacher = Teacher(firstname='zizo', surname='slim')
    teacher.save()
    return render(request, 'output.html',{'posts':posts})

# def student_list_(request):
#     posts = Student.objects.exclude(age=24)
#     print(posts)
#     print(connection.queries)
#
#     return render(request, 'output.html',{'posts':posts})

# def student_list_(request):
#     posts = Student.objects.filter(classroom=1).only("firstname","age")
#     print(posts)
#     print(connection.queries)#see teh queries performance
#
#     return render(request, 'output.html',{'data':posts})

#RAW QUERIESù
#MAPPING
# def student_list_(request):
#
#    posts = Student.objects.all()
#
#     #equivalent to sql statement
#    for students in Student.objects.raw("SELECT * FROM student_student  WHERE AGE='24'"):
#        print(students)
     ##!!!!!!!!!!!!!!!!!!!FOR BETTER CODE ORGANIZATION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#     sql ="SELECT * FROM student_student  WHERE AGE='24'"
#     student_query=Student.objects.raw(sql)
#
#     #mapping
#    student_mapping={'fname':'firstname','sname':'surname'}
#    objs=Student.objects.raw("SELECT * FROM student_student",translations=student_mapping)
#    student=objs[0].firstname,objs[0].surname
#    print(student)
#    print(connection.queries)
#
#    return render(request, 'output.html',{'data':student})

#
def student_list_(request):

    #equivalent to sql statement
    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})