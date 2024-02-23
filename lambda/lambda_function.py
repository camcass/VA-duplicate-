# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response
from Library import Library

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
library = Library()
class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome to the book reader! You can say start reading to read the book"
        library.createBook1()
        library.startReadingSession()
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class StartReadingIntentHandler(AbstractRequestHandler):
    """Handler for initiating a reading session wth only the demo book in the library"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("StartReadingIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Reading Curious George a Winter's Nap from page 1. You can ask for the page to be read, image descriptions, discussion questions, or navigate the book"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class GetTextIntentHandler(AbstractRequestHandler):
    """Handler for initiating a reading session wth only the demo book in the library"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GetTextIntent")(handler_input)
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = library.getText()
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class GetDiscussionQuestionsIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("GetDiscussionQuestionsIntent")(handler_input)

    def handle(self, handler_input):
        questions = library.getDiscussionQuestions()
        if not questions:
            return (
                handler_input.response_builder
                    .speak("There are no discussion questions available for this page.")
                    .set_should_end_session(True)
                    .response
            )

        question = questions.pop(0)  # Get the first question
        
        # Store the remaining questions in session attributes
        session_attr = handler_input.attributes_manager.session_attributes
        session_attr["questions"] = questions

        speak_output = question
        reprompt_text = "Would you like another discussion question?"

        if questions:  # Only ask if more questions are available
            speak_output += " " + reprompt_text

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_text if questions else None)
                .response
        )
class YesIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.YesIntent")(handler_input)

    def handle(self, handler_input):
        session_attr = handler_input.attributes_manager.session_attributes
        questions = session_attr.get("questions", [])
        long_descriptions = session_attr.get("long_descriptions", [])

        if questions:
            question = questions.pop(0)
            session_attr["questions"] = questions

            speak_output = question
            reprompt_text = "Would you like another discussion question?"

            if questions:
                speak_output += " " + reprompt_text
                return (
                    handler_input.response_builder
                        .speak(speak_output)
                        .ask(reprompt_text)
                        .response
                )
            else:
                return (
                    handler_input.response_builder
                        .speak(speak_output)
                        .set_should_end_session(True)
                        .response
                )

        elif long_descriptions:
            long_description = long_descriptions.pop(0)
            session_attr["long_descriptions"] = long_descriptions

            speak_output = long_description
            reprompt_text = "Would you like to hear another detailed description?"

            if long_descriptions:
                speak_output += " " + reprompt_text
                return (
                    handler_input.response_builder
                        .speak(speak_output)
                        .ask(reprompt_text)
                        .response
                )
            else:
                return (
                    handler_input.response_builder
                        .speak(speak_output)
                        .set_should_end_session(False)
                        .response
                )
class NoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.NoIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = " "

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(False)
                .response
        )
class GetShortImageDescriptionsIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("GetShortImageDescriptionsIntent")(handler_input)

    def handle(self, handler_input):
        short_descriptions = library.getShortImageDescriptions()
        long_descriptions = library.getLongImageDescriptions()

        session_attr = handler_input.attributes_manager.session_attributes
        speak_output = ''.join(short_descriptions)

        # Check if long descriptions are available and not the 'no description' message
        if long_descriptions and long_descriptions != ['No long description is available for this page.']:
            session_attr["long_descriptions"] = long_descriptions
            reprompt_text = "Would you like to hear a more detailed description?"
            speak_output += " " + reprompt_text
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(reprompt_text)
                    .response
            )
        else:
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .set_should_end_session(False)
                    .response
            )
