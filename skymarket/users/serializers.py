from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
# TODO Здесь нам придется переопределить сериалайзер, который использует djoser
# TODO для создания пользователя из за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    # email = serializers.CharField(max_length=50, validators=[UniqueValidator(queryset=User.objects.all()), EmailValidator])

    class Meta:
        model = User
        fields = '__all__'
    
    # def create(self, validated_data):

    #     user = super().create(validated_data)
    #     user.set_password(user.password)
    #     user.save()
        
    #     return user
    pass

class CurrentUserSerializer(serializers.ModelSerializer):
    pass
