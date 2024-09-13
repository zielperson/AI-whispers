# Paul's Panel, my changes.

## Original Prompt
[Original](https://github.com/zielperson/AI-whispers/blob/master/PanelGPT%20CoT/originalpaul.md) von Paul Meyrat.
ein PanelGPT, sehr genau gesteuert durch einen CoT Prozess und Output Vorgaben.

## Übersicht der Versionen

| Version         | Beschreibung                                                                                                                                                              | URL                                                                                                                                                               | Tokens | Characters |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------------|
| Original Paul   | Original - prompt von Paul                                                                                                                                                 | [originalpaul.md](https://github.com/zielperson/AI-whispers/blob/master/PanelGPT%20CoT/originalpaul.md)                                                         | 1,152  | 4,136      |
| First Changes   | Erste manuelle Änderungen am Prompt. Übersicht über die Changes [hier](https://github.com/zielperson/AI-whispers/blob/master/PanelGPT%20CoT/changelog.md)                | [V1_00 First changes.md](https://github.com/zielperson/AI-whispers/blob/master/PanelGPT%20CoT/V1_00%20First%20changes.md)                                     | 853    | 3,104      |
| SOCAR refined   | Sent the manually changed prompt through SOCAR refinement.                                                                                                                 | [V1_01 SOCAR analysis on V1_0.md](https://github.com/zielperson/AI-whispers/blob/master/PanelGPT%20CoT/V1_01%20Socar%20analysis%20on%20V1_0.md)                  | 830    | 3,017      |

*Tokens berechnet mit [OpenAI Tokenizer](https://platform.openai.com/tokenizer?view=bpe) *
*Stand 23.09.2024 - Benutzt Tokenizer Modell 3.5 & 4 , noch kein neueres verfügbar.*

<img src="https://github.com/user-attachments/assets/abfdfe30-9355-4a50-82cd-a0107819780e" width="600"/>

## V1_00 First Changes
Ergebnis nach einigem editieren des Originals.

### Änderungen
#### Allgemein
* Klarere Hierarchie durch Benutzen von Markdown Titeln und Untertiteln.
* Kürzung wenn möglich.
* Entfernen von Doppelungen.
* Genauere Wortwahl.
#### Struktur
* Rolle neu definiert als Moderator.
* Ziel knapper und genauer formuliert.
* Wichtigen Hinweis weit oben in Hierarchie eingebunden, auf 1 Nennung reduziert.
* Hinweis positiv formuliert.
* Diverse Unterpunkte kombiniert.
#### Im Detail
* Genaue Angaben aller Changes hier:
  [Changelog](https://github.com/zielperson/AI-whispers/blob/master/PanelGPT%20CoT/changelog.md)

## V1_01 SOCAR Analyse und Refinement
Hier habe ich auf die vorherige Version V1_00 meinen eigenen SOCAR Prompt Refiner angesetzt.
Benutzt wurde GPT1o-preview (Stand 23.09.2024).
Die Änderungen sind leicht, aber merklich.

Erste Tests mit dem [SOCAR refined Panel Prompt](https://github.com/zielperson/AI-whispers/blob/master/PanelGPT%20CoT/V1_01%20Socar%20analysis%20on%20V1_0.md) (mit GPT10) sind vielversprechend. 

## To Do
- Weitere Tests mit den refined Prompt, auch unter GPT-4 Varianten und mistral.
- Weitere Manuelle version des Prompts (ich habe da noch Ideen).




