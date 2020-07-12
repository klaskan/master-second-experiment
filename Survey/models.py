
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'Survey'
    players_per_group = None
    num_rounds = 20
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    s1 = models.StringField(choices=[['svar1', 'Pay a 10 point fine. '], ['svar2', "Pay what you didn't declare and a fine of 100% of what you tried to evade."], ['svar3', "Pay back what you didn't declare."]], label='What punishment will the tax authority give you if you get caught for tax evasion? ', widget=widgets.RadioSelect)
    s2 = models.StringField(choices=[['1', "How well/fast it's done. "], ['2', 'You get paid the same regardless of how well you do it. '], ['3', 'Every job pays 10 points. ']], label='What is the deciding factor of what you get paid for doing a job?', widget=widgets.RadioSelect)
    s3 = models.StringField(choices=[['v1', '20%'], ['v2', 'It depends on how much you earn on a job.'], ['v3', '40%']], label='What is the tax rate? ', widget=widgets.RadioSelect)
    s4 = models.StringField(choices=[['yes', 'Yes.'], ['no', 'No.']], label='Will you know the possibility of getting audited?', widget=widgets.RadioSelect)