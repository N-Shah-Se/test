from rest_framework import views, status
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from .models import UserModel
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from user_manager.permissions import AllowOptionsAuthentication

class UserManager(views.APIView):
    permission_classes = (AllowOptionsAuthentication,)
    # permission_classes = (IsAuthenticated,)

    serializer_class = UserSerializer

    @api_view(['POST'])
    # @permission_classes([])
    def add_user(request):
        rec = UserModel.objects.filter(is_admin=True)
        if not rec:
            if not request.data._mutable:
                request.data._mutable = True
                request.data['is_admin'] = True
                password = request.data['password']
                request.data['password'] = make_password(password)
                request.data._mutable = False
            User = UserSerializer(data=request.data)

            if User.is_valid():
                User.save()
            if status.HTTP_200_OK:
                return JsonResponse({"User Id": User.data['id']})
            elif status.HTTP_500_INTERNAL_SERVER_ERROR:
                return JsonResponse({"error": "Internal Server Error"})

        request.data._mutable = True
        password = request.data['password']
        request.data['password'] = make_password(password)
        request.data._mutable = False
        User = UserSerializer(data=request.data)
        if User.is_valid():
            User.save()
        if status.HTTP_200_OK:
            return JsonResponse({"User Id": User.data['id']})
        elif status.HTTP_500_INTERNAL_SERVER_ERROR:
            return JsonResponse({"error": "Internal Server Error"})

    @api_view(['PUT'])
    # @permission_classes([IsAuthenticated])
    def update_password(request):

        new_password = make_password(request.data['password'])
        is_admin = request.user.is_admin
        if is_admin:
            user = UserModel.objects.filter(id=request.data['user_id'])
            if user is None:
                return JsonResponse({"UserData": "User Not Found"})
            user.update(password=new_password)
            return JsonResponse({"UserData": "Changed Password"})
        if status.HTTP_200_OK:
            return JsonResponse({"status": "UnAuthenticated"})
        elif status.HTTP_500_INTERNAL_SERVER_ERROR:
            return JsonResponse({"error": "Internal Server Error"})

    @api_view(['DELETE'])
    # @permission_classes([IsAuthenticated])
    def delete_user(request, user_id):
        is_admin = request.user.is_admin

        if request.user.id == user_id:
            return JsonResponse({"UserData": "Admin Couldn't be Deleted"})
        elif is_admin:
            user = UserModel.objects.filter(id=user_id)

            if not user:
                return JsonResponse({"UserData": "User Not Found"})
            else:
                user.delete()
                return JsonResponse({"UserData": "Deleted User"})

        if status.HTTP_200_OK:
            return JsonResponse({"status": "UnAuthenticated"})
        elif status.HTTP_500_INTERNAL_SERVER_ERROR:
            return JsonResponse({"error": "Internal Server Error"})