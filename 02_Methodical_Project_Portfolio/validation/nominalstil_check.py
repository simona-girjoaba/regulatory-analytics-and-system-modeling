#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zentrales automatisiertes Prüfskript zur Einhaltung des formellen Nominalstils.
Prüfungsstandard: C2-Sprachtraining / Regulatorische Revisionssicherheit.
"""

import os
import sys

def check_nominalstil(file_path, max_words=150):
    if not os.path.exists(file_path):
        print(f"[-] Validierungsfehler: Datei '{file_path}' existiert nicht.")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Berechnung der Metriken
    words = text.split()
    word_count = len(words)
    text_lower = text.lower()

    print(f"[+] Analyse der Datei: {file_path}")
    print(f"[+] Registrierte Wortanzahl: {word_count} / {max_words}")

    # 1. Hartes Audit des Wortlimits
    if word_count > max_words:
        print(f"[❌] Kritischer Fehler: Wortlimit überschritten ({word_count}/{max_words} Wörter).")
        return False

    # 2. Audit verbotener verbaler Phrasen (Grob-Filter zur Qualitätssicherung)
    forbidden_phrases = [
        "wir müssen prüfen", 
        "wir bitten sie", 
        "schulen damit", 
        "wir haben geprüft"
    ]
    
    violations_detected = False
    for phrase in forbidden_phrases:
        if phrase in text_lower:
            print(f"[❌] Stilistischer Fehler: Unzulässige verbale Phrase '{phrase}' entdeckt.")
            violations_detected = True

    if violations_detected:
        print("[❌] Audit fehlgeschlagen: Der Nominalstil wurde verletzt.")
        return False

    print("[✅] Qualitätssicherung erfolgreich: Formeller Nominalstil formal eingehalten.")
    return True

if __name__ == "__main__":
    # Standardpfad für das Montags-Artefakt Woche 1
    target_file = "02_Methodical_Project_Portfolio/Woche_1/01_email_ki_kompetenz.md"
    
    # Ausführung des Audits
    success = check_nominalstil(target_file, max_words=150)
    
    # Rückgabe des System-Exit-Codes für CI/CD-Pipelines oder Git-Hooks
    if not success:
        sys.exit(1)
    sys.exit(0)