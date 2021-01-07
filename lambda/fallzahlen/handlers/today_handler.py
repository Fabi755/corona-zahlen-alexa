import random
from fallzahlen.utils.api import get_germany_data, get_state_data, get_district_data, find_state_id, find_district_id
from fallzahlen.utils.location import get_location_info

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

        speak_text = ""
        if handler_input.request_envelope.context.system.user.permissions:
            device_id = handler_input.request_envelope.context.system.device.device_id

            address_client = handler_input.service_client_factory.get_device_address_service()
            address = address_client.get_country_and_postal_code
            print(f"Post code: {address.postal_code}")

            # TODO: check for valid postcode
            # TODO: Save post code, district ID, state ID data in (dynamodb) database for caching
            location = get_location_info('38440')
            print(location) # TODO: remove logs, if exception handling was added
            district_id = find_district_id(location.district)
            state_id = find_state_id(location.state)
            print(district_id) # TODO: remove logs, if exception handling was added
            
            district_data = get_district_data(district_id)
            district_speak = f"{district_data['name']} hat {self._speak_number(district_data['delta']['cases'])} neue Erkrankungen und weitere {self._speak_number(district_data['delta']['deaths'])} Todesfälle. " +\
                             f"Die 7-Tagesinzidenz liegt bei {self._speak_number(int(district_data['weekIncidence']))} je 100.000 Einwohner."
            speak_text = speak_text + f"<p>{district_speak}</p>"

            state_data = get_state_data(state_id)
            state_speak = f"{self._speak_number(state_data['delta']['cases'])} neue Erkrankungen und {self._speak_number(state_data['delta']['deaths'])} neue Todesfälle wurden in deinem Bundesland {state_data['name']} registriert. " +\
                             f"Die 7-Tagesinzidenz liegt bei {self._speak_number(int(state_data['weekIncidence']))} je 100.000 Einwohner."
            speak_text = speak_text + f"<p>{state_speak}</p>"

        germany_data = get_germany_data()
        germany_speak = f"In gesamt Deutschland gibt es {self._speak_number(germany_data['delta']['cases'])} neue Erkrankungen und weitere {self._speak_number(germany_data['delta']['deaths'])} Todesfälle. " +\
                         f"Die 7-Tagesinzidenz liegt bei {self._speak_number(int(germany_data['weekIncidence']))} je 100.000 Einwohner."
        speak_text = speak_text + f"<p>{germany_speak}</p>"

        # TODO: ask for permission consent card (short address)
        if not handler_input.request_envelope.context.system.user.permissions:
            permission_speak = "Um Daten für deinen Landkreis und dein Bundesland zu erhalten, erteile uns bitte die Erlaubnis deine Adresse zu verwenden und trage deine Postleitszahl ein. " +\
                               "Dies kannst du in der Alexa App in den Skill Details tun."
            speak_text = speak_text + f"<p>{permission_speak}</p>"


        return (
            handler_input.response_builder
                .speak(speak_text)
                .response
        )

    def _speak_number(self, value):
        return f"<say-as interpret-as=\"number\">{value}</say-as>"