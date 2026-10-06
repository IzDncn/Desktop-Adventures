# Changelog

Jede Etappe ist ein Git-Tag. Alte Staende ansehen: `git checkout etappe-2` (zurueck: `git checkout main`).

## Etappe 4 (`etappe-4`)
- Charaktere kommen aus `Characters/<id>/character.json` (Name, Sitzplatz, Texte, Outfits, Frame-Groesse/-Timing)
- Outfits pro Charakter (Wanderer: `default` + `winter`), Wechsel per `Character.SetOutfit`
- Zwei Charaktere am Feuer (Wanderer, Pip der Barde); eigene Sprechblase pro Charakter, gelegentliches Selbstgespraech
- Neue Struktur: `CampScene` (Aufbau + Takt), `CharacterView` (UI), `Character` (Logik), `Data/` (JSON-Modelle + Loader), `SceneLayout`
- Fehlerhafte Charaktere werden uebersprungen und beim Start gemeldet
- Doku: `docs/CHARAKTERE.md`; Sprite-Generator liegt jetzt in `tools/`

## Etappe 3.1 (`etappe-3.1`)
- Fix: 6 px Abstand zum unteren Bildschirmrand, damit die Autohide-Taskleiste einfahren kann (`WindowDocker.BottomGap`)

## Etappe 3 (`etappe-3`)
- Projekt heisst jetzt **Desktop Adventures**
- Neu: `Platform/Taskbar.cs` liest die sichtbare Taskleisten-Hoehe aus (auch bei Autohide)
- Neu: `Platform/WindowDocker.cs` schiebt das Fenster sanft mit der Taskleiste mit
- `MainWindow` nutzt den Docker statt fester Positionierung

## Etappe 1+2 (`etappe-2`)
- Transparentes Fenster, animiertes Feuer, Charakter mit Idle und Klick-Reaktion
