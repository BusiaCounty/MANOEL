from django.contrib import admin
from .models import FinancialYear, BudgetAllocation, Expenditure

@admin.register(FinancialYear)
class FinancialYearAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')

@admin.register(BudgetAllocation)
class BudgetAllocationAdmin(admin.ModelAdmin):
    list_display = ('project', 'financial_year', 'amount')
    list_filter = ('financial_year',)
    search_fields = ('project__name',)

@admin.register(Expenditure)
class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('project', 'amount', 'payee', 'payment_date')
    list_filter = ('project', 'payment_date')
    search_fields = ('project__name', 'payee', 'description')
