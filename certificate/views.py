# import os
# import json
# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
# from django.template.loader import get_template
# from django.conf import settings
# from pyhtml2pdf import converter
# from django.template import TemplateDoesNotExist
# from django.views.decorators.csrf import csrf_exempt
# from users.models import User
# from django.shortcuts import render

# @csrf_exempt
# def generate_pdf(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         user_id = data.get('user_id')
#         user = User.objects.filter(id=user_id).first()
#         user_name = user.ism
#         user_surname = user.familya
        
#         html_template_path = os.path.join(settings.BASE_DIR, 'certificate/templates/certificate', 'pdf.html')


      
#         template = get_template(html_template_path)
#         html_content = template.render({'ism': user_name, 'familya': user_surname})


#         pdf_output_path = os.path.join(settings.BASE_DIR, 'media/certificate', f'{user_name}.pdf')
#         converter.convert(f'file:///{html_template_path}', f'file/sertificates/{user_name}.pdf')
        
        
#         return render(request, 'certificate/pdf.html', {'ism': user_name, 'familya': user_surname})
#     else:
#         return JsonResponse({'error': 'Invalid HTTP method.'}, status=400)

# def pdf(request):
#     return render(request, 'certificate/pdf.html', {'ism': 'John', 'familya': 'Doe'})
from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin
from users.models import User
from django.views.generic import DetailView




class PDFUserDetailView(PDFTemplateResponseMixin, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'certificate/pdf.html'