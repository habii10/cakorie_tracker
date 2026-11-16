from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response

from food_log.models import Calorie
from food_log.serializers import CalorieSerializers
# Create your views here.
class CalorieListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    def get(self,request):


        auth_user=request.user

        qs=Calorie.objects.filter(owner=auth_user)

        serialiser_instance=CalorieSerializers(qs,many=True)

        return Response(serialiser_instance.data)

    def post(self,request):

        form_data=request.data

        auth_user=request.user

        serializer_instance=CalorieSerializers(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(owner=auth_user)
            return Response(serializer_instance.data)
        else:
             return Response (serializer_instance.errors)
        
from food_log.permissions import IsOwner
class CalorieRetrieveUpdateDeleteView(APIView):
     authentication_classes=[authentication.BasicAuthentication]
     permission_classes=[IsOwner]

     def get(self,request,pk=None):
        #qs=Calorie.objects.get(id=pk)
        qs=get_object_or_404(Calorie,id=pk)

        self.check_object_permissions(request,qs)

        serialized_instance=CalorieSerializers(qs)
        return Response(serialized_instance.data)        

     def put(self,request,pk=None):
         instance=get_object_or_404(Calorie,id=pk)
         self.check_object_permissions(request,instance)

         form_data=request.data
         serialized_instance=CalorieSerializers(data=form_data,instance=instance)

         if serialized_instance.is_valid():
             serialized_instance.save()
             return Response(data=serialized_instance.data)

         else:
             return Response(data=serialized_instance.errors)

     def delete(self,request,pk=None):
         qs=get_object_or_404(Calorie,id=pk)
         self.check_object_permissions(request,qs)
         qs.delete()
         return Response({"message":"deleted..."})    



        
       