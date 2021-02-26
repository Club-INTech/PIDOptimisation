# Algorithme génétique pour l'optimisation autimatique de PID

## Idéé générale

L'idéé générale consiste à écrire un algorithme génétique, capable de remplacer un humain dans la correction des coefficients PID.
On réçoit alors un échantillon "sortie (s) en fonction du temps (t)" dépendant des coefficients PID de individu (GA) concrèt.

## Plan:

* [Téchnologies](#Téchnologies)
* [Contenu](#Contenu)
* [GA](#GA)
* [Modification de GA](#Modification de GA)

## Téchnologies

Le projet est fait avec Python, en utilisant la lib random et les modules écrit à la main pour le GA.
Pour le simulateur et les tests matplotlib, scipy, numpy, linalg, unittest sont utilisées.

## Contenu

Dossier principal contient trois dossiers : GA, simulator et test, ainsi que le .tex et le pdf, expliquant la modélisation.

### GA
Dans le dossier GA se trouve l'algorithme génétique. sample_lib_utils analyse des échantillons de données et calcule le score associé.
individual_class est un individu de la population. ga_pid_const contient des constantes pour GA et le ga_pid contient algorithme lui-même.

### Simulator
Dans le dossier simulator se trouve un simulator pour tester un GA. p_t_generator est utilisé pour générer un array du temps et un
array dans le domaine de Laplace (avec des valeurs réelles). transfer est une fonction de transfert du système modélisé. modelisation_info contient
les constantes de simulation. model contient une méthode pour générer un output temporel.

### Test

Des tests, quoi

### Logger

Contient le logger utilisé pour la sauvegarde d'un étape d'évolution
Il suffit juste de définir le path vers le dossier des logs.

## GA

Testing

## Modification de GA

Adaptiveness testing