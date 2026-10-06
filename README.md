# Mini SOC 🛡️

Projeto de estudo em Python desenvolvido para monitoramento, análise de logs e detecção de eventos de segurança em sistemas Linux, com foco em automação e engenharia de sistemas.

## Sobre o Projeto

O **Mini-SOC** é uma ferramenta de monitoramento leve desenvolvida em Python que interage diretamente com o subsistema de logs do Linux (`journalctl`). O objetivo principal é analisar tentativas de autenticação em tempo real, aplicando regras de segurança (threshold/limiar) para detectar possíveis ataques de força bruta, além de fornecer um painel visual (*live dashboard*) direto no terminal.

## Funcionalidades Atuais

* **Monitoramento em Tempo Real (Modo Vigia):** Executa um loop contínuo de varredura com atualização automática de tela (estilo painel de SOC).
* **Extração Cirúrgica com Regex:** Utiliza expressões regulares (`re`) para varrer logs brutos e extrair com precisão o **alvo** (`user`) e a **origem** (`tty`) da tentativa de acesso.
* **Regra de Limiar de Alerta (Threshold):** Sistema inteligente que diferencia erros humanos pontuais de múltiplos eventos suspeitos, disparando um alarme apenas quando atinge o limite configurado (3+ falhas) para evitar fadiga de alerta.
* **Interface CLI Otimizada:** Relatórios estruturados visualmente para facilitar a leitura rápida de eventos críticos.

## Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Sistema Operacional / SO Logs:** Linux (Fedora / Journalctl)
* **Bibliotecas Python Nativas:** `subprocess`, `re`, `time`, `os`
* **Controle de Versão:** Git & GitHub

## Como Executar o Projeto

1. Clone o repositório em sua máquina Linux:
   ```bash
   git clone [https://github.com/nuneslabs/Mini-Soc.git](https://github.com/nuneslabs/Mini-Soc.git)
   cd Mini-Soc