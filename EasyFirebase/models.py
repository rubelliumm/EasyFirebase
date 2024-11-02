from django.db import models
from django.utils.translation import gettext_lazy as _

from EasyFirebase.fields import FirebaseImageField
from EasyFirebase.firebase import deleteUid, uploadFromFile


class FirebaseModel(models.Model):
    class Meta:
        abstract = True

    file_uuid = models.JSONField(
        _("Files UUID"), default=dict, editable=False, blank=True
    )

    def save(self, *args, **kwargs):
        firebase_image_fields = [
            getattr(self, field.name)
            for field in self._meta.get_fields()
            if isinstance(field, FirebaseImageField)
        ]
        for image_field in firebase_image_fields:
            if image_field:
                uid = upload(image=image_field.file)
                try:
                    self.file_uuid[str(image_field.field.name)].append(uid)
                except (AttributeError, KeyError):
                    self.file_uuid[str(image_field.field.name)] = [uid]
                except Exception as e:
                    raise ValueError(f"Failed to process {e} while saving model")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        firebase_image_fields = getattr(self, "file_uuid")
        for field, values in firebase_image_fields.items():
            deleteFromSource(field, values)
        super().delete(*args, **kwargs)


def deleteFromSource(field, values: list):
    for x in values:
        try:
            deleteUid(x)
        except:
            raise ValueError(f"Could not delete Image with id={x} from source.")


def upload(image):
    uid = uploadFromFile(image)
    return uid
