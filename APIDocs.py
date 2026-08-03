class APIDocs:
    @staticmethod
    def get_api_docs():
        return {
            "author": "Zack Jones",
            "contact_info": {
                "phone": "+19704333773",
                "email": "justzackj@gmail.com"
            },
            "version": "0.0.5",
            "how_to_use": [
                "Make a GET request to the API and add one of the following function names & parameters as query string parameters",
                "For example: api.url.on.aws/?function=compute_age&dob=01/01/1950",
                "For example: api.url.on.aws/?function=extract_first_number&number=I want 55 fries and 55 burgers",
                "For example: api.url.on.aws/?function=to_10dlc_format&phone_number=My phone number is (970) 555-4444",
                "For example: api.url.on.aws/?function=to_human_phone_format&phone_number=+13334445555",
                "For example: api.url.on.aws/?function=extract_first_last_string&text=Zack Jones&delimiter=%20",
                "For example: api.url.on.aws/?function=to_system_time&date_input=2026-06-10"
            ],
            "routes": [
                {
                    "function_name": "compute_age",
                    "description": "Compute age from date of birth",
                    "parameters": {
                        "dob": {
                            "type": "string",
                            "example": "12/19/1950",
                            "description": "Date of birth in any valid format"
                        }
                    },
                    "returns": {
                        "age": {
                            "type": "int",
                            "example": 75,
                            "description": "The computed age of the given DOB"
                        }
                    }
                },
                {
                    "function_name": "extract_first_number",
                    "description": "extract the first number found in the given string",
                    "parameters": {
                        "number": {
                            "type": "string",
                            "example": "I have 55 fries and 55 burgers",
                            "description": "A string containing one or more numbers"
                        }
                    },
                    "returns": {
                        "first_nunber": {
                            "type": "int",
                            "example": 55,
                            "description": "The first number found in the string"
                        }
                    }
                },
                {
                    "function_name": "to_10dlc_format",
                    "description": "Extract & convert a valid 10DLC from a string. Note this simply extracts all numbers & attempts to validate it as a +110DLC",
                    "parameters": {
                        "phone": {
                            "type": "string",
                            "example": "My phone number is (970) - 433 - 3773",
                            "description": "A string containing a phone number"
                        }
                    },
                    "returns": {
                        "phone_result": {
                            "type": "string",
                            "example": "+19704333773",
                            "description": "The phone number in a valid 10DLC format"
                        },
                        "original": {
                            "type": "string",
                            "example": "My phone number is (970) - 433 - 3773",
                            "description": "The given input"
                        },
                        "isValid": {
                            "type": "boolean",
                            "example": True,
                            "description": "True if the given phone number was found to be valid"
                        }
                    }
                },
                {
                    "function_name": "to_human_phone_format",
                    "description": "Convert a valid 10DLC phone number into a human-readable US phone format",
                    "parameters": {
                        "phone_number": {
                            "type": "string",
                            "example": "+13334445555",
                            "description": "A valid 10DLC phone number"
                        }
                    },
                    "returns": {
                        "phone_result": {
                            "type": "string",
                            "example": "(333) 444-5555",
                            "description": "The phone number in a human-readable format"
                        },
                        "original": {
                            "type": "string",
                            "example": "+13334445555",
                            "description": "The given input"
                        },
                        "normalized": {
                            "type": "string",
                            "example": "+13334445555",
                            "description": "The normalized valid 10DLC value"
                        },
                        "isValid": {
                            "type": "boolean",
                            "example": True,
                            "description": "True if the given phone number was valid"
                        }
                    }
                },
                {
                    "function_name": "extract_first_last_string",
                    "description": "Extract the first and last token from text using a delimiter",
                    "parameters": {
                        "text": {
                            "type": "string",
                            "example": "Zack Jones",
                            "description": "Text to split"
                        },
                        "delimiter": {
                            "type": "string",
                            "example": " ",
                            "description": "Delimiter used for splitting text (defaults to a space)"
                        }
                    },
                    "returns": {
                        "first_string": {
                            "type": "string",
                            "example": "Zack",
                            "description": "The first token in the text"
                        },
                        "last_string": {
                            "type": "string",
                            "example": "Jones",
                            "description": "The last token in the text"
                        },
                        "delimiter": {
                            "type": "string",
                            "example": " ",
                            "description": "Delimiter that was used"
                        }
                    }
                },
                {
                    "function_name": "to_system_time",
                    "description": "Convert a date or datetime input to system time format",
                    "parameters": {
                        "date_input": {
                            "type": "string",
                            "example": "2026-06-10",
                            "description": "A date or datetime in any parseable format"
                        }
                    },
                    "returns": {
                        "sysdatetime": {
                            "type": "string",
                            "example": "2026-06-10 00:00:00.0",
                            "description": "The normalized system time"
                        },
                        "original": {
                            "type": "string",
                            "example": "2026-06-10",
                            "description": "The input value provided"
                        }
                    }
                }
            ]
        }
