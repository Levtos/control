# ADR 0001: Einheitlicher UX-, Technologie- und Designstandard

- Status: angenommen und bindend
- Datum der Entscheidung: 2026-07-24
- Aktives Tracking: [Levtos/control#17](https://github.com/Levtos/control/issues/17)
- Historische Quelle: [GitLab control#58](https://gitlab.b-struck.de/ha-platform/control/-/work_items/58)
- Geltungsbereich: die gemeinsamen UX-Bausteine der Home-Assistant-Integrationen

## Entscheidung

Die fachlichen Backends bleiben 19 eigenständige native Home-Assistant-
Integrationen. Die gemeinsame UX wird als einheitliche Plattform gebaut:

1. ein zentrales statisches Frontend-Bundle mit App-Shell, Navigation,
   Designsystem, wiederverwendbaren Komponenten und typisiertem Contract-Modell;
2. ein schlankes UX-Gateway für Authentifizierung, Contract-Normalisierung und
   Live-Kommunikation;
3. integrationsspezifische Seiten als getrennte Module oder Adapter innerhalb
   dieser gemeinsamen UX.

Das Gateway darf keine Domänenlogik aus den Integrationen duplizieren. Die
fachliche Datenhoheit, Domain-Logik, Registry- und Integrationsverantwortung
bleiben in den jeweiligen nativen Backends.

## Backend- und Deployment-Grenze

- Es gibt keinen gemeinsamen Docker- oder LXC-Backend-Ersatz für die
  Integrationen.
- Der primäre Bereitstellungsweg ist eine Home-Assistant-App bzw. ein Add-on
  über Ingress.
- Docker, LXC oder statisches Hosting sind alternative Verpackungen desselben
  Bundles, keine abweichenden Architekturen.
- Browser → Gateway → Home Assistant ist die zulässige Kommunikationsgrenze.
- Authentifizierung und Autorisierung liegen serverseitig.
- Ein SUPERVISOR_TOKEN oder andere Zugangsdaten dürfen niemals im Frontend,
  in localStorage, in URLs oder in Diagnosedaten landen.

## Eingefrorener Frontend-Stack

Verbindliche Basis:

- Svelte 5
- Vite
- TypeScript
- statische SPA-Ausgabe
- Bits UI
- shadcn-svelte als kontrolliert übernommener Quellcode
- Tailwind
- CSS Custom Properties für Design-Tokens
- Lucide für Icons
- Svelte-5-Runes
- typisierte Stores und Contracts

Nicht vorgesehen sind React, Vue, Angular, eine SSR-Pflicht durch SvelteKit,
mehrere konkurrierende UI-Bibliotheken, CDN-Abhängigkeiten, Remote-Fonts,
Pro-Komponentenbibliotheken oder eine Runtime-Abhängigkeit von UI Vault.

## Designstandard

Der visuelle Standard heißt Graphite Dark – semantic accent system:

- dunkles Graphit statt reinem Schwarz;
- semantische Farb-Tokens für Erfolg, Information, Warnung und Fehler;
- keine globale Pink- oder Neon-Farbwelt;
- Systemschrift;
- 4-Pixel-Raster;
- Radien 8 und 12 Pixel als Standard;
- Lucide-Icons statt Emoji oder uneinheitlicher Icon-Sammlungen;
- klare Hierarchie, ausreichender Kontrast und sichtbare Fokuszustände.

## Zustands- und Interaktionsvertrag

Jede UX muss die Zustände loading, ready, empty, stale, degraded,
unavailable, reconnecting, offline, error und blocked explizit darstellen.
Degraded bedeutet eine eingeschränkte oder unsichere Teilfunktion, nicht
automatisch einen Totalausfall.

Die primäre Zielumgebung ist Desktop. Touch-Bedienung mit mindestens 44 Pixel
großen Zielen und Kiosk-Nutzung auf einem Lenovo M11 werden unterstützt, ohne
die Architektur auf dieses Gerät zu verengen.

Statische Builds, Lazy Loading und die Vermeidung von CSS-in-JS sind Standard.
Bewegungen liegen typischerweise im Bereich von 120 bis 240 Millisekunden,
respektieren prefers-reduced-motion und dürfen keine Information nur über
Animation vermitteln.

Deutsch ist die primäre Sprache. Datums-, Zeit- und Zeitzonenlogik verwendet
de-DE und Europe/Berlin; spätere Internationalisierung bleibt möglich.

## Contract- und Transportmodell

- Contracts zwischen Gateway und Frontend sind typisiert und versioniert.
- REST liefert Snapshots; WebSocket liefert Live-Änderungen.
- Commands und Events sind getrennte Nachrichtenarten.
- Nach einer Unterbrechung folgt reconnect → resync.
- Breaking Changes erhalten eine neue Major-Version.
- Komponenten binden auf den UX-Contract, nicht auf rohe Home-Assistant-
  Entity-Strukturen.
- Jede berechnete Bedeutung besitzt genau einen Owner.

## Sicherheit und Datenschutz

Das Frontend enthält keine Tokens, Passwörter, privaten Schlüssel oder
sonstigen Geheimnisse. Zugangsdaten werden nur serverseitig verarbeitet.
Mutierende Aktionen müssen authentifiziert, autorisiert und nachvollziehbar
sein. Credentials gehören weder in Logs noch in Fehlermeldungen,
Screenshots, Issues, Repository-Dateien oder Diagnose-Payloads.

## Lizenz- und Architekturregeln

Verwendete Bibliotheken müssen mit der Projektverteilung vereinbar sein,
beispielsweise MIT oder Apache-2.0. Neue Abhängigkeiten dürfen den
eingefrorenen Stack nicht stillschweigend ausweiten.

Eine Abweichung von Frontend-Framework, Build-System, Komponentenbibliothek,
Design-Token-System, Contract-Modell, zentraler Shell,
Authentifizierungsmodell, Deployment-Grundmodell oder Statussemantik benötigt
eine neue fachliche Entscheidung vom Typ decision und eine ersetzende ADR.

## Folgen

Die 19 Integrationen erhalten eine gemeinsame visuelle und technische
Leitplanke, ohne ihre fachliche Autonomie zu verlieren. Ältere React-,
native-JavaScript- oder integrationsspezifische Panels werden schrittweise
migriert; das ist kein Big-Bang-Cutover. Vor einer Migration müssen Contract,
Owner, Consumer, Auth-Grenze, Rollback und Live-Gate dokumentiert sein.

Die Standardisierung erhöht die Contract-Disziplin. Ein Backend muss seine
fachliche Wahrheit und seinen Gateway-Adapter liefern, bevor eine Seite in die
gemeinsame Shell aufgenommen wird.

## Abgrenzung zum Core-Contracts-Projekt

Core Contracts ist eine eigenständige Foundation-Integration. Der aktuelle
verifizierte Stand ist ein read-only Shadow-only-Slice ohne öffentliche
Home-Assistant-Entities, Services, Actuation oder Policy-Logik. Die
gemeinsame UX-ADR definiert die Technologie und die UX-Grenze; sie ersetzt
nicht die fachliche Core-Contracts-Entscheidung aus GitLab control#57.

Das aktuelle Core-Contracts-Zielbild und die offenen Übergangsgates stehen in
der [GitHub-Provenienz zu control#57](https://github.com/Levtos/benni-core-contracts/issues/1).
Ältere Wiki-Atlas-Texte, die Core Devices als alleinige L0-Grundlage oder
Opening/Lock dort als endgültigen Owner beschreiben, sind deshalb als
historischer Zwischenstand zu behandeln, bis der Published-Entity- und
Consumer-Cutover ausdrücklich verifiziert ist.

## Quellen

- [GitHub control#17](https://github.com/Levtos/control/issues/17)
- [GitLab control#58](https://gitlab.b-struck.de/ha-platform/control/-/work_items/58)
- [GitLab control#57](https://gitlab.b-struck.de/ha-platform/control/-/work_items/57)
- [UX-Einstieg](../ux/README.md)
- [Bereinigter Wiki-Snapshot](../wiki/README.md)
