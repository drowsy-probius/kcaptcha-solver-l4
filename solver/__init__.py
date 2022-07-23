from base64 import b64encode
import json, time, traceback
from django.http import HttpResponse, HttpResponseBadRequest

import numpy as np
import tflite_runtime.interpreter as tflite
from .run_lite import main

def current_milli_time():
  return time.time() * 1000

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def captchar_solver(request):
  try:
    start = current_milli_time()
    response = {
      "success": False, 
      "response_time": 0,
      "result": "????"
    }

    print(get_client_ip(request))

    if "image" not in request.FILES:
      raise Exception("image binary should be in files!")

    image_binary = request.FILES["image"]
    if image_binary.size > 10000:
      raise Exception("image is too large. max size is 160x60")
    
    # image_binary = b64encode(image_binary.read())
    answer = main(image_binary)

    response["result"] = answer
    response["success"] = True
    response["response_time"] = current_milli_time() - start
    return HttpResponse(json.dumps(response))
  except Exception as e:
    print(traceback.format_exc())
    return HttpResponseBadRequest(e)
