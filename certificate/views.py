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
    
@csrf_exempt
def pdf(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get("user_id")
        
        user = CustomUser.objects.filter(id=user_id).first()
        if not user:
            return JsonResponse({'error': 'User not found'}, status=404)
        
        user_name = user.first_name
        user_surname = user.last_name
        
        pdf_url = f'http://127.0.0.1:8000/api/pdf/{user_id}'
        pdf_filename = f'{user_name}{user_surname}.pdf'
        pdf_filepath = os.path.join(settings.MEDIA_ROOT, 'certificate', pdf_filename)
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(pdf_filepath), exist_ok=True)
        
        # Generate the PDF and save it to the specified path
        converter.convert(pdf_url, pdf_filepath)
        
        return JsonResponse({'message': 'PDF generated successfully!', 'pdf_url': f'{settings.MEDIA_URL}certificate/{pdf_filename}'})
    else:
        return HttpResponse(status=405)