
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'Job9'
    players_per_group = None
    num_rounds = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    typeracer = models.LongStringField(blank=True)
    this_round_point = models.FloatField(initial=0)
    random_num = models.IntegerField(initial=0)
    declare = models.FloatField(min=0)
    fine = models.FloatField(initial=0)
    not_deklarert = models.FloatField(initial=0)
    score_after_taxes = models.FloatField()
    got_audited_score = models.FloatField(initial=0)
    not_audited_score = models.FloatField()
    eq1 = models.IntegerField(label='21-12 =')
    eq2 = models.IntegerField(label='43-15 = ')
    eq3 = models.IntegerField(label='76-20  =')
    eq4 = models.IntegerField(label='90-45 = ')
    eq5 = models.IntegerField(label='22-11 = ')
    eq6 = models.IntegerField(label='61-26 =')
    eq7 = models.IntegerField(label='53-15 =')
    eq8 = models.IntegerField(label='38-22 =')
    eq9 = models.IntegerField(label='15*3 =')
    eq10 = models.IntegerField(label='33 + 36 =')
    def declare_max(self):
        return self.this_round_point
    def posibility(self):
        import random
        self.random_num = random.randint(1,100)