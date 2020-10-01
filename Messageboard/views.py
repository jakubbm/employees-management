from django.shortcuts import render
from datetime import timedelta, datetime
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MessageSerializer, MessageSerializerWrite
from .models import Message


@login_required
def messageBorad(request):
    user_id = request.user.employee.id
    context = {'user_id': user_id}

    eight_before = datetime.today()-timedelta(days=14)
    seven_before = datetime.today()-timedelta(days=7)
    # Delete old object - older than 7 days
    Message.objects.filter(date__range=[seven_before, eight_before]).delete()

    return render(request, 'Messageboard/message_board.html', context)


@api_view(['GET'])
def messageList(request):
    messages = Message.objects.all().order_by('date')
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def messageQuantity(request):
    quantity = Message.objects.all().count()
    return Response(quantity)


@api_view(['POST'])
def messageCreate(request):
    serializer = MessageSerializerWrite(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print("Error")
    return Response({"success": "Message created successfully"})
