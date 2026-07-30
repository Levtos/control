# Release, Testing, Live und Rollback

## Grundsatz

GitHub ist die aktive Code-, Workflow- und HACS-Plattform. GitLab bleibt
historisches Archiv und Rollback-Ziel. Forgejo ist außer Betrieb.

## HACS-Release

1. Änderung auf Branch umsetzen und Pull Request öffnen.
2. Manifest-Version nach Scope bumpen.
3. Den vorgesehenen Release- und Mirror-Weg aus dem Repository verwenden.
4. CI, Tag, Release und aktuelle Main-SHA serverseitig verifizieren.
5. Issue mit Tests, Risiken und verbleibendem Live-Gate aktualisieren.

Ein erfolgreicher Push, lokaler Test oder Merge beweist keine Live-Installation.
Benni führt den Home-Assistant-Pull, Reload, Restart und Deploy als eigenes
Live-Gate aus, sofern nicht ausdrücklich delegiert.

## Contract-Rollout

Bei Contract-Änderungen wird zuerst der Producer oder Feeder bereitgestellt.
Danach werden Consumer geprüft und umgestellt. Breaking Changes erhalten eine
neue Major-Version oder eine ausdrücklich dokumentierte Kompatibilitätsphase.

## Rollback

- Normale Revert-Änderung per Pull Request.
- Reverteten Stand als neue Patch-Version veröffentlichen.
- Ursache, betroffene Consumer und Rückweg im Issue dokumentieren.
- Keine Force-Pushes, Tag-Löschungen oder manuellen Release-Eingriffe.
- Home-Assistant-seitige Restores und Downgrades bleiben am geschützten
  Live-System.

## Dokumentationsgrenze

Private Hosts, Tokens, lokale Pfade und Betriebsdetails gehören nicht in
Release-Notes, Issues oder diesen Wiki-Snapshot.
