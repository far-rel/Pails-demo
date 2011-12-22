from Pails.core.controllers import BaseController

class UserController(BaseController):
    
    def show(self):
        self._set_render_parameters({ 'echo' : str(self._params) })
