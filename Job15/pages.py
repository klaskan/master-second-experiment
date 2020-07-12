
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
    form_model = 'player'
class NumberRacer(Page):
    form_model = 'player'
    form_fields = ['numbers']
    timeout_seconds = 30
    def before_next_page(self):
        #Hvor mange ord spilleren klarer å skrive
        user_input = self.player.numbers
        #Teksten som spiller skal matche
        #Gjør user_input om til listeform
        my_string = "596 11 907 96 24 879 49 349 27 281 426 44 129 387 86 94 831 63 759 32 561 21 66 566 594 834 12 80 27 190 521 24 13 56 404 112 95 544 23 267 762 448 87 47 201 855 43 696 94 67 925 44 91 31 135 318 49 202 51 38"
        my_list = my_string.split(" ")
        list_user_data = user_input.split(" ")
        #Antall poeng
        self.player.this_round_point = len(set(list_user_data).intersection(my_list))
        
        #Generate random number
        self.player.posibility()
        
class Deklarer_poeng(Page):
    form_model = 'player'
    form_fields = ['declare']
    def before_next_page(self):
        #Regn ut skatt
        mengde_ikke_deklarert = self.player.this_round_point - self.player.declare
        self.player.score_after_taxes = self.player.this_round_point * 0.6
        
        #størrelse fine
        self.player.fine = mengde_ikke_deklarert * 2 #Det man ikke deklarerer betaler man straff på
        
        #Score (Got audited)
        self.player.got_audited_score = (self.player.this_round_point * 0.6) - ((self.player.this_round_point - self.player.declare )*2)
        #Score (Did not get audited)
        self.player.not_audited_score = (self.player.declare * 0.6) + self.player.not_deklarert
        
class Got_Audited(Page):
    form_model = 'player'
    def is_displayed(self):
        
        if self.player.random_num <= 40 and self.player.declare != self.player.this_round_point:
            self.player.payoff = (self.player.this_round_point * 0.6) - ((self.player.this_round_point - self.player.declare )*2)
            return True
        else:
            self.player.payoff = (self.player.declare * 0.6) + (self.player.this_round_point -self.player.declare)
            return False
class Show_stats(Page):
    form_model = 'player'
page_sequence = [Intro, NumberRacer, Deklarer_poeng, Got_Audited, Show_stats]