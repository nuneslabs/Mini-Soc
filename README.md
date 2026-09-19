# Mini SOC

Projeto de estudo desenvolvido em Python com o objetivo de aprender, na prática, conceitos de monitoramento, análise de logs e detecção de eventos de segurança em sistemas Linux.

## Sobre o projeto

A ideia do Mini SOC é acompanhar eventos registrados pelo sistema e, a partir deles, identificar situações que possam indicar algum problema ou atividade suspeita.

O projeto está sendo desenvolvido aos poucos, conforme novos conceitos de Cibersegurança e programação são estudados.

## Status

**Em desenvolvimento**

Atualmente, o projeto consegue:

* Coletar logs do sistema Linux usando Python
* Ler eventos através do `journalctl`
* Separar os eventos individualmente
* Fazer uma análise básica dos eventos por meio de palavras-chave

### Próximos passos

* Detectar tentativas de login malsucedidas
* Identificar possíveis tentativas de força bruta
* Criar um sistema de alertas
* Armazenar os eventos coletados
* Desenvolver uma interface para visualizar os eventos

## Tecnologias

* Python
* Linux
* journalctl
* Git
* GitHub

## Objetivo

Usar o projeto como forma de colocar em prática conhecimentos de Python, Linux e Cibersegurança, além de acompanhar minha evolução durante os estudos.
