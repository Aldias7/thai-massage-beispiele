# Bildquellen

Alle Bilder auf den drei Entwürfen sind **selbst gezeichnete Platzhalter** (SVG-Grafik: Lotus, Farn, Steine, Chedis, Orchideen, Webborten und Ähnliches). Es sind keine Fotos, keine Personen, keine fremden Bilder und keine Logos. Es gibt keine externen Bildquellen und keine Lizenzpflichten.

Gezeichnet werden sie von `werkzeug/platzhalter_bauen.py` (Bausteine in `werkzeug/platzhalter_lib.py`). Die Dateien liegen in `beispiel-1/bilder/`, `beispiel-2/bilder/` und `beispiel-3/bilder/`.

## Echte Fotos später einsetzen

Jedes Platzhalterbild hat das Seitenverhältnis seines Platzes (im `<img>` als `width` und `height` eingetragen). Ein eigenes Foto im gleichen Seitenverhältnis (zum Beispiel 3:2, 4:5, 2:3, 3:4, 1:1, 8:5) ersetzt es, indem nur `src`, `width`, `height` und `alt` im `<img>` getauscht werden. Eigene Fotos aus dem Laden (mit Einwilligung abgebildeter Personen) verkleinert als WebP oder JPG ablegen.

## Schriften (schriften/)

Jost, Newsreader und EB Garamond, jeweils unter der SIL Open Font License, lokal abgelegt (keine Verbindung zu Google beim Aufruf der Seite). Quelle der Dateien: Google Fonts.

## Eigenes Foto der Inhaberin (chuan-640.webp, chuan-1200.webp)

Das Porträt in `bilder/chuan-640.webp` und `bilder/chuan-1200.webp` ist ein **eigenes Foto der Inhaberin Chuan**, von Aldias am 27.11.2026 geliefert (Original: Handy-Screenshot, bleibt lokal in `eigene-fotos/` und kommt nicht ins Repo). Zuschnitt 4:5 ohne Rand, Balken und Blumen-Rahmen, Metadaten (EXIF/GPS) entfernt; Skript `werkzeug/chuan_zuschnitt.py`. Eingebaut in `beispiel-1`, `beispiel-2` und `beispiel-3` (Abschnitt „Über uns“). Alle anderen Bilder bleiben die Platzhalter.

**Offen vor dem Livegang:** Ihre Zustimmung zur Veröffentlichung des Fotos auf der Website (über Aldias) ist noch nicht bestätigt. Aldias bestätigt sie, bevor etwas ins Netz geht.
