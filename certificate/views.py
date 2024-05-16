import os
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.conf import settings
from pyhtml2pdf import converter
from django.template import TemplateDoesNotExist
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def generate_pdf(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        name = data.get('name')

        html_template_path = os.path.join(settings.BASE_DIR, 'certificate/templates/certificate', 'pdf_template.html')

        template = get_template(html_template_path)
        html_content = template.render({'firstname': firstname, 'lastname': lastname, 'name': name})

        pdf_output_path = os.path.join(settings.BASE_DIR, 'media/certificate', f'{firstname}.pdf')

        converter.convert(f'file:///{html_template_path}', f'{firstname}.pdf')

        # with open(pdf_output_path, 'rb') as pdf_file:
        #     response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        #     response['Content-Disposition'] = f'inline; filename="{firstname}.pdf"'

        return JsonResponse({'message': 'Certificate created successfully.'}, status=200)
