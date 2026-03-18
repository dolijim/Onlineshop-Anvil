from ._anvil_designer import ProdukteTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Produkte(ProdukteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_startseite_von_produkte", "click")
  def button_startseite_von_produkte_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Startseite", row_dict=self.item)
