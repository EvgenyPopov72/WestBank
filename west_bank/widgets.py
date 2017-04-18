from django import forms

from WestLink_test import settings


class CalendarWidget(forms.TextInput):
    class Media:
        js = (
            settings.STATIC_URL + 'js/bootstrap-datetimepicker.js',
            settings.STATIC_URL + 'js/dp-widget.js',
        )
        css = {
            'all': (
                settings.STATIC_URL + 'css/bootstrap-datetimepicker.css',
            )
        }

    def __init__(self, attrs={}):
        super(CalendarWidget, self).__init__(attrs={'class': 'form_datetime', 'size': '16'})


class CalendarWidget1(forms.TextInput):
    class Media:
        js = (
            settings.STATIC_URL + 'js/bootstrap-datetimepicker.js',
            settings.STATIC_URL + 'js/dp-widget.js',
        )
        css = {
            'all': (
                settings.STATIC_URL + 'css/bootstrap-datetimepicker.css',
            )
        }

    def __init__(self, attrs={}):
        super(CalendarWidget1, self).__init__(attrs={'class': 'form_date', 'size': '16'})
