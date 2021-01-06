import random

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

        return (
            handler_input.response_builder
                .speak("Test test")
                .response
        )
