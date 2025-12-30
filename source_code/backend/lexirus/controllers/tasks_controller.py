import os

from celery import shared_task, chain, group

# Models
from lexirus.models import InputDocument



@shared_task(bind=True)
def process_image_document(self, document_id):
    """Main task to orchestrate image document translation"""
    try:
        doc = InputDocument.objects.get(id=document_id)
        doc.task_process_status = 1  # Processing
        doc.save()

        # Create task chain for image processing
        workflow = chain(
            extract_image_to_markdown.s(document_id),
            translate_markdown.s(document_id),
            convert_markdown_to_image.s(document_id)
        )
        
        workflow.apply_async()
        
    except InputDocument.DoesNotExist:
        print(f"Document {document_id} not found")
    except Exception as e:
        doc = InputDocument.objects.get(id=document_id)
        doc.task_process_status = -1  # Error
        doc.save()
        raise
    
    

@shared_task(bind=True)
def process_pdf_document(self, document_id):
    """Main task to orchestrate PDF document translation"""
    try:
        doc = InputDocument.objects.get(id=document_id)
        doc.task_process_status = 1  # Processing
        doc.save()

        # Create task chain for PDF processing
        workflow = chain(
            split_pdf_to_pages.s(document_id),
            convert_pages_to_markdown.s(document_id),
            translate_all_markdowns.s(document_id),
            rejoin_pdf_from_markdowns.s(document_id)
        )
        
        workflow.apply_async()
        
    except InputDocument.DoesNotExist:
        print(f"Document {document_id} not found")
    except Exception as e:
        doc = InputDocument.objects.get(id=document_id)
        doc.task_process_status = -1  # Error
        doc.save()
        raise
    
    
    
    
@shared_task(bind=True)
def extract_image_to_markdown(self, document_id):
    """Task 1: Extract text from image and create markdown"""
    try:
        doc = InputDocument.objects.get(id=document_id)
        
        # TODO: Implement OCR or image-to-text extraction
        # Example using pytesseract or similar:
        # from PIL import Image
        # import pytesseract
        # image = Image.open(doc.file.path)
        # text = pytesseract.image_to_string(image, lang=doc.from_lang)
        
        # Save markdown to temporary location or database field
        markdown_path = f"/tmp/markdown_{document_id}.md"
        # with open(markdown_path, 'w') as f:
        #     f.write(text)
        
        print(f"Extracted markdown for image document {document_id}")
        return {"document_id": document_id, "markdown_path": markdown_path}
        
    except Exception as e:
        print(f"Error extracting image to markdown: {e}")
        raise
    
    
    
@shared_task(bind=True)
def translate_markdown(self, previous_result, document_id):
    """Task 2: Translate markdown according to format"""
    try:
        doc = InputDocument.objects.get(id=document_id)
        markdown_path = previous_result.get("markdown_path")
        
        # Read original markdown
        # with open(markdown_path, 'r') as f:
        #     original_text = f.read()
        
        # Translate based on format
        if doc.translation_format == "LINE_CONN":
            translated = translate_line_connection(doc, "original_text")
        elif doc.translation_format == "SENTENCE":
            translated = translate_sentence_level(doc, "original_text")
        elif doc.translation_format == "NOUNS_VERBS":
            translated = translate_nouns_verbs(doc, "original_text")
        
        # Save translated markdown
        translated_path = f"/tmp/translated_{document_id}.md"
        # with open(translated_path, 'w') as f:
        #     f.write(translated)
        
        print(f"Translated markdown for document {document_id}")
        return {"document_id": document_id, "translated_path": translated_path}
        
    except Exception as e:
        print(f"Error translating markdown: {e}")
        raise
    


@shared_task(bind=True)
def convert_markdown_to_image(self, previous_result, document_id):
    """Task 3: Convert translated markdown back to image"""
    try:
        doc = InputDocument.objects.get(id=document_id)
        translated_path = previous_result.get("translated_path")
        
        # TODO: Convert markdown to image
        # This might involve rendering text with proper formatting
        
        output_path = f"translated_images/translated_{document_id}.png"
        
        # Update document with output path
        doc.task_process_status = 2  # Completed
        doc.save()
        
        print(f"Converted markdown to image for document {document_id}")
        return {"document_id": document_id, "output_path": output_path}
        
    except Exception as e:
        doc = InputDocument.objects.get(id=document_id)
        doc.task_process_status = -1  # Error
        doc.save()
        raise





