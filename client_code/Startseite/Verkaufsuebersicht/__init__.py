from ._anvil_designer import VerkaufsuebersichtTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Verkaufsuebersicht(VerkaufsuebersichtTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_startseite_von_verkaufsuebersicht", "click")
  def button_startseite_von_verkaufsuebersicht_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Startseite", row_dict=self.item)
