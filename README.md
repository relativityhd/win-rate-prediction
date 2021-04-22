# win-rate-prediction

Data Exploration Project

## Local Setup

Es gibt zwei Jupyter Notebooks, das Erste: `data_cleaning` im `data` Ordner und das Zweite: `model_assembly` im `model` Ordner. Die Ordner `app` und `frontend` sind für das Userinterface notwendig. In `app` befindet sich ein Fast-Api Server und in `frontend` ein VueJS-Frontend. Das Frontend baut einen Staticfile Ordner nach `app` welchen dann vom Fast-API Server genutzt wird. Diesen kann man local starten mit:

```sh
uvicorn main:app --reload
```

oder alternativ mit Docker:

```sh
docker build -t data-exploration .
docker run -d -p 80:80 data-exploration
```

## Projekt

In diesem Projekt soll anhand von gecleanten Spielerdaten der letzten vier Seasons und einem neuronalen Netz, die Win Rate vorhergesagt werden.
Die Daten sind aus dem Spiel League of Legends (LoL).

League of Legends ist ein teambasiertes Strategiespiel, in dem zwei Teams mit je fünf so genannten Champions gegeneinander antreten, um die jeweils andere Basis zu zerstören. Man hat die Wahl aus über 140 Champions, welche alle unterschiedliche Fähigkeiten aufweisen.
Der Nexus ist das Herzstück der Basis beider Teams. Das erste Team, das den gegnerischen Nexus zerstört gewinnt. Da dies vom gegnerischen Team verhindert wird, müssen deren Champions getötet werden um den Nexus, und die Verteidigungstürme die diesen beschützen, zu zerstören. Um die Oberhand über die gegnerischen Champions zu gewinnen, können Items mit Gold gekauft werden.
Um Gold zu erhöten können gegnerische Creeps und Champions getötet werden, kann bei einem Kill geholfen werden oder Verteidigungsgebäude zerstört werden.
Mit diesen Mechanismen können ebenfalls Erfahrungspunkte gesammelt werden. Wenn Champions eine bestimmte Menge Erfahrung gewonnen haben, steigen sie eine Stufe auf und können Fähigkeiten freischalten oder verbessern und damit ihre Werte erhöhen.
League of Legends besitzt mitlerweile eine große, internationale Esport-Szene und somit besteht auch ein Bedarf an Analysen, ähnlich wie im Fußball, Basketball oder anderen Sportarten.

### Data Management

Als Daten für unser Projekt wurden die Daten der letzten vier Seasons von LoL ausgewählt und für die Weiterverarbeitung, durch die Bereinigung und erneute Formatierung von den Datensätzen, vorbereitet. Dadurch wird sichergestellt, dass alle für die Analyse verwendeten Daten von hoher Qualität sind.
Der Datenaufbereitungsprozess beginnt mit der Identifizierung der benötigten Daten. Ein wichtiger Schritt nach der Datenerfassung ist die Ermittlung aller Datensätze. Dies dient dazu, die Daten zu verstehen und festzustellen, welche Maßnahmen nötig sind, um die Daten für einen bestimmten Zusammenhang nützlich zu machen.

Die Datenbereinigung ist oft der zeitaufwendigste Teil des Datenaufbereitungsprozesses, aber dennoch extrem wichtig, um fehlerhafte Daten zu entfernen und Lücken zu schließen. Wichtige Aufgaben sind hier u. a.:

- Entfernung von irrelevanten Daten und Ausreißern
- Hinzufügen fehlender Werte
- Anpassung der Daten an ein standardisiertes Muster

Nach dieser Aufbereitung war es uns möglich mit diesen Daten weiterzuarbeiten und uns an das neuronale Netz zu setzen. Denn dieses kann nur qualitativ gut gelingen wenn die Daten dafür gut aufbereitet wurden.

### Model Assembly

Künstliche Neuronale Netze (KNN) sind dem menschlichen Gehirn nachempfunden und werden für maschinelles Lernen und künstliche Intelligenz eingesetzt. Computerbasiert lassen sich damit diverse Problemstellungen lösen, die für uns Menschen fast unmöglich wären bzw. sehr rechenaufwendig.

#### Künstliches Neuronales Netzwerk

Künstliche Neuronale Netze sind Netze aus künstlichen Neuronen, die dem menschlichen Gehirn nachempfunden sind. Dieses abstrahierte Modell von verbundenen künstlichen Neuronen ermöglicht es, komplexe Aufgaben aus den Bereichen Statistik, Informatik und Wirtschaft durch Computer zu lösen.

Durch Neuronale Netze lassen sich in unserem Beispiel Tabellen interpretieren und Informationen oder Muster extrahieren, um diese auf unbekannte oder neue Daten anzuwenden. So lassen sich datengetrieben Vorhersagen für die Zukunft erstellen. In unserem Beispiel soll somit die Win Rate vorhergesagt werden.

#### Aufbau eines künstlichen neuronalen Netzes

Vereinfacht kann man sich den Aufbau eines KNN folgendermaßen vorstellen: Das Modell des neuronalen Netzes besteht aus Knoten, auch Neuronen genannt, die Informationen von anderen Neuronen oder von außen aufnehmen, modifizieren und als Ergebnis ausgeben. Dies erfolgt über drei verschiedene Schichten, denen jeweils eine Art Neuronen zugeordnet werden kann: solche für den Input (Eingabeschicht), für den Output (Ausgabeschicht) und die sogenannten Hidden-Neuronen (verborgene Schichten).

Die Information wird durch die Input-Neuronen aufgenommen und durch die Output-Neuronen ausgegeben. Die Hidden-Neuronen liegen dazwischen und bilden innere Informationsmuster ab. Die Neuronen sind miteinander über sogenannte Kanten verbunden. Je stärker die Verbindung ist, desto größer die Einflussnahme auf das andere Neuron:

- Eingabeschicht: Die Eingangsschicht versorgt das neuronale Netz mit den notwendigen Informationen. Die Input-Neuronen verarbeiten die eingegebenen Daten und führen diese gewichtet an die nächste Schicht weiter.
- Verborgene Schicht: Die verborgene Schicht befindet sich zwischen der Eingabeschicht und der Ausgabeschicht. Während die Ein- und Ausgabeschicht lediglich aus einer Ebene bestehen, können beliebig viele Ebenen an Neuronen in der verborgenen Schicht vorhanden sein. Hier werden die empfangenen Informationen erneut gewichtet und von Neuron zu Neuron bis zur Ausgabeschicht weitergereicht. Die Gewichtung findet in jeder Ebene der verborgenen Schicht statt. Die genaue Prozessierung der Informationen ist jedoch nicht sichtbar. Daher stammt auch der Name, verborgene Schicht.
- Ausgabeschicht: Die Ausgabeschicht ist die letzte Schicht und schließt unmittelbar an die letzte Ebene der verborgenen Schicht an. Die Output-Neuronen beinhalten die resultierende Entscheidung, die als Informationsfluss hervorgeht.

![img](https://media.springernature.com/lw1000/springer-cms/rest/v1/img/17663890/v4/4by3?as=jpg)

Quelle:<https://www.springerprofessional.de/neuronale-netze/kuenstliche-intelligenz/wie-funktionieren-kuenstliche-neuronale-netze-/17663746>

Quellen:
<https://datasolut.com/neuronale-netzwerke-einfuehrung/>
<https://www.talend.com/de/resources/what-is-data-preparation/>
<https://gol.gg/players/list/season-S11/split-Spring/tournament-ALL/>
<https://euw.leagueoflegends.com/de-de/how-to-play/>
