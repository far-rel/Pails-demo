from Pails.core.controllers import BaseController

class UserController(BaseController):
    
    def show(self):
        if self.session['count']:
            self.session['count'] = int(self.session['count']) + 1
        else:
            self.session['count'] = 1
        self.render(params = { 'echo' : str(self._params) + ' Cookie: ' + str(self.cookies['user'] + 'Count: ' + str(self.session['count'] ))})

    def new(self):
        self.redirect(self.path.account())

    def edit(self):
        self.cookies['user'] = 'New User'
        self.redirect(self.path.account())
