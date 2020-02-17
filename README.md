Easy Twitter Collector 
=======

Aplicação criada utilizando a biblioteca open-source [Tweepy](https://www.tweepy.org/ "tweepy website") que fornece um wrapper para facilitar o acesso para Twitter API. A proposta de uso é de fornecer ao desenvolvedor um método fácil para realizar coletas de tweets em streaming (e outros métodos em futuras implementações). É disponibilizado  uma interface da qual é possível alterar a forma de como os dados são recebidos conforme a necessidade do usuário e também um módulo para a realização da escrita do logs de execução, erros e exceções.
 
Requerimentos
------------
Python 3.x.x e a biblioteca tweepy que pode ser baixada através do instalador de pacotes python [PIP](https://pypi.org/project/pip/) com o comando:  

    pip install tweepy

Como Usar
------------
Altere o arquivo config.json com o serviço que será usado, o método de coleta e os parâmetros que serão enviados. Também deve ser alterado caminho para os logs e o carácter divisor de diretório conforme for seu sistema operacional. 

**Exemplo**:   
```json
{
  "service" : "streaming",
  "method" : "stream_tweets",
  "log_path": "\\path\\to\\logs",
  "escape": "\\ ( ou / em caso de sistemas operacionais Unix)",  
  "parameters" : {
    "param1": "valor1",
    "param2": "valor2",
    "param3": "valor3"
  }
}
```

Com as configurações corretamente feitas execute o arquivo main.py na pasta raiz da aplicação.

- **Consultar descrições dos métodos no arquivo servicesDetails.md**

Alterando o módulo para persistência dos dados
------------
Caso seja interessante ao usuário alterar o módulo para persistência dos dados para algum criado pelo próprio deve-se seguir os seguintes passos: 
1.  Realizar a importação do módulo customizado no arquivo manager/persisters.py.

```python
'''  manager/persisters.py  '''

from SaveOnDataBase import *
```
2. Após isso deve-se criar uma classe herdando a interface `` DataSaver``. Essa interface contém apenas um método chamado ``persist(self, data, **kwargs)`` que realiza a tratativa dos dados recebidos pela API. Deve ser colocado neste método logica de uso do modulo de persistencia customizado do usuário. Caso seja necessário alguma configuração previa defina um construtor para nova classe. 

```python
'''  manager/persisters.py  '''

class CustomTweetSaver(DataSaver):
    def __init__(self, args):
        ... Pre-configuration setup ...

    def persist(data, **kwargs):
        ... Your Logic to persist data ...

```
3. Por fim deve-se alterar no arquivo main.py no método principal a variável ``saver`` atribuindo a esta uma instância da classe que foi criada no passo anterior. Por ser uma classe pertencente ao módulo manager/persisters.py devemos instanciar ela a partir do módulo 

```python
'''  main.py  '''

def main():
  ...
  saver = persisters.CustomTweetSaver(your_args)
  ...
```

Modulo gerenciador de logs
------------
**IMPORTATE**: Será criado uma serie de diretórios para cada tipo de informação referente e data e o tipo da ocorrência da mensagem de log.   

* **execution**: Informações sobre a execução da aplicação (arquivos separados por dia).

* **error**: Informações sobre a erros que ocorreram durante a execução da aplicação (arquivos separados por dia).

* **execption**: Informações sobre a exceções que ocorreram durante a execução da aplicação (arquivos únicos para cada ocorrência).

Caso queira utilizar o modulo de log realize a importação /EasyTwitterCollector/util/log.py  e utilize o método ``write_log`` passando como parâmetro a menssagem a ser escrita e o tipo de log da qual ela se refere.

```python
from easyTwiiterCollector.util import log
log.write_log('Any information', 'log_type')
```

Contato
------------
Qualquer coisa pode me chamar no discord ou mesmo mandar um email fica ao seu criterio :) 
* Discord: reaborn#8454
* Email: henrique.hott1996@gmail.com