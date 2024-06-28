from ._anvil_designer import AdSenseTemplate
from anvil import *
import anvil.server


class AdSense(AdSenseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def display_ad(self):
    ad_code = '''
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4787864388418651"
    crossorigin="anonymous"></script>
    <!-- Horizontal Responsive -->
    <ins class="adsbygoogle"
        style="display:block"
        data-ad-client="ca-pub-4787864388418651"
        data-ad-slot="1877386277"
        data-ad-format="auto"
        data-full-width-responsive="true"></ins>
    <script>
        (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
    '''
