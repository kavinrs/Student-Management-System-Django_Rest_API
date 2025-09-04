from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class Auth_Serializers(TokenObtainPairSerializer):

    def validate(self, attrs):
        
        data= super().validate(attrs)

        data.update({
            'username':self.user.username
        })

        return data