# Bereinigter Wiki-Snapshot

Dieser Ordner ist ein bereinigter, navigierbarer Snapshot von früheren
Projekt-Memory-Seiten. GitHub ist die einzige versionierte Arbeits- und
Wissensquelle; ältere Plattformen bleiben höchstens nicht-normative Provenienz
und sind keine Archive oder Rollback-Ziele.

Der Snapshot wurde am 2026-07-30 aus den Wiki-Seiten und den zugehörigen
Issues erstellt. Er ist bewusst bereinigt:

- keine Tokens, Zugangsdaten, privaten Schlüssel oder geheimen URLs;
- keine lokalen IP-Adressen oder detaillierte private Netzwerktopologie;
- keine Home-Assistant-Backups, Live-Diagnosedaten oder sonstigen privaten
  Betriebsdaten;
- die historische MCP-Wiki-Testseite wurde nicht übernommen, weil sie keinen
  Projektinhalt enthält;
- historische Aussagen bleiben als historisch markiert und werden nicht
  automatisch zum aktuellen Zielzustand.

## Kanonische Einstiegspunkte

- [Plattform-Architektur](../architecture/platform.md)
- [Contracts](../contracts/overview.md)
- [UX-Standard / ADR 0001](../adr/0001-ux-frontend-standard.md)
- [Workflow](../workflow/README.md)
- [GitHub-Issue-Mapping](../migration/github-issue-mapping.md)

## Überführte Seiten

### Plattform

- [Architecture](Platform/Architecture.md)
- [Workflow](Platform/Workflow.md)
- [Glossary](Platform/Glossary.md)
- [Operational Repositories](Platform/Operational-Repositories.md)

### Integrationen

- [Integrations Overview](Integrations/Overview.md)
- [Core Contracts UX](Integrations/Core-Contracts/UX.md)
- [Media Overview](Integrations/Media/Overview.md)

### Contracts und Betrieb

- [Contracts Overview](Contracts/Overview.md)
- [Live Evidence](Operations/Live-Evidence.md)
- [Release and Rollback](Operations/Release-and-Rollback.md)

### Entscheidungen und Runbooks

- [Decisions Overview](Decisions/Overview.md)
- [Runbooks Overview](Runbooks/Overview.md)

## Umgang mit Widersprüchen

Soll und Ist werden getrennt dokumentiert. Die ältere Atlas-Struktur entstand
vor dem Core-Contracts-Zielbild und kann deshalb bei Foundation-, Opening- und
Lock-Ownership abweichen. Die aktuelle verbindliche UX-Entscheidung steht in
ADR 0001. Die fachliche Core-Contracts-Entscheidung und der spätere Published-
Entity-/Consumer-Cutover bleiben in
[benni-core-contracts#1](https://github.com/Levtos/benni-core-contracts/issues/1)
und dem zugehörigen Issue-Verlauf.

Konkrete Logs, Zeitstempel, Hypothesen und einzelne Live-Vorfälle bleiben in
GitHub-Issues. Der Wiki-Snapshot beschreibt nur dauerhaft wiederverwendbares
Wissen.
