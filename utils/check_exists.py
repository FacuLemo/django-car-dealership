from django.core.exceptions import ValidationError


def check_exists(form, propertyName):
    value = form.cleaned_data.get(propertyName)
    instance = type(form.save(commit=False))
    kwargs = {
        "{0}".format(propertyName): value,
    }
    value_exists = instance.objects.filter(**kwargs).exists()
    if value_exists:
        raise ValidationError(f"{value} ya está en uso")
    return value
