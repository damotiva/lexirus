from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Models
from lexirus.models import InputDocument

# Serializers
from lexirus.serializers import InputDocumentSerilizer

# Controllers
from lexirus.controllers import tasks_controller

@csrf_exempt
def upload_input_document(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("file")

        if not uploaded_file:
            return JsonResponse({"error": "No file uploaded"}, status=400)

        # Create DB record
        doc = InputDocument.objects.create(
            doc_name=uploaded_file.name,
            doc_type=uploaded_file.content_type,
            from_lang=request.POST.get("from_lang", ""),
            to_lang=request.POST.get("to_lang", ""),
            task_process_status=0,
            translation_format=request.POST.get("translation_format", "")
        )

        # Attaching file
        doc.file = uploaded_file
        doc.save()


        # Dispatch to appropriate task based on file type
        if doc.doc_type.startswith('image/'):
            # Queue image processing task
            tasks_controller.process_image_document.delay(doc.id)
        elif doc.doc_type == 'application/pdf':
            # Queue PDF processing task
            tasks_controller.process_pdf_document.delay(doc.id)
        else:
            return JsonResponse({
                "error": "Unsupported file type. Only images and PDFs are supported."
            }, status=400)

        # Create Scheduled Tasks to Translate Document
        
        # Tasks List for Image Document
        
        # 1 - Create Markdown format for the Image
        
        # 2 - Translate Markdown accordint to Metadata
        
        # 3 - Convert Markdown to Image
        
        
        
        # Tasks List for PDF Document
        #
        # 1 - Create PDF Single Pages from Whole Document 
        # to Single PDF Pages
        
        # 2 - Create Single PDF Pages Markdown Formats
        
        # 3 - Translate Each Markdown according to Metadata
        
        # 4 - Rejoin to Whole PDF from Single Markdowns  
        

        return JsonResponse({
            "message": "File uploaded successfully",
            "document_id": doc.id
        })
