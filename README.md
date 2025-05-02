# SWork / Simple Work:

--

Cliente:
Empresa metalurgica que atua no mercado de montagem/industria/Construção civil.

Negocio:
Gerenciar o controle de ferramentas, materiais, funcionarios e locais de obras.

Regras de Negócio:
Aplicação desenvolvida em 3 estagios.
Gerenciar o controle de ferramentas baseado nos locais de obra.
Gerenciar materiais, andamento e pessoal nos locais de obra.


Gerenciamento de ferramentas
---------------
            Negocio:
Gerenciar o controle de ferramentas baseado nos locais de trabalho

            Atributos Principais:
Id = identificador da ferramenta e chave primaria do banco
tipo = Tipo de ferramenta; se é do tipo chave/furadeira/esmerilhadeira
Marca = Propriedade da ferramenta
Modelo = Propriedade da ferramenta
Tensão = Opcional, caso seja elétrica

            Atributos de atribuição:
Local = Localização da ferramenta;
Status = Representa o estado atual da ferramenta; Se está No local ou Em transito
Condição = Condição ao qual a ferramenta se encontra; Funcionando/Em manutenção

            Métodos:
Cadastrar/Adicionar = Adiciona a ferramenta ao banco de dados
Editar/Alterar = Altera os atributos de uma ferramenta já adicionada
Remover/Deletar = Remove do banco de dados uma ferramenta já adicionada

Projeto Em andamento...
---
Gerenciamento de funcionários
Gerenciamento de locais de obra;
Gerenciamento de materiais;

Sistema
---
Arquitetura em camadas:
Modulo Repository - Regras do banco de dados
Modulo Entity - Modelo de dados
Modulo views - Interface gráfica
Modulo Controller - Funcionalidades do sistema

Tecnologia utilizada:
Software feito em python.
Com interface usando pyside.
Banco de dados sql3 orientado a objeto.
