from app.controller.application_controller import ApplicationController


class Router:
    @staticmethod
    def process(request):
        if request.path == '/':
            return ApplicationController(request).home()

        elif request.path == '/pages':
            return ApplicationController(request).pages()

        elif request.path == '/contact_send':
            return ApplicationController(request).contact_send()

        else:
            return ApplicationController(request).not_found()
