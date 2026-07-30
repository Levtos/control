# Live Evidence

Der tatsächliche Ist-Zustand wird nur durch passende technische oder
autorisierte Live-Evidence belegt, nicht durch ein Label, ein Dokument oder
einen Agentenbericht allein.

## Evidence-Stufen

| Kennzeichnung | Bedeutung |
|---|---|
| evidence/missing | Noch kein ausreichender Nachweis |
| evidence/tests-pass | Tests, Review oder Pilot mit konkretem Nachweis erfolgreich |
| evidence/live-verified | Verhalten am laufenden System mit Was, Wo und Wann beobachtet |

Ein gemergter oder getaggter Release ist keine Live-Evidence.

## Prinzipien

- Read-only und minimal: kleinste ausreichende Beobachtung.
- Beobachtung zuerst dokumentieren, Interpretation danach.
- Fehlgeschlagene Verifikation wird nicht maskiert.
- Degraded, stale oder unavailable werden sichtbar gehalten.
- Live-Evidence darf private Tokens, Pfade oder Zugangsdaten nicht ausgeben.

## Ablauf

testing bedeutet: Umsetzung abgeschlossen, Live-Nachweis offen. Erst nach
dokumentierter Live-Evidence und erfülltem Abschluss-Gate wird ein Issue live.
