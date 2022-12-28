import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    id = models.UUIDField(
        verbose_name="UUID",
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True, 
        primary_key=True)
    name = models.CharField(_("Username"), blank=False, max_length=255)
    birth_date = models.DateField(verbose_name=_("Birthday"), null=True, blank=True)
    mobile_number = models.CharField(
        verbose_name=_("Cell Phone"), max_length=11, null=True, blank=True
    )

    #: First and last name do not cover name patterns around the globe
    first_name = None  # type: ignore
    last_name = None  # type: ignore