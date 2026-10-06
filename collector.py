import subprocess
import re


def verificar_autenticacao():
    resultado = subprocess.run(
        ["journalctl", "--since", "10 min ago", "--no-pager"],
        capture_output=True,
        text=True
    )

    falhas_autenticacao = 0

    print("\n" + "="*30)
    print("   RELATORIO DO MINI SOC ")
    print("="*30)

    for linha in resultado.stdout.split("\n"):
        if "pam_unix" in linha.lower() and "authentication failure" in linha.lower():
            falhas_autenticacao += 1

        pesquisa = re.search(r"user=(\S+)", linha)

        if pesquisa:
            usuario = pesquisa.group(1)
            print(f"alvo detectado: {usuario}")

        pesquisa_origem = re.search(r"tty=(\S+)", linha)

        if pesquisa_origem:
            origem =  pesquisa_origem.group(1)
            print(f"origem do ataque: {origem}")


    print(f"Eventos analisados: ultimos 10 minutos")
    print(f"Falhas de autenticacao: {falhas_autenticacao}")

    if falhas_autenticacao >= 3:
        print("\n  ALERTA: Possivel atividade suspeita! Multiplas falhas de autenticação detectadas.")
    else:
        print("\n Status: Sistema seguro. Nenhuma anomalia detectada.")

verificar_autenticacao()