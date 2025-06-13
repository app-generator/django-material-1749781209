# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    profile = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Cliente(models.Model):

    #__Cliente_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)

    #__Cliente_FIELDS__END

    class Meta:
        verbose_name        = _("Cliente")
        verbose_name_plural = _("Cliente")


class Projeto(models.Model):

    #__Projeto_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.TextField(max_length=255, null=True, blank=True)

    #__Projeto_FIELDS__END

    class Meta:
        verbose_name        = _("Projeto")
        verbose_name_plural = _("Projeto")



#__MODELS__END
