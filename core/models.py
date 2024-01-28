from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    is_best_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, through='Enrollment')

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.name}"
