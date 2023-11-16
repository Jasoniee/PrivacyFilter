from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import spacy
import os

# Load your spaCy model
current_directory = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(current_directory, 'fine_tuned_ner_model')
nlp = spacy.load(model_path)
@csrf_exempt
def mark_text(request):
    data = json.loads(request.body)
    text = data['text']
    doc = nlp(text)
    marked_text = replace_entities_with_markup(doc)
    return JsonResponse({'marked_text': marked_text})

@csrf_exempt
def anonymize_text(request):
    data = json.loads(request.body)
    text = data['text']
    doc = nlp(text)
    anonymized_text = anonymize_entities(doc)
    return JsonResponse({'anonymized_text': anonymized_text})

def replace_entities_with_markup(doc):
    marked_text = ""
    last_idx = 0
    for ent in doc.ents:
        # Append text before the entity
        marked_text += doc[last_idx:ent.start].text
        # Wrap the entity in a span with a class for styling
        marked_text += f'<span class="highlight">{" "+ent.text+ " "}</span>'
        last_idx = ent.end
    # Append remaining text after the last entity
    marked_text += doc[last_idx:].text
    return marked_text



def anonymize_entities(doc):
    anonymized_text = ""
    last_idx = 0
    for ent in doc.ents:
        anonymized_text += doc[last_idx:ent.start].text + " [REDACTED] "
        last_idx = ent.end
    anonymized_text += doc[last_idx:].text
    return anonymized_text

