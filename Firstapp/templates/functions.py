def handle_upload_file(f):
    with open("Firstapp/static/upload/"+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)