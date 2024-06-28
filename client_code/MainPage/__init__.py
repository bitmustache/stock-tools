from ._anvil_designer import MainPageTemplate
from anvil import *
import anvil.server
from ..AdSense import AdSense


class MainPage(MainPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    # Initialize an instance of AdSense form
    self.adsense_form = AdSense()

    # Add the AdSense form to the ad_container component
    self.ad_container.clear()
    self.ad_container.add_component(self.adsense_form)

    # Call the display_ad method to show the ad
    self.adsense_form.display_ad()
    
  def mainpage_link_click(self, **event_args):
    open_form('MainPage')
  
  def compoundinterestcalc_link_click(self, **event_args):
    open_form('MainPage.CompoundInterestCalculator')


  



