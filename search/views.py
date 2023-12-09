# from django.shortcuts import render
# from django.views.generic import ListView
# from app.models import NewsAndEvents


# class SearchNewsAndEventsView(ListView):
#     template_name = "search/search_view.html"

#     def get_context_data(self, *args, **kwargs):
#         context = super(SearchNewsAndEventsView, self).get_context_data(*args, **kwargs)
#         query = self.request.GET.get('q')
#         context['query'] = query
#         context['obj_counter'] = NewsAndEvents.objects.search(query).count()
#         # SearchQuery.objects.create(query=query)
#         return context

#     def get_queryset(self, *args, **kwargs):
#         request = self.request
#         method_dict = request.GET
#         query = method_dict.get('q', None) # method_dict['q']
#         if query is not None:
#             return NewsAndEvents.objects.search(query)
#         return NewsAndEvents.objects.all()
#         '''
#         __icontains = field contains this
#         __iexact = fields is exactly this
#         '''










# search.views.py
from itertools import chain
from django.views.generic import ListView

from django.db.models import Q

from accounts.models import User, Student
from app.models import NewsAndEvents
from course.models import Program, Course



class SearchView(ListView):
    template_name = 'search/search_view.html'
    paginate_by = 20
    count = 0
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

  
            # combine querysets 
          