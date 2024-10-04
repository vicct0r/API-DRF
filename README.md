# API de Cursos - Django Rest Framework

Este repositório contém a estrutura inicial de uma API desenvolvida utilizando o **Django Rest Framework** (DRF). A proposta deste projeto é oferecer um exemplo de configuração adequada e eficiente para a implementação de APIs em Django, servindo como base para estudos e futuras expansões.

## Descrição do Projeto

A aplicação central deste repositório é denominada **'cursos'**, que contempla dois principais modelos:

- **Curso**: Representa os cursos disponíveis, com os campos `titulo` e `url`.
- **Avaliação**: Representa as avaliações feitas pelos usuários sobre os cursos, permitindo que cada avaliação esteja associada a um curso existente na API.

Este projeto tem como principal objetivo consolidar o conhecimento prático na criação e configuração de APIs utilizando o Django Rest Framework, seguindo boas práticas de desenvolvimento.

## Tecnologias Utilizadas

- **Django**: Framework principal para o desenvolvimento da aplicação.
- **Django Rest Framework**: Biblioteca utilizada para a criação e gerenciamento da API.

## Configurações Iniciais

O repositório foi estruturado visando atender às configurações essenciais para o funcionamento correto de uma API utilizando o Django Rest Framework. Estas configurações foram elaboradas com o intuito de facilitar o processo de construção de uma API robusta e de fácil manutenção, permitindo um desenvolvimento escalável e organizado.

## Estrutura da Aplicação

### Curso

- **Título**: Nome do curso.
- **URL**: Link que direciona para mais informações sobre o curso.

### Avaliação

- **Curso**: Referência ao curso que está sendo avaliado.
- **Nome**: Nome do usuário que realizou a avaliação.
- **Comentário**: Comentários sobre o curso.
- **Avaliação**: Nota atribuída ao curso.
- **Criação**: Data em que a avaliação foi criada.
- **Ativo**: Indica se a avaliação está ativa ou não.

## Objetivo

Este projeto foi desenvolvido com fins didáticos, visando o aprendizado das melhores práticas no uso do Django Rest Framework, especialmente no que tange às configurações iniciais e criação de uma API básica. Embora seja uma aplicação simples, ela representa a base para o desenvolvimento de sistemas mais complexos no futuro.

## Prints da API

![HTTP GET](/get.png)
![HTTP POST](/post.png)

