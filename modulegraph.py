from itertools import count

from quiz import Joueur, quiz_add, read_quiz_file
from tkinter import *


class windows:

    def __init__(self, name, joueur):

        self.name = name
        self.Joueur = joueur

        self.window = Tk()
        self.window.title("QUIZ GAME")

        self.window.minsize(width=600, height=800)
        self.window.maxsize(width=700, height=800)

        l1 = Label(self.window, text="QUIZ GAME")
        l1.pack(pady=20)

        frame = Frame(self.window, relief=GROOVE, borderwidth=2,
                      bg="dark slate gray")
        frame.pack(pady=10, padx=10, fill=BOTH, expand=True)

        # Add a label inside the frame
        label = Label(frame, text="entrer vos choix de reponse : ", font=("Arial", 14), fg="white",
                      bg="dark slate gray")
        label.pack()

        ####### la premiere fenetre

        self.v = StringVar()
        Entry(self.window, font=("Corbel", 18), bd=5, border=1, textvariable=self.v).pack()

        self.Joueur.nom = self.v.get()

        Button(self.window, text="Enter", bg='green', fg="yellow", width=30, height=5, command=self.Accueil).pack(
            pady=200)

        # Run the main loop
        self.window.mainloop()

    def game_begin(self, n):

        self.w3.withdraw()

        self.w4 = Toplevel(self.window)
        self.w4.title("QUIZ GAME")
        self.w4.minsize(width=600, height=500)
        self.w4.maxsize(width=700, height=800)

        # Create and pack the label for the new window
        Label(self.w4, text="ONLINE", font="Arial 16 bold").pack(pady=20)

        self.score_label = Label(self.w4, text=f"Score: {self.Joueur.score}", font="Arial 14", bg="dim gray")
        self.score_label.pack(pady=10)

        #######################################################################################################################################################

        #######################################################################################################################################################
        # Function to display the next question
        def display_question(i):

            try:

                self.score_label.pack()
                # Clear the canvas and any previous frames
                for widget in self.w4.winfo_children():
                    if widget not in [self.score_label]:
                        widget.destroy()

                # Create the canvas again for the question text
                canvas2 = Canvas(self.w4, width=580, height=150, bg='ivory')
                canvas2.pack(side=TOP, padx=10, pady=10)

                self.question_data = questions[i]
                self.question_text = self.question_data['question']

                choices = [self.question_data['correct_answer']] + self.question_data['incorrect_answers']

                # Display the question text on the canvas
                canvas2.create_text(290, 100, text=self.question_text, font="Arial 12 italic", fill="black", width=550)

                frame = Frame(self.w4, relief=GROOVE, borderwidth=3, bg="steel blue")
                frame.pack(pady=10, padx=10, fill=BOTH, expand=True)

                # Display the options as buttons inside the frame, using grid()
                for idx, choice in enumerate(choices):
                    # Pass 'choice' correctly by setting it as a default argument in the lambda function
                    bu1 = Button(frame, text=choice, font="Calibri", bg="steel blue",
                                 command=lambda c=choice: on_choice_selected(c, i))
                    bu1.grid(row=idx, padx=20, pady=5, sticky="ew", columnspan=1)

            except IndexError:
                print(f"Error: Question index {i} is out of range.")
            except KeyError as e:
                print(f"Error: Missing key in question data: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

            # Add the QUIT button
            Button(self.w4, text='QUIT', bg='blue', fg="yellow", width=15, height=2, command=quit).pack(side=LEFT,
                                                                                                        padx=10, pady=5)

            Button(self.w4, text='Retour', bg='blue', fg="yellow", width=15, height=2,
                   command=lambda: self.retour(self.w4, self.window)).pack(side=LEFT, padx=10, pady=10)

            #######################################################################################################################################################

            #######################################################################################################################################################
            # Handle what happens when a choice is selected
            def on_choice_selected(c, question_index):

                print(f"You selected: {c} for question {question_index + 1}")
                # Check if the answer is correct
                if c == self.question_data['correct_answer']:
                    # modification
                    self.Joueur.update_score(1)  # Update the score
                    Joueur.score += 1

                # modification
                print(f"Score updated: {Joueur.score}")
                self.score_label.config(text=f"Score: {Joueur.score}")

                if question_index + 1 < len(questions):
                    display_question(question_index + 1)  # Display next question
                else:
                    self.w4.withdraw()
                    self.w5 = Toplevel(self.window)
                    self.w5.title("QUIZ GAME")

                    # Create and pack the label for the new window
                    l1 = Label(self.w5, text="ONLINE", font="Arial 16 bold")
                    l1.pack(pady=20)

                    # Mettre le score label en global pour le modifier plus tard

                    canvas2 = Canvas(self.w5, width=580, height=150, bg='ivory')
                    canvas2.pack(side=TOP, padx=10, pady=10)
                    canvas2.create_text(290, 100,
                                        text=f" You've finished the quiz!. Score:{Joueur.score}. number of question {self.n}  ",
                                        font="Arial 12 italic",
                                        fill="black",
                                        width=550)

                    print("You've finished the quiz!")

        # Get questions from the quiz
        if n == "ONLINE":
            questions = self.Joueur.getquiz(4, 9, 'easy')
            print(f"ONLINE mode: Retrieved questions: {questions}")
        else:
            questions = read_quiz_file()
            print(f"OFFLINE mode: Loaded questions: {questions}")

        # Validate questions list before proceeding
        if not questions:
            print("No questions available. Exiting.")
            return

        # Start by displaying the first question
        display_question(0)

    #######################################################################################################################################################

    #######################################################################################################################################################
    ### version locale du quiz
    def question_number(self):

        self.w3.withdraw()

        self.w6 = Toplevel(self.window)
        self.w6.title("Enter Number of Questions")

        canvas = Canvas(self.w6, width=400, height=100, bg='ivory')
        canvas.pack(side="top", padx=10, pady=10)
        canvas.create_text(200, 50, text="Combien de question voulez-vous entrer?", font="Arial 12 italic",
                           fill="black")

        self.n = StringVar()
        entry = Entry(self.w6, font=("Calibri", 13), bd=3, textvariable=self.n, bg="lightyellow", width=20)
        entry.pack(pady=10)

        Button(self.w6, text='Continuer', bg='blue', fg="yellow", width=15, height=2,
               command=self.local_game).pack(side="right", padx=10, pady=10)

    def local_game(self):

        self.w6.destroy()
        self.w7 = Toplevel(self.window)
        self.w7.title("quiz making")

        self.w7.minsize(width=600, height=500)

        Label(self.w7, text="Local Game Making", font=("Arial", 14, "bold")).pack(pady=10)

        ## entrer des valeur
        frame_text = Frame(self.w7, relief=GROOVE, borderwidth=2)
        frame_text.pack()

        message_box = Text(frame_text, font=("Calibri", 14), bd=5, border=2, width=70, height=5, wrap="word",
                           relief=RAISED, bg="lightyellow")
        message_box.pack(pady=20)

        ### recuperer la valeur des choix :

        self.c1 = StringVar()
        self.c2 = StringVar()
        self.c3 = StringVar()
        self.c4 = StringVar()
        self.c_rt = StringVar()

        frame = Frame(self.w7, relief=GROOVE, borderwidth=2,
                      bg="dark slate gray")
        frame.pack(pady=10, padx=10, fill=BOTH, expand=True)

        # Add a label inside the frame
        label = Label(frame, text="entrer vos choix de reponse", font=("Arial", 14), fg="white", bg="dark slate gray")
        label.pack()

        frame_2 = Frame(frame, relief=GROOVE, borderwidth=2)
        frame_2.pack(side=LEFT, pady=10)

        ### champ d'entré des options de choix
        entry_1 = Entry(frame, font=("Calibri", 13), bd=3, border=2, textvariable=self.c1, width=60, bg="lightyellow")
        entry_1.pack(ipady=10, pady=10)

        entry_2 = Entry(frame, font=("Calibri", 13), bd=3, border=2, textvariable=self.c2, width=60, bg="lightyellow")
        entry_2.pack(ipady=10, pady=10)

        entry_3 = Entry(frame, font=("Calibri", 13), bd=3, border=2, textvariable=self.c3, width=60, bg="lightyellow")
        entry_3.pack(ipady=10, pady=10)

        entry_4 = Entry(frame, font=("Calibri", 13), bd=3, border=2, textvariable=self.c4, width=60, bg="lightyellow")
        entry_4.pack(ipady=10, pady=10)

        # =========================================================== correct answer imput
        frame_3 = Frame(self.w7, relief=GROOVE, borderwidth=2,
                        bg="dim gray")
        frame_3.pack(pady=10, padx=10, fill=BOTH, expand=True)

        # Add a label inside the frame
        label_1 = Label(frame_3, text="entrer la reponse correct ", font=("Arial", 14), fg="white", bg="dim gray")
        label_1.pack()

        entry_5 = Entry(frame_3, font=("Calibri", 13), bd=3, border=2, textvariable=self.c_rt, width=60)
        entry_5.pack(ipady=15, pady=5)

        # ===========================================================
        # Button(self.w7, text='afficheé', bg='blue', fg="yellow", width=15, height=2,
        #        command=lambda: print(f"la question entré est: {question} {message_box.get('1.0', 'end-1c')}")).pack(
        #     side=RIGHT, padx=10, pady=10)

        Button(self.w7, text='Ajouter ', bg='blue', fg="yellow", width=15, height=2, relief=RAISED,
               command=lambda: quiz_add(message_box.get('1.0', 'end-1c'), self.c1.get(), self.c2.get(), self.c3.get(),
                                        self.c4.get(),
                                        self.c_rt.get())).pack(
            side=RIGHT, padx=10, pady=10)

        # Add buttons  of return and continue

        Button(self.w7, text='Retour', bg='blue', fg="yellow", width=15, height=2, relief=RAISED,
               command=lambda: self.retour(self.w7, self.w3)).pack(
            side=LEFT, padx=10, pady=10)

        Button(self.w7, text='Commencer ', bg='blue', fg="yellow", width=15, height=2, relief=RAISED,
               command=lambda: self.game_begin("LOCAL")).pack(
            side=LEFT, padx=10, pady=10)

    ##button pour continuer le quiz apres avoir rentrer tous les quiz
    # Button(self.w6, text='Continuer', bg='blue', fg="yellow", width=15, height=2, command=self.f).pack(side=RIGHT,padx=10, pady=10)

    #######################################################################################################################################################

    ## fonction pour choisir l'option jeu en ligne ou creation de quiz soit meme

    def Choix(self):
        self.w2.withdraw()  # Close the first window

        # Create the second window

        self.w3 = Toplevel(self.window)
        self.w3.title("QUIZ GAME - INSTRUCTIONS")

        # Create and pack the label for the second window
        l1 = Label(self.w3, text="QUIZ GAME")
        l1.pack(pady=20)

        text = """   
        Objectif et fonctionnement du Quiz
    
    Bienvenue dans le Quiz Game ! Le but de ce quiz est de tester vos connaissances sur divers sujets, en vous amusant. Vous avez deux options :
    
    Créer votre propre quiz : Dans cette option, vous pouvez entrer vos propres questions et choix de réponses. Personnalisez le quiz selon vos envies et défiez vos amis ou vous-même avec vos questions !
    
    Faire un quiz en ligne : Cette option vous permet de participer à un quiz préexistant en ligne, 
    
    Temps limité pour chaque question.
    Choix multiples : Sélectionnez la bonne réponse parmi plusieurs options.
    Scores : Chaque bonne réponse vous rapporte des points.
    Retour : Vous pouvez revenir en arrière pour revoir les questions précédentes.
    Continuer : Passez à la question suivante ou terminez le quiz.
    Bonne chance et amusez-vous bien !
        
        """

        canvas1 = Canvas(self.w3, width=580, height=350, bg='slate gray')
        canvas1.pack(side=TOP, padx=10, pady=10)

        # Add text to the canvas
        canvas1.create_text(290, 175, text=text, font="Arial 12 italic", fill="black", width=550)

        Button(self.w3, text='ONLINE', bg='blue', fg="yellow", width=15, height=2, relief=RAISED,
               command=lambda: self.game_begin("ONLINE")).pack(side=LEFT, padx=10, pady=10)

        Button(self.w3, text='LOCAL', bg='blue', fg="yellow", width=15, height=2, command=self.question_number,
               relief=RAISED).pack(
            side=RIGHT, padx=10,
            pady=10)
        self.w3.minsize(width=600, height=500)
        self.w3.maxsize(width=700, height=800)

    ##fonction pour gerer le retour en arriere
    def retour(self, window_to_close, window_to_show):
        # Fermer la fenêtre spécifiée
        window_to_close.withdraw()
        # Afficher la fenêtre cible
        window_to_show.deiconify()

    # Function to open the second window and close the first one
    def Accueil(self):
        ##fermeture de la premier fenetre
        self.window.withdraw()

        # Create the second window
        self.w2 = Toplevel(self.window)
        self.w2.title("QUIZ GAME - INSTRUCTIONS")
        self.w2.minsize(width=600, height=500)
        self.w2.maxsize(width=700, height=800)

        # Create and pack the label for the second window
        l1 = Label(self.w2, text="QUIZ GAME")
        l1.pack(pady=20)

        # Instructions text
        cible = """Bienvenue dans le Quiz !
    
    L'objectif de ce quiz est de tester vos connaissances sur différents sujets et de vous amuser en répondant à des questions stimulantes. Vous aurez la chance de découvrir votre niveau tout en vous divertissant !
    
    Règles du quiz:
    1. Vous avez un temps limité pour répondre à chaque question.
    2. Pour chaque question, plusieurs choix de réponses vous sont proposés. Sélectionnez la réponse qui vous semble correcte.
    3. Chaque réponse correcte vous rapporte des points. À la fin du quiz, votre score total vous sera affiché.
    
    Navigation:
    - Retour : Vous pouvez revenir en arrière pour revoir les questions précédentes si vous en avez besoin. Cela vous permettra de revoir ou de modifier vos réponses.
    - Continuer : Une fois prêt, vous pouvez continuer pour passer à la question suivante ou terminer le quiz.
    
    Bonne chance et amusez-vous bien !"""

        # Create a canvas and add it to the second window
        canvas = Canvas(self.w2, width=580, height=350, bg='slate gray')
        canvas.pack(side=TOP, padx=10, pady=10)

        # Add text to the canvas
        canvas.create_text(290, 175, text=cible, font="Arial 12 italic", fill="black", width=550)

        # Add buttons to the second window
        Button(self.w2, text='Retour', bg='blue', fg="yellow", width=15, height=2, relief=RAISED,
               command=lambda: self.retour(self.w2, self.window)).pack(
            side=LEFT, padx=10, pady=10)

        Button(self.w2, text='Continuer', bg='blue', fg="yellow", width=15, height=2, command=self.Choix,
               relief=RAISED).pack(
            side=RIGHT,
            padx=10,
            pady=10)
