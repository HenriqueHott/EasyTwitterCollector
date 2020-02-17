Service/Streaming
=====

Módulo para uso do serviço de coleta em tempo real de tweets disponibilizada pela API.

**stream_tweets**
-----
 Método para executar a coleta em tempo real de tweets filtrando a coleta conforme os parâmetros enviados pelo usuário.   

**Parâmetros**:
* api_token* (String) -> Chave da aplicação

* api_secret* (String) -> Chave secreta da aplicação 
* access_token* (String) -> Chave de acesso para API
* access_secret* (String) -> Chave secreta de acesso a API
* keywords (List: String) -> Lista de palavras para filtrar a coleta
* users (List: String) -> Lista dos IDs ou nome dos usuários dos quais será realizado a coleta
* locations (List: [Float, Float]) -> Lista de duplas contanto as coordenadas de longitude latitude para filtrar a coleta no formato [lat, lon]
* stall_warning (Bool) -> Habilita menssagens quando o usuário estiver alcançando seu limite de uso. Padrão: True


 **Exemplo**:
 ```json
{
  "service" : "streaming",
  "method" : "stream_tweets",
  "log_path": "\\path\\to\\logs",
  "escape": "\\",  
  "parameters" : {
    "api_token": "mytoken",
    "api_secret": "mytoken",
    "access_token" : "mytoken",
    "access_secret" : "mytoken",
    "keywords": ["banana", "split"],
    "users": ["FelipeBeto", "5574585541"]
  }
}
````
**Informações**:  

https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/post-statuses-filter


-----
\* = Campos Obrigatórios