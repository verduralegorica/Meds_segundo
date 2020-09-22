
from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants, Player, Group

import json

class Eleccion0(Page):

    pass

class Eleccion1(Page):

    form_model = 'player'
    form_fields = ['e1', 'e1x', 'e1y']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

    def is_displayed(self):
        if self.participant.vars['MobilePhones'] is False:
            return True
        else:
            return False

class Eleccion2(Page):

    form_model = 'player'
    form_fields = ['e21', 'e21x', 'e22']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

    def is_displayed(self):
        if self.participant.vars['MobilePhones'] is False:
            return True
        else:
            return False

class Eleccion3(Page):

    form_model = 'player'
    form_fields = ['e3', 'e3x', 'e3y']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

    def is_displayed(self):
        if self.participant.vars['MobilePhones'] is False:
            return True
        else:
            return False

class Eleccion4(Page):

    form_model = 'player'
    form_fields = ['e41', 'e41x', 'e42']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

    def is_displayed(self):
        if self.participant.vars['MobilePhones'] is False:
            return True
        else:
            return False

class Eleccion5(Page):

    form_model = 'player'
    form_fields = ['e5', 'e5x', 'e5y']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

    def is_displayed(self):
        if self.participant.vars['MobilePhones'] is False:
            return True
        else:
            return False

class Eleccion6(Page):

    form_model = 'player'
    form_fields = ['e61', 'e61x', 'e62']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

    def is_displayed(self):
        if self.participant.vars['MobilePhones'] is False:
            return True
        else:
            return False

#Una secuencia definida inicialmente (que luego se aleatorizará)
initial_page_sequence = [
    Eleccion0,
    Eleccion1,
    Eleccion2,
    Eleccion3,
    Eleccion4,
    Eleccion5,
    Eleccion6
]

page_sequence = [

]

class Eleccion0(Page):

    def inner_dispatch(self):
        page_seq = int(self.__class__.__name__.split('_')[1])
        page_to_show = json.loads(self.player.page_sequence)[page_seq]
        self._is_frozen = False
        self.__class__ = globals()[page_to_show]
        return super(globals()[page_to_show], self).inner_dispatch()


for i, _ in enumerate(initial_page_sequence):
    NewClassName = "Page_{}".format(i)
    A = type(NewClassName, (Eleccion0,), {})
    locals()[NewClassName] = A
    page_sequence.append(locals()[NewClassName])

class Eleccion0(Page):
    def is_displayed(self):
            return False