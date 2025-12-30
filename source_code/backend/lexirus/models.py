from django.db import models

# Input Documents Model
class InputDocument(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)

    doc_name = models.CharField(max_length=200, blank=True)
    doc_type = models.CharField(max_length=200, blank=True)
    from_lang = models.CharField(max_length=200, blank=True)
    to_lang = models.CharField(max_length=200, blank=True)
    # - Line Connection Translation (LINE_CONN)
    # - Sentence Level Translation (SENTENCE)
    # - Nouns & Verbs Level Translation (NOUNS_VERBS)
    
    file = models.FileField(upload_to='input_documents/')

    translation_format = models.CharField(max_length=200, blank=True) 
    task_process_status = models.CharField(max_length=200, blank=True) 
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'input_documents'
        

# Languages Model
class Language(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)

    lang_title = models.CharField(max_length=200, blank=True)
    lang_keyword = models.CharField(max_length=200, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'languages'