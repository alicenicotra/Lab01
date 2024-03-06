class Domanda:
    def __init__(self, livello):
        self.livello = livello
        self.risposte =[]

    def append(self, risposta):
        self.risposte.append(risposta)


infile = open("domande.txt", "r")

lines = infile.readlines()



infile.close()