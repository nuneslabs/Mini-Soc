import subprocess

resultado = subprocess.run(
    ["journalctl", "-n", "10", "--no-pager"],
    capture_output=True,
    text=True
)

for linha in resultado.stdout.split("\n"):
    print(linha)

    if "error" in linha.lower():
        print("⚠️ Possível erro encontrado!")

    elif "warning" in linha.lower() or "timeout" in linha.lower(): 
         print("🟡aviso encontrado!")

    else:
        print("evento normal!")