RawTwitterSaver
=======

Classe para salvar os dados brutos recebidos da API em disco. 

* Os dados brutos recebidos da API são salvos em arquivos sem extensão um JSON por linha.

* Os arquivos são nomeados conforme um **prefixo** e a data de quando foi salvo o primeiro JSON nele. Cada arquivo contém um número parametrizável de JSONs e são organizados em diferentes diretórios na seguinte estrutura: **TipoDoDado/Ano/Mes/Dia**.

* Os dados podem ser do tipo **apiMessage** referente a mensagens recebidas da API ou **statuses** que se referem ao tweets propriamente ditos.
 
* O prefixo também será usado para criar o diretório raiz dos resultados.

```
path/prefixo/TipoDoDado/Ano/Mes/Dia/prefixo_034441
   {"created_at": "Wed Feb 12 03:44:41 +0000 2020", ... 
   {"created_at": "Wed Feb 12 03:44:41 +0000 2020", ...
````

Configurando
-----

As configurações da classe devem ser feitas alterando os campos do arquivo ```enviroment.json```. Segue a descrição de cada campo: 

  * base_path (String): caminho base para criação dos diretórios,
  * prefix (String): Prefixo que nomeia a base.

  * escape(String): Caracter usado para dividir os diretórios em seu S.O (/ ou \\). 
  * max_lines(int): Máximo de linhas por arquivos.
  * unicode: Conjunto Unicode
  * fields(List/String): Campos do JSON recebidos da API que serão armazenados. Se não for preenchido com o valor ``null`` será salvo todos os campos.


Exemplos
-----
Salvando todos campos do JSON
```json
{
  "base_path": "F:\\workfolder",
  "prefix": "myBase",
  "escape": "\\",
  "max_lines": 500,
  "unicode": "utf8",
  "fields": null
}
```
Selecionado os campos...

```json
{
  "base_path": "base/dir",
  "prefix": "myBase",
  "escape": "\\(windows) or /(Unix)",
  "max_lines": 500,
  "unicode": "utf8",
  "fields": ["id_str", "create_at", "text", "user"]
}
```