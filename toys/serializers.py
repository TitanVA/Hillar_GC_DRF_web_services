from rest_framework import serializers
from .models import Toy


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = (
            "id",
            "name",
            "description",
            "toy_category",
            "release_date",
            "was_included_in_home",
            "created"
        )
