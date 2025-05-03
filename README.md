# SWork / Simple Work:

            Descrição.:
            Software criado para auxiliar no gerenciamento de empresa do ramo montagem/industria/Construção civil.

            Negocio.:
            Gerenciar o controle de ferramentas nos locais de trabalho.
            Gerenciar o controle e escala de funcionarios nos locais de trabalho.
            Gerenciar o andamento do trabalho nos locais de trabalho.
            
            Observações do projeto.:
            Desenvolvimento será feito em 3 estágios principais, contendo sua etapas subsequentes para cada estágio.


Estagio 1 - Gerenciamento de ferramentas
---
            Negocio:
            Gerenciar o controle de ferramentas nos locais de trabalho

            Descrição:

            Atributos Principais:
            Id = identificador da ferramenta e chave primaria do banco
            tipo = Tipo de ferramenta; Se é do tipo chave/furadeira/esmerilhadeira
            Marca = Propriedade da ferramenta
            Modelo = Propriedade da ferramenta
            Tensão = Opcional, caso seja elétrica
            Estado = Estado atual da ferramenta; Em transito para .../ No local
            Condição = Condição ao qual a ferramenta se encontra; Funcionando/Em manutenção
            
                        Métodos:
            Cadastrar/Adicionar = Adiciona a ferramenta ao banco de dados
            Editar/Alterar = Altera os atributos de uma ferramenta já adicionada
            Remover/Deletar = Remove do banco de dados uma ferramenta já adicionada

            Requisitos:
            Local = Localização da ferramenta; Vem dos locais cadastrados
            Log = Registro contendo todas as alterações

Estagio 2 - Gerenciamento dos locais de trabalho
---
            Negocio:
            
            
Gerenciamento de materiais;

Sistema
---
            Arquitetura em camadas:
            Modulo Repository - Regras do banco de dados
            Modulo views - Interfaces da aplicação
            Modulo Controller - Funcionalidades e serviços do sistema

            Tecnologia utilizada:
            Software feito em python.
            Com interface usando pyside.
            Banco de dados sql3 orientado a objeto.

# Projeto Em andamento...
