
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

    name_in_url = 'experimento_de_medicamentos2'  # name in webbrowser

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
    e1 = models.IntegerField(choices=[[0, 'Ninguna'], [1, 'Loratadina'], [2, 'Alatarina']],
                             label='Imagina que presentas ciertos síntomas debido a una gripe como estornudos, secreción nasal, picazón en los ojos, nariz y garganta. Por ello, decides consultar con un médico y este te dice que, para contrarrestarlos, podrías tomar un medicamento. ¿Cuál elegirías? (solo una toma, es decir, una pastilla/cápsula)', widget=widgets.RadioSelect)
    e1x = models.IntegerField(choices=[[1, 'Porque el otro es muy barato'], [0, 'Porque el otro es muy caro'], [4, 'Me da miedo consumir genéricos'],[3, 'Los genéricos no tienen tanta eficacia'], [2, 'Confío en los genéricos']],
                             label='En caso haya marcado alguno de los dos medicamentos: ¿Por qué seleccionó esa opción? Si marcó “ninguna”, entonces dejar en blanco.',
                             widget=widgets.RadioSelect, blank=True)
    e1y = models.IntegerField(choices=[[1, 'Soy alérgico(a) a estos medicamentos'], [2, 'Suelo ser alérgico(a) a medicamentos (no me quiero arriesgar)'], [3, 'Prefiero soluciones naturales (hierbas, medicina cacera, etc.)'], [4, 'Otro']],
                              label='En caso haya marcado “ninguna”: ¿Por qué seleccionó esa opción? Si marcó algún medicamento, entonces dejar en blanco.',
                              widget=widgets.RadioSelect, blank=True)
    e21 = models.IntegerField(choices=[[0, 'Ninguna'], [1, 'Ibuprofeno'], [2, 'Daloflax']],
                              label='Imagina que te da una inflamación de amígdalas que te produce dolor y fiebre; por tanto, decides consultar con un médico. Este te dice que es porque tienes síntomas de gripe y para contrarrestarlos podrías tomar algún medicamento. Dada la información indicada debajo (la cual representa el costo de una pastilla), ¿cuál elegirías?',
                              widget=widgets.RadioSelect)
    e21x = models.IntegerField(choices=[[4, 'Me da miedo consumir genéricos'],[3, 'Los genéricos no tienen tanta eficacia'], [2, 'Confío en los genéricos']],
                             label='En caso haya marcado alguno de los dos medicamentos: ¿Por qué seleccionó esa opción? Si marcó “ninguna”, entonces dejar en blanco.',
                             widget=widgets.RadioSelect, blank=True)
    e22 = models.FloatField(label='¿Cuánto pagarías por cada pastilla del medicamento escogido? (solo una toma, es decir, una pastilla/cápsula). Ingrese el monto en soles. Si has marcado ninguna en la pregunta anterior, coloca 0.', min=0, max=50)


    e3 = models.IntegerField(choices=[[0, 'Ninguna'], [1, 'Ranitidina'], [2, 'Anitaral']],
                             label='Imagina que tienes calor estomacal y el doctor te ha dicho que es probable que tengas úlceras. Este te dice que, para contrarrestarlos, quizá podrías tomar algún medicamento. Dada la información indicada debajo, ¿cuál elegirías? (solo una toma, es decir, una pastilla/cápsula)',
                             widget=widgets.RadioSelect)
    e3x = models.IntegerField(choices=[[1, 'Porque el otro es muy barato'], [0, 'Porque el otro es muy caro'], [4, 'Me da miedo consumir genéricos'],[3, 'Los genéricos no tienen tanta eficacia'], [2, 'Confío en los genéricos']],
                             label='En caso haya marcado alguno de los dos medicamentos: ¿Por qué seleccionó esa opción? Si marcó “ninguna”, entonces dejar en blanco.',
                             widget=widgets.RadioSelect, blank=True)
    e3y = models.IntegerField(choices=[[1, 'Soy alérgico(a) a estos medicamentos'], [2, 'Suelo ser alérgico(a) a medicamentos (no me quiero arriesgar)'], [3, 'Prefiero soluciones naturales (hierbas, medicina cacera, etc.)'], [4, 'Otro']],
                              label='En caso haya marcado “ninguna”: ¿Por qué seleccionó esa opción? Si marcó algún medicamento, entonces dejar en blanco.',
                              widget=widgets.RadioSelect, blank=True)

    e41 = models.IntegerField(choices=[[0, 'Ninguna'], [1, 'Amoxicilina'], [2, 'Valimax']],
                              label='Imagina que tienes una infección intestinal; por lo que decides consultar con un médico. Este te dice que, para contrarrestarlos, podrías tomar algún medicamento. Dada la información indicada debajo, ¿cuál elegirías? (solo una toma, es decir, una pastilla/cápsula)',
                              widget=widgets.RadioSelect)
    e41x = models.IntegerField(choices=[[4, 'Me da miedo consumir genéricos'],[3, 'Los genéricos no tienen tanta eficacia'], [2, 'Confío en los genéricos']],
                             label='En caso haya marcado alguno de los dos medicamentos: ¿Por qué seleccionó esa opción? Si marcó “ninguna”, entonces dejar en blanco.',
                             widget=widgets.RadioSelect, blank=True)
    e42 = models.FloatField(label='¿Cuánto pagarías por cada pastilla del medicamento escogido? (solo una toma, es decir, una pastilla/cápsula). Ingrese el monto en soles. Si has marcado "Ninguna" en la pregunta anterior, coloca 0.', min=0, max=50)


    e5 = models.IntegerField(choices=[[0, 'Ninguna'], [1, 'Dexametasona'], [2, 'Valafax']],
                             label='Imagina que te detectan COVID-19 y por los síntomas que estás presentando, el doctor recomienda que compres alguno de estos medicamentos. Dada la información indicada debajo (la cual representa el costo de una ampolleta), ¿cuál elegirías?', widget=widgets.RadioSelect)
    e5x = models.IntegerField(choices=[[1, 'Porque el otro es muy barato'], [0, 'Porque el otro es muy caro'], [4, 'Me da miedo consumir genéricos'],[3, 'Los genéricos no tienen tanta eficacia'], [2, 'Confío en los genéricos']],
                             label='En caso haya marcado alguno de los dos medicamentos: ¿Por qué seleccionó esa opción? Si marcó “ninguna”, entonces dejar en blanco.',
                             widget=widgets.RadioSelect, blank=True)
    e5y = models.IntegerField(choices=[[1, 'Soy alérgico(a) a estos medicamentos'], [2, 'Suelo ser alérgico(a) a medicamentos (no me quiero arriesgar)'], [3, 'Prefiero soluciones naturales (hierbas, medicina cacera, etc.)'], [4, 'Otro']],
                              label='En caso haya marcado “ninguna”: ¿Por qué seleccionó esa opción? Si marcó algún medicamento, entonces dejar en blanco.',
                              widget=widgets.RadioSelect, blank=True)

    e61 = models.IntegerField(choices=[[0, 'Ninguna'], [1, 'Epinefrina'], [2, 'Indecan']],
                              label='Imagina que presentas síntomas fuertes del COVID-19, como fiebres altas; por lo que decides consultar con un médico. Este te dice que podrías tomar algún medicamento. ¿Cuál elegirías? (solo una toma, es decir, una ampolleta).',
                              widget=widgets.RadioSelect)
    e61x = models.IntegerField(choices=[[4, 'Me da miedo consumir genéricos'], [3, 'Los genéricos no tienen tanta eficacia'], [2, 'Confío en los genéricos']], label='En caso haya marcado alguno de los dos medicamentos: ¿Por qué seleccionó esa opción? Si marcó “ninguna”, entonces dejar en blanco.',
                               widget=widgets.RadioSelect, blank=True)
    e62 = models.FloatField(label='¿Cuánto pagarías por cada pastilla del medicamento escogido? (solo una toma, es decir, una pastilla/cápsula). Ingrese el monto en soles. Si has marcado ninguna en la pregunta anterior, coloca 0.', min=0, max=50)


    # Para la secuencia de páginas
    page_sequence = models.StringField()

