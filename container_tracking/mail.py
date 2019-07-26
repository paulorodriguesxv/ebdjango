from django.core.mail import send_mail


def send_feedback_email(feedback):
    send_mail(
        f"Nós recebemos um feedback",
        ("Olá. \n"
         "Este é um e-mail automático gerado pela nossa aplicação Django. \n"
         "Isso significa que alguém enviou um feedback. \n"
         "--------------------------------------------------------\n"
         f"Dados: {feedback} \n"), "codekraftofficial@gmail.com",
        ["codekraftofficial@gmail.com"], False)
