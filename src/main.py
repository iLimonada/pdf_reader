import os
from pdf_utils import escanear_diretorio, gerar_relatorio_excel
from email_utils import enviar_gmail
from config import EMAIL_RECIPIENT

def validar_diretorio():
    """Pede para o usuário digitar um caminho válido contendo os arquivos PDFs"""
    while True:
        folder_path = input("Digite o caminho da pasta onde estão os arquivos PDFs: ").strip()

        if os.path.isdir(folder_path):
            return os.path.normpath(folder_path)
        else:
            print("Caminho inválido. Tente novamente")


def main():
    user_folder = validar_diretorio()
    print(f"Pasta selecionada: {user_folder}")

    pdf_list = escanear_diretorio(user_folder)

    output_excel = "relatorio_pdf.xlsx"

    gerar_relatorio_excel(pdf_list, output_excel)

    enviar_gmail(
        recipient=EMAIL_RECIPIENT,
        subject="PDF Report",
        body="Anexo do Excel com os arquivos PDFs e suas paginas.",
        attachment=output_excel
    )

if __name__ == "__main__":
    main()