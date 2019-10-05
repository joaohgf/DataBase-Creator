# DataBase-Creator

Neste algoritmo você é capaz de adicionar e posteriormente solicitar algumas exibições de acordo com o menu.


# Pré-requisitos

É necessário possuir o Python3 instalado, Sqlite3 e o algoritmo salvo.  

# Utilizando o algoritmo
Após ser executado o algoritmo irá criar um banco de dados na pasta onde ele mesmo foi salvo, e o usuário terá acesso a um menu onde haverá 4 opções: 
- 1 opção: É onde o usuário pode inserir dados.
- 2 opção: É onde será exibido o nome do cliente, seu CPF e seu contato.
- 3 opção: É onde será exibido o CPF para identificação e o custo de cada cliente.
- 4 opção: É onde será exibido o CPF, o custo, o preço, o lucro de cada cliente e o lucro total da empresa.
> #### Quando é escolhido a primeira opção, é exibido o seguinte menu:
>- CPF(11 dígitos):  
>Onde há um limite de 11 números.
>- Nome:
>É possível digitar apenas nomes com no máximo 50 letras.
>- Telefone
>- Custo da entrega    
>Em reais, pois as exibições posteriores são feitas em real.
>- Preço da entrega
>Em reais, pois as exibições posteriores são feitas em real.
>- Lucro da entrega
>Em reais, pois as exibições posteriores são feitas em real.
>- Data de envio
>No formato DD/MM/AA, onde DD são os dias, MM os meses, AA os anos.
>- Data da entrega
Também no formato DD/MM/AA, onde DD são os dias, MM os meses, AA os anos.

>#### Quando é escolhido a segunda opção, é exibido:
> 
|CPF | Contato | Nome|
|--|--|--|
| 11111111111 | 21 993852134 |José Carlos|
| 22222222222 | 22 993145623 | Caio Andrade

> #### Quando é escolhido a terceira opção, é exibido: 
>
|CPF  | CUSTO  |
|--|--|
| 11111111111  |350  |
|22222222222 |450
|**CUSTO TOTAL** : |800
>#### Quando é escolhido a quarta opção, é exibido:
>
| CPF |Custo  |Preço|Lucro|
|--|--|--|--|
|11111111111  | 350|600|250|
|22222222222 |450|700|250|
|**LUCRO TOTAL** : |500
>Caso seja escolhida a quarta opção, o programa irá fechar. E se for digitado algum número diferente dos que estão presentes no menu, será emitido um erro. 
## Considerações
 >É necessário seguir a forma de inserção de dados correta. 

### Criação por:
>João Henrique.
>Email: joao.henriquefreitas@outlook.com .
>Linkedin: https://www.linkedin.com/in/joao-henrique-g-622976134/
