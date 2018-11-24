from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
import os.path

def importar_pedidos(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        try:
          salvar_arquivo(myfile)
          break
        except:
          print("Erro")
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
  wb = load_workbook(filename = 'tmp/' + nome_arquivo)
  sheet_ranges = wb['Plan1']
  limpar_planilha(sheet_ranges)

def limpar_planilha(planilha):
  linhas = []
  for index, linha in enumerate(planilha):
    if index > 0:
      linhas.append(linha)

  ler_colunas(linhas)

def ler_colunas(linhas):
  produtos = []
  for linha in linhas:
    produto = {}
    produto['codigo'] = linha[0].value
    produto['descricao'] = linha[1].value
    produto['preco'] = linha[2].value
    produto['pontos'] = linha[3].value
    produto['quantidade'] = linha[4].value
    produto['total'] = linha[5].value
    produtos.append(produto)

  salvar_pedidos(produtos)

def salvar_pedidos(produtos):
  pass