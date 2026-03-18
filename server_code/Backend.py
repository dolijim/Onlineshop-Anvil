import sqlite3
import anvil.server
from anvil.files import data_files

@anvil.server.callable
def get_Bestellung():
  with sqlite3.connect(data_files['shop.db']) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute("""
        SELECT Bestell_ID, Datum, Kunden_ID FROM Bestellung
    """).fetchall()
    return [dict(row) for row in result]
