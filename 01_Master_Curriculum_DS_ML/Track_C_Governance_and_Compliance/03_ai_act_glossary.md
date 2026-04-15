# Strategisches Glossar: EU KI-Verordnung (AI Act) für AML & Privacy Engineering
**Fokus:** AML Data Science & Privacy Engineering  
**Erstellungsdatum:** 15. April 2026  
**Datei:** `03_ai_act_glossary.md`

---

## 1. Kontextuelle Einleitung: Die Konvergenz von KI-Regulierung und Finanz-Compliance

Die europäische Finanzmarktregulierung erreicht durch das Ineinandergreifen der **EU KI-Verordnung (Regulation 2024/1689)** und der neuen Anti-Geldwäsche-Architektur (**GwG/AuA 2.0** und die kommende **AMLR**) eine neue Reifestufe. Wir beobachten eine kritische regulatorische Dynamik: Die Grenze zwischen **ESG-Reporting** und **AML-Monitoring** verschwimmt, da Umweltverbrechen (z. B. illegale Abholzung) nun explizit als Vortaten der Geldwäsche eingestuft werden.

- **Hochrisiko-Klassifizierung:** Gemäß Anhang III der KI-Verordnung sind KI-Systeme für das AML-Screening (Transaktionsüberwachung) und Kredit-Scoring als **„Hochrisiko“** eingestuft. Dies erfordert eine lückenlose Governance von der Datenquelle bis zur Modellentscheidung.

- **Strategischer Imperativ XAI:** **Explainable AI (XAI)** ist kein „Nice-to-have“ mehr. Für die Begründung von Verdachtsmeldungen (SARs) gegenüber der FIU müssen Modelle sowohl **globale** (generische) als auch **lokale** (fallbezogene) Erklärbarkeit bieten.

- **Technische Konvergenz:** Die Implementierung erfordert eine Allianz aus **Legal Compliance** und **Privacy Engineering**, um Anforderungen wie manipulationssichere Audit-Logs und diskriminierungsfreie Algorithmen programmatisch zu validieren.

---

## 2. Strategisches Fachglossar (Tabellarische Übersicht)

| Begriff | Definition (gemäß AI Act / Source) | Operationaler Bezug: AML & Privacy Engineering |
| :--- | :--- | :--- |
| **1. KI-System** | Ein maschinengestütztes System, das aus Eingaben Ergebnisse (Vorhersagen, Empfehlungen) ableitet. | Rückgrat der automatisierten Transaktionsüberwachung und KYC-Prozesse zur Erkennung komplexer Geldwäsche-Typologien. |
| **2. Anbieter (Provider)** | Person/Stelle, die ein KI-System entwickelt und unter eigenem Namen in Verkehr bringt. | Software-Vendoren für AML-Lösungen; primär haftbar für die Einhaltung der technischen Standards ab Werk. |
| **3. Betreiber (Deployer)** | Stelle, die KI unter eigener Verantwortung nutzt (z. B. Finanzinstitut). | Institute haften für den ordnungsgemäßen Betrieb und die Integration in den Compliance-Workflow (z. B. Stop-and-Approve). |
| **4. Hochrisiko-KI** | KI-Systeme mit hohem Gefährdungspotenzial für Grundrechte (Anhang III). | Umfasst AML-Tools. Neu: Gemäß BaFin AuA 2.0 (2025) müssen Hochrisiko-Kunden nun jährlich (statt alle 2 Jahre) überprüft werden. |
| **5. Transparente KI** | Fokus auf Erklärbarkeit (XAI). Ermöglicht Interpretierbarkeit der Ergebnisse. | Einsatz von **Explainable Boosting Machines (EBM)**. Ermöglicht MLROs die präzise Begründung von SARs gegenüber Behörden. |
| **6. Konformitätsbewertung** | Prüfprozess vor Inverkehrbringen zur Validierung der Anforderungen. | Umfassende Prüfung auf algorithmischen Bias und Modell-Genauigkeit (Precision/Recall) durch Data Scientists. |
| **7. Notifizierte Stelle** | Unabhängige Konformitätsbewertungsstelle für externe Audits. | Externe Prüfinstanz, die die Einhaltung der KI-Verordnung für Finanz-KI-Modelle zertifiziert. |
| **8. Grundrechte-Folgenabschätzung** | Pflicht zur Bewertung der Auswirkungen auf natürliche Personen. | Schutz vor Diskriminierung beim Kredit-Scoring; Wahrung der finanziellen Inklusion und Privatsphäre. |
| **9. Technische Dokumentation** | Umfassende Nachweise (Art. 11/17) über Funktionsweise und QM-Systeme. | Art. 17 Pflicht: Versionierung von Code-basierten Policies; Nachweis der Datenherkunft (Data Lineage) und SHA-256 Integrität. |
| **10. Marktüberwachung** | Behördliche Aufsicht durch nationale Organe (z. B. BaFin). | Prüfung von Algorithmen. Post-SAR: Reduktion des Risiko-Einstufungszeitraums bei Geldwäsche-Verdacht auf 21 Tage. |

