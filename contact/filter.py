from pyexpat import model
from tkinter import filedialog
from attr import field
import django_filters
from .models import *

class ContactFilter(django_filters.FilterSet):
    class Meta:
        model = Contacts
        fields = '__all__'