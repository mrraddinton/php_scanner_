import requests
import smtplib

# Site para checagem
ALVO = "http://test.com"

# Detalhes do E-mail
SMTP_SERVIDOR = "smtp.test.com"
SMTP_PORTA = 587
REMETENTE_EMAIL = "noreply@test.com"
DESTINATARIO_EMAIL = "admin@test.com"
EMAIL_NOMEDOUSUARIO = "noreply@test.com"
EMAIL_SENHA = "your_email_password"

# Envie uma solicitação GET para o site
response = requests.get(ALVO)

# Pega a versão do cabeçalho
php_version = response.headers.get("X-Powered-By")

# Ira verificar se a versão do PHP é vulnerável
if "PHP/5.6" in php_version:
    print(f"[!] {TARGET} está usando uma versão PHP desatualizada e vulnerável: {php_version}")
    # Envia a notificação por e-mail
    with smtplib.SMTP(SMTP_SERVIDOR, SMTP_PORTA) as server:
        server.starttls()
        server.login(EMAIL_NOMEDOUSUARIO, EMAIL_SENHA)
        subject: str = f"[ALERTA] Versão PHP desatualizada em {ALVO}"
        body = f"O site {ALVO} está usando uma versão PHP desatualizada e vulnerável: {php_version}.Por favor,atualize."
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(REMETENTE_EMAIL, DESTINATARIO_EMAIL_EMAIL, msg)
    print("[+] Notificação Eviada por e-mail")
else:
    print(f"[+] {ALVO}  está usando uma versão PHP segura,Parabéns! .")
