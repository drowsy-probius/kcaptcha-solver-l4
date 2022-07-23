import argparse

import dataset
import numpy as np
import tflite_runtime.interpreter as tflite

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--image",
        required=True,
        help="input captcha image path",
    )
    parser.add_argument(
        "-m",
        "--model",
        default="model.tflite",
        help="keras pre-trained densenet121 model path",
    )
    parser.add_argument(
        "-l",
        "--length",
        default=4,
        help="captcha character length"
    )
    args = parser.parse_args()
    return args


def decode_prediction(predicted, char_set, length=2):
    l = len(char_set)
    chars = []
    for i in range(length):
        chars.append(char_set[np.argmax(predicted[i * l : (i + 1) * l])])

    return "".join(chars)


def main():
    args = parse_args()

    image_path = args.image
    captcha_length = args.length
    available_chars = "0123456789"
    width = 160
    height = 60
    base_model_path = args.model


    data_loader = dataset.KCaptchaDataLoader(
        image_path=image_path,
        captcha_length=captcha_length,
        available_chars=available_chars,
        width=width,
        height=height,
    )

    interperter = tflite.Interpreter(model_path=base_model_path)
    interperter.allocate_tensors() 

    input_details = interperter.get_input_details()[0]
    output_details = interperter.get_output_details()[0]


    valset, val_size = data_loader.get_input()

    images = valset[0][0]

    interperter.set_tensor(input_details["index"], images)
    interperter.invoke()

    output_data = interperter.get_tensor(output_details["index"])[0]
    output_data = decode_prediction(output_data, available_chars, captcha_length)
    print(output_data)


if __name__ == "__main__":
    main()
