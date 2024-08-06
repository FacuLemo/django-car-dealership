from django.core.exceptions import ValidationError


def check_exists(form, propertyName):
    property = form.cleaned_data.get(propertyName)
    instance = type(form.save(commit=False))
    kwargs = {
        '{0}'.format(propertyName): property
    }
    property_exists = instance.objects.filter(**kwargs).exists()
    if property_exists:
        raise ValidationError(f"{property} ya está en uso")
    return property