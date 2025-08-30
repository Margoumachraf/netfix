# from django.apps import AppConfig


# class ServicesConfig(AppConfig):
#     name = 'services'


from django.apps import AppConfig

class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'

    def ready(self):
        # import here, inside the function
        Type = self.get_model('type')

        services = [
            "Air Conditioner",
            "All in One",
            "Carpentry",
            "Electricity",
            "Gardening",
            "Home Machines",
            "House Keeping",
            "Interior Design",
            "Locks",
            "Painting",
            "Plumbing",
            "Water Heaters",
        ]
        for s in services:
            Type.objects.get_or_create(name=s)
