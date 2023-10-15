from core.abstract.serializers import AbstractSerializer
from core.user.models import User


class UserSerializer(AbstractSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'bio',
                  'avatar', 'email', 'is_active', 'created', 'updated']
        read_only_field = ['is_active']