---

## 3. Technische Umsetzungsparameter für High-Risk-Systeme

Für AML-KI-Systeme definieren die **Artikel 12–15** des AI Acts spezifische Anforderungen, die direkt in die Systemarchitektur integriert werden müssen:

- **Protokollierung (Art. 12):**  
  Implementierung manipulationssicherer Audit-Logs mittels kryptografischer Verfahren wie **SHA-256 Hash-Chaining**. Jede Modellentscheidung muss unveränderbar verkettet werden, um die Revisionssicherheit gegenüber BaFin/FIU zu garantieren.

- **Menschliche Aufsicht (Art. 14):**  
  Einbau von programmatischen Sperrfunktionen. In der Code-Logik wird eine `approve_human()`-Blocking-Funktion implementiert, die sicherstellt, dass kritische Aktionen (z. B. Kontosperrung nach KI-Signal) erst nach expliziter Freigabe durch den MLRO ausgeführt werden.

- **Genauigkeit und Robustheit (Art. 15):**  
  Sicherung gegen **„Drift“**. Systeme müssen Anomalien im KYC-Profil erkennen, wenn sich Kundenverhalten schleichend ändert. Dies erfordert kontinuierliches Monitoring der Modell-Performance gegen reale Transaktionsdaten.

---

## 4. Strategische Compliance-Timeline

Finanzinstitute müssen ihre Roadmap an zwei parallelen regulatorischen Schienen ausrichten:

| Datum | Meilenstein | Fokus für AML-Beauftragte |
| :--- | :--- | :--- |
| **Februar 2025** | BaFin AuA 2.0 | Kompression der KYC-Review-Zyklen (Hochrisiko: Jährlich; Geringes Risiko: Max. 5 Jahre). |
| **August 2026** | AI Act (Vollanwendbarkeit) | Volle Konformitätspflicht für Hochrisiko-Systeme; Einrichtung von Art. 17 QM-Systemen. |
| **Juli 2027** | AMLR Single Rulebook | Übergang von statischer Compliance zu dynamischer, EU-weit harmonisierter Risikoevaluation. |

### „No-Regret“-Maßnahmen für AML-Beauftragte

- **Inventory & Technical Documentation:**  
  Abgleich bestehender Black-Box-Modelle mit den Dokumentationspflichten nach Art. 11 (Data Lineage & Versionierung).

- **XAI-Migration:**  
  Pilotierung von **EBM-Frameworks** zur Ablösung intransparenten Scorings, um SAR-Ablehnungen durch mangelnde Erklärbarkeit zu minimieren.

- **ESG-AML Integration:**  
  Entwicklung von **Heatmaps** zur Verknüpfung von Umweltdaten (z. B. Vegetationsverlust-Scores) mit Transaktionsmustern zur Identifikation neuer Vortaten.

---

## 5. Programmatische Validierung und Daten-Governance

Die technische Integrität wird durch moderne **Data Engineering** Praktiken und **Privacy-Technologien** gesichert:

