from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated


class UserModelViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_data = User.objects.all()
        return user_data

    # def retrieve(self, request, *args, **kwargs):
    #     params = kwargs
    #     params_list = params['pk'].split('-')
    #     user_data_filtered = User.objects.filter(city=params_list[0], age=params_list[1])
    #     serializer = UserSerializer(user_data_filtered, many=True)
    #     return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user_data = request.data
        new_user = User.objects.create(name=user_data['name'], age=user_data['age'], city=user_data['city'])
        new_user.save()
        serializer = UserSerializer(new_user)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        # logged_in_user = request.user
        # if (logged_in_user == "admin"):
        user_data = self.get_object()
        user_data.delete()
        msg = "Delete method overrided... Item has been deleted!"
        # else:
        #     msg = "Not allowed!"
        return Response(msg)
    
    