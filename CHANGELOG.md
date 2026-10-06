# Changelog

Jede Etappe ist ein Git-Tag. Alte Staende ansehen: `git checkout etappe-2` (zurueck: `git checkout main`).

## Etappe 3.1 (`etappe-3.1`)
- Fix: 6 px Abstand zum unteren Bildschirmrand, damit die Autohide-Taskleiste einfahren kann (`WindowDocker.BottomGap`)

## Etappe 3 (`etappe-3`)
- Projekt heisst jetzt **Desktop Adventures**
- Neu: `Platform/Taskbar.cs` liest die sichtbare Taskleisten-Hoehe aus (auch bei Autohide)
- Neu: `Platform/WindowDocker.cs` schiebt das Fenster sanft mit der Taskleiste mit
- `MainWindow` nutzt den Docker statt fester Positionierung

## Etappe 1+2 (`etappe-2`)
- Transparentes Fenster, animiertes Feuer, Charakter mit Idle und Klick-Reaktion