class SetPageIntentHandler(AbstractRequestHandler):
    """Handler for setting the book to a specific page"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SetPageIntent")(handler_input)

    def handle(self, handler_input):
        # Get the slot value from the request
        slots = handler_input.request_envelope.request.intent.slots
        page_number = int(slots["pageNumber"].value)

        # Conditional to check for page 1 or 2 and redirect to page 3
        if page_number == 1 or page_number == 2:
            speak_output = "The start page of this book is page 3. Turning to page 3."
            reprompt_text = speak_output
            page_number = 3  # Redirect to page 3
        else:
            speak_output = f"Turning to page {page_number}."
            reprompt_text = speak_output

        # Call the function to set the page number
        library.setPage(page_number)

        # Create the response with the reprompt
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_text)  # Add a reprompt in case the user does not respond.
                .response
        )
class NextPageIntentHandler(AbstractRequestHandler):
    """Handler for initiating a reading session wth only the demo book in the library"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NextPageIntent")(handler_input)

    def handle(self, handler_input):
        currentPage = library.nextPage()
        speak_output = str(currentPage)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class PrevPageIntentHandler(AbstractRequestHandler):
    """Handler for initiating a reading session wth only the demo book in the library"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PrevPageIntent")(handler_input)

    def handle(self, handler_input):
        currentPage = library.prevPage()
        speak_output = str(currentPage)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
# Required helper functions------------------------------------
class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )
class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.
class PageThreeIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 4"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageThreeIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 3"
        library.setPage(4)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageFourIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 4"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageFourIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 4"
        library.setPage(4)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageFiveIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 5"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageFiveIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 5"
        library.setPage(5)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageSixIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 6"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageSixIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 6"
        library.setPage(6)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageSevenIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 7"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageSevenIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 7"
        library.setPage(7)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageEightIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 8"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageEightIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 8"
        library.setPage(8)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageNineIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 9"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageNineIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 9"
        library.setPage(9)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageTenIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 10"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageTenIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 10"
        library.setPage(10)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageElevenIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 11"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageElevenIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 11"
        library.setPage(11)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageTwelveIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 12"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageTwelveIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 12"
        library.setPage(12)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageThirteenIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 13"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageThirteenIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 13"
        library.setPage(13)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageFourteenIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 14"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageFourteenIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 14"
        library.setPage(14)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageFifteenIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 15"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageFifteenIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 15"
        library.setPage(15)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageSixteenIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 16"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageSixteenIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 16"
        library.setPage(16)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageSeventeenIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 17"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageSeventeenIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 17"
        library.setPage(17)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageEighteenIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 18"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageEighteenIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 18"
        library.setPage(18)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageNineteenIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 19"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageNineteenIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 19"
        library.setPage(19)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageTwentyIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 20"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageTwentyIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 20"
        library.setPage(20)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageTwentyOneIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 21"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageTwentyOneIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 21"
        library.setPage(21)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageTwentyTwoIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 22"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageTwentyTwoIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 22"
        library.setPage(22)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageTwentyThreeIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 23"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageTwentyThreeIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 23"
        library.setPage(23)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PageTwentyFourIntentHandler(AbstractRequestHandler):
    """Active listening handler for page 24"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PageTwentyFourIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Detected page 24, which is the last page of the story."
        library.setPage(24)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
sb = SkillBuilder()
sb.add_request_handler(PageThreeIntentHandler())
sb.add_request_handler(PageFourIntentHandler())
sb.add_request_handler(PageFiveIntentHandler())
sb.add_request_handler(PageSixIntentHandler())
sb.add_request_handler(PageSevenIntentHandler())
sb.add_request_handler(PageEightIntentHandler())
sb.add_request_handler(PageNineIntentHandler())
sb.add_request_handler(PageTenIntentHandler())
sb.add_request_handler(PageElevenIntentHandler())
sb.add_request_handler(PageTwelveIntentHandler())
sb.add_request_handler(PageThirteenIntentHandler())
sb.add_request_handler(PageFourteenIntentHandler())
sb.add_request_handler(PageFifteenIntentHandler())
sb.add_request_handler(PageSixteenIntentHandler())
sb.add_request_handler(PageSeventeenIntentHandler())
sb.add_request_handler(PageEighteenIntentHandler())
sb.add_request_handler(PageNineteenIntentHandler())
sb.add_request_handler(PageTwentyIntentHandler())
sb.add_request_handler(PageTwentyOneIntentHandler())
sb.add_request_handler(PageTwentyTwoIntentHandler())
sb.add_request_handler(PageTwentyThreeIntentHandler())
sb.add_request_handler(PageTwentyFourIntentHandler())

sb.add_request_handler(PrevPageIntentHandler())
sb.add_request_handler(NextPageIntentHandler())
sb.add_request_handler(SetPageIntentHandler())

sb.add_request_handler(YesIntentHandler())
sb.add_request_handler(NoIntentHandler())
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(StartReadingIntentHandler())
sb.add_request_handler(GetDiscussionQuestionsIntentHandler())
sb.add_request_handler(GetTextIntentHandler())
sb.add_request_handler(GetShortImageDescriptionsIntentHandler())

sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()