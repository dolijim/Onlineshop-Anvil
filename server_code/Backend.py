import sqlite3
import anvil.server

# --- Generische Abfrage ---
@anvil.server.callable
def query_database(query: str):
  # Pfad zur Data File
  db_path = "shop.db"  # direkt Name der Data File
  with sqlite3.connect(db_path) as conn:
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return result


@anvil.server.callable
def query_database_dict(query: str):
  db_path = "shop.db"
  with sqlite3.connect(db_path) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]


@anvil.server.callable
def meist_verkaufte_produkte(limit=5):
  db_path = "shop.db"
  with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    cursor.execute(f"""
            SELECT p.Produktname, SUM(z.Gesamtpreis) AS total_umsatz
            FROM Bestellung b
            JOIN Produkt p ON b.Produkt_id = p.Produkt_ID
            JOIN Zahlung z ON b.Bestell_ID = z.Bestell_ID
            GROUP BY p.Name
            ORDER BY total_umsatz DESC
            LIMIT {limit};
        """)
    daten = cursor.fetchall()
  return daten