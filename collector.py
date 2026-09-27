import subprocess
def verificar_autenticacao():

    resultado = subprocess.run(
        ["journalctl", "--since", "10 min ago", "--no-pager"],
        capture_output=True,
        text=True
    )

    falhas_autenticação = 0

    for linha in resultado.stdout.split("\n"):
        if "pam_unix" in linha.lower() and "authentication failure" in linha.lower():
            falhas_autenticação += 1

    print("\n" + "="*30)
    print(" 🛡️  RELATÓRIO DO MINI SOC 🛡️")
    print("="*30)

    print(f"Eventos analisados: últimos 10 minutos")
    print(f"Falhas de autenticação: {falhas_autenticação}")

    if falhas_autenticação >= 3:
        print("\n⚠️  ALERTA: Possível atividade suspeita! Múltiplas falhas de autenticação detectadas.")
    else:
        print("\n✅ Status: Sistema seguro. Nenhuma anomalia detectada.")

verificar_autenticacao()