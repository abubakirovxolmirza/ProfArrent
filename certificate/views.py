# views.py
import os
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from pyhtml2pdf import converter
from django.template import TemplateDoesNotExist
    
def generate_pdf(request):
    html_template_path = os.path.join(settings.BASE_DIR, 'certificate/templates/certificate', 'pdf_template.html')

    template = get_template(html_template_path)
    html_content = template.render()

    pdf_output_path = os.path.join(settings.BASE_DIR, 'media')

    converter.convert(f'file:///{html_template_path}', pdf_output_path)

    with open(pdf_output_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="sample2.pdf"'
    
    return response
