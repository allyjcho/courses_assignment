from django.db import models

class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['course_name'] = "Name must be at least 5 characters."
        if len(postData['desc']) < 15:
            errors['description'] = "Description must be at least 15 characters."
        return errors

class Course(models.Model):
    course_name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()