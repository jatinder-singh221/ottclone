from django.core.exceptions import ValidationError

def input_validation(values):
    if len(values)>10:
        if all(value.isalpha() or value.isspace() for value in values):
            pass
    else:
        raise ValidationError('Only letters and spaces Minimum of 11 words')

def image_validation(image):
    list_of_extension = ['jpg','jpeg','png']
    extension_of_image = str(image).split('.')[-1]
    if extension_of_image.lower() in list_of_extension:
        pass
    else:
        raise ValidationError("Only 'jpg','jpeg','png' are allowed")

def vedio_validation(vedio):
    list_of_extension = ['mp4','avi','mkv']
    extension_of_vedio = str(vedio).split('.')[-1]
    if extension_of_vedio.lower() in list_of_extension:
        pass
    else:
        raise ValidationError("Only 'mp4' and 'avi' are allowed")