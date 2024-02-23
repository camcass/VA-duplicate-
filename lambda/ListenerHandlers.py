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