from quiz import  Joueur, quiz_add, read_quiz_file
from modulegraph import windows

# Création d'une instance de Joueur









jou1 = Joueur(nom="Player1",sco_re=0)

wi = windows(name="joan", joueur=jou1)

print(f"joueur  {jou1.score}")

