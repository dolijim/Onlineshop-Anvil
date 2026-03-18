from ._anvil_designer import VerkaufsuebersichtTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

SCHÖNE_FARBEN = [
  "#4C9BE8",  # Blau
  "#F4845F",  # Orange
  "#56C596",  # Grün
  "#F7C948",  # Gelb
  "#A078D4",  # Lila
  "#E8607A",  # Pink
  "#4ECDC4",  # Türkis
  "#F9A03F",  # Amber
  "#7BC67E",  # Hellgrün
  "#5B8DEF",  # Kornblume
]

def get_farbe(produkt, farben_map):
  if produkt not in farben_map:
    index = len(farben_map) % len(SCHÖNE_FARBEN)
    farben_map[produkt] = SCHÖNE_FARBEN[index]
  return farben_map[produkt]

class Verkaufsuebersicht(VerkaufsuebersichtTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.label_1.text = "Die meisten Verkäufe"

    farben_map = {}

    produkte, anzahlen = anvil.server.call('get_verkäufe_nach_kategorie')
    produkte2, umsaetze = anvil.server.call('get_umsatz_nach_kategorie')

    farben1 = [get_farbe(p, farben_map) for p in produkte]
    farben2 = [get_farbe(p, farben_map) for p in produkte2]

    # Diagramm 1 (links) – Stückzahl pro Produkt
    self.plot_1.data = [{
      "labels": produkte,
      "values": anzahlen,
      "type": "pie",
      "textinfo": "label",
      "marker": {"colors": farben1}
    }]
    self.plot_1.layout = {
      "title": {
        "text": "nach Stück",
        "x": 0.5,
        "xanchor": "center",
        "font": {"size": 18}
      }
    }

    # Diagramm 2 (rechts) – Umsatz pro Produkt
    self.plot_2.data = [{
      "labels": produkte2,
      "values": umsaetze,
      "type": "pie",
      "textinfo": "label",
      "marker": {"colors": farben2}
    }]
    self.plot_2.layout = {
      "title": {
        "text": "nach Umsatz in €",
        "x": 0.5,
        "xanchor": "center",
        "font": {"size": 18}
      }
    }

  @handle("button_startseite_von_verkaufsuebersicht", "click")
  def button_startseite_von_verkaufsuebersicht_click(self, **event_args):
    open_form("Startseite", row_dict=self.item)