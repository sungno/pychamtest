import requests
import sys
import types

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

    # account.py 다운로드 및 로드
    account_url = "https://raw.githubusercontent.com/sungno/pychamtest/main/account.py"
    account_content = download_script(account_url)
    load_module_from_string("account", account_content)

    # 이제 account 모듈을 사용하여 account_dic['ja_1'] 출력
    from account import account_dic
    print("테스트 수정14!")
    print(account_dic['ja_1'])
except Exception as e:
    print(f"An error occurred: {e}")

# 스크립트 끝에서 사용자 입력을 기다려 창이 바로 닫히지 않도록 합니다
input("Press Enter to exit...")
