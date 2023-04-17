<img src="annexes/esilv_logo.png" alt="drawing" width="50"/> 

# Projet hackathon

## Introduction au projet

__Participants :__ 

Théophile RABUT / __theofow__ 

Tahir Aboukhassib / __tahirabou__

Geoffrey Aubrée / __Glyx__
 
Matisse Marchand / __matisse08__



### Approche du projet

Notre projet consiste en la création d'une simulation de robots autonomes en utilisant le language __python__. Ce language est très utile pour la manipulation de données.

Dans le cadre de notre projet, nous allons nous servir de ce language afin de concevoir une simulation de robots aux déplacements autonomes et intrinsèquement aléatoire du fait de leur mission : récolter des ressources.


### Robots
Chaque agent a pour mission de récolter des ressources et de les ramener à sa station. Il dispose d'une batterie limitée ainsi qu'un espace de stockage limité. Il revient donc à sa station lorsque son stockage est plein ou que sa batterie est presque vide.

Voici quelques information qui résument très bien le comportement des robots :
- Un robot emprunte toujours le chemin le plus optimal vers son target
- Un robot cible en priorité les ressources proches
- Un robot rentre immédiatement en station quand sa batterie ou son stockage ne lui permet pas de continuer sa mission

### Ressources

Les données concernant les ressources sont :
- Leur position
- Leur valeur
- Leur volume
- Leur ID

Classement des ressources de la moins chère à la plus chère : 

__Pierre < Bois < Eau < Or.__

>Liste des ressources:
>
>ID: 001 - Pierre | **1pt**
>
>ID: 002 - Bois | **2pts**
>
>ID: 003 - Eau | **3pts**
>
>ID: 004 - Or | **5pts**

Chaque ressource apparait aléatoirement, ce qui crée donc un comportement aléatoire chez les robots qui vont cibler les ressources à portée.


## Fonctionnement

Lors du lancement du programme, les robots partent de leur station en quête de ressources à récupérer. Une fois plein, ou déchargé, chaque robot ira à sa station et ajoutera donc du score à son nom. Le premier agent qui atteint le score max met fin à la simulation.

## Précisions 

Voici quelques précisions à prendre en compte dans le cadre de ce projet :

>- Notre groupe travaille sous __VSCODE__ uniquement.
>- Le projet utilise les _bibliothèques python_ __random__ et __pygame__

# Mise en place de l'environnement

Dans un premier temps, il est nécessaire de mettre en place l'environnement dans lequel nous allons travailler.

## Installation de <img src="annexes/git_logo.png" alt="drawing" width="50"/>


- Télécharger git 

L'installation peut s'effectuer sur internet via [ce lien](https://git-scm.com/downloads).

<img src="annexes/screen_git.png" alt="drawing" width="500"/> 

Une fois le téléchargement terminé, procéder à l'installation.

- Initialiser Git sur VSCode

Pour commencer, il faut cloner le repository github sur l'ordinateur utilisé.

<img src="annexes/screen_vscode.png" alt="drawing" width="500"/> 

Entrez la clé __HTTP__ du repository.


## Installation de <img src="annexes/pygame_logo.png" alt="drawing" width="70"/>

- Intaller pygame sur vscode

`pip install pygame`

<img src="annexes/screen_install_pygame.png" alt="drawing" width="500"/> 

- Utiliser Pygame

Pour utiliser des fonctions de pygame il suffit d'utiliser `import pygame`.

Cependant il faut noter qu'il sera parfois nécéssaire d'intégrer d'autres fonctions plus spécifiques.

La documentation est accessible [ici](https://www.pygame.org/docs/) pour plus de précisions.


# Lancer le projet

Pour lancer le projet, utiliser `main.py` uniquement.