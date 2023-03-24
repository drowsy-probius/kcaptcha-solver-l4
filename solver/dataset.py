from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import densenet
import numpy as np
from PIL import Image


class KCaptchaDataLoader:
    def __init__(
        self,
        image_binary,
        captcha_length,
        available_chars,
        width,
        height,
        verbose=True,
    ):
        self.image_binary = image_binary
        self.captcha_length = captcha_length
        self.available_chars = available_chars
        self.available_chars_cnt = len(self.available_chars)
        self.image_width = width
        self.image_height = height
        self.ext = "png"
        self.verbose = verbose
        self.preproces_func = densenet.preprocess_input

        self.datagen = image.ImageDataGenerator(
            # rescale=1.0 / 255,
            # preprocess_input does scaling (https://github.com/tensorflow/tensorflow/blob/v2.3.1/tensorflow/python/keras/applications/imagenet_utils.py)
            preprocessing_function=self.preproces_func,
        )
        self.dataset_loaded = False
        
        self.x_run = None 
        self.y_run = None

    def one_hot_encode(self, label):
        """
        e.g.) 17 ==> [0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 1.0, 0, 0,]
        """
        vector = np.zeros(self.available_chars_cnt * self.captcha_length, dtype=float)
        for i, c in enumerate(label):
            idx = i * self.available_chars_cnt + int(c)
            vector[idx] = 1.0
        return vector

    def one_hot_decode(self, vec):
        char_pos = vec.nonzero()[0]
        text = []
        for i, c in enumerate(char_pos):
            digit = c % self.available_chars_cnt
            text.append(str(digit))
        return "".join(text)

    # def preprocess(self, img_path):
    #     img = image.load_img(
    #         img_path,
    #         target_size=(self.image_height, self.image_width),
    #         # color_mode="grayscale",
    #     )
    #     img = image.img_to_array(img)
    #     return img

    def preprocess(self, image_binary):
        img = Image.open(image_binary)
        # img = Image.open(io.BytesIO(image_binary))
        img = img.convert('RGB')
        img = img.resize((self.image_width, self.image_height))
        img = image.img_to_array(img)
        return img


    def load_dataset(self):
        def _load_image_from_dir(image_binary):
            return np.array([
                self.preprocess(image_binary)
            ]), np.array([self.one_hot_encode("0000")])
        
        self.x_run, self.y_run = _load_image_from_dir(self.image_binary)
        self.dataset_loaded = True

    def _get_dataset(self, x, y, batch_size):
        return (
            self.datagen.flow(
                x=x,
                y=y,
                batch_size=batch_size,
                shuffle=True,
            ),
            len(y),
        )

    def get_input(self):
        if not self.dataset_loaded:
            self.load_dataset()
        return self._get_dataset(self.x_run, self.y_run, batch_size=1)

    def _log(self, msg):
        if self.verbose:
            print(f"[*] {self.__class__.__name__}: {msg}")
