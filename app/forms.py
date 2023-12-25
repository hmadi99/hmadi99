from django import forms
from django.db import transaction

from .models import NewsAndEvents, Session, Semester, SEMESTER


# news and events
class NewsAndEventsForm(forms.ModelForm):
    class Meta:
        model = NewsAndEvents
        fields = ('title', 'summary', 'posted_as',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control'})
        self.fields['posted_as'].widget.attrs.update({'class': 'form-control'})


class SessionForm(forms.ModelForm):
    session = forms.CharField(
        label=" الجلسة ",
        required=True
    )
    
    next_session_begins = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                'type': 'date',
            }
        ), label="بداية الجلسة القادمة ",
        required=True)
    is_current_session = forms.BooleanField(
            label = "الجلسة الحالية", 
            required=False)
        

    class Meta:
        model = Session
        fields = ['session', 'is_current_session', 'next_session_begins']
        
        


class SemesterForm(forms.ModelForm):
    semester = forms.CharField(
        widget=forms.Select(
            choices=SEMESTER,
            attrs={
                'class': 'browser-default custom-select',
            }
        ),
        label="الفصل الدراسي",
    )
    is_current_semester = forms.CharField(
        widget=forms.Select(
            choices=((True, 'Yes'), (False, 'No')),
            attrs={
                'class': 'browser-default custom-select',
            }
        ),
         label=" الفصل الدراسي الحالي ؟ ",
    )
    session = forms.ModelChoiceField(
        queryset=Session.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'browser-default custom-select',
            }
        ),
       
        label="جلسة",
        required=True
    )

    next_semester_begins = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
            }
        ),
        label="بداية الفصل الدراسي",
        required=True)

    class Meta:
        model = Semester
        fields = ['semester', 'is_current_semester', 'session', 'next_semester_begins']
