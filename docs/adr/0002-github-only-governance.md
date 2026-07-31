# ADR 0002: GitHub-only Governance, Agenten-Workflow und Repository-Lebenszyklus

- Status: beschlossen; technische Umsetzung über Pull Request
- Datum der Entscheidung: 2026-07-31
- Aktives Tracking: [Levtos/control#21](https://github.com/Levtos/control/issues/21)
- Bezug: [ADR 0001](0001-ux-frontend-standard.md)
- Geltungsbereich: GitHub-Projekt `Levtos`, `control/docs/` und die aktiven
  öffentlichen Integrations-Repositories

## Entscheidung

### Quelle und Verbindlichkeit

GitHub ist die einzige aktive und historische Arbeits-, Nachweis- und
Wissensquelle für das Projekt. GitLab, Plane und Forgejo sind keine gültigen
Alternativen, Archive oder Rollback-Ziele. Historische Links dürfen als
bereinigte Provenienz erhalten bleiben, sind aber nicht normativ und nicht Teil
des laufenden Arbeits- oder Wiederherstellungswegs.

`control/docs/` ist die einzige versionierte und dauerhafte Regelquelle. Issues
und ihre Kommentare enthalten den aktuellen Auftrag, Entscheidungen,
Beobachtungen, technische Nachweise, Risiken und offene Gates. Eine kurze
ChatGPT-Projektanweisung ist nur eine gleichlautende Leitplanke und verweist auf
diese Dokumentation; sie bildet keine zweite Regelquelle.

### Rollen und Ownership

- Benni entscheidet fachliches Soll, Priorität, Scope und die abschließende
  Live-Verifikation.
- ChatGPT übernimmt im Projektordner Triage, lesende Evidenzprüfung,
  Architekturklärung, Issue-Qualität und Review-Kontext. ChatGPT nimmt keine
  Code-, Konfigurations-, Test-, Workflow-, Deployment- oder Live-Änderungen
  vor.
- Pro Issue arbeitet genau ein lokaler Umsetzungsagent. Der aktive Agent wird
  als `agent:codex` oder `agent:claude` im Issue festgelegt.
- Codex und Claude dürfen grundsätzlich in allen aktiven Repositories arbeiten;
  die Ownership gilt pro Issue und ist keine dauerhafte Repository-Sperre.
- Der Issue-Agent verantwortet Branch, Umsetzung, Tests, PR, serverseitigen
  Merge, Abschlussnotiz und bei fachlichen Änderungen eine kurze versionierte
  Entscheidungsnotiz. Die Live-Abnahme bleibt Benni vorbehalten.

Eine Übergabe erfolgt ausschließlich über eine vollständige Issue-Notiz mit
aktuellem Soll/Ist, Branch und Commit, geänderten Dateien, Tests, Risiken,
offenen Entscheidungen und dem nächsten Schritt. Der bisherige Agent beendet
seine Umsetzung, der neue Agent liest und bestätigt den Stand; parallele
Implementierungen oder konkurrierende Lösungen sind nicht zulässig.

### Zuständigkeit und Grenzen

Fachliche Fehler werden im beobachteten Fach- oder Instanz-Repository erfasst.
`control` ist für plattformweite Regeln, Standards, Architekturentscheidungen,
Repository-Lebenszyklus und übergreifende Migrationen zuständig. Neue
Integrations- oder Live-Änderungen gehören nicht stillschweigend in ein
Governance-Issue.

Jede neue UX-Arbeit folgt ADR 0001. `core-devices` bleibt im Betrieb Legacy,
bis der Published-Contract- und Consumer-Cutover von `core-contracts` live
verifiziert ist; diese ADR ändert keine Migrationslogik. Umbenennungen,
Archivierungen, Löschungen und mögliche Integrationsfusionen bleiben Backlog
und sind nicht Teil dieser Entscheidung.

CTX ist für lokale Agentenarbeit der verpflichtende erste Kontextschritt, sofern
CTX in der lokalen Umgebung verfügbar ist. Installation oder Konfiguration von
CTX ist nicht Teil dieser ADR.

## Verbindlicher Workflow

1. Issue vollständig lesen, einschließlich aller Kommentare, Labels,
   Project-Felder, relevanter `control/docs/`-Seiten und einer passenden
   Funktionsspezifikation.
2. Issue in `Platform Workflow` führen und Status, Typ, Owner, Scope, Evidence
   sowie Priority/Module nur setzen, wenn sie belegt sind.
3. Mit sauberem Clone oder isoliertem Worktree vom verifizierten Default-Branch
   arbeiten; fremde oder schmutzige Checkouts nicht überschreiben.
4. Ausschließlich den entschiedenen Scope umsetzen und risikogerechte Tests
   sowie Dokumentations- und Linkprüfungen ausführen.
5. Branch pushen und einen PR eröffnen. Beschreibung, Checks, Risiken,
   Release-/HACS-Auswirkung und verbleibendes Live-Gate müssen nachvollziehbar
   sein.
6. Review-Funde im selben PR scope-konform bearbeiten; neue Produktfragen
   werden als Entscheidung im Issue angehalten.
7. Nach technischem Abschluss Issue, Project, PR, Commit, Checks und Risiken
   dokumentieren. `Testing`/`Tests Pass` bedeutet nicht `Live`; `Live` und
   `Live Verified` bleiben Bennis Gate.

Fachliche Änderungen erhalten zusätzlich eine kurze versionierte
Entscheidungsnotiz unter `docs/adr/` oder in der zuständigen kanonischen
Dokumentationsstelle. Routine-Bugfixes und rein technische Dokumentations-
änderungen brauchen keine künstliche ADR.

## Repository-Lebenszyklus

Die Statuswerte und die aktuelle Registry stehen in
[operations/repositories.md](../operations/repositories.md). Ein Status ist
eine dokumentierte Einordnung, keine automatische Archivierungs-, Lösch- oder
Migrationsaktion. Jede Änderung braucht ein eigenes GitHub-Issue und die
fachliche Freigabe im passenden Scope.

## Folgen und Nicht-Ziele

Der Arbeitsweg ist eindeutig GitHub-zentriert, Agenten-Ownership ist
nachvollziehbar und technische Fertigstellung bleibt von der Live-Abnahme
getrennt. Diese ADR migriert keine Integration, ändert keine Home-Assistant-
Konfiguration, aktiviert keinen Dienst und führt keine Repository-Umbenennung,
Archivierung, Löschung oder Fusion aus.

## Quellen

- [Levtos/control#21](https://github.com/Levtos/control/issues/21)
- [ADR 0001](0001-ux-frontend-standard.md)
- [GitHub workflow](../workflow/README.md)
- [Agent orchestration](../workflow/agent-orchestration.md)
- [Repository registry](../operations/repositories.md)
