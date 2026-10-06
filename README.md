# Desktop Adventures

Ein kleines Pixel-Art-Spiel ohne richtiges Fenster: Ein Lagerfeuer mit Charakteren sitzt
direkt auf der Taskleiste. Transparente Bereiche sind klickdurchlaessig.

## Starten (Rider)
1. `Lagerfeuer.csproj` oeffnen (File > Open)
2. Run-Konfiguration "Lagerfeuer" waehlen, Play druecken
3. Beenden: Rechtsklick auf Feuer oder Figur > Beenden

Voraussetzung: .NET 8 SDK, Windows.

## Sprites
`make_sprites.py` (Python + Pillow) erzeugt die Platzhalter-Sprites in `Assets/`.
Eigene Sprites einfach als horizontale Sprite-Sheets (Frames nebeneinander) ersetzen.

## Etappen
- [x] 1. Transparentes Fenster mit animiertem Lagerfeuer
- [x] 2. Ein Charakter mit Idle-Animation und Klick-Reaktion
- [x] 3. Taskleisten-Verhalten (folgt der Autohide-Taskleiste)
- [ ] 4. Charaktere aus JSON (Aussehen, Outfits, Texte austauschbar)
- [ ] 5. Das "Fenster": klarer, gerahmter Spielbereich
- [ ] 6. Erstes Minigame samt Freischaltung
- [ ] 7. Speichern, Tageszeit-Stimmung, Tray-Icon

Siehe `CHANGELOG.md`. Jede Etappe ist als Git-Tag abgelegt (`etappe-2`, `etappe-3`, ...).
