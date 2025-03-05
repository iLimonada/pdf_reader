import fitz
import pandas as pd
import os

def escanear_diretorio(base_path):
    """Verifica a existência do diretório digitado pelo usuário"""
    pdf_files = []


    for root, _, files in os.walk(base_path):
            for file in files:
                if file.lower().endswith(".pdf"):
                    full_path = os.path.join(root, file)
                    pdf_files.append(full_path)
    
    return pdf_files

def contar_paginas_pdf(pdf_path):
    """Navega entre os arquivos contando as páginas dos arquivos PDFs"""
    pdf_path = os.path.normpath(pdf_path)

    if not os.path.exists(pdf_path):
        print(f"Arquivo não encontrado: {pdf_path}")
        return None
    
    try:
        with fitz.open(pdf_path) as pdf:
            return pdf.page_count
    except Exception as ex:
        print(f"Erro ao processar {pdf_path}: {ex}")
        return 


def gerar_relatorio_excel(pdf_files,  output_excel):
    """Gera um relatório em Excel, dado os dados nome do arquivo e o número de páginas"""
    if not pdf_files:
        print("Nao foi encontrado nenhum arquivo.")
        return None

    pdf_data = []

    for pdf_path in pdf_files:
        pdf_name = os.path.basename(pdf_path)
        pages_number = contar_paginas_pdf(pdf_path)

        if pages_number is None:
            pdf_data.append([pdf_name, 'Erro ao contar paginas pdf'])
        else:
            pdf_data.append([pdf_name, pages_number])


    excel_data_frame = pd.DataFrame(pdf_data, columns=["Nome do arquivo", "Número de páginas"])

    excel_data_frame.to_excel(output_excel, index=False)
    print(f"Sucesso arquivo salvo: {output_excel}")
