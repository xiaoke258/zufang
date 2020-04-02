from django.test import TestCase

# Create your tests here.
# import hashlib
#
# hasher = hashlib.md5()
# with open('views.py','rb') as file:
#     data = file.read(512)
#     while data:
#         hasher.update(data)
#         data= file.read(512)
# print(hasher.hexdigest())

import os
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zufang2.settings')
    import django
    django.setup()
    from app01 import models