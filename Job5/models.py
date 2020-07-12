
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'Job5'
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
    numbers = models.LongStringField(blank=True)
    def declare_max(self):
        return self.this_round_point
    def posibility(self):
        import random
        self.random_num = random.randint(1,100)