from django.views.generic import ListView
from django.shortcuts import render

from .models import Prospect
from .filters import LeadFilter

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class LeadsListView(ListView, LoginRequiredMixin):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"
    def get_queryset(self):
        user = self.request.user
        if user.Agent:
           queryset = Prospect.objects.filter(Agent= user)
        else:
            queryset = Prospect.objects.all()
        return queryset
        
@login_required
def lead_list(request):
    if request.user.Agent:
       leads = Prospect.objects.filter(Agent=request.user)
    else: leads = Prospect.objects.all()
    

    myFilter = LeadFilter(request.GET, queryset= leads)
    leads = myFilter.qs
    
    context = {
        "leads": leads,
        "myFilter": myFilter,
    }
    return render(request, "leads/lead_list.html", context)


##class SearchResultsView(ListView):
 #   model = Prospect
 #   template_name = "search_results.html"

  #  def get_queryset(self):  # new
     #   query = self.request.GET.get("q")
        #object_list = Prospect.objects.filter(
        #    Q(Nom__icontains=query) | Q(Prénom__icontains=query | | Q(status__in=query)
        #)
        #return object_list



