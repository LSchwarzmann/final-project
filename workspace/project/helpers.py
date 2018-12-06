import io
import json
from flask import redirect, render_template, request, session, jsonify


# Implements the Google Speech-to-Text API to transcribe audio files into text
def transcribe_file(speech_file):
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
      content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code='en-US')

    response = client.recognize(config, audio)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.

    full_text = ""

    for result in response.results:
        # The first alternative is the most likely one for this portion.
        full_text += format(result.alternatives[0].transcript)

    return full_text

# Implements the Google sentiment analysis API to determine sentiment of text
def analyze_sentiment(content):
    from google.cloud import language_v1
    from google.cloud.language_v1 import enums
    import six
    import json

    client = language_v1.LanguageServiceClient()

    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {'type': type_, 'content': content}

    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment

    # Store score and magnitude in a dictionary
    dct = {
        "score": sentiment.score,
        "magnitude": sentiment.magnitude
    }

    return dct


# Implements the Google sentiment analysis API to determine sentiment of text
def entities_text(text):
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types
    import six
    import json
    """Detects entities in the text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities

    # entity types from enums.Entity.Type
    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

    entity_list = list()

    for entity in entities:
        dct = {
            'name': entity.name,
            'type': entity_type[entity.type],
            'salience': entity.salience,
            }
        entity_list.append(dct)

    return entity_list


def syntax_text(text):
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types
    import six
    import json
    """Detects syntax in the text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects syntax in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    tokens = client.analyze_syntax(document).tokens

    # part-of-speech tags from enums.PartOfSpeech.Tag
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
               'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')

    token_list = list()

    for token in tokens:
        dct = {
            "tag": pos_tag[token.part_of_speech.tag],
            "content": token.text.content
        }
        token_list.append(dct)

    return token_list


def classify_text(text):
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types
    import sys
    import six
    import json
    """Classifies content categories of the provided text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    document = types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

    # Catche an error where there are no entities to base classification on
    try:
        categories = client.classify_text(document).categories
    except:
        return list()

    category_list = list()

    for category in categories:
        dct = {
            'name': category.name,
            'confidence': category.confidence
        }

        category_list.append(dct)

    return category_list


# http://flask.pocoo.org/docs/0.12/patterns/apierrors/
# Handles invalid submission errors
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv