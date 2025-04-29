# SWork
            Simple Work:

cliente:
Empresa de metalurgia/Construção civil.

Negócio:
Gerenciar controle de ferramentas baseado nos locais

Descrição:
Empresa opera com venda de materiais em aço;
Atua na montagem de estruras metalicas na de construção civil;
Produz peças metalicas em larga escala.

Requisitos:
-------------------------------------------------------------------------
            Gerenciamento de ferramentas:
 
    Métodos:
Cadastrar ; Editar ; Remover ; Visão geral ;

    <i>Atributos:</i>
Id(primario) ; Marca ; Modelo ; Condição ; Tensão ; Local ;
-------------------------------------------------------------------------
            Gerenciamento de funcionários;
    Métodos
Cadastrar ; Editar ; Remover ; Visão geral ;

  
Gerenciamento de locais de obra;
Gerenciamento de materias;
Compra e venda de materiais;

3 estágios:


Tecnologia utilizada:
Software feito em python.
Com interface usando pyside.
Banco de dados sql orientado a objeto.

Arquitetura em camadas:
Modulo Repository - Regras do banco de dados
Modulo Entity - Modelo de dados
Modulo views - Interface gráfica
Modulo Controller - Funcionalidades do sistema

Cada modelo e pagina terá seu próprio pacote.

Ex.:
Pagina inicial, com seus pacotes:


