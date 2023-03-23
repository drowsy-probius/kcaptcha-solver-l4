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
# 
# it gives several INFO or WARNINGs
./scripts/run.server.sh
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
