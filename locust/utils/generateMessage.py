import random
import string

def generate_random_payload(length):
    payload = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return payload