# Trabalho Prático
Projeto da Disciplina Técnicas Avançadas de Desenvolvimento de Software

Aluno: Antonio Thomaz Oliveira Reis

Faculdade de Computação - Universidade Federal do Mato Grosso do Sul (UFMS)

O projeto consiste em um sistema baseado em arquitetura de serviços (SOA) projetado para coletar, gerenciar e disseminar informações sobre condições climáticas.

## Objetivos
O objetivo principal deste sistema é fornecer um meio eficiente e escalável para coletar dados, disseminar boletins informativos com base nos dados coletados, e oferecer uma interface amigável para os usuários finais, além de garantir a integração e comunicação entre os diferentes serviços do sistema.

## Escopo do sistema
1. Data Service: Serviço que faz a coleta de dados e permite a consulta dos dados coletados.
2. Newsletter Service: Serviço que faz o cadastro de pessoas interessadas em receber boletins de atualizações do tempo de acordo com os dados coletados.
3. Website UI: Serviço que disponibiliza uma interface web para acesso às funcionalidades da aplicação.
4. API Gateway: API Gateway é um ponto onde clientes poderão se comunicar com os microserviços da aplicação.

## Requisitos Funcionais

1. Data Service

        Requisito funcional 1.1: O sistema deve ser capaz de coletar dados de várias fontes.
        Requisito funcional 1.2: O sistema deve permitir a consulta de dados coletados por período, fonte, e outros filtros relevantes.
        Requisito funcional 1.3: Os dados coletados devem ser armazenados de forma segura e eficiente.
        Requisito funcional 1.4: Deve haver um mecanismo para a atualização e exclusão dos dados coletados.

2. Newsletter Service

       Requisito funcional 2.1: O sistema deve permitir o cadastro de usuários interessados em receber boletins.
       Requisito funcional 2.2: Os usuários devem poder selecionar as categorias de boletins que desejam receber.
       Requisito funcional 2.3: O sistema deve enviar boletins de acordo com as preferências dos usuários.
       Requisito funcional 2.4: Deve ser possível gerenciar (editar/excluir) os cadastros dos usuários.
       Requisito funcional 2.5: O sistema deve garantir a conformidade com as leis de proteção de dados (ex: LGPD, GDPR).

3. Website UI

        Requisito funcional 3.1: O website deve oferecer uma interface amigável para cadastro de usuários.
        Requisito funcional 3.2: O website deve permitir a consulta de dados coletados.
        Requisito funcional 3.3: O website deve ser responsivo e acessível a partir de dispositivos móveis.
        Requisito funcional 3.4: O website deve permitir aos usuários gerenciar suas inscrições em boletins.

4. API Gateway

        Requisito funcional 4.1: O API Gateway deve atuar como um ponto central de comunicação entre os clientes e os microserviços.
        Requisito funcional 4.2: O API Gateway deve fornecer autenticação e autorização para acesso aos serviços.
        Requisito funcional 4.3: O API Gateway deve ser capaz de rotear as solicitações para os serviços apropriados.
        Requisito funcional 4.4: O API Gateway deve realizar balanceamento de carga entre os serviços.
        Requisito funcional 4.5: Deve ser possível monitorar e registrar as requisições através do API Gateway.

## Requisitos não funcionais

    Requisito não funcional 1: O sistema deve ser capaz de lidar com altas cargas de requisições simultâneas sem degradação significativa de desempenho.
    Requisito não funcional 2: A arquitetura deve permitir a adição de novos serviços e a expansão dos serviços existentes sem grandes modificações.
    Requisito não funcional 3: Todos os serviços devem seguir práticas robustas de segurança, incluindo criptografia de dados sensíveis, autenticação forte e proteção contra ataques comuns (ex: DDoS, SQL Injection).
    Requisito não funcional 4: O sistema deve ser altamente disponível, com redundância e mecanismos de failover para minimizar o tempo de inatividade.
    Requisito não funcional 5: O código deve ser bem documentado e modular, facilitando a manutenção e a adição de novas funcionalidades.
