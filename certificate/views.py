import os
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.conf import settings
from pyhtml2pdf import converter
from django.template import TemplateDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from users.models import User, CustomUser
from django.shortcuts import render

@csrf_exempt
def certificate(request, pk):
    try:
        user = CustomUser.objects.filter(id=pk).first()
        user_name = user.first_name
        user_surname = user.last_name
        template = get_template('certificate/pdf.html')
        context = {'ism': user_name, 'familya': user_surname}
        html = template.render(context)
        return HttpResponse(html)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    
