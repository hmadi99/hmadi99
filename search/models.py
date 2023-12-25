from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db.models.signals import pre_save
from django.db.models import Q
from accounts.models import Student
from course.models import Course


PASS = "PASS"
FAIL = "FAIL"
COMMENT = (
    (PASS, "PASS"),
    (FAIL, "FAIL"),
)


# # Create your models here.
# class TakenCourse(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='taken_courses')
#     assignment = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
#     attendance = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
#     comment = models.CharField(choices=COMMENT, max_length=200, blank=True)
#     def get_absolute_url(self):
#         return reverse('course_detail', kwargs={'slug': self.course.slug})

#     def __str__(self):
#         return "{0} ({1})".format(self.course.title, self.course.code)

#     # @staticmethod
#     def get_total(self, assignment, mid_exam, quiz, attendance, final_exam):
#         return float(assignment) + float(mid_exam) + float(quiz) + float(attendance) + float(final_exam) 

#     # @staticmethod
  
