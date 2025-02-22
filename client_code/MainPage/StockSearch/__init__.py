from ._anvil_designer import StockSearchTemplate
from anvil import *
import anvil.server

class StockSearch(StockSearchTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings
        self.init_components(**properties)
        self.stocksearch_card2.visible = False
        self.stockgraph_card.visible = False

    def mainpage_link_click(self, **event_args):
        open_form('MainPage')

    def compoundinterestcalc_link_click(self, **event_args):
        open_form('MainPage.CompoundInterestCalculator')

    def stocksearch_link_click(self, **event_args):
        open_form('MainPage.StockSearch')

    def stocksearch_button_click(self, **event_args):
        """Runs when the search button is clicked"""
        print("Search button clicked!")  # Debugging output

        # Get the stock symbol from the text box
        symbol = self.stocksearch_box.text.strip()  # Strip spaces
        print(f"Symbol entered: {symbol}")  # Debugging output

        if symbol:
            self.get_stock_data(symbol)
            self.stocksearch_card2.visible = True
            self.stockgraph_card.visible = True
        else:
            self.stocksearch_label.text = "Please enter a stock symbol"

    def get_stock_data(self, symbol):
        """Calls the server function to fetch stock price"""
        try:
            print("Calling Uplink function...")  # Debugging output
            stock_data = anvil.server.call('get_stock_price', symbol)

            print(f"Received response: {stock_data}")  # Debugging output
            
            if 'price' in stock_data:
                self.stocksearch_label.text = f"Price of {symbol}: ${stock_data['price']}"
            else:
                self.stocksearch_label.text = f"Error: {stock_data['error']}"

        except Exception as e:
            self.stocksearch_label.text = f"Error: {str(e)}"
            print(f"Exception occurred: {e}")  # Debugging output

def stocksearch_button_click(self, **event_args):
    """Fetch stock graph when search is pressed"""
    symbol = self.stocksearch_box.text.strip().upper()  # Get user input

    if not symbol:
        self.stocksearch_label.text = "Please enter a stock symbol!"
        return

    self.stocksearch_label.text = "Fetching data..."
    
    try:
        img_base64 = anvil.server.call('get_stock_graph', symbol)

        if isinstance(img_base64, dict) and 'error' in img_base64:
            self.stocksearch_label.text = f"Error: {img_base64['error']}"
        else:
            # Convert base64 to image and display
            self.stocksearch_image.source = f"data:image/png;base64,{img_base64}"
            self.stocksearch_label.text = f"Stock Price Progression for {symbol}"

    except Exception as e:
        self.stocksearch_label.text = f"Error: {str(e)}"