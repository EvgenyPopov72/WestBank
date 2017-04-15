from django import forms

from WestLink_test import settings


class CalendarWidget(forms.TextInput):
    class Media:
        js = ('/admin/jsi18n/',
              settings.STATIC_URL + 'admin/js/vendor/jquery/jquery.min.js',
              settings.STATIC_URL + 'admin/js/jquery.init.js',
              settings.STATIC_URL + 'admin/js/core.js',
              settings.STATIC_URL + 'admin/js/calendar.js',
              settings.STATIC_URL + 'admin/js/admin/DateTimeShortcuts.js')
        css = {
            'all': (
                settings.STATIC_URL + 'admin/css/forms.css',
                settings.STATIC_URL + 'admin/css/widgets.css',)
        }

    def __init__(self, attrs={}):
        super(CalendarWidget, self).__init__(attrs={'class': 'vDateField', 'size': '10'})
