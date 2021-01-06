import random
from fallzahlen.utils.api import get_germany_data, get_state_data, get_district_data

import ask_sdk_core.utils as ask_utils
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response


class TodayIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input) or ask_utils.is_intent_name("TodayIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        district_data = get_district_data('03153')
        district_speak = f"In {district_data['name']} gibt es {district_data['delta']['cases']} neue Fälle und weitere {district_data['delta']['deaths']} Todesfälle. " +\
                         f"Die 7-Tagesinzidenz liegt bei {int(district_data['weekIncidence'])} je 100.000 Einwohner."


        state_data = get_state_data('NI')
        state_speak = f"{state_data['delta']['cases']} neue Fälle und {state_data['delta']['deaths']} neue Todesfälle wurden in deinem Bundesland {state_data['name']} registriert. " +\
                         f"Die 7-Tagesinzidenz liegt bei {int(state_data['weekIncidence'])} je 100.000 Einwohner."

        germany_data = get_germany_data()
        germany_speak = f"In gesamt Deutschland gibt es {germany_data['delta']['cases']} neue Fälle und weiter {germany_data['delta']['deaths']} Todesfälle. " +\
                         f"Die 7-Tagesinzidenz liegt bei {int(germany_data['weekIncidence'])} je 100.000 Einwohner."

        return (
            handler_input.response_builder
                .speak(f"<p>{district_speak}</p>\n<p>{state_speak}</p>\n<p>{germany_speak}</p>")
                .response
        )
