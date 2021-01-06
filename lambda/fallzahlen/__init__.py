from ask_sdk_core.skill_builder import SkillBuilder

from fallzahlen.handlers.today_handler import TodayIntentHandler
from fallzahlen.handlers.close_handler import CloseRequestHandler
from fallzahlen.handlers.help_handler import HelpHandler
from fallzahlen.handlers.fallback_handler import FallbackHandler
from fallzahlen.handlers.exception_handler import ExceptionHandler

builder = SkillBuilder()
builder.add_request_handler(TodayIntentHandler())
builder.add_request_handler(CloseRequestHandler())
builder.add_request_handler(HelpHandler())
builder.add_request_handler(FallbackHandler())
builder.add_exception_handler(ExceptionHandler())

handler = builder.lambda_handler()
