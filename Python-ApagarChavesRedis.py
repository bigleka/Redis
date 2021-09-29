# antes de começar lembre de instalar o python
# após instalar o python pip install redis
# aconcelho ver se seu editor favorito tem a opção de criar ambiente (environment) e criar a estrutura de lá

import redis 
import time
from redis import StrictRedis

r=redis.StrictRedis(
    host='IP ou FQDN do servidor do REDIS' # lembre-se de trocar o endereço
    , port=6379 # ou a porta que você está usando
    , password='senha' # caso o seu Redis utilize autenticação
)


pattern = "*" # filtro de pesquisa
cursor = '0'
while cursor != 0:
        cursor, data = r.scan(cursor, pattern, 1000)
        print ("cursor: "+str(cursor))
        for key in data:
                r.delete(key)
                print ("removendo chave: "+str(key))
        time.sleep(1) # adiciona um suspiro entre as entradas de 1000, pode ser comentado

# claro que tem formas mas fáceis de fazer como FLUSHALL ou outros métodos,
# mas a ideia desse método é gerar tráfego de comandos.
