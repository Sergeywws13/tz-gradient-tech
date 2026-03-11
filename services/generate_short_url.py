import string
from secrets import choice


ALPHABET: str = string.ascii_letters + string.digits

def generate_random_url():
    short_url = ""
    for _ in range(6):
        short_url += choice(ALPHABET)

    return short_url
