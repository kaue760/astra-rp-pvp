# Astra RP/PVP

Game mode SA-MP que junta a GM de RP (Santa Group) com a GM de PVP (Abelha).
Ao entrar, o jogador escolhe PVP ou RP.

## Compilar
O GitHub compila sozinho quando os arquivos `astra*.pwn` sao enviados.
O resultado fica na pasta `saida/` (`astra.amx`, `log.txt` e `erros.txt`).

## Correcoes
Trechos a corrigir entram em `correcoes.json` e sao aplicados antes de compilar
(pelo `aplicar_correcoes.py`).
