from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def importar_pedidos(request):
    folder='tmp/'
    if request.method == 'POST':
        myfile = request.FILES['file']
        fs = FileSystemStorage(location=folder) #defaults to   MEDIA_ROOT  
        filename = fs.save(myfile.name, myfile)
        file_url = fs.url(filename)
    else:
      pass
      
    return render(request, 'pedidos/importar.html')
