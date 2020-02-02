from django.http import HttpResponse
# Create your views here.
from django.template import loader

from photos.models import Photo


def index(req):
    photos = Photo.objects.all().order_by('id')
    template = loader.get_template('index.html')
    context = {
        'photos': photos,
    }
    return HttpResponse(template.render(context, req))

