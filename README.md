 ## IntegraVendas

A **InteraVendas** desenvolve middleware focado em varejo. Nosso principal produto é uma aplicação que roda em segundo plano sincronizando, de hora em hora, o estoque de sistemas internos de lojas físicas com E-commerce atráves de API.

## Problemas atuais

| Problema                                                          | Descrição                                                                                                                                                                                   |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Branches longas**                                             | Eles desenvolvem em branches separadas por semanas.                                                                                                                                         |
| **Integração tardia e alto impacto financeiro (Falta de Testes)** | Não há um pipeline de Integração Contínua (CI). Como não existem testes automatizados validando a transformação dos dados a cada commit, erros de conversão só são descobertos em produção. |
| **Deploy manual e indisponibilidade (Toil)**                      | A atualização do sistema é um processo manual e doloroso.                                                                                                                                   |

## Pipeline de CI

Este repositório inclui um workflow GitHub Actions em `.github/workflows/ci.yml`.
O pipeline é disparado em `push` e `pull_request` na branch `main` e garante feedback rápido ao falhar nas etapas abaixo:

- Checkout do código (`actions/checkout@v4`)
- Setup de Python (`actions/setup-python@v5`)
- Cache de dependências com `actions/cache@v4`
- Instalação via `pip install -r requirements.txt`
- Lint com `ruff`
- Build com `python -m compileall src`
- Testes com `pytest`
- Publicação de artefato opcional com `actions/upload-artifact@v4`
