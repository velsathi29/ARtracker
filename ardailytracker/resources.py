from import_export import resources
from .models import Detail

class DetailResource(resources.ModelResource):
    class Meta:
        model = Detail