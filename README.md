# Astra RP/PVP

Game mode SA-MP que junta a GM de RP (Santa Group) com a GM de PVP (Abelha).
Ao entrar, o jogador escolhe PVP ou RP.

## Como compilar
1. O arquivo `compilar.yml` precisa ficar em `.github/workflows/compilar.yml`.
2. Suba o `Astra_repo_github.zip` (sem extrair) na raiz do repositorio.
3. O GitHub descompacta e compila sozinho. O resultado fica em `saida/`
   (`astra.amx`, `log.txt` e `erros.txt`).

## Correcoes
Trechos a corrigir entram em `correcoes.json` e sao aplicados antes de compilar
(pelo `aplicar_correcoes.py`).
