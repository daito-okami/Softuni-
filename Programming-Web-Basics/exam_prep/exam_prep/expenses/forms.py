from django import forms

from exam_prep.expenses.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"


class CreateExpenseForm(ExpenseForm):
    pass


class EditExpenseForm(ExpenseForm):
    pass


class DeleteExpenseForm(ExpenseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
