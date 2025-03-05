# PDF Scanner and Email Report

## Este projeto escaneia uma pasta em busca de arquivos PDF, conta o número de páginas de cada um, gera um relatório em Excel e o envia por e-mail.

### Como Usar

1. Instalar Dependências

Certifique-se de que tem o Python instalado e execute:
 - pip install -r requirements.txt

2. Modificar o Arquivo .env
 - EMAIL_SENDER=seu_email@gmail.com
 - EMAIL_PASSWORD=sua_senha_de_app
 - EMAIL_RECIPIENT=email_destino@gmail.com

3. Executar o Programa
 - No terminal, dentro da pasta src/, execute:
   python main.py

Digite o caminho da pasta com os arquivos PDF e aguarde o relatório ser gerado e enviado.

### Funcionalidades
 - Escaneia uma pasta em busca de arquivos PDF
 - Conta o número de páginas de cada PDF
 - Gera um relatório em Excel
 - Envia o relatório por e-mail automaticamente

### Tecnologias Utilizadas
 - Python
 - PyMuPDF (fitz)
 - Pandas
 - smtplib (para envio de e-mail)
 - dotenv (para variáveis de ambiente)

### Licença

Este projeto é de uso pessoal e pode ser modificado conforme necessário.
