# Integrationen — Übersicht

Dies ist ein bereinigter Snapshot der historischen 19-Integrationen-Karten.
Die Versionsstände stammen aus dem GitLab-Wiki und sind datierte Provenienz,
nicht automatisch installierte Live-Versionen. Aktuelle Code- und Issue-
Nachweise stehen in den jeweiligen GitHub-Repositories.

## Foundation und Feeder

### core-devices

Normalisiert rohe Home-Assistant-Entitäten zu Geräte-Masters und stabilen
Domain-Signalen. Es entscheidet keine Policy. Watt-primäre Aktivität,
Weather-Cutover und einzelne Geräteklassen waren im Snapshot eigene offene
Themen.

### core-state

Leitet Bio-State, Aktivität, Presence und Live-Status aus stabilen Quellen
ab. Es liefert Kontext und entscheidet keine Geräte- oder Aktions-Policy.

### core-contracts

Eigenständige Foundation aus dem internen Signalgraphen. Der aktuelle
verifizierte Slice ist read-only und Shadow-only. Öffentliche Entities,
Services, Actuation und Policy-Logik sind im aktuellen Slice ausgeschlossen.
Das spätere Published-Entity-Zielbild und der Consumer-Cutover sind separat
zu entscheiden. Siehe [Core Contracts UX](Core-Contracts/UX.md).

### title-classifier

Kanonisiert Titel und Apps zu stabilen Enums. Der Idle-Sentinel ist Teil des
Consumer-Vertrags; Inaktivlisten müssen bei Änderungen mitgezogen werden.

### media-state

Liefert Media-Kontext, Subkontext, aktives Gerät, Gaming-Signale, Quiet Mode,
Private Time und den Activity-Feed an core-state.

### media-context

Historische Standalone-Extraktion des Media-Contexts. Die fachliche
Restrolle und ein eventueller Consumer-Cutover bleiben getrennt zu verifizieren.

## Policies

### light-policy

Entscheidet Looks je Raum und Kontext und delegiert das Rendern an
scene-presets.

### blind-policy

Entscheidet Rollo-Ziele aus Tagesphase, Hitze, Privatsphäre und
Fenstersicherheit. Opening-Sicherheit muss über einen stabilen Opening-Contract
bezogen werden.

### climate-policy

Besitzt Heizungs- und Klima-Policies, Zieltemperaturen und Heizprofile.

### door-policy

Besitzt Tür-/Schloss-Policies, einschließlich der fachlichen Guards für
Auto-Unlock. Roh-Lock- und Opening-Quellen werden nicht dauerhaft doppelt
interpretiert.

### media-policy

Entscheidet Audio-Owner, Aktionen, Volume-Ziele, Ducking, Subwoofer-
Erlaubnis und Apply-Gates.

### plug-policy-engine

Entscheidet Steckdosen- und Cut-Safety anhand von Archetypen, Masters und
Kontext. Die endgültige Cut-Entscheidung bleibt Policy-Ownership.

### notification-router

Routet Ereignisse kontextabhängig an Benachrichtigungsziele.

## Render und Apply

### scene-presets

Rendert von light-policy angeforderte Looks und führt keine eigenständige
Kontext-Policy.

### media-apply

Setzt media-policy-Ziele idempotent an Geräten um. Es denkt nicht und baut
keine Domain-Wahrheit neu auf.

## UX und ergänzende Integrationen

### media-core

Umbrella-Panel, Router und WebSocket-Gateway für Media; keine Business-Logik.

### media-art-wrapper

Liefert Cover-Art- und Wrapper-Entities für Player ohne Artwork.

### discord-game

Liefert Discord-Status und Spielsignale als eigenständige Integration.

### wake-planner

Berechnet Wake-Contracts wie next_wake, wake_state und wake_needed.

### stash-integration

Liefert Stash-Playback- und Library-Signale sowie die zugehörigen Services.

## Architekturhinweis

Der historische Atlas ordnete core-devices als alleinige L0-Foundation ein.
Das neue Core-Contracts-Zielbild ist davon abzugrenzen: Es wurde als
unabhängige Foundation entschieden und darf nicht als unveränderte Kopie,
Alias oder automatischer Ersatz von Core Devices behandelt werden.
