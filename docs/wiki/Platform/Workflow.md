# Workflow — bereinigte Wiki-Fassung

Die verbindliche Vollversion liegt in docs/workflow. Diese Seite ist die
kompakte Arbeitsfassung und keine zweite Regelquelle.

## Wahrheitsquellen

- Soll: mit Benni entschiedene, vollständig dokumentierte GitHub-Issue samt
  Kommentaren und verknüpften ADRs.
- Ist: kleinste ausreichende technische Evidenz aus Code, Tests,
  installierten Versionen und autorisierter Live-Beobachtung.
- Konflikte werden nicht stillschweigend entschieden. Soll und Ist werden
  getrennt benannt, im Issue dokumentiert und gezielt angeglichen.
- GitHub ist die einzige aktive und historische Arbeits-, Nachweis- und
  Release-Plattform. GitLab, Plane und Forgejo sind retired und keine gültigen
  Alternativen, Archive oder Rollback-Ziele.

## Rollen

- Benni ist fachlicher Entscheider und gibt die Live-Verifikation frei.
- ChatGPT versteht Problem und Kontext, liest Issue, Wiki und Contracts,
  trennt Ist, Hypothese und Soll und pflegt die dauerhaften Artefakte.
- Codex und Claude liefern angeforderte technische Evidenz oder setzen einen
  bereits entschiedenen Soll-Zustand scope-konform um.
- Pro Issue gibt es genau einen aktiven Agenten, festgelegt als `agent:codex`
  oder `agent:claude`; die verbindliche Übergaberegel steht in
  [docs/workflow/agent-orchestration.md](../../workflow/agent-orchestration.md).

Technische Agenten entscheiden kein fachliches Soll eigenständig und bauen
keine ungefragten Alternativen.

## Auftragstypen

### Read-only-Evidenzauftrag

Issue, Wiki und benannte Codepfade vollständig lesen; nur die angeforderten
Fakten prüfen; keine Lösung entscheiden; keine Dateien oder Live-Systeme
verändern; den Befund im Issue dokumentieren.

### End-to-End-Umsetzungsauftrag

Issue und relevante Dokumentation lesen; den dort beschlossenen Soll-Zustand
minimal umsetzen; tests, Branch, Pull Request, Release- und Rollbackweg sowie
Issue-Evidence vollständig pflegen. Stopp nur bei neuer fachlicher
Entscheidung, wesentlichem Risiko oder echtem Blocker.

## Issue-Struktur

Arbeits-Issues trennen:

- Beobachtung
- betroffener Bereich
- technischer Ist-Nachweis
- fachlicher Soll-Zustand
- offene Entscheidungen
- verbindlicher Umsetzungsauftrag
- Akzeptanzkriterien
- Tests und technische Verifikation
- Release, Deployment und Rollback
- Wiki-Auswirkung
- Live-Verifikation

## Status und Evidence

Issue-first → Entscheidung → in-progress → testing → Live-Evidence → live.

testing bedeutet umgesetzt, aber Live-Nachweis offen. live bedeutet
implementiert, geprüft und dokumentiert; das bleibt Bennis Gate.

## Datenschutz

Keine Secrets in Issues, Kommentaren, Repository-Dateien, Logs,
Prozessargumenten oder Screenshots. Private Home-Assistant-Konfiguration und
Netzwerkdetails bleiben außerhalb des öffentlichen Repositories.

## Verifikation

Die Tiefe folgt dem Blast-Radius: Dokumente erhalten Link- und Strukturchecks,
Contract-Änderungen Producer-/Consumer-Prüfung, Live-Verhalten zusätzlich
autorisierte Live-Evidence.
