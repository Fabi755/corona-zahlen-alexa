from ask_sdk.standard import StandardSkillBuilder

from fallzahlen.handlers.today_handler import TodayIntentHandler
from fallzahlen.handlers.close_handler import CloseRequestHandler
from fallzahlen.handlers.help_handler import HelpHandler
from fallzahlen.handlers.fallback_handler import FallbackHandler
from fallzahlen.handlers.exception_handler import ExceptionHandler

builder = StandardSkillBuilder()
builder.add_request_handler(TodayIntentHandler())
builder.add_request_handler(CloseRequestHandler())
builder.add_request_handler(HelpHandler())
builder.add_request_handler(FallbackHandler())
builder.add_exception_handler(ExceptionHandler())

handler = builder.lambda_handler()
