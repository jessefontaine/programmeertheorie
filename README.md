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
  -m, --output_moves  output moves made to csv file(s)
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
restarthill
sahill
```
## Algoritmen
Om de puzzels op te lossen zijn er verschillende algoritmen die gebruikt kunnen worden. Deze algoritmen zijn random, constructief (Breadth First Search, 
Depth First Search en Best Depth First Search) en iteratief (Hill Climber). Hierbij wordt gebruik gemaakt van stappen die een voertuig kan doen. Zo wordt verticaal of horizontaal bewegen gezien als een stap, ongeacht de hoeveelheid hokjes die het voertuig verplaatst over het speelbord.
### Random
In het random algoritme wordt er telkens een willekeurig gekozen stap gezet totdat de rode auto voor de uitgang staat.
### Breadth First Search
Bij Breadth First Search maken we een graaf aan, waar de wortel (beginknoop) van de graaf het startbord is van het spel. Vanuit iedere knoop worden kinderen aangemaakt aan de hand van de verschillende stappen die gezet kunnen worden. Vervolgens wordt voor elk van de kinderen gekeken of de oplossing is gevonden. Het algortime gaat door totdat de oplossing is gevonden, dit is tevens altijd de kortste oplossing.
### Depth First Search
Bij Depth First Search maken we een graaf aan, waar de wortel (beginknoop) van de graaf het startbord is van het spel. Hierbij worden eerst de kinderen aangemaakt aan de hand van de verschillende stappen die gezet kunnen worden. Vervolgens wordt er willekeurig een van deze kinderen gekozen. Hiermee wordt dus een tak gekozen en vervolgens wordt er in deze tak zo ver mogelijk doorgezocht totdat de oplossing is gevonden. Wanneer een van de kinderen een bord is wat eerder is tegenkomen, wordt de tak gepruned.
### Best Depth First Search
Het Best Depth First Search algoritme borduurt voort op het Depth First Search algoritme. Echter wordt er niet willekeurig een van de kinderen gekozen, maar op zo'n manier dat er rekening wordt gehouden met de plek van de rode auto en de hoeveelheid voertuigen die de uitgang blokkeren. 
### Hill Climber
Het Hill Climber algoritme kan gebruikt worden om een kortere oplossing te vinden. Door over een oplossing heen te itereren worden er telkens twee willekeurige borden binnen de oplossing gekozen. Vervolgens wordt er geprobeerd een nieuw, korter pad te vinden, zodat de uiteindelijke oplossing wordt verkleind. Dit algoritme kan toegepast worden op iedere gevonden oplossing en kan verbeterd worden met random, Breadth First Search, Depth First Search en Best Depth First Search. 
### Restart Hill Climber
Het Restart Hill Climber 

<!-- Kies een random start state
Herhaal tot na N-keer niet meer verbetert:
Doe een kleine random aanpassing
Als de state is verslechterd:
Maak de aanpassing ongedaan -->
### Simulated Annealing
In tegenstelling tot het Hill Climber algoritme, waar iedere oplossing die kleiner is dan de vorige geaccepteerd wordt, worden er bij Simulated Annealing ook slechtere oplossingen geaccepteerd aan de hand van een temperatuur. De temperatuur neemt af naarmate het aantal iteraties oploopt, waardoor de acceptatiekans wordt verkleind.

## Structuur
De volgende lijst toont de belangrijkste mappen en files in dit project en waar je ze kunt vinden:
- **/code**: bevat alle code van dit project
    - **/code/algorithms**: bevat de code voor alle algoritmen
      - **/code/algorithms/base_algorithms**: bevat de basis code die voor meerdere algoritmen gebruikt wordt
    - **/code/classes**: bevat de drie verschillende classes voor de case
    - **/code/functions**: bevat de functies om main te runnen
- **/game_boards**: bevat de verschillende speelborden

## Auteurs
- Jesse Fontaine
- Annemarie Geertsema
- Laura Haverkorn
