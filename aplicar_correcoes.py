# Aplica correcoes listadas em correcoes.json nos arquivos antes de compilar.
# Formato: [{"arquivo": "x.inc", "antigo": "texto", "novo": "texto"}]
# Com "regex": true, "antigo" e uma expressao regular (modo multilinha).
import json
import re
import sys

try:
    correcoes = json.load(open('correcoes.json', encoding='utf-8'))
except FileNotFoundError:
    correcoes = []

for c in correcoes:
    arq = c['arquivo']
    try:
        with open(arq, encoding='latin-1', newline='') as f:
            txt = f.read()
    except FileNotFoundError:
        print('AVISO: arquivo nao encontrado: %s' % arq)
        continue
    txt = txt.replace('\r\n', '\n')
    antigo = c['antigo']
    if c.get('regex'):
        novo, qtd = re.subn(antigo, c['novo'], txt, flags=re.M)
    else:
        qtd = txt.count(antigo)
        novo = txt.replace(antigo, c['novo']) if c.get('todas') else txt.replace(antigo, c['novo'], 1)
    if qtd == 0:
        print('AVISO: trecho nao encontrado em %s: %r' % (arq, antigo[:80]))
        continue
    with open(arq, 'w', encoding='latin-1', newline='') as f:
        f.write(novo.replace('\n', '\r\n'))
    print('OK: %s (%d ocorrencia(s))' % (arq, qtd))

print('%d correcao(oes) listada(s)' % len(correcoes))
sys.exit(0)
