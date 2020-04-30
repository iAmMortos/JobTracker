import ui

class MainView(ui.View):
  def __init__(self):
    pass
  
  def did_load(self):
    self.name = 'Job Tracker'
    
  @staticmethod
  def load_view():
    return ui.load_view()
