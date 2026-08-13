import json, re
from Utils import Utils
from APIDocs import APIDocs

ERROR = ""

def lambda_handler(event, context):
    # Read from query string parameters (for GET requests)
    params = event.get("queryStringParameters") or {}
    print(f"Params are: {params}")
    function_name = params.get("function") or params.get("function_name")

    result = None
    error = None

    if len(params) == 0:
        result = APIDocs.get_api_docs()
    elif function_name == "compute_age":
        dob_string = params.get("dob")
        if not dob_string:
            error = "Missing 'dob' query parameter"
        else:
            result = Utils.compute_age(dob_string)
            if result is None:
                error = f"Invalid date: {dob_string}"
    elif function_name == "extract_first_number":
        number_string = params.get("number")
        if not number_string:
            error = "Missing 'number' query parameter"
        else:
            result = Utils.extract_first_number(number_string)
            if result is None:
                error = f"Invalid number: {number_string}"
    elif function_name == "to_10dlc_format":
        phone_number = params.get("phone_number")
        if not phone_number:
            error = "Missing 'phone_number' query parameter"
        else:
            result = Utils.enforce_10dlc_format(phone_number)
            if result is None:
                error = f"Invalid phone number: {phone_number}"
    elif function_name == "to_human_phone_format":
        phone_number = params.get("phone_number")
        if not phone_number:
            error = "Missing 'phone_number' query parameter"
        else:
            result = Utils.format_10dlc_as_human_phone(phone_number)
            if result is None:
                error = f"Invalid 10DLC phone number: {phone_number}"
    elif function_name == "extract_first_last_string":
        text = params.get("text")
        if not text:
            error = "Missing 'text' query parameter"
        else:
            delimiter = params.get("delimiter", " ")
            result = Utils.extract_first_last_string(text, delimiter)
            if result is None:
                error = f"Invalid text: {text}"
    elif function_name == "to_system_time":
        date_input = params.get("date_input")
        if not date_input:
            error = "Missing 'date_input' query parameter"
        else:
            result = Utils.to_system_time(date_input)
            if result is None:
                error = f"Invalid date input: {date_input}"
    elif function_name == "calculate_days_difference":
            start_date = params.get("start_date")
            end_date = params.get("end_date")
            
            if not start_date or not end_date:
                error = "Missing 'start_date' or 'end_date' query parameters"
            else:
                result = Utils.calculate_days_difference(start_date, end_date)
                if not result.get("isValid"):
                    error = result.get("error", f"Invalid date formats: {start_date}, {end_date}")
    else:
        error = f"Unknown function: {function_name}"

    if error or result is None:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": error})
        }
    elif result is not None:
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            },
            "body": json.dumps(result)
        }
