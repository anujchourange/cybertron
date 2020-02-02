from django import forms
from .models import report
from tempus_dominus.widgets import DateTimePicker


class ReportCrime(forms.ModelForm):

    #image = forms.ImageField(upload_to='report_images')
    title = forms.CharField(max_length=50, required=False)
    description = forms.CharField(max_length=100, required=False)
    location_lat = forms.FloatField(required=True)
    location_lng = forms.FloatField(required=True)
    user_id = forms.EmailField(required=True)
    event_time = forms.DateTimeField(label="Event Time", widget=DateTimePicker(
        options={
            'useCurrent': True,
            'collapse': True,
        },
        attrs={
            'append': 'fa fa-calendar',
            'icon_toggle': True,
        }
    ))
    #event_report = forms.DateTimeField(label="Report Time", required=False)

    class Meta:
        model = report
        # ['fname', 'lname', 'email', 'phone_number', 'password1']
        fields = ['event_time', 'title', 'description',
                  'location_lat', 'location_lng', 'user_id', 'image']  # 'event_time', 'event_report',
