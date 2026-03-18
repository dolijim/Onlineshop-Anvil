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


  def __init__(self, **properties):
    self.init_components(**properties)

    self.plot_1.data = [{
      "labels": ["Äpfel", "Bananen", "Kirschen"],
      "values": [10, 20, 30],
      "type": "pie"
    }]

  def __init__(self, **properties):
    self.init_components(**properties)

    # 🔝 Großer Haupttitel (Label im Designer: label_1)
    self.label_1.text = "Die meisten Verkäufe"

    # 🥧 Diagramm 1 (links)
    self.plot_1.data = [{
      "labels": ["Äpfel", "Bananen", "Kirschen"],
      "values": [10, 20, 30],
      "type": "pie",
      "textinfo": "label+percent"
    }]

    self.plot_1.layout = {
      "title": {
        "text": "nach Stück",
        "x": 0.5,
        "xanchor": "center",
        "font": {"size": 18}
      }
    }

    # 🥧 Diagramm 2 (rechts)
    self.plot_2.data = [{
      "labels": ["Rot", "Blau", "Grün"],
      "values": [15, 25, 10],
      "type": "pie",
      "textinfo": "label+percent"
    }]

    self.plot_2.layout = {
      "title": {
        "text": "nach Umsatz in €",
        "x": 0.5,
        "xanchor": "center",
        "font": {"size": 18}
      }
    }