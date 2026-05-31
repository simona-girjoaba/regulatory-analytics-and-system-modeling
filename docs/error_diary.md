# 🐛 Zentrales Fehlertagebuch | Error & Debugging Ledger

Dieses Dokument protokolliert systematisch identifizierte Laufzeitfehler, logische Defekte in den Daten-Pipelines und deren strukturelle Behebung.

---

## 🔴 KeyError: ('imdb_score', 'gross')

* **Datum:** 2026-05-27
* **Modul / Kontext:** Woche 1 – Data Analysis mit Python (Homework 4 – Summarize Movie & Ratings Data)
* **Fehlertyp:** `KeyError`

### ❌ Inkorrekte Implementierung
```python
score_gross_description = df['imdb_score', 'gross'].describe()
🐞 Aufgerufene Fehlermeldung

KeyError: ('imdb_score', 'gross')

🔍 Ursachenanalyse (Root Cause)
Die Verwendung eines Kommas innerhalb der einfachen eckigen Klammern df[...] initialisiert ein Python-Tuple. Pandas interpretiert dieses Tuple als ein einzelnes, spezifisches Spaltenlabel (üblich bei Multi-Index-Strukturen). Da keine Spalte mit dieser exakten Tuple-Bezeichnung im DataFrame existiert, bricht die Ausführung mit einem KeyError ab.

✅ Korrigierte Implementierung
Python
score_gross_description = df[['imdb_score', 'gross']].describe()
💡 Funktionsweise der Behebung
Die Implementierung von doppelten eckigen Klammern [[...]] übergibt eine explizite Python-Liste von Spaltennamen. Dies veranlasst die Pandas-Engine zur korrekten Selektion mehrerer Spalten und zur korrekten Rückgabe eines mehrdimensionalen DataFrame-Objekts.

🛡️ Präventivmaßnahmen
Bei der Selektion einer multidisziplinären Spaltenmatrix ist konsequent die Listensyntax [['col1', 'col2']] anzuwenden.

Das Auftreten eines Tuples innerhalb einer Pandas-Fehlermeldung signalisiert syntaktische Fehler bei der Definition der eckigen Klammern und erfordert eine sofortige Überprüfung der Indexierung.

📚 Referenzen
Pandas Indexing Documentation

🔴 AssertionError: Pivot Table Shape Mismatch
Datum: 2026-05-27

Modul / Kontext: Woche 1 – Data Analysis mit Python (Homework 4 – Summarize Movie & Ratings Data)

Fehlertyp: AssertionError (Struktureller Konflikt der DataFrame-Dimensionen)

❌ Inkorrekte Implementierung (Iterative Fehlversuche)
Python
# Iteration 1 – Fehlende Indexvariable 'country', Aggregationsfunktion als String definiert
pivot_agg = df.pivot_table(index='director_name', values='imdb_score', aggfunc='median')

# Iteration 2 – Verwendung einer inkorrekten Indexvariable (director_id)
pivot_agg = df.pivot_table(index='director_id', values='imdb_score', aggfunc='median')

# Iteration 3 – Korrekte Zeilenhierarchie, jedoch unzulässige String-Formatierung der aggfunc
pivot_agg = df.pivot_table(index=['country', 'director_name'], values='imdb_score', aggfunc='median')
🐞 Aufgerufene Fehlermeldung
AssertionError: DataFrame shape mismatch
[left]:  (Dimension variabel, z. B. 117, 1)
[right]: (125, 1) (Hierarchische Multi-Index-Struktur)
🔍 Ursachenanalyse (Root Cause)
Die automatisierungstechnische Validierungseinheit (Test-Suite) setzt eine Pivot-Tabelle voraus, die sowohl eine hierarchische Zeilenstruktur (country -> director_name) als auch einen Multi-Level-Spalten-Header aufweist.

Wird das Argument aggfunc als einfacher String übergeben ('median'), resultiert daraus eine flache Spaltenbezeichnung ('imdb_score').

Wird aggfunc stattdessen als Liste übergeben (['median']), generiert Pandas zwingend einen hierarchischen Tuple-Spaltennamen: ('imdb_score', 'median').

Da das vordefinierte Lösungsobjekt sol.pivot_agg diese zweistufige Spaltenstruktur besitzt, scheitert die Dimensionsprüfung (AssertionError) trotz inhaltlich korrekter Datenwerte.

✅ Korrigierte Implementierung
Python
pivot_agg = df.pivot_table(
    index=['country', 'director_name'],
    values='imdb_score',
    aggfunc=['median']       # Die Listensyntax erzwingt die Erstellung des Multi-Level-Spalten-Headers
)
💡 Funktionsweise der Behebung
Die Zuweisung index=['country', 'director_name'] generiert die geforderte hierarchische Zeilenstruktur im Index.

Die Übergabe von aggfunc=['median'] stellt sicher, dass der Spalten-Header als Tuple aufgebaut wird, wodurch eine exakte strukturelle Identität mit dem Validierungsobjekt hergestellt wird.

pivot_table akzeptiert hierbei Strings, Callables oder Listen; die Test-Suite erzwingt den Listentyp.

🛡️ Präventivmaßnahmen
Vor der Code-Finalisierung ist die Spaltenstruktur des Zielobjekts mittels des Attributs columns (z. B. sol.pivot_agg.columns) mathematisch zu analysieren.

Beim Erkennen eines MultiIndex innerhalb der Ziel-Headerschnittstelle müssen die Aggregationsparameter standardmäßig als Liste übergeben werden, um den Funktionsnamen in der Ausgabe stabil zu kapseln.

📚 Referenzen
Pandas pivot_table API Documentation