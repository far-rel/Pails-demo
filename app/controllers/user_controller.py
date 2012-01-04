from Pails.core.controllers import BaseController

class UserController(BaseController):
    
    def show(self):
        self.render(params = { 'echo' : str(self._params) })

    def new(self):
        self.redirect(self.path.account())