- **Data Cleaning & Normalization via Python:**  
  Vor der Validierung ist eine Normalisierung unumgänglich. Mittels `re.sub(r'\s+', '', iban)` werden Nutzerfehler (Leerzeichen) bereinigt, bevor die IBAN-Prüfung gegen länderspezifische Regex-Patterns (z. B. `^DE\d{20}$` für Deutschland) erfolgt. Während LLMs gut für qualitative Analysen sind, bietet Python-Regex die notwendige 100%ige Präzision für quantitative KPI-Extraktionen.

- **Unstrukturierte Daten:**  
  Einsatz von Python zur Transformation unstrukturierter PDF-Berichte in strukturierte JSON-Formate. Dies ermöglicht das **„Heatmapping“** von ESG-Risiken (z. B. Arbeitsrechtsverletzungen in der Lieferkette) direkt gegen AML-Datenbanken.

- **Privacy Engineering (FHE):**  
  Um den Datenaustausch innerhalb von EU-Bankengruppen **GwG- und DSGVO-konform** zu gestalten, wird **Fully Homomorphic Encryption (FHE)** implementiert. Dies erlaubt die Analyse verschlüsselter Kundendaten ohne Entschlüsselung, was die Identifikation grenzüberschreitender Geldwäsche-Cluster ermöglicht.

---

  ## 6. English Terms and Explanations (International Reference)

For cross-border collaboration and English-language documentation, the following table provides the official English terminology alongside concise definitions aligned with the EU AI Act and AML/Privacy Engineering context.

| German Term | English Term | Explanation (English) |
| :--- | :--- | :--- |
| **KI-System** | **AI System** | A machine-based system designed to operate with varying levels of autonomy, generating outputs such as predictions, recommendations, or decisions that influence physical or virtual environments. In AML, this refers to automated transaction monitoring and customer risk scoring engines. |
| **Anbieter** | **Provider** | The natural or legal person, public authority, agency, or other body that develops an AI system or has it developed and places it on the market under its own name or trademark. In the AML context, this is typically the software vendor or the financial institution if it builds proprietary models. |
| **Betreiber** | **Deployer** | The natural or legal person, public authority, agency, or other body using an AI system under its own authority, excluding personal non‑professional use. In AML, this is the compliance department or the bank operating the transaction monitoring system. |
| **Hochrisiko-KI** | **High‑Risk AI System** | An AI system classified under Annex III of the AI Act due to its significant potential harm to health, safety, or fundamental rights. AML systems used for creditworthiness assessment or fraud detection fall into this category when they impact access to essential financial services. |
| **Transparente KI** | **Transparent AI** | The principle requiring that the operation of an AI system is understandable and explainable to deployers and affected individuals. In AML, this mandates Explainable AI (XAI) techniques to justify why a transaction was flagged as suspicious. |
| **Konformitätsbewertung** | **Conformity Assessment** | The systematic process to verify and demonstrate that an AI system meets all applicable requirements of the AI Act before being placed on the market or put into service. For AML models, this includes validation of data quality, bias testing, and performance metrics. |
| **Notifizierte Stelle** | **Notified Body** | An independent third‑party conformity assessment body designated by a national authority and notified to the European Commission to carry out conformity assessments for certain high‑risk AI systems. In the financial sector, such bodies may certify AML‑AI compliance. |
| **Grundrechte‑Folgenabschätzung** | **Fundamental Rights Impact Assessment (FRIA)** | A mandatory assessment for deployers of high‑risk AI systems that are public bodies or private entities providing public services, evaluating the potential impact on fundamental rights (e.g., non‑discrimination, data protection). For AML, this involves checking for algorithmic bias against protected groups. |
| **Technische Dokumentation** | **Technical Documentation** | The comprehensive set of records describing the AI system's design, development, training data, testing, and risk management measures, as required by Art. 11 and Art. 17 of the AI Act. In AML, this includes model cards, data lineage, and hyperparameter logs. |
| **Marktüberwachung** | **Market Surveillance** | The activities carried out by national competent authorities to ensure that AI systems already on the market or in service continue to comply with the AI Act. In Germany, BaFin and data protection authorities exercise this oversight for AML‑related AI systems. |