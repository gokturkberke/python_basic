import sys
#getsizeof
a = [1, 2, 3]
print("a listesinin boyutu:", sys.getsizeof(a), "bayt")
#----------------------------------------------
#sys.version
print("Python sürümü:", sys.version)
#----------------------------------------------
print("Python yorumlayıcısının yolu:", sys.executable)
# Çıktı örneği (Linux): /usr/bin/python3
# Çıktı örneği (Windows): C:\Python39\python.exe
#----------------------------------------------
print("Çalıştığınız platform:", sys.platform)
# Örnek Çıktılar:
# 'win32' -> Windows
# 'linux' -> Linux
# 'darwin' -> macOS
#----------------------------------------------
#sys.prefix
# Python'un kurulu olduğu dizini görüntüle
print("Python kurulum dizini:", sys.prefix)
#----------------------------------------------
print("Bir metin girin (bitirmek için Ctrl+D veya Ctrl+Z basın):")
input_text = sys.stdin.read()  # Tüm girdi okunur
print("Girdiğiniz metin:")
print(input_text)
#----------------------------------------------
# print("Programdan çıkıyorum.")
sys.exit()
print("Bu satır çalışmayacak.")  # Bu satır sys.exit() nedeniyle çalışmaz