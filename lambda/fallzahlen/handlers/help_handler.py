# -*- coding: utf-8 -*-

import logging

import ask_sdk_core.utils as ask_utils
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class HelpHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        return (
            handler_input.response_builder
                .speak("<p>Ich verrate dir, welche aktuellen Coron Fallzahlen.</p>"
                       "<p>Um die Fallzahlen für deinen Landkreis zu bekommen, trage deine Adresse in den Alexa Einstellungen ein und erlaube uns diese zu verwenden.</p>"
                       "<p>Frage mich, wie sind die Fallzahlen heute?</p>")
                .ask("Frage mich, wie sind die Fallzahlen heute?")
                .response
        )
