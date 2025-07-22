from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import RateLimit
from django.utils import timezone
from datetime import timedelta

RATE_LIMIT = 5  # max 5 requests
TIME_WINDOW = 60  # in seconds

# RequestLog – your model to access request history (DB).

@api_view(['GET'])
def my_protected_api(request):
    ip = get_client_ip(request)
    endpoint = request.path
    now = timezone.now()
    window_start = now - timedelta(seconds=TIME_WINDOW)

    # Count how many requests from this IP in the last X seconds
    recent_requests = RateLimit.objects.filter(
        ip_address=ip,
        endpoint=endpoint,
        timestamp__gte=window_start
    )

    if recent_requests.count() >= RATE_LIMIT:
        return Response({'error': 'Rate limit exceeded. Try again later.'}, status=429)

    # Record the request
    RateLimit.objects.create(ip_address=ip, endpoint=endpoint)
    return Response({'message': 'This is your protected data'}, status=200)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR') #gets ip address of client

 # 'HTTP_X_FORWARDED_FOR' - It contains the original IP address, \
    # plus any proxies it passed through. eg "123.45.67.89, 98.76.54.32"
    # We split by comma, take the first IP (original client IP.)

#REMOTE_ADDR is the direct IP address from the
#socket connection — works if there's no proxy involved.
