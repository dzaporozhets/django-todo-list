from django.template import Context, loader
from lists.models import Task
from django.http import HttpResponse

def index(request):
  latest_task_list = Task.objects.all().order_by('-pub_date')[:5]
  t = loader.get_template('tasks/index.html')
  c = Context({
    'latest_task_list': latest_task_list,
  })
  return HttpResponse(t.render(c))
