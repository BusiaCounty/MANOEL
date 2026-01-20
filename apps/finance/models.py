from django.db import models
from apps.projects.models import Project

class FinancialYear(models.Model):
    name = models.CharField(max_length=20, unique=True, help_text="e.g. 2024/2025")
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class BudgetAllocation(models.Model):
    project = models.ForeignKey(Project, related_name='budgets', on_delete=models.CASCADE)
    financial_year = models.ForeignKey(FinancialYear, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    allocation_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('project', 'financial_year')

    def __str__(self):
        return f"{self.project.name} - {self.financial_year}: {self.amount}"

class Expenditure(models.Model):
    project = models.ForeignKey(Project, related_name='expenditures', on_delete=models.CASCADE)
    budget_allocation = models.ForeignKey(BudgetAllocation, related_name='expenditures', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    payment_date = models.DateField()
    payee = models.CharField(max_length=255)
    description = models.TextField()
    evidence_file = models.FileField(upload_to='expenditure_evidence/', blank=True, null=True)

    def __str__(self):
        return f"{self.project.name} - {self.amount} on {self.payment_date}"
