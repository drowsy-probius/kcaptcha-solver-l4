import solver.dataset as dataset
import numpy as np
import tflite_runtime.interpreter as tflite
import os

def decode_prediction(predicted, char_set, length=2):
  l = len(char_set)
  chars = []
  for i in range(length):
    chars.append(char_set[np.argmax(predicted[i * l : (i + 1) * l])])

  return "".join(chars)

def main(captcha_image):
  image_binary = captcha_image
  captcha_length = 4
  available_chars = "0123456789"
  width = 160
  height = 60
  
  data_loader = dataset.KCaptchaDataLoader(
    image_binary=image_binary,
    captcha_length=captcha_length,
    available_chars=available_chars,
    width=width,
    height=height,
  )

  interperter = tflite.Interpreter(model_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), "model.tflite"))
  interperter.allocate_tensors() 

  input_details = interperter.get_input_details()[0]
  output_details = interperter.get_output_details()[0]

  valset, val_size = data_loader.get_input()

  images = valset[0][0]

  interperter.set_tensor(input_details["index"], images)
  interperter.invoke()

  output_data = interperter.get_tensor(output_details["index"])[0]
  output_data = decode_prediction(output_data, available_chars, captcha_length)
  return output_data

