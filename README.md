# Rush Hour
Rush Hour is een simpel puzzeltje waarbij op een vierkant veld een rode auto staat die naar de uitgang moet. Echter versperren andere auto's en vrachtwagens de weg. Deze voertuigen kunnen enkel bewegen in één bepaalde richting en kunnen dus niet draaien. 

## Aan de slag
### Vereisten
Deze codebase is volledig geschreven in Python 3.7. In requirements.txt staan alle benodigde packages om de code te draaien. Deze zijn te installeren via 
```
pip install -r requirements.txt
```
Of via conda:
```
conda install --file requirements.txt
```

## Gebruik
De code kan gerund worden door het aanroepen van 
```
$ python3 main.py -h
usage: main.py [-h] [-m] input_csv output_folder mode runs

Run the Rush Hour solver

positional arguments:
  input_csv           gameboard csv file
  output_folder       folder for output
  mode                solver mode
  runs                amount of runs

optional arguments:
  -h, --help          show this help message and exit
  -m, --output_moves  Output moves made to file(s)
```
Om bijvoorbeeld de eerste puzzel tien keer op te lossen met het random algoritme, run:
```
python3 main.py game_boards/Rushhour6x6_1.csv output random 10
```

De commands om de verschillende algoritmen te runnen zijn:
```
random
breadth
depth
bestdepth
hill
```
## Structuur
De volgende lijst toont de belangrijkste mappen en files in dit project en waar je ze kunt vinden:
- **/code**: bevat alle code van dit project
    - **/code/algorithms**: bevat de code voor alle algoritmen
    - **/code/classes**: bevat de drie verschillende classes voor de case
    - **/code/functions**: bevat de functies om main te runnen
- **/game_boards**: bevat de verschillende speelborden

## Auteurs
- Annemarie Geertsema
- Jesse Fontaine
- Laura Haverkorn