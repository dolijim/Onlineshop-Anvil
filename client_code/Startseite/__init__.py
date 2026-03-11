from ._anvil_designer import StartseiteTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_produkte", "click")
  def button_produkte_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Startseite.Produkte", row_dict=self.item)

  @handle("button_bestellungen", "click")
  def button_bestellungen_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Startseite.Bestellungen", row_dict=self.item)

  @handle("button_kunden", "click")
  def button_kunden_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Startseite.Kunden", row_dict=self.item)
