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

# Junta as partes astra_p1.pwn, astra_p2.pwn... num unico astra.pwn
# (variaveis static do Pawn so valem dentro do proprio arquivo)
import glob
partes = sorted(glob.glob('astra_p[0-9]*.pwn'), key=lambda n: int(re.findall(r'\d+', n)[0]))
if partes:
    with open('astra.pwn', 'w', encoding='latin-1', newline='') as saida:
        for p in partes:
            with open(p, encoding='latin-1', newline='') as f:
                saida.write(f.read())
    print('astra.pwn montado a partir de %d partes: %s' % (len(partes), ', '.join(partes)))
sys.exit(0)
