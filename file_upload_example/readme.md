## File/Image Upload Example App
This is a django app which is the demo of the uploading image through REST API.

We needs to create,
- Model (`models.py` file contains Models)
  - Model is used to store the image.
  - FileField or ImageField can be used as field in dinago Model.
- Serializer (`serializers.py` fie contains Serializers)
  - used restframework ModelSerializer
- Views (`views.py` file contains Views)
  - used restframework APIView
- urls (`urls.py` file inside the app contains urls)

**Note:** *The files uploaded to FileField or ImageField are not saved in the database but in the file system of your server. 
In the database it's the fields are represented by a VARCHAR containing the reference to the file.*

It's mandatory to MEDIA_URL and MEDIA_ROOT in django project settings file.

#### Parser is must inside the View Class.
- The responsibility of Parsers is to parse the data that is sent by request methods GET, POST and PUT, etc.
- Default parser used in django REST is 'JSONParser'. It only parses the data JSON data[numbers, string, date]. It ignores the data like FILES.
- In order to parse the FILES we need to use parsers like "MultiPartParser" or "FormParser".

When we use property `request.data` then parser will parse the data.

#### Details Reading
- [Django REST Framework Image File Upload Tutorial](https://www.techiediaries.com/django-rest-image-file-upload-tutorial/)
