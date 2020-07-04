from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm


def upload_file(request):
    # import ipdb; ipdb.set_trace()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        form.content = handle_uploaded_file(request.FILES['content'])
        if form.is_valid():
            form.save()
            return render(request, 'preview.html', {'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    # with open('file.txt', 'wb+') as destination:
    #     for chunk in f.chunks():
    #         destination.write(chunk)
    return f.read()