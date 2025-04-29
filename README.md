# SWork / Simple Work:

Descrição:


Regra do Negócio:
Gerenciar o controle de ferramentas.
Gerenciar materiais, andamento e pessoal nos locais de obra.
Auxiliar no controle e tomada de decisão.

Cliente:
Empresa de metalurgia/Construção civil.
Empresa opera com venda de materiais em aço;
Atua na montagem de estruras metalicas na de construção civil;
Produz peças metalicas em larga escala.

Requisitos:
---------------
Gerenciamento de ferramentas:
---------------
            Descrição:
            

            Atributos:
            id = Chave primária ; Marca ; Modelo ; Tensão ; Status ; Localização ;

            Métodos:
            Cadastrar ; Editar ; Remover ; Visão geral ;

Gerenciamento de funcionários;
---------------

            Atributos:

            Métodos
Cadastrar ; Editar ; Remover ; Visão geral ;

  
Gerenciamento de locais de obra;
Gerenciamento de materias;

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
