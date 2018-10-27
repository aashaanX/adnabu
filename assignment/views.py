from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from assignment.models import URequest
from assignment.serializer import URequestSerializer
from .tasks import extract_async

class ExtractUrls(APIView):


    def post(self, request, format=None):
        try:
            print(request.data)
            request_data = URequestSerializer(data=request.data)
            if request_data.is_valid():
                print("data is valid")
                urequest = URequest()
                urequest.email_id = request_data.validated_data["email"]
                urequest.save()
                urequest.add_urls(request_data.validated_data["urls"])
                extract_async.apply_async((urequest,),countdown=0)
            else:
                return Response(data={"SUCCESS": False, "message":"Invalid request"}, status=status.HTTP_200_OK)
        except Exception as e:
            print("Something Went Wrong", e)
            return Response(data={"SUCCESS":False, "message":"Something went wrong, please report the issue"})

        return Response(data={"SUCESS":True}, status=status.HTTP_200_OK)
