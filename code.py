import logging
import math
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    num = req.params.get('num')
    if not num:
        try:
            num = req.get_json().get('num')
        except ValueError:
            pass

    try:
        num = int(num)
        return func.HttpResponse(f"Factorial of {num} is: {math.factorial(num)}")
    except:
        status_code=200
        return func.HttpResponse("Invalid input")

