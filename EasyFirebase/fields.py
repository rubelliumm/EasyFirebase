from typing import Any
from django.db import models


class FirebaseImageField(models.ImageField):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if value is not None:
            return value
        return super().to_python(value)

    def pre_save(self, model_instance, add):
        setattr(
            model_instance, self.attname, None
        )  # None for not saving the image file.
        return super().pre_save(model_instance, add)
