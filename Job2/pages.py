
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
    form_model = 'player'
class Questions_flag(Page):
    form_model = 'player'
    timeout_seconds = 10
class Answer_flag(Page):
    form_model = 'player'
    form_fields = ['flag1', 'flag2', 'flag3', 'flag4', 'flag5', 'flag6', 'flag7']
    timeout_seconds = 20
    def before_next_page(self):
        #Generate random number
        self.player.posibility()
        
        if self.player.flag1 == "Mexico":
            #Hvor mye poeng man får for å ha rett
            self.player.this_round_point = self.player.this_round_point + 5
            
        if self.player.flag2 == "Canada":
            self.player.this_round_point = self.player.this_round_point + 5
            
        if self.player.flag3 == "Japan":
            self.player.this_round_point = self.player.this_round_point + 5
            
        if self.player.flag4 == "The United Kingdom":
            self.player.this_round_point = self.player.this_round_point + 5
            
        if self.player.flag5 == "Australia":
            self.player.this_round_point = self.player.this_round_point + 5
            
        if self.player.flag6 == "Sweden":
            self.player.this_round_point = self.player.this_round_point + 5
            
        if self.player.flag7 == "Spain":
            self.player.this_round_point = self.player.this_round_point + 5
        
        
            
            
        #self.participant.vars['player_point'] = self.participant.vars['player_point'] + self.player.this_round_point #legger poengene man tjener til i global variabel
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
        if self.player.random_num <= 5 and self.player.declare != self.player.this_round_point:
            self.player.payoff =  (self.player.this_round_point * 0.6) - ((self.player.this_round_point - self.player.declare )*2)
            return True
        else:
            self.player.payoff = (self.player.declare * 0.6) + (self.player.this_round_point -self.player.declare)
            return False
class Show_stats(Page):
    form_model = 'player'
page_sequence = [Intro, Questions_flag, Answer_flag, Deklarer_poeng, Got_Audited, Show_stats]