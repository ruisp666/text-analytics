import json
from urllib.request import urlopen
import pickle

def get_api_key():
    f = open('../keys/key', 'rb')
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


