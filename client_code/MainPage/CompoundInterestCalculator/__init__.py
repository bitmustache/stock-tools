from ._anvil_designer import CompoundInterestCalculatorTemplate
from anvil import *


class CompoundInterestCalculator(CompoundInterestCalculatorTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def mainpage_link_click(self, **event_args):
    open_form('MainPage')