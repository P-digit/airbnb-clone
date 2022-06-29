from django.contrib import admin
from . import models


@admin.register(models.Conversation)
class ConversationsAdmin(admin.ModelAdmin):

    """Conversaton Model Definition"""

    list_display = ("__str__", "count_messages", "count_participants")


@admin.register(models.Message)
class MessagesAdmin(admin.ModelAdmin):

    """Message Model Definition"""

    list_display = ("__str__", "created")
