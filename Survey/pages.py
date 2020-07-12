
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Information_about_game(Page):
    form_model = 'player'
class Understanding_quiz(Page):
    form_model = 'player'
    form_fields = ['s1', 's2', 's3', 's4']
    def app_after_this_page(self, upcoming_apps):
        if self.player.s1 == 'svar2' and self.player.s2 == '1' and self.player.s3 == "v3" and self.player.s4 == "yes":
            return upcoming_apps[0]
page_sequence = [Information_about_game, Understanding_quiz]