import sqlite3
import anvil.server
from anvil.files import data_files

@anvil.server.callable
def get_Bestellung():
  with sqlite3.connect(data_files['shop.db']) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute("""
        SELECT b.Bestell_ID, b.Datum, b.Kunden_ID, k.Name, k.Adresse FROM Bestellung b JOIN Kunde k ON k.Kunden_ID = b.Kunden_ID;
    """).fetchall()
    return [dict(row) for row in result]

@anvil.server.callable
def get_Bestellung_Details(Bestell_ID:int):
  with sqlite3.connect(data_files['shop.db']) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(f"""
        SELECT z.Zahlungs_ID, b.Bestell_ID, p.Name, p.Preis, z.Gesamtbetrag FROM Bestellung b JOIN Zahlung z on z.Bestell_ID = b.Bestell_ID JOIN bestellung_produkt bp ON bp.Bestell_ID = b.Bestell_ID JOIN Produkt p ON p.Produkt_ID = bp.Produkt_ID JOIN Kunde k ON k.Kunden_ID = b.Kunden_ID WHERE b.Bestell_ID = {Bestell_ID};
    """).fetchall()
    return [dict(row) for row in result]


@anvil.server.callable
def get_Produkt():
  with sqlite3.connect(data_files['shop.db']) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute("""
        SELECT Produkt_ID, p.Name, Kategorie, Preis, l.Name AS Name_Lieferant, l.Lieferanten_ID FROM Produkt p JOIN Lieferant l ON p.Lieferanten_ID = l.Lieferanten_ID;
    """).fetchall()
    return [dict(row) for row in result]


@anvil.server.callable
def get_Kunden():
  with sqlite3.connect(data_files['shop.db']) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute("""
        SELECT Kunden_ID, Name, Adresse FROM Kunde
    """).fetchall()
    return [dict(row) for row in result]
