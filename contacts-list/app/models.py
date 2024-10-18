from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        if self.is_favorite:
            return f"* {self.name} - Phone: {self.phone}; email: {self.email}"
        else:
            return f"{self.name} - Phone: {self.phone}; email: {self.email}"


def create_contact(name, email, phone, is_favorite=False):
    c = Contact.objects.create(
        name=name, email=email, phone=phone, is_favorite=is_favorite
    )
    c.save()
    return c


def all_contacts():
    return Contact.objects.all()


def find_contact_by_name(name):
    try:
        return Contact.objects.get(name=name)
    except Contact.DoesNotExist:
        return None


def favorite_contacts():
    return Contact.objects.filter(is_favorite=True)


def update_contact_email(name, new_email):
    contact = Contact.objects.get(name=name)
    contact.email = new_email
    contact.save()
    return contact


def delete_contact(name):
    Contact.objects.get(name=name).delete()
