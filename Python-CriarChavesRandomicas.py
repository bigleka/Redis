# antes de começar lembre de instalar o python
# após instalar o python pip install redis
# aconcelho ver se seu editor favorito tem a opção de criar ambiente (environment) e criar a estrutura de lá

import redis
from datetime import timedelta

import random
import string
import uuid
from random import randint


r=redis.StrictRedis(
    host='IP ou FQDN do servidor do REDIS' # lembre-se de trocar o endereço
    , port=6379 # ou a porta que você está usando
    , password='senha' # caso o seu Redis utilize autenticação
)


def get_random_string(length,time):
    letters = string.ascii_lowercase # usa letras minusculas
    result_str = ''.join(random.choice(letters) for i in range(length))
    uuid_str=str(uuid.uuid4())
    print("Valor gerado randomicamente para a chave", result_str, "foi:",uuid_str)
    r.setex(result_str,timedelta(seconds=time),value=uuid_str)
    valueRedis=r.get(result_str)
    print(valueRedis)



for _ in range(100): # quantidade de execuções
    get_random_string(10,3000) # quantidade de caracteres para a chave, tempo de vida da chave
