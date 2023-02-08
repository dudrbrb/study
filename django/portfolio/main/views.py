from django.views import generic
from .models import Works, Stacks
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'data_list'
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        datalist = {'Works': Works.objects.all(), 'Stacks' : Stacks.objects.all()}
        return datalist