from django import forms
from dashboard.models import Budget, Capital_equip,Salaryy,Investigation1,Investigation2,Consumable

class BudgetForm(forms.ModelForm):

    class Meta:
        model = Budget
        fields = '__all__'
        labels = {
            'Nop': "No of Patients Sanctioned for the study",
            "Travel_allow": "Patient Travel Allowance/Compensatory allowance",
            "No_of_visit": "Total no of visits per patient",
            "Rs_per_visit": "Rs per visit patient",
            " Research_fellow_id": "Research Fellow/Clinical Asst",
            "Miscellan":"Miscellaneous"
        }


class CapitalForm(forms.ModelForm):

    class Meta:
        model = Capital_equip
        fields = ("Name", "Price")


class Invest1(forms.ModelForm):

    class Meta:
        model = Investigation1
        fields = ("tests", "exist_test_id", "No_of_pat", "Tarrif")
        labels = {
            "tests" : "Name of Test",
            "exist_test_id" : "Existing Test",
            "No_of_pat": "No of Patients",
        }


class Salary(forms.ModelForm):

    class Meta:
        model = Salaryy
        fields = ("Name", "Study", "Salary")


class Invest2(forms.ModelForm):
    class Meta:
        model = Investigation2
        fields = ("tests", "exist_test_id", "No_of_pat", "Followup", "Tarrif")
        labels = {
            "tests": "Name of Test",
            "exist_test_id": "Existing Test",
            "No_of_pat": "No of Patients",
            "Followup" : "Follow-up"
        }


class Consumable(forms.ModelForm):
    class Meta:
        model = Consumable
        fields = ("consum_name", "qty", "Rs_per_unit", "Catlog_no", "Name_of_manufact")
        labels ={
            "consum_name" : "Consumables Name",
            "qty" : "Quantity Required",
            "Rs_per_unit" : "Rate/Unit",
            "Catlog_no" : "Catalog Number",
            "Name_of_manufact" : "Name of Manufacturer / Supplier"
        }
