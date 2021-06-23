import sys
import pikepdf
from tqdm import tqdm

PDF_FILE_NAME = sys.argv[1]
PASSWORDS_FILE_NAME = "passwords.txt"

passwords = [ line.strip() for line in open(PASSWORDS_FILE_NAME) ]

for password in tqdm(passwords, "HaCkEaNdO o PdF"):
    try:
        with pikepdf.open(PDF_FILE_NAME, password=password) as pdf:
            print("ALA, ACHO SAPORRA:", password)
            sys.exit(0)
    except pikepdf._qpdf.PasswordError as e:
        continue

print("IH RAPA, ACHO NÃO, TENTA OUTRAS SENHAS, SEPÁ VAI")
sys.exit(1)
