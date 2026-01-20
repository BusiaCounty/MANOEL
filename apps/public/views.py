from django.shortcuts import render
from django.db.models import Sum, Count
from apps.projects.models import Project
from apps.finance.models import BudgetAllocation

def home(request):
    total_projects = Project.objects.count()
    completed_projects = Project.objects.filter(status=Project.Status.COMPLETED).count()
    in_progress_projects = Project.objects.filter(status=Project.Status.IN_PROGRESS).count()
    
    total_budget_decimal = BudgetAllocation.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    # Convert to Millions for display
    total_budget = round(total_budget_decimal / 1000000, 1) if total_budget_decimal else 0

    recent_projects = Project.objects.select_related('ward').order_by('-updated_at')[:5]

    context = {
        'total_projects': total_projects,
        'completed_projects': completed_projects,
        'in_progress_projects': in_progress_projects,
        'total_budget': total_budget,
        'recent_projects': recent_projects,
    }
    return render(request, 'index.html', context)
