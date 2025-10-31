from flask import current_app, render_template
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email_sendgrid(to_list, subject, html_content_body):
    """Envia e-mail com SendGrid."""
    
    # Carrega as configs do app atual
    config = current_app.config
    full_subject = f"{config['FLASKY_MAIL_SUBJECT_PREFIX']} {subject}"

    # Prepara o formato do destinatário (string ou tuple)
    if len(to_list) == 1:
        destinos = to_list[0]
    else:
        destinos = tuple(to_list)

    message = Mail(
        from_email=config['API_FROM'],
        to_emails=destinos,
        subject=full_subject,
        html_content=html_content_body
    )
    try:
        sg = SendGridAPIClient(config['SENDGRID_API_KEY'])
        response = sg.send(message)
        print(f"E-mail enviado para {to_list}, status: {response.status_code}")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
