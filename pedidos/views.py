from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from openpyxl import load_workbook
import os.path

def importar_pedidos(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        salvar_arquivo(myfile)
    else:
      pass
      
    return render(request, 'pedidos/importar.html')

def salvar_arquivo(arquivo):
  folder='tmp/'
  fs = FileSystemStorage(location=folder)
  filename = fs.save(arquivo.name, arquivo)
  file_url = fs.url(filename)
  ler_arquivo(file_url)

def ler_arquivo(nome_arquivo):
  # print(os.path.dirname())
  wb = load_workbook(filename = 'tmp/' + nome_arquivo)
  sheets = wb.sheetnames
  print(sheets)