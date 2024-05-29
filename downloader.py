import requests,sys,types


# def download_and_execute_script(url):
#     headers = {'Cache-Control': 'no-cache'}
#     response = requests.get(url, headers = headers)
#     response.raise_for_status()  # 다운로드가 성공했는지 확인
#     script_content = response.text
#     print()
#     print("Downloaded script content:")
#     print(script_content)
#     print("-----------------------------------")
#
#     # 다운로드한 스크립트를 메모리에서 직접 실행
#     exec(script_content, globals())

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

def execute_script(script_content):
    exec(script_content, globals())

if __name__ == "__main__":
    # GitHub raw 파일 URL
    # script_url = "https://raw.githubusercontent.com/sungno/pychamtest/main/test.py"
    # local_script = "test.py"
    #
    # download_and_execute_script(script_url)

    try:
        # GitHub raw 파일 URL
        script_url = "https://raw.githubusercontent.com/sungno/pychamtest/main/test.py"

        # 메인 스크립트 다운로드
        main_script_content = download_script(script_url)

        # 메인 스크립트 실행
        execute_script(main_script_content)

    except Exception as e:
        print(f"An error occurred: {e}")

        # 스크립트 끝에서 사용자 입력을 기다려 창이 바로 닫히지 않도록 합니다
    input("Press Enter to exit...")