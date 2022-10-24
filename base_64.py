import base64


def encode(pwd):
    return base64.b64encode(pwd.encode('ascii')).decode('ascii')

def decode(pwd):
    return base64.b64decode(pwd.encode('ascii')).decode('ascii')
