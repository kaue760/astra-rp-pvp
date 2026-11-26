# Aplica correcoes listadas em correcoes.json nos arquivos .pwn antes de compilar.
# Formato: [{"arquivo": "astra_p2.pwn", "antigo": "texto velho", "novo": "texto novo"}]
import json
import sys

try:
    correcoes = json.load(open('correcoes.json', encoding='utf-8'))
except FileNotFoundError:
    correcoes = []

for c in correcoes:
    arq = c['arquivo']
    with open(arq, encoding='latin-1', newline='') as f:
        txt = f.read()
    txt = txt.replace('\r\n', '\n')
    antigo = c['antigo']
    qtd = txt.count(antigo)
    if qtd == 0:
        print('AVISO: trecho nao encontrado em %s: %r' % (arq, antigo[:80]))
        continue
    txt = txt.replace(antigo, c['novo']) if c.get('todas') else txt.replace(antigo, c['novo'], 1)
    with open(arq, 'w', encoding='latin-1', newline='') as f:
        f.write(txt.replace('\n', '\r\n'))
    print('OK: %s (%d ocorrencia(s) encontradas)' % (arq, qtd))

print('%d correcao(oes) listada(s)' % len(correcoes))
sys.exit(0)
