from rest_framework import serializers
from api.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ['email', 'password', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
    extra_kwargs = {
        'password': {'write_only': True}
    }

  def create(self, validated_data):
    password = validated_data.pop('password')
    user = CustomUser.objects.create_user(
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name'],
      is_active=validated_data.get('is_active', True),
      is_staff=validated_data.get('is_staff', False),
      is_superuser=validated_data.get('is_superuser', False)
    )
    # Criptografa a senha
    user.set_password(password)
    # Salva o usuário no banco de dados
    user.save()
    return user
