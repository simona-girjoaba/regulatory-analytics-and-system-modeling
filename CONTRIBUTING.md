# Richtlinien für Akademische Git-Commits (Data Science & Governance)

Dieses Dokument definiert die verbindlichen Standards für Commit-Nachrichten in diesem Repository. Ziel ist die Wahrung der akademischen Wissenschaftssprache (C1/C2) und die transparente Dokumentation interdisziplinärer Systemmodellierung.

## 1. Grundregeln der Syntax
1. **Struktur:** `<Präfix>: <Akademische Beschreibung im Nominalstil>`
2. **Länge:** Maximal 72 Zeichen in der Kopfzeile.
3. **Stil:** Verwendung des Passivs oder des Nominalstils (Substantivierung von Verben). Vermeidung von Füllwörtern (z.B. *ein bisschen*, *eigentlich*, *gemacht*).
4. **Präzision:** Spezifische Nennung der mathematischen Methode, des Datensatzes oder der regulatorischen Norm.

## 2. Standardisierte Präfixe und Anwendungsfälle

| Präfix | Fokus-Bereich | Erlaubte Anwendung | Unzulässige Anwendung |
| :--- | :--- | :--- | :--- |
| **feat:** | Code / Mathematik | Implementierung neuer Algorithmen, Modelle oder Datenstrukturen. | "feat: Code geändert" |
| **fix:** | Code / Mathematik | Behebung von Laufzeitfehlern, logischen Fehlern in Beweisen oder Daten-Pipelines. | "fix: Bug entfernt" |
| **docs:** | Governance / Sprache | Ergänzung von Markdown-Dateien, Ethik-Richtlinien oder Kommentaren. | "docs: Text geschrieben" |
| **refactor:**| Systemarchitektur | Umstrukturierung von Code ohne Änderung der Endfunktion (z.B. Effizienzsteigerung). | "refactor: aufgeräumt" |
| **chore:** | Administration | Aktualisierung von Abhängigkeiten (z.B. `requirements.txt`), Umgebungsvariablen. | "chore: Sachen geupdatet" |

## 3. Akademische Vokabel-Matrix (Vorlagen)

Nutzen Sie diese Verben/Nomen für die Konstruktion der Nachricht:

* **Statt "bauen/machen":** Implementierung, Konstruktion, Entwicklung, Modellierung.
* **Statt "ändern/besser machen":** Optimierung, Kalibrierung, Refaktorierung, Restrukturierung.
* **Statt "Fehler finden":** Identifikation, Behebung, Korrektur, Validierung.
* **Statt "prüfen":** Evaluation, Analyse, Auditierung (im Governance-Kontext).

## 4. Konkrete Beispiele für Topic-Locked Sprints

**Schlecht (Umgangssprachlich):**
* `feat: Ich habe die Migrationstabelle bereinigt.`
* `docs: Ein paar Notizen zum AI Act hinzugefügt.`
* `fix: Mathe-Formel für Vektoren korrigiert.`

**Korrekt (Akademischer Nominalstil):**
* `feat: Durchführung der Normalisierung und Bereinigung des Destatis-Migrationsdatensatzes`
* `docs: Dokumentation der Risikoklassifizierung gemäß Artikel 6 des EU AI Acts`
* `fix: Korrektur der Matrix-Dimensionen innerhalb der Vektor-Multiplikation`
* `refactor: Optimierung der Speichereffizienz bei der Verarbeitung großer Pandas-DataFrames`