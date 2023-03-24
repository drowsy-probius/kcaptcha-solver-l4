### Forked from [kcaptcha-solver](https://github.com/ryanking13/kcaptcha-solver)

# requirements

- Python 3.8 virtual environment
> Not working in Python 3.9 or later due to `tflite_runtime` dependency.

- and some packages in `requiements.txt`

# how to run server
This app is not suitable for production.

```bash
# run below line in root directory of this repository
python3.8 -m venv venv

# activate venv
source ./venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run server
# server running on 0.0.0.0:8000
./scripts/run.server.sh
# or
python manage.py runserver 0.0.0.0:8000
```


```bash
# and it may gives below info or warnings, but it works...
Performing system checks...

2023-03-24 07:31:47.833276: I tensorflow/tsl/cuda/cudart_stub.cc:28] Could not find cuda drivers on your machine, GPU will not be used.
2023-03-24 07:31:47.885463: I tensorflow/tsl/cuda/cudart_stub.cc:28] Could not find cuda drivers on your machine, GPU will not be used.
2023-03-24 07:31:47.885971: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-03-24 07:31:48.671494: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
System check identified no issues (0 silenced).
March 24, 2023 - 07:31:49
Django version 4.1.7, using settings 'app.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

# usage

## curl in bash
```bash
# NOTE: trailing `/`
curl -F image=@./solver/7286.jpg localhost:8000/kcaptcha/

# returns
# {"success": true, "response_time": 60.352783203125, "result": "7286"}
```

## python requests
```python
import requests

res = requests.post(
  "http://localhost:8000/kcaptcha/",
  files={
    "image": open("./solver/7286.jpg", "rb")
  }
)
print(res.json())
# {"success": true, "response_time": 60.352783203125, "result": "7286"}
```

-------

php 모듈 kcaptcha로 생성된 캡챠 이미지 중에서 0123456789 문자로 길이가 4인 캡챠를 풀어주는 코드입니다.

[ryanking13](https://github.com/ryanking13)님의 코드를 사용해서 학습한 모델을 이용하여 제작되었습니다.

사용 시 책임은 개발자가 아닌 사용자 본인에게 있습니다.

## See also
- [kcaptcha-solver](https://github.com/ryanking13/kcaptcha-solver)
