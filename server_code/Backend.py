import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

import anvil.server
import sqlite3

@anvil.server.callable
def get_bestellungen():
  conn = sqlite3.connect("shop.db")
  cursor = conn.cursor()

  cursor.execute("""
        SELECT bestell_id, kunden_id, datum, zahlung
        FROM bestellungen
    """)

  rows = cursor.fetchall()

  conn.close()

  return rows