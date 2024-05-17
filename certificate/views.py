import os
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.conf import settings
from pyhtml2pdf import converter
from django.template import TemplateDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from users.models import User
from django.shortcuts import render

def certificate(request, pk):
    try:
        user = User.objects.filter(id=pk).first()
        user_name = user.ism
        user_surname = user.familya
        template = get_template('certificate/pdf.html')
        context = {'ism': user_name, 'familya': user_surname}
        html = template.render(context)
        return HttpResponse(html)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    
# from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin
# from users.models import User
# from django.views.generic import DetailView
@csrf_exempt
def pdf(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        user = User.objects.filter(id=user_id).first()
        user_name = user.ism
        user_surname = user.familya
        
        # return converter.convert(f'http://127.0.0.1:8000/api/pdf/{user_id}', f'{user_name}{user_surname}.pdf')
    # converter.convert(f'http://127.0.0.1:8000/api/pdf/{user_id}', f'{user_name}{user_surname}.pdf')
    converter.convert(f'http://127.0.0.1:8000/api/pdf/{user_id}', f'{user_name}{user_surname}.pdf')
    return JsonResponse({'message': 'Pdf is generated successfully!'})


# class PDFUserDetailView(PDFTemplateResponseMixin, DetailView):
#     model = User
#     context_object_name = 'user'
#     template_name = 'certificate/pdf.html'