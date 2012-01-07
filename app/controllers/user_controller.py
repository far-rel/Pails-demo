from Pails.core.controllers import BaseController

class UserController(BaseController):
    
    def show(self):
        self.render(params = { 'echo' : str(self._params) + ' Cookie: ' + str(self.cookies['user'] )})

    def new(self):
        self.redirect(self.path.account())

    def edit(self):
        self.cookies['user'] = 'New User'
        self.redirect(self.path.account())
