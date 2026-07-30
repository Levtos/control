# Media-Stack — Übersicht

Die Media-Logik ist die Kette Feeder → Policy → Apply plus Umbrella-UX.
Module konsumieren Verträge statt Python-Imports aus anderen Integrationen.

## Kette und Verantwortungsgrenzen

| Modul | Schicht | Frage |
|---|---|---|
| media-state | L1 Feeder | Was sieht das System? |
| media-policy | L2 Policy | Was soll passieren und warum? |
| media-apply | L3 Executor | Was wurde wirklich ausgeführt? |
| media-core | L4 Umbrella | Wie wird es angezeigt und aggregiert? |
| media-context | L1 Legacy | Welche Restrolle hat die historische Extraktion? |

media-state entscheidet nichts, media-policy führt nichts aus und media-apply
denkt nicht. Der Activity-Feed von media-state ist eine Boundary zu core-state
statt einer zweiten Aktivitätserkennung.

## Quellen

- core-devices-Masters liefern normalisierte Geräte- und Watt-Signale.
- title-classifier liefert stabile Titel-/App-Enums.
- media-state leitet Kontext, Subkontext, aktives Gerät, Gaming-Quelle,
  Quiet Mode und Private Time ab.
- media-policy entscheidet Audio-Owner, Aktionen, Volume Matrix, Ducking,
  Subwoofer-Erlaubnis und Apply-Gates.
- media-apply konvergiert reale Geräte idempotent auf das Policy-Ziel.
- media-core aggregiert State, Policy und Apply in eine Umbrella-UX.

## Contracts

Der historische Media-Cockpit-Contract benni_media.v1 nutzt getrennte
Overview-, State-, Policy-, Apply- und Diagnostics-Abfragen. Fehlende Module
werden als Empty- oder Error-State angezeigt, nie als Blank Page.

Policy- und Apply-Contracts umfassen unter anderem volume_target,
audio_owner, action, subwoofer_allowed und volume_apply_allowed.

## Bekannte Sonderfälle

- Player-Dropouts dürfen bei realer Last nicht blind als OFF interpretiert
  werden; watt-primäre Gates und begrenzte Holds bleiben sichtbar.
- Stale webOS- oder denonavr-States werden nicht ungeprüft als Gerätewahrheit
  verwendet.
- Eine geteilte Denon-Senke darf nur enden, wenn kein anderer Konsument aktiv
  ist.
- Wake-Gates dürfen Schlaf- und Weckphasen nicht durch Idle-Resume brechen.
- Entity-ID-Präfixe dürfen in Bindings nicht aus einem idealisierten Slug
  geraten werden.
- Meterless-Geräte dürfen keinen erfundenen Watt-Vertrag erhalten.

## UX-Abgrenzung

Der geplante Media-Cockpit-Neubau muss ADR 0001 folgen: Svelte 5, Vite,
statisches Bundle, dünnes Gateway, typed REST/WebSocket und kein duplizierter
Media-Backend-Code.

## Dokumentationsstatus

Die Wiki-Quelle enthielt veraltete README- und Scaffold-Hinweise sowie
historische Versionsstände. Welche Version live installiert ist, ergibt sich
nur aus dem jeweiligen GitHub-Issue mit Tests- oder Live-Evidence.
