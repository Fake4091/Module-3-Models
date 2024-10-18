from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_starred = models.BooleanField(default=False)

    def __str__(self):
        if self.is_starred:
            return f"{'\033[1m'}* Title:{'\033[0m'} {self.title}\n{'\033[1m'}Desc:{'\033[0m'} {self.description}\n{40*'-'}"
        else:
            return f"{'\033[1m'}Title:{'\033[0m'} {self.title}\n{'\033[1m'}Desc:{'\033[0m'} {self.description}\n{40*'-'}"


def new_note(title, description, is_starred=False):
    note = Note(title=title, description=description, is_starred=is_starred)
    note.save()
    return note


def view_notes():
    notes = Note.objects.all()

    return notes


def search_notes_by_title(search):
    try:
        note = Note.objects.get(title=search)
        return note
    except Note.DoesNotExist:
        return None
    except Note.MultipleObjectsReturned:
        return None


def starred_notes():
    notes = Note.objects.filter(is_starred=True)

    return notes


def star_unstar_note(title):
    try:
        note = Note.objects.get(title=title)
        note.is_starred = not note.is_starred
        note.save()
        return note
    except Note.DoesNotExist:
        return None


def update_note(title, new_description):
    try:
        note = Note.objects.get(title=title)
        note.description = new_description
        note.save()
        return note
    except Note.DoesNotExist:
        return None


def delete_note(title):
    try:
        note = Note.objects.get(title=title)
        note.delete()
        return True
    except Note.DoesNotExist:
        return None
