import base64

# WE use ascii encoding here WOOOHOOO

# Encodes the password in question
def encode(pwd):
    return base64.b64encode(pwd.encode('ascii')).decode('ascii')

# Decodes the pasword in question
def decode(pwd):
    return base64.b64decode(pwd.encode('ascii')).decode('ascii')
