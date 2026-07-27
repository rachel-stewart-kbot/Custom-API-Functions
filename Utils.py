import json, base64, re
from urllib.request import Request, urlopen
from datetime import datetime, date
from dateutil import parser

class Utils:
    # Decode a base64 string to utf-9
    @staticmethod
    def decode_base64(encoded):
        decoded_bytes = base64.b64decode(encoded)
        decoded_string = decoded_bytes.decode("utf-8")
        return decoded_string

    # Given a phone number of any recognizable format
    #   Convert it to the normal US 10DLC format: +13335554444
    @staticmethod
    def enforce_10dlc_format(phone_number):
        try:
            # 1. strip the given phone number down to just numbers
            enforced = ''.join(filter(str.isdigit, phone_number))
            # 2. if the number is 11 digits and starts with 1, remove the 1
            if len(enforced) == 11 and enforced[0] == '1':
                enforced = enforced[1:]
            # 3. if the number is 10 digits, add a +1 to the front
            if len(enforced) == 10:
                enforced = '+1' + enforced
            return {
                "phone_result": enforced,
                "original": phone_number,
                "isValid": Utils.is_10dlc_format(enforced)
            }
        except (ValueError, AttributeError):
            return {
                "phone_result": None,
                "original": phone_number,
                "isValid": False
            }

    @staticmethod
    def is_10dlc_format(phone_number):
        starts_with_plus_1 = phone_number[0:2] == '+1'
        is_12_digits = len(phone_number) == 12
        is_numeric_after_plus_1 = phone_number[2:].isnumeric()
        return starts_with_plus_1 and is_12_digits and is_numeric_after_plus_1

    @staticmethod
    def compute_age(dob_string):
        result = None
        try:
            dob = parser.parse(dob_string)
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            result = {"age": age}
        except (ValueError, TypeError):
            pass
        return result

    @staticmethod
    def extract_first_number(number_string):
        result = None
        try:
            match = re.search(r'\d+', number_string)
            if match:
                result = {"first_number": int(match.group())}
        except (ValueError, AttributeError):
            pass
        return result

    @staticmethod
    def format_10dlc_as_human_phone(phone_number):
        result = None
        try:
            normalized = Utils.enforce_10dlc_format(phone_number)
            if normalized and normalized.get("isValid"):
                digits = normalized["phone_result"][2:]
                formatted = f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
                result = {
                    "phone_result": formatted,
                    "original": phone_number,
                    "normalized": normalized["phone_result"],
                    "isValid": True
                }
        except (ValueError, AttributeError, TypeError):
            pass
        return result

    @staticmethod
    def extract_first_last_string(text, delimiter=' '):
        result = None
        try:
            if delimiter is None or delimiter == '':
                delimiter = ' '

            parts = [part.strip() for part in text.split(delimiter) if part.strip()]
            if len(parts) > 0:
                result = {
                    "first_string": parts[0],
                    "last_string": parts[-1],
                    "delimiter": delimiter
                }
        except (AttributeError, TypeError, ValueError):
            pass
        return result

    @staticmethod
    def to_system_time(date_input):
        result = None
        try:
            if isinstance(date_input, datetime):
                dt_value = date_input
            elif isinstance(date_input, date):
                dt_value = datetime.combine(date_input, datetime.min.time())
            else:
                dt_value = parser.parse(str(date_input))

            result = {
                "system_time": dt_value.strftime("%Y-%m-%d %H:%M:%S") + ".0",
                "original": date_input
            }
        except (ValueError, TypeError, OverflowError):
            pass
        return result

class PayloadObject():
    def __init__(self, payload):
        self.raw_input = payload
        self.payload = json.loads(payload) if isinstance(payload, str) else payload
    
    def get_key(self, key): return self.payload[key]
    def __str__(self): return json.dumps(self.payload)