@shared_task(bind=True)
def split_pdf_to_pages(self, document_id):
    """Task 1: Split PDF into single pages"""
    try:
        doc = InputDocument.objects.get(id=document_id)
        
        # TODO: Use PyPDF2 or similar to split PDF
        # from PyPDF2 import PdfReader, PdfWriter
        # reader = PdfReader(doc.file.path)
        # pages = []
        # for i, page in enumerate(reader.pages):
        #     writer = PdfWriter()
        #     writer.add_page(page)
        #     output_path = f"/tmp/page_{document_id}_{i}.pdf"
        #     with open(output_path, 'wb') as f:
        #         writer.write(f)
        #     pages.append(output_path)
        
        pages = []  # List of page paths
        print(f"Split PDF {document_id} into pages")
        return {"document_id": document_id, "pages": pages}
        
    except Exception as e:
        print(f"Error splitting PDF: {e}")
        raise


@shared_task(bind=True)
def convert_pages_to_markdown(self, previous_result, document_id):
    """Task 2: Convert each PDF page to markdown"""
    try:
        pages = previous_result.get("pages", [])
        markdown_files = []
        
        for page_path in pages:
            # TODO: Extract text from PDF page
            # Use pdfplumber, PyMuPDF, or similar
            # markdown_content = extract_text_from_pdf_page(page_path)
            
            markdown_path = page_path.replace('.pdf', '.md')
            # with open(markdown_path, 'w') as f:
            #     f.write(markdown_content)
            
            markdown_files.append(markdown_path)
        
        print(f"Converted {len(markdown_files)} pages to markdown")
        return {"document_id": document_id, "markdown_files": markdown_files}
        
    except Exception as e:
        print(f"Error converting pages to markdown: {e}")
        raise


@shared_task(bind=True)
def translate_all_markdowns(self, previous_result, document_id):
    """Task 3: Translate each markdown file"""
    try:
        doc = InputDocument.objects.get(id=document_id)
        markdown_files = previous_result.get("markdown_files", [])
        translated_files = []
        
        for markdown_file in markdown_files:
            # with open(markdown_file, 'r') as f:
            #     original_text = f.read()
            
            # Translate based on format
            if doc.translation_format == "LINE_CONN":
                translated = translate_line_connection(doc, "original_text")
            elif doc.translation_format == "SENTENCE":
                translated = translate_sentence_level(doc, "original_text")
            elif doc.translation_format == "NOUNS_VERBS":
                translated = translate_nouns_verbs(doc, "original_text")
            
            translated_path = markdown_file.replace('.md', '_translated.md')
            # with open(translated_path, 'w') as f:
            #     f.write(translated)
            
            translated_files.append(translated_path)
        
        print(f"Translated {len(translated_files)} markdown files")
        return {"document_id": document_id, "translated_files": translated_files}
        
    except Exception as e:
        print(f"Error translating markdowns: {e}")
        raise


@shared_task(bind=True)
def rejoin_pdf_from_markdowns(self, previous_result, document_id):
    """Task 4: Rejoin translated markdowns into final PDF"""
    try:
        doc = InputDocument.objects.get(id=document_id)
        translated_files = previous_result.get("translated_files", [])
        
        # TODO: Convert each markdown to PDF page and merge
        # Use reportlab, weasyprint, or similar for markdown to PDF
        # Then use PyPDF2 to merge all pages
        
        output_path = f"translated_pdfs/translated_{document_id}.pdf"
        
        # Update document status
        doc.task_process_status = 2  # Completed
        doc.save()
        
        print(f"Rejoined PDF for document {document_id}")
        return {"document_id": document_id, "output_path": output_path}
        
    except Exception as e:
        doc = InputDocument.objects.get(id=document_id)
        doc.task_process_status = -1  # Error
        doc.save()
        raise


# ===== TRANSLATION HELPER FUNCTIONS =====

def translate_line_connection(doc, text):
    """
    Translate with line connection format:
    Original line
    Word1 - translation1, Word2 - translation2, ...
    """
    # TODO: Implement line-by-line translation with word connections
    # Example output:
    # "Не хочу хвастаться"
    # "Не - not, хочу - want, хвастаться - to brag"
    pass


def translate_sentence_level(doc, text):
    """
    Translate at sentence level:
    Original sentence
    Translated sentence
    """
    # TODO: Implement sentence-level translation
    pass


def translate_nouns_verbs(doc, text):
    """
    Translate only nouns and verbs with connections:
    Original line
    Noun1 - translation1, Verb1 - translation1, ...
    """
    # TODO: Implement nouns/verbs extraction and translation
    # Use NLP to identify nouns and verbs, then translate
    pass


# celery.py (in your Django project root)
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

app = Celery('your_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# settings.py additions
"""
# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
"""


# models.py additions
"""
from django.db import models

class InputDocument(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=100)
    from_lang = models.CharField(max_length=10)
    to_lang = models.CharField(max_length=10)
    task_process_status = models.IntegerField(default=0)
    # 0: Pending, 1: Processing, 2: Completed, -1: Error
    translation_format = models.CharField(max_length=20)
    # LINE_CONN, SENTENCE, NOUNS_VERBS
    file = models.FileField(upload_to='input_documents/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
"""