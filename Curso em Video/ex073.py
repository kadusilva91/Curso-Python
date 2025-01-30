# Crie uma tupla preenchida com os vinte primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre: Os 5 primeiros times. Os ultimos 4 colocados. Times em ordem alfabética. Em que posição esta o time da chapecoense.
times = ('Corinthina','Palmeiras','Santos','Gremio','Cruzeiro',
         'Flamengo','Vasco','Chapecoense','Atlético-MG','Botafogo',
         'Atlético-PR','Bahia','São Paulo','Fluminense','Sport',
         'Vitória','Coritiba','Avaí','Pnte Preta','Atlético-GO')
print('-='*15)
print(f'Lista de Times do Brasileirão {times}')
print('-='*15)
print(f'Os cinco primeiros colocados são {times[0:5]}')
print('-='*15)
print(f'Os quatro últimos colocado são {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética {sorted(times)}')
print('-='*15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
