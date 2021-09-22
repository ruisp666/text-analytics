import json
from urllib.request import urlopen
import pickle
import re

def get_api_key():
    f = open('../keys/key.pickle', 'rb')
    api_key = pickle.load(f)['key']
    f.close()
    return api_key

API_KEY = get_api_key()

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


def extract_call_transcript(ticker: str, quarter: int, year: int):
    """
    Returns the transcript of a selected company's
    Parameters
    ----------
    ticker : str
    quarter : int
    year : int

    Returns
    -------
    transcript :str
    """
    url = f'https://financialmodelingprep.com/api/v3/earning_call_transcript/' \
          f'{ticker}?quarter={quarter}&year={year}&apikey={API_KEY} '
    obj = get_jsonparsed_data(url)
    transcript = obj[0]['content']
    return transcript


def nlp_tag_sentences_by_characters(transcript,  spacy_model, pattern='.*\$|.*\%'):
    transcript = re.sub(r'\.([a-zA-Z])', r'. \1', transcript) # Add 1 space after periods with letters
    transcript= re.sub('/\s\s+/g', ' ', transcript) # Reduce multiple white spaces to a single space
    doc_parsed = spacy_model(transcript)
    doc_sentences  = [sen for sen in doc_parsed.sents]
    tagged_sentences = [(i, s.text) for i, s in enumerate(doc_sentences) if re.search(pattern, s.text)] #match sentences with the pattern
    return doc_parsed, tagged_sentences

