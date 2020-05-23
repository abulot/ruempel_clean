from flask import render_template
from flask_mail import Mail

from app.models.contact_request import ContactRequest
from app.models.mailer import Mailer
from flask import current_app as app


class ApplicationController:

    def __init__(self, request):
        self.params = request.args
        self.xdata = request.form
        self.pages_set = ['home', 'entruempelung', 'haushaltsaufloesung', 'betriebsaufloesung', 'entkernung', 'about', 'test', 'contact', 'contact_confirm']
        self.layout = "base"
        self.mail = Mail(app)

    def home(self):
        return render_template('pages/home.html', title='Home', layout=self.layout)

    def pages(self):
        page_slug = self.params['slug']
        if self.__is_valid_page(page_slug):
            return render_template('pages/' + page_slug + '.html', layout=self.layout)
        else:
            return self.not_found()

    def contact_send(self):
        contact_request = ContactRequest(self.xdata['email'], self.xdata['subject'], self.xdata['text'])
        if contact_request.is_valid():
            Mailer().send_contact_request(contact_request).send(self.mail)
            return render_template('pages/contact_confirm.html', layout=self.layout)
        else:
            return "Bad Request", 400

    def not_found(self):
        return render_template('base.html', title='Home', error='GIBBES NICH!!'), 404

    def __is_valid_page(self, slug):
        return slug in self.pages_set
