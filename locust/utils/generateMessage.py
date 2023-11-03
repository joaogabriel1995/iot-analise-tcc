import random
import string

def generate_random_payload(length, client_id, request_count):
    message_data = {
    'message': "",
    'metadata': {
        'request_count': request_count,
    },
    'client_id': client_id,
}
    payload = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length -len('{}'.format(message_data))))
    message_data["message"] = payload

    return '{}'.format(message_data)