
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
    form_model = 'player'
class Equations(Page):
    form_model = 'player'
    form_fields = ['eq1', 'eq2', 'eq3', 'eq4', 'eq5', 'eq6', 'eq7', 'eq8', 'eq9', 'eq10']
    timeout_seconds = 30
    def before_next_page(self):
        #Generate random number
        self.player.posibility()
        
        if self.player.eq1 == 9:
            #Hvor mye poeng man får for å ha rett
            self.player.this_round_point = self.player.this_round_point + 3
            
        if self.player.eq2 == 28:
            self.player.this_round_point = self.player.this_round_point + 3
            
        if self.player.eq3 == 56:
            self.player.this_round_point = self.player.this_round_point + 3
            
        if self.player.eq4 == 45:
            self.player.this_round_point = self.player.this_round_point + 3
            
        if self.player.eq5 == 11:
            self.player.this_round_point = self.player.this_round_point + 3
            
        if self.player.eq6 == 35:
            self.player.this_round_point = self.player.this_round_point + 3
            
        if self.player.eq7 == 38:
            self.player.this_round_point = self.player.this_round_point + 3
            
        if self.player.eq8 == 16:
            self.player.this_round_point = self.player.this_round_point + 3
            
        if self.player.eq9 == 45:
            self.player.this_round_point = self.player.this_round_point + 3
            
        if self.player.eq10 == 69:
            self.player.this_round_point = self.player.this_round_point + 3
        
        
        ###self.participant.vars['player_point'] = self.participant.vars['player_point'] + self.player.this_round_point 
        #self.player.points_earned = self.participant.vars['player_point']
            
        
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
        
        if self.player.random_num <= 20 and self.player.declare != self.player.this_round_point:
            self.player.payoff = (self.player.this_round_point * 0.6) - ((self.player.this_round_point - self.player.declare )*2)
            return True
        else:
            self.player.payoff = (self.player.declare * 0.6) + (self.player.this_round_point -self.player.declare)
            return False
class Show_stats(Page):
    form_model = 'player'
page_sequence = [Intro, Equations, Deklarer_poeng, Got_Audited, Show_stats]