from django.db import models
from typing import List, Optional
from django.shortcuts import get_object_or_404

class BaseRepository():
    def get_all(self) -> List[models.Model]:
        return self.model.objects.all()
    
    def get_by_id(self, id: int) -> Optional[models.Model]:
        return self.model.objects.get(pk=id)
    
    def get_or_404(self, id):
        return get_object_or_404(self.model, pk=id)
    
    def filter_by_id(self, id: int) -> Optional[models.Model]:
        return self.model.objects.filter(pk=id).first()
    
    def filter_by_property_name(self, property, value):
        kwargs = {
            '{0}__name__icontains'.format(property): value
        }
        return self.model.objects.filter(**kwargs)
    
    def delete(self, instance: models.Model):
        instance.delete()