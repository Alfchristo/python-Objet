class Theatre:

    def __init__(self, nom, capaciter_max, inscrits_totale, recette_totale):
        self.nom = nom
        self.capaciter_max = capaciter_max
        self.inscrits_totale = inscrits_totale
        self.recette_totale = recette_totale

    @classmethod
    def inscrire(cls, nb_clients, prix_place):
        if cls.inscrits_totale + nb_clients <= cls.capaciter_max:
            cls.inscrits_totale += nb_clients
            cls.recette_totale += nb_clients * prix_place
        else:
            print("Attention, capacité maximale atteinte")


# Mise en Oeuvre:
theatre = Theatre("Opéra Comédie", 1200, 0, 0)

theatre.inscrire(350, 20.40)
print("Situation actuel :", theatre.inscrits_totale)

