
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'Job2'
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
    flag1 = models.StringField(choices=[['Japan', 'Japan'], ['Sweden', 'Sweden'], ['Australia', 'Australia'], ['Canada', 'Canada'], ['The United Kingdom', 'The United Kingdom'], ['Mexico', 'Mexico'], ['Spain', 'Spain']], label='1')
    flag2 = models.StringField(choices=[['Japan', 'Japan'], ['Sweden', 'Sweden'], ['Australia', 'Australia'], ['Canada', 'Canada'], ['The United Kingdom', 'The United Kingdom'], ['Mexico', 'Mexico'], ['Spain', 'Spain']], label='2. ')
    flag3 = models.StringField(choices=[['Japan', 'Japan'], ['Sweden', 'Sweden'], ['Australia', 'Australia'], ['Canada', 'Canada'], ['The United Kingdom', 'The United Kingdom'], ['Mexico', 'Mexico'], ['Spain', 'Spain']], label='3. ')
    flag4 = models.StringField(choices=[['Japan', 'Japan'], ['Sweden', 'Sweden'], ['Australia', 'Australia'], ['Canada', 'Canada'], ['The United Kingdom', 'The United Kingdom'], ['Mexico', 'Mexico'], ['Spain', 'Spain']], label='4. ')
    flag5 = models.StringField(choices=[['Japan', 'Japan'], ['Sweden', 'Sweden'], ['Australia', 'Australia'], ['Canada', 'Canada'], ['The United Kingdom', 'The United Kingdom'], ['Mexico', 'Mexico'], ['Spain', 'Spain']], label='5.')
    flag6 = models.StringField(choices=[['Japan', 'Japan'], ['Sweden', 'Sweden'], ['Australia', 'Australia'], ['Canada', 'Canada'], ['The United Kingdom', 'The United Kingdom'], ['Mexico', 'Mexico'], ['Spain', 'Spain']], label='6. ')
    flag7 = models.StringField(choices=[['Japan', 'Japan'], ['Sweden', 'Sweden'], ['Australia', 'Australia'], ['Canada', 'Canada'], ['The United Kingdom', 'The United Kingdom'], ['Mexico', 'Mexico'], ['Spain', 'Spain']], label='7')
    def declare_max(self):
        return self.this_round_point
    def posibility(self):
        import random
        self.random_num = random.randint(1,100)