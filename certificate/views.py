# views.py
import os
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from pyhtml2pdf import converter
from django.template import TemplateDoesNotExist
    
def generate_pdf(request):
    # Path to the HTML template
    html_template_path = os.path.join(settings.BASE_DIR, 'templates', 'certificate', 'pdf_template.html')

    # Load the HTML template
    template = get_template(html_template_path)
    html_content = template.render()

    # Path to save the PDF file
    pdf_output_path = os.path.join(settings.BASE_DIR, 'media', 'sample2.pdf')

    # Convert HTML to PDF
    converter.convert(f'file:///{html_template_path}', pdf_output_path)

    # Read the generated PDF
    with open(pdf_output_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="sample2.pdf"'
    
    return response
