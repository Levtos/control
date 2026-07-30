# Glossar

| Begriff | Bedeutung |
|---|---|
| Fleet | Gesamtheit der Benni-Integrationen und ihrer abgestimmten Contracts |
| Profil | Zielhaushalt einer Integrationsinstanz |
| Master | stabiler, normalisierter Domain-Vertrag; die endgültige Ownership muss pro Domain dokumentiert sein |
| watt-primär | Aktivitätserkennung anhand realer elektrischer Last statt eines möglicherweise stale Player-States |
| Contract | langlebige Schnittstelle aus Schema, Attributen oder API |
| Consumer Cutover | kontrolliertes Umhängen eines Consumers auf den neuen Owner |
| Feeder | L1-Modul, das Bedeutung ableitet, aber keine Policy entscheidet |
| Policy | L2-Modul, das ein Ziel und die Begründung entscheidet |
| Apply | L3-Modul, das ein Policy-Ziel idempotent ausführt |
| Shadow-only | berechnen, prüfen und diagnostizieren ohne öffentliche Wirkung oder Actuation |
| Published Entity | ausdrücklich erlaubte öffentliche Home-Assistant-Entity eines Contracts |
| Look | benannter Licht-Zielzustand |
| Scenario / Context | abgeleitete Situationsbeschreibung |
| Private Time | privater Media-Kontext mit eigenen Caps und Anzeigegrenzen |
| Quiet Mode | Ruheanforderung aus dem Media-Kontext |
| Audio Owner | Policy-Verantwortung für den aktuellen Audio-Konsumenten |
| Volume Matrix | datengetriebene Ziel-Lautstärke je Gerät, Kontext und Tagesphase |
| Media Cockpit | Umbrella-UX ohne eigene Business-Logik |
| Strangler | schrittweise Extraktion aus einem Legacy-Monolithen |
| Live Evidence | autorisierte Beobachtung am laufenden System |
| testing | Umsetzung abgeschlossen, technischer oder Live-Nachweis offen |
| live | umgesetzt, verifiziert und dokumentiert |

Begriffe wie Opening, Lock, Activity State und dreistufiger Fensterzustand
werden bei der Core-Contracts-Neuordnung fachlich neu gegen den aktuellen
Contract und seine Consumer geprüft; alte Alias- oder Legacy-Bedeutungen
gelten nicht automatisch als Zielvertrag.
