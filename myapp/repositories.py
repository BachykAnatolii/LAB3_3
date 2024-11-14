# repositories.py
from .models import Appraiser, Role


class AppraiserRepository:
    @staticmethod
    def get_all():
        return Appraiser.objects.all()

    @staticmethod
    def get_by_id(appraiser_id):
        return Appraiser.objects.get(id=appraiser_id)

    @staticmethod
    def create(data):
        # Convert role ID to Role instance
        role_id = data.pop("role")
        role_instance = Role.objects.get(id=role_id)

        # Create the appraiser with the role instance
        appraiser = Appraiser.objects.create(role=role_instance, **data)
        return appraiser

    @staticmethod
    def update(appraiser_id, data):
        appraiser = Appraiser.objects.get(id=appraiser_id)

        # Convert role ID to Role instance if it's provided in the data
        if "role" in data:
            role_id = data.pop("role")
            data["role"] = Role.objects.get(id=role_id)

        # Update the appraiser fields and save
        for key, value in data.items():
            setattr(appraiser, key, value)
        appraiser.save()
        return appraiser

    @staticmethod
    def delete(appraiser_id):
        appraiser = Appraiser.objects.get(id=appraiser_id)
        appraiser.delete()
