from django.db.models import Q
from django.http import HttpResponse
import json

from task1.models import Product


def live_search(request, template_name="shop/livesearch_results.html"):
    q = request.GET.get("q", "")
    if True:
        result_list = list(Product.objects.filter(Q(slug__icontains='q')
                                                  | Q(name__icontains='q')
                                                  | Q(description__icontains='q')))
    else:
        result_list = "Nothing found"
    return HttpResponse(json.dumps(str(result_list)), content_type='application/json')
