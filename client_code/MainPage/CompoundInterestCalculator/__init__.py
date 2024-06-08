from ._anvil_designer import CompoundInterestCalculatorTemplate
from anvil import *


class CompoundInterestCalculator(CompoundInterestCalculatorTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def mainpage_link_click(self, **event_args):
    open_form('MainPage')

  def compoundinterestcalc_link_click(self, **event_args):
    open_form('MainPage.CompoundInterestCalculator')

  def calculate_compoundinterest_button_click(self, **event_args):
    # get the user inputs
    principal = float(self.principal_textbox.text)
    interest_rate = float(self.interestrate_textbox.text)
    years = float(self.years_textbox.text)
    times_compounded = float(self.timescompounded_textbox.text)

    # calculate the future value based on inputs
    future_value = self.compound_interest(principal, interest_rate, years, times_compounded)

    self.result_label.text = f"The future value of your investment is: ${future_value: .2f}"
    
  def compound_interest(self, principal, interest_rate, years, times_compounded):
    amount = principal * (1 )
