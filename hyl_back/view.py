from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    '''
        Esta clase se usa para sobre escribir los datos que contendra
        el token que se envia cuando el usuario se loguea
    '''
    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)

        permision = []
        for x in user.get_all_permissions():
            permision.append(x)

        # Add custom claims
        token['permissions'] = permision
        token['first_name'] = user.first_name

        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
