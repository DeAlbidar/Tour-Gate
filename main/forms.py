from django import forms
from .models import Folder
from mptt.forms import TreeNodeChoiceField

class CreateNewList(forms.Form):
	name = forms.CharField(label="Name", max_length=200)
	check = forms.BooleanField(required=False)

class NewFolderForm(forms.ModelForm):
	parent = TreeNodeChoiceField(queryset=Folder.objects.all())

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['parent'].required = False
		self.fields['parent'].label = ""
		self.fields['name'].label = ""
		self.fields['parent'].widget.attrs.update({'class':'d-none'})

	class Meta:
		model = Folder
		fields = ('parent','name')
		widgets = {
			'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
		}

class NewFolderFileForm(forms.ModelForm):
	parent = TreeNodeChoiceField(queryset=Folder.objects.all())

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['parent'].required = False
		self.fields['parent'].label = ""
		self.fields['name'].label = ""
		self.fields['file'].label = ""
		self.fields['parent'].widget.attrs.update({'class':'d-none'})

	class Meta:
		model = Folder
		fields = ('parent','name','file')
		widgets = {
			'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
		}