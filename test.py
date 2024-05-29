import requests,sys,types

# 공통 다운로드 및 로드 기능을 포함한 스크립트에서 필요한 기능을 가져옵니다
def download_script(url):
    headers = {'Cache-Control': 'no-cache'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def load_module_from_string(module_name, module_content):
    module = types.ModuleType(module_name)
    exec(module_content, module.__dict__)
    sys.modules[module_name] = module
    return module

try:
    # 필요한 모듈 다운로드 및 로드
    method_url = "https://raw.githubusercontent.com/sungno/pychamtest/main/method.py"
    method_content = download_script(method_url)
    load_module_from_string("method", method_content)

    # 이제 method 모듈을 사용할 수 있습니다
    from method import *
    print("테스트 수정12!")
    print(a)
    print(b)
except Exception as e:
    print(f"An error occurred: {e}")

input("Press Enter to exit...")