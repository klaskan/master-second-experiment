
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
        my_string = "471 24 88 857 503 11 937 21 81 518 97 327 652 913 82 502 981 25 971 68 303 44 679 69 88 119 843 862 415 307 187 38 10 210 22 724 604 756 23 34 691 756 58 102 173 179 189 421 46 892 881 292 79 96 36 94 593 643 128 703 54"
        my_list = my_string.split(" ")
        list_user_data = user_input.split(" ")
        #Antall poeng
        self.player.this_round_point = len(set(list_user_data).intersection(my_list))
        
        #Make random number
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
        if self.player.random_num <= 5 and self.player.declare != self.player.this_round_point:
            self.player.payoff = (self.player.this_round_point * 0.6) - ((self.player.this_round_point - self.player.declare )*2)
            return True
        else:
            self.player.payoff =  (self.player.declare * 0.6) + (self.player.this_round_point -self.player.declare)
            return False
class Show_stats(Page):
    form_model = 'player'
page_sequence = [Intro, NumberRacer, Deklarer_poeng, Got_Audited, Show_stats]