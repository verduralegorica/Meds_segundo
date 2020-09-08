
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
import itertools
import json

doc = ''


class Constants(BaseConstants):
    """
    Description:
        Inherits oTree Class BaseConstants. Defines constants for
        the experiment these will remain unchanged
    """

    players_per_group = None
    num_rounds = 1
    timer = 20
    payment_per_answer = c(0.2)


    instructions_template = 'meds_segundo/InstruccionesB.html'
    instructions_button = "meds_segundo/Instructions_Button.html"
    contact_template = "meds_segundo/Contactenos.html"

    name_in_url = 'pxe_otr_med2'  # name in webbrowser




class Subsession(BaseSubsession):

    def creating_session(self):

        from .pages import initial_page_sequence
        ini = [i.__name__ for i in initial_page_sequence]
        for p in self.get_players():
            pb = ini.copy()
            random.shuffle(pb)
            p.page_sequence = json.dumps(pb)

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    # Para el pay-off del sistema
    def set_payoffs(self):
        p.payoff = self.player.quiz_earnings


    # Elecciones
    p1 = models.IntegerField(choices=[[0, 'Ninguna'], [1, 'Ibuprofeno'], [2, 'Daloflax']], label='Imagina que te da una inflamación de amígdalas que te produce dolor y fiebre; y, por tanto, decides consultar con un médico. Este te dice que es porque tienes síntomas de gripe y para contrarrestarlos podrías tomar algún medicamento. Dada la información indicada debajo (la cual representa el costo por cada pastilla), ¿cuál elegirías?', widget=widgets.RadioSelect)
    p2 = models.IntegerField(choices=[[0, 'Ninguna'], [1, 'Amoxicilina'], [2, 'Valimax']], label='Imagina que tienes problemas gastrointestinales; por lo que decides consultar con un médico. Este te dice que, para contrarrestarlos, podrías tomar algún medicamento. Dada la información indicada debajo,  ¿cuál elegirías? (solo una toma, es decir, una pastilla/cápsula)', widget=widgets.RadioSelect)
    p31 = models.IntegerField(choices=[[0, 'Ninguna'], [1, 'Loratadina'], [2, 'Alataran']], label='Imagina que presentas síntomas de alergia, por lo que decides consultar con un médico. Este te dice que, para contrarrestarlos, podrías tomar un medicamento. ¿Cuál elegirías? (solo una toma, es decir, una pastilla/cápsula)', widget=widgets.RadioSelect)
    p32 = models.FloatField(label='¿Cuánto pagarías por cada pastilla del medicamento escogido? (solo una toma, es decir, una pastilla/cápsula). Si has marcado "Ninguna" en la pregunta anterior, coloca 0', min=0)
    p41 = models.IntegerField(choices=[[0, 'Ninguna'], [1, 'Dexametasona'], [2, 'Valafax']], label='Imagina que presentas síntomas fuertes del COVID-19, como fiebres altas, por lo que decides consultar con un médico. Este te dice que podrías tomar un medicamento. ¿Cuál elegirías?', widget=widgets.RadioSelect)
    p42 = models.FloatField(label='¿Cuánto pagarías por cada pastilla del medicamento escogido? (solo una toma, es decir, una pastilla/cápsula). Si has marcado "Ninguna" en la pregunta anterior, coloca 0', min=0)

    # Para la secuencia de páginas
    page_sequence = models.StringField()

