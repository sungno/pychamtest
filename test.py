# 공통 다운로드 및 로드 기능을 포함한 스크립트에서 필요한 기능을 가져옵니다
from downloader import download_script, load_module_from_string

# 필요한 모듈 다운로드 및 로드
method_url = "https://raw.githubusercontent.com/sungno/pychamtest/main/method.py"
method_content = download_script(method_url)
load_module_from_string("method", method_content)

# 이제 method 모듈을 사용할 수 있습니다
from method import *
print("테스트 수정13!")
print(a)
input()