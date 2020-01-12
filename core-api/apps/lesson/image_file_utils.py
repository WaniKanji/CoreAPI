import base64

from django.core.files.base import ContentFile

def save_base64_to_file(data, folder, filename):
    format, image_data = data.split(';base64,')
    file_extension = format.split('/')[-1]
    
    with open('{}/{}.{}'.format(folder, filename, file_extension), 'wb') as f:
        f.write(base64.b64decode(image_data))
    return '{}.{}'.format(filename, file_extension)
