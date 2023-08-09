from django import forms

from .models import (
    Order,
    PaperType,
    Discipline,
    WeeklyAssigment
)

class AssignmentForm(forms.ModelForm):
    # ppt = forms.IntegerField(widget=forms.NumberInput(attrs={
    #             "class":"px-4 py-2 text-sm font-medium text-gray-900 bg-white border-t border-b border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white",
    #             "id":"ppt-count"
    #         }), initial=0)
    
    
    def __init__(self, *args, **kwargs):
        super(AssignmentForm,self).__init__(*args, **kwargs)
        # self.fields['pages'].disabled=True
        # self.fields['words'].disabled=True
        self.fields['type_of_paper'].queryset = PaperType.objects.all()
        self.fields['discipline'].queryset = Discipline.objects.all()
        self.fields['ppt'].initial=0
    
    class Meta:
        model = Order
        fields = [
            "type_of_paper","discipline", "deadline_date","deadline_time","pages","words","academic_level",
            "paper_instruction","files","paper_format","type_of_service",
            "reference_copies","sms_update","turnitin_report","writer_choice","ppt"
            ,"software_tools","software_tool_description"
        
        ]
        
        widgets = {
            "pages":forms.NumberInput(attrs={
                "class": "px-4 py-2 text-sm font-medium text-gray-900 bg-white border-t border-b border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white",
                "id":"page-count"
            }),
            "words":forms.NumberInput(attrs={
                "class":"text",
                "id":"word-count"
            }),
            "type_of_paper":forms.Select(attrs={
                "class":"form-select px-4 py-3 rounded-md appearance-none w-[100%] mb-3",
                "id":"type_of_paper"
            }),
            "discipline":forms.Select(attrs={
                "class":"form-select px-4 py-3 rounded-md appearance-none w-[100%] mb-3",
                "id":"discipline"
            }),
            "deadline_time":forms.TimeInput(format='%H:%M', attrs={
                "class":" border border-1 border-gray-400 peer block min-h-[auto] w-full rounded border-0 bg-transparent px-3 py-[0.32rem] leading-[1.6] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 peer-focus:text-primary data-[te-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-neutral-200 dark:placeholder:text-neutral-200 dark:peer-focus:text-primary [&:not([data-te-input-placeholder-active])]:placeholder:opacity-0",
                "id":"timepicker-disable-future"
            }),
            "deadline_date":forms.DateInput(attrs={
                "class":"peer block min-h-[auto] w-full rounded border-0 bg-transparent px-3 py-[0.32rem] leading-[1.6] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 peer-focus:text-primary data-[te-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-neutral-200 dark:placeholder:text-neutral-200 dark:peer-focus:text-primary [&:not([data-te-input-placeholder-active])]:placeholder:opacity-0",
                "id":"deadline_date"
            }),
            "type_of_service":forms.RadioSelect(choices=(
                ("ER", "Editting Rewriting"),
                ("CALC", "Calculations"),
                ("IT", "Programming")
            ), attrs={
                "class": "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500",

            }),
            "price":forms.HiddenInput(attrs={
                "id":"order_price"
            }),

        
        }



class WeeklyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
            visible.field.widget.attrs['placeholder'] = visible.field.label
    
    
    class Meta:
        model = WeeklyAssigment
        fields = "__all__"
        exclude = ['client', "duration","price"]

