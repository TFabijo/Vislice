import random

STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "0"
NAPACNA_CRKA = "-"

ZMAGA = "W" 
PORAZ = "X"

class Igra:

    def __init__(self,geslo,crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:     
            self.crke = crke

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]
    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return all([crka in self.crke for crka in self.geslo]) #all ali so vi true obratno ay#

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
    
    def pravilni_del_gesla(self):
        s = ""
        for crka in self.geslo:
            if crka in self.crke:
                s += crka + " "
            else:
                s += "_ "
        return s
    
    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA

with open("besede.txt",encoding="UTF-8") as f:
    bazen_besed = [vrstica.strip().upper() for vrstica in f] #strip ireze vse ne znakvne znake na zacetku ali koncu#


def nova_igra():
    return Igra(random.choice(bazen_besed))










            











