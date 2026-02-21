from django.db import models
from django.contrib.auth.models import User

class AttendanceRecord(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late')]
    )
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.username} - {self.date} - {self.status}"

    class Meta:
        verbose_name = "Attendance Record"
        verbose_name_plural = "Attendance Records"
