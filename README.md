![Badge projeto](https://img.shields.io/badge/Projeto-Em%20Desenvolvimento-blue)
![Badge Version](https://img.shields.io/badge/Version-0.0.01-blue)
![Badge em Desenvolvimento](https://img.shields.io/badge/Status-Em%20Desenvolvimento-blue)

<h1 align=center> SWork / Simple Work </h1>
<br>
<a href="https://excalidraw.com/#json=kTAp5SwzSIc4253NQkJ8B,Gu1_0uzelE7VDyOhndgZRA">Diagrama do projeto</a>
<br><br>
<div>
	<p>
            <b>Descrição do projeto:</b>
            <br>Software criado para auxiliar no gerenciamento de empresa do ramo <i>Construção civil</i>.
            </p>
            <p>
            <b>Observações do projeto:</b>
            <br>Desenvolvimento feito em 3 <i>estágios principais</i>, contendo sua etapas subsequentes para cada estágio.</i>
            </p>
            <p>
            <b>Regras de Negocio:</b>
            <br>Gerenciar ferramentas nos locais de trabalho.
            <br>Gerenciar funcionarios nos locais de trabalho.
            <br>Gerenciar o andamento do trabalho nos locais.
            </p>
</div>
<div>
            <h2>Estagio 1 - Gerenciamento de ferramentas</h2>
            <br>
            <p>
            <b>Negocio:</b>
            <br>Gerenciar o controle de ferramentas nos locais de trabalho.
            </p>
            <p>
            <b>Descrição:</b>
            <br>Utiliza do cadastramento para gerenciar o controle total de ferramentas.
            <br>Ferramentas cadastradas são adicionadas a um local de trabalho.
            <br>Necessário que os locais já tenham sido cadastrados.
            <br>Ao transferir uma ferramenta a um local de trabalho, a mesma entrará em transito; Sendo necessário confirmar a chegada ao local.
            <br>Ferramentas em transito ficarão aninhadas na janela inicial, aguardando a confimação de chegada.
            </p>
            <p>
            <b>Como usar:</b>
            </p>
            <p align=center><b>Propriedades:</b></p>
            
            Atributos Principais:
            Id = identificador da ferramenta e chave primaria do banco
            tipo = Tipo de ferramenta; Se é do tipo chave/furadeira/esmerilhadeira
            Marca = Propriedade da ferramenta
            Modelo = Propriedade da ferramenta
            Tensão = Opcional, caso seja elétrica
            Estado = Estado atual da ferramenta; Em transito para LOCAL/ No local
            Condição = Condição ao qual a ferramenta se encontra; Funcionando/Em manutenção
            
                        Métodos:
            Cadastrar/Adicionar = Adiciona a ferramenta ao banco de dados
            Editar/Alterar = Altera os atributos de uma ferramenta já adicionada
            Remover/Deletar = Remove do banco de dados uma ferramenta já adicionada

            Requisitos:
            Local = Localização da ferramenta; Vem dos locais cadastrados
            Log = Registro contendo todas as alterações
</div>
<div>
<h2>Estagio 2 - Gerenciamento dos locais de trabalho</h2>
<br>
</div>
<div>
<h2>Estagio 3 - Gerenciamento do andamento dos locais</h2>
</div>
<div>
<h2>Sistema</h2>
            <p><b>Arquitetura em camadas:</b>
            <br>Modulo Repository - Regras do banco de dados
            <br>Modulo views - Interfaces da aplicação
            <br>Modulo Controller - Funcionalidades e serviços do sistema
            </p>

Tecnologia utilizada:
Software feito em python.
Com interface usando pyside.
Banco de dados sql3 orientado a objeto.
</div>

# Projeto Em andamento...
