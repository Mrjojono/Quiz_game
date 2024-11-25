import random
import json
from operator import index
### modification importante apporter a la fonction quizadd de sorte a l'utiliser dans le modulegraph.
import requests


##################################################################
def read_quiz_file():
    data_list = []
    # Ouvrir le fichier en mode lecture
    with open("quiz.txt", "r") as fichier:
        # Lire chaque ligne du fichier
        for ligne in fichier:
            # Convertir chaque ligne JSON en dictionnaire
            data = json.loads(ligne.strip())  # strip() pour enlever le saut de ligne
            print(data)
            #  stockage  des données dans une liste

            data_list.append(data)

    return data_list
##################################################################


##======================================================================================================================##
def quiz_add(q, c_1, c_2, c_3, c_4, cor_t):
    data = {}

    question = q
    choix = []
    choix.append(c_1)
    choix.append(c_2)
    choix.append(c_3)
    choix.append(c_4)

    correct = cor_t
    data = {
        "correct_answer": correct,
        "incorrect_answers": choix,
        "question": question,
    }
    ##########################################
    ##ecriture des quiz dans un fichier json##
    with open("quiz.txt", "a") as fichier:
        fichier.write(json.dumps(data) + "\n")
    print("Dictionnaires avec identifiants enregistrés.")
    print(data)

    return data


##======================================================================================================================##

class Joueur:
    score = 0

    def __init__(self, nom, sco_re):
        self.nom = nom
        self.score = sco_re

    ## fonction d'ajout du quiz
    #     def quiz_add(self,q,c1,c2,c3,c4,n):
    #
    #         while True:
    #            # question = input("Entrer votre question: ")
    #             question = q
    #             try:
    #                 q != "  "
    # ## n = int(input("Entrer le nombre de choix: "))
    #             except ValueError:
    #                 choix = []
    #
    #                 #print("Veuillez entrer un chiffre.")
    #                 # n = int(input("Entrer le nombre de choix: "))
    #
    #
    #                 #choix.append(input(f"Entrer un choix de réponse numéro {i + 1}: "))
    #                 choix.append(c1)
    #                 choix.append(c2)
    #                 choix.append(c3)
    #                 choix.append(c4)
    #
    #             correct = input("entrer la reponse correct:")
    #             data = {
    #                 "correct" : correct,
    #                 "question": question,
    #                 "choix": choix
    #             }
    #             quiz = []
    #
    #             quiz.append(data)
    #
    #             # if input("Voulez-vous ajouter une autre question ? (O/N): ").upper() != "O":
    #             #     print("choisir les bonnes reponses: ")
    #             #     for i in range(len(data["choix"])):
    #             #         print(f"{i}: {choix[i]}  \n")
    #             # else:
    #             #     break

    ## fonction qui recupere le quiz en ligne
    def getquiz(self, amount, category, difficulty):

        url = f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type=multiple"

        responses = requests.get(url)

        if responses.status_code == 200:

            posts = responses.json()
            return posts['results']
        else:
            print("Failed to retrieve data")
            return []

    ## fonction our verifier le ui

    def onlinequiz(self, questions):
        for i, j in enumerate(questions):
            print(f" \nquestion {i + 1}: {j['question']} ")

            choice = [j['correct_answer']] + j['incorrect_answers']
            random.shuffle(choice)

            correct = j['correct_answer']

            for k, l in enumerate(choice):
                print(f" {k}: {l} ")

            # Prompt the user after displaying all options
            try:
                user_choice = int(input("entrer votre choix: "))
            except IndexError:
                user_choice = int(input("entrer votre choix !"))

            # Check if the chosen option is correct
            if choice[user_choice] == correct:
                print("correct!")
                self.score += 1
                print(f" votre score actuelle est :{self.score} \n")
            else:
                print("mauvaise reponse")
                print(f"votre score actuelle est: {self.score}")

            def setScore(self, s):
                self.score = s




    def update_score(self, points):
        self.score += points



