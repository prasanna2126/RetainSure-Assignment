import string, random, validators
from datetime import datetime

db = {}

def validate_url(url):
    return validators.url(url)

def generate_short_code(url):
    short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    while short_code in db:
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    db[short_code] = {'original_url': url, 'clicks': 0, 'created_at': datetime.utcnow().isoformat()}
    return short_code

def increment_click(code):
    if code in db:
        db[code]['clicks'] += 1

def get_url_info(code):
    return db.get(code)
  
