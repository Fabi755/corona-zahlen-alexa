# -*- coding: utf-8 -*-

import ask_sdk_core.utils as ask_utils
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response


class FallbackHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        return (
            handler_input.response_builder
                .speak("Ich weiß leider nicht was du meinst. Versuche deine Aussagen anders zu formulieren oder "
                       "sage Hilfe für weitere Informationen.")
                .ask("Bitte sage Hilfe für weitere Informationen.")
                .response
        )
