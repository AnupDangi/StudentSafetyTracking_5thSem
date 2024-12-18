
from django.contrib import admin
from .models import Student, Attendance
from django.utils.timezone import now, localtime, timedelta


class AttendanceInline(admin.TabularInline):
    model = Attendance
    extra = 0
    readonly_fields = ('timestamp',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'age', 'city', 'is_active', 'is_staff', 'attendance_alert')
    inlines = [AttendanceInline]

    def attendance_alert(self, obj):
        # Check the most recent attendance record
        last_attendance = Attendance.objects.filter(student=obj).order_by('-timestamp').first()
        if last_attendance:
            time_diff = localtime(now()) - last_attendance.timestamp
            if time_diff > timedelta(hours=24):
                return "Alert Needed"
        return "All Good"

    attendance_alert.short_description = "Attendance Alert"

admin.site.register(Student, StudentAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'timestamp', 'alert_needed')

    @admin.display(description='Alert Needed')
    def alert_needed(self, obj):
        time_difference = now() - obj.timestamp
        return time_difference > timedelta(hours=24)

admin.site.register(Attendance, AttendanceAdmin)