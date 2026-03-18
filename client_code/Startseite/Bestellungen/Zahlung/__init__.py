from ._anvil_designer import ZahlungTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Zahlung(ZahlungTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_startseite_von_zahlung", "click")
  def button_startseite_von_zahlung_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Startseite", row_dict=self.item)

  @handle("button_bestellungen_von_zahlung", "click")
  def button_bestellungen_von_zahlung_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Startseite.Bestellungen", row_dict=self.item)
