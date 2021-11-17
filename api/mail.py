from flask_mail import Mail

mail :Mail = Mail()

def init_mail(app):
    return mail.init_app(app)