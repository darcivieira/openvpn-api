# from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .vpn import OpenVPN


class StatusAPIView(APIView):
    vpn = OpenVPN()

    def get(self, request):
        date = self.vpn.get_status()
        return Response(date)


class LogAPIView(APIView):
    vpn = OpenVPN()

    def get(self, request):
        date = self.vpn.get_log()
        return Response(date)


class StateAPIView(APIView):
    vpn = OpenVPN()

    def get(self, request):
        date = self.vpn.get_state()
        return Response(date)