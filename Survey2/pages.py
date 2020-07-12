
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'pay_taxes', 'occupation', 'country']
class RiskPreference(Page):
    form_model = 'player'
    form_fields = ['number1', 'number2', 'number3', 'number4', 'number5', 'number6', 'number7', 'number8', 'number9']
    def before_next_page(self):
        self.player.generate_string()
        
class CodePage(Page):
    form_model = 'player'
page_sequence = [Demographics, RiskPreference, CodePage]