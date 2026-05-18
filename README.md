# EvaluationSMA
Evaluation de fin de module SMA
# LangChain RAG Multi-Agent Project

## Description du projet

Ce projet implémente un système de Retrieval-Augmented Generation (RAG) basé sur LangChain et Ollama afin de planifier un voyage de N jours à une destination précise.

Le système permet :
- d’interroger des documents (PDF / TXT)
- d’utiliser un retriever basé sur FAISS
- de générer des réponses intelligentes avec un LLM local (Ollama)
- d’organiser le workflow avec des agents (Supervisor / Researcher / generator)

---

## Architecture

- **Supervisor** : orchestre le workflow et choisit les agents
- **Researcher** : récupère les informations via le retriever (FAISS)
- **generator** : génère du code ou des réponses techniques
- **Retriever** : recherche les documents pertinents dans la base vectorielle
- **Vector DB (FAISS)** : stockage des embeddings

---

## Tech Stack

- LangChain
- LangGraph
- FAISS (Vector Database)
- HuggingFace Embeddings
- Ollama (LLM local)
- Python 3.12
- uv (dependency manager)

---

## Installation

```bash
git clone https://github.com/jihane1107/EvaluationSMA.git
cd EvaluationSMA.git

uv venv
uv sync

## Test

    Pose ta question : quel est le meilleur plan de voyage à Milan en 3jours?
    Bonjour ! Voici mon plan de réponse basé sur les informations organisées :

    **Curieux Voyageurs**

    Marion : "J'aime Milan pas seulement pour sa beauté, mais aussi pour sa proximité avec le Lac de Côme ou encore Bergame ! Parfait pour les amoureux de la nature et de la ville !".

    Max : "Ma période préférée à Milan ? Noël ! Il y a une telle féerie avec les marchés de noël, le sapin de noël de la Galerie Vittorio Emmanuele ou encore celui de la Place du Duomo !".

    Iris : "Si je devais donner 3 bonnes raisons de visiter Milan, je dirais pour les musées, l'architecture et la gastronomie ! La ville parfaite le temps d'un weekend !".

    Hannah : "Si vous avez l'occasion de visiter Milan au moment de la Fashion Week, ne manquez pas la Rue Montenapoleone ou quelques stars du podium s'y promènent ! A cette période, les expos de grands couturiers et de jeunes créateurs se multiplient à travers la ville, on peut y faire de belles découvertes ! J'ai fait l'exposition Vogue Jeunes Talents, c'était génial !".

    Sophie : "Si je devais donner 3 bonnes raisons de visiter Milan, je dirais pour les musées, l'architecture et la gastronomie ! La ville parfaite le temps d'un weekend !".

    **PRATIQUE**

    * 5 apéritivos à tester à Milan :
            1. N'Ombra de Vin (2 Via San Marco)
            2. Il Salumaio di Montenapoleone (5 Via Gesù)
            3. Lubar (Via Palestro 16)
            4. Ceresio 7 (7 Via Ceresio)
            5. Otto (8 Via Paolo Sarpi)
    * 5 librairies coups de cœur :
            1. SPAZIO BK (20 Via Luigi Porro Lambertenghi)
            2. VERSO (40 corso di Porto Ticinese)
            3. CORRAINI 121 (Via Savona 17/5)
            4. 5 ROSSO (Via Alfredo Albertini 6)
            5. LIBRERIA. DEL MONDO OFFESO (Piazza S. Simpliciano 7)

    **ITINERAIRE ET BUDGET**

    * Itinéraire de 3 jours à Milan :
            JOUR 1 : Arrivée à Milan à 6h via le train de nuit Thello, dépôt des bagages à l'hôtel "The Street Milano Duomo" puis balade dans la galerie Vittorio Emmanuele ainsi que sur la place du Duomo.
            JOUR 2 : Petit café dans la pâtisserie historique Marchesi 1825 situé dans la galerie Vittorio Emmanuele afin de profiter des illuminations et du sapin. Visite du musée novecento sur la place du Duomo. Balade sur la Piazza della Scala pour observer les trams d'époque puis visite du théâtre della Scala.
            JOUR 3 : Petit déjeuner sur le pouce chez Luini. Ascension du Duomo à pied et visite de la cathédrale. Déjeuner chez Signorvino. Glace chez Cioccolati Italiani. Après-midi dans le quartier de Navigli et de son marché vintage.
    * Budget pour 3 jours à Milan :
            TRANSPORTS : Aller-retour Paris-Milan avec Thello (à partir de 58€ en couchette 6 personnes) ; pass transports 3 jours à Milan (12€).
            LOGEMENT : 2 nuits dans le train (inclus dans le transport) ; 2 nuits chez The Street Milano Duomo (410€ - vous pouvez trouver un hôtel beaucoup moins cher à Milan, nous avons fait le choix d'être en hyper-centre pour ce séjour !).
            ACTIVITES : Musée Novecento (5€) ; entrée Théâtre della Scala (9€) ; Rooftop du Duomo (13€).

    **MILAN**

    * 15
    * MILAN14
    * Quelles sont les raisons de voyager en train jusqu'à Milan ?
            1. C'est une alternative écologique au transport aérien.
            2. C'est pratique et économique aussi bien famille, en couple ou entre amis !
            3. Thello est pet-friendly !

    **Se déplacer à Milan**

    * La ville de Milan est très bien desservie en transports en commun, inutile de louer une voiture ! Tout est accessible soit en tram, en bus ou en métro.
    * Sinon, le ticket à l'unité coûte 1.5€. Plus d'informations sur atm.it.
    * Autre moyen de transport répandu : le vélo ! Ils sont en libre-service un peu partout dans la ville, BikeMi, l'équivalent de Vélib !
    * Finalement, le meilleur moyen de découvrir Milan et ses petites ruelles secrètes, c'est la marche !

    **Visiter Milan en fin d'année**

    * Entre le dernier weekend de novembre et début janvier, l'esprit de noël se fait sentir à travers la capitale économique italienne !
    * A partir de novembre, vous pourrez découvrir le superbe sapin Swarovski illuminé dans la Galerie Vittorio Emmanuelle ! Il y a également la foire de noël " Oh Bej Oh Bej" à Sant'Ambrogio, le sapin et le marché de noël de la place du Duomo, les illuminations à Navigli ainsi que la patinoire sur la Piazza Gae Aulenti.
    * Vous pouvez également admirer les belles illuminations Via Montenapoleone, chez les plus grands couturiers.

