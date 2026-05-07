# IntegraVendas Middleware

[cite_start]A IntegraVendas é uma organização que desenvolve middlewares focados no setor de varejo, cujo principal produto é uma aplicação em Python responsável por sincronizar estoques de sistemas internos de lojas físicas com plataformas de e-commerce[cite: 72].

## 🛑 Problemas atuais

| Problema | Descrição |
| :--- | :--- |
| **Branches longas** | [cite_start]O trabalho isolado por semanas acumula divergências severas no código, tornando a resolução de conflitos no merge um processo exaustivo e perigoso[cite: 74]. |
| **Integração tardia e alto impacto financeiro (Falta de Testes)** | [cite_start]Sem testes automatizados a cada commit, erros na conversão de dados só são descobertos em produção, podendo gerar prejuízos reais para os lojistas (ex: zerar estoque indevidamente)[cite: 75]. |
| **Deploy manual e indisponibilidade (Toil)** | [cite_start]A atualização nos servidores é manual, aumentando a chance de falhas operacionais e causando indisponibilidade[cite: 76]. |

## ⚙️ Pipeline de CI

Este repositório inclui um workflow GitHub Actions em `.github/workflows/ci.yml`. O pipeline é disparado em `push` e `pull_request` na branch `main` e garante feedback rápido ao falhar nas etapas abaixo:

* Checkout do código (`actions/checkout@v4`)
* Setup de Python (`actions/setup-python@v5`)
* Cache de dependências com `actions/cache@v4`
* Instalação via `pip install -r requirements.txt`
* Lint com `ruff`
* Build com `python -m compileall src`
* [cite_start]Testes automatizados com `pytest` [cite: 88]
* Publicação de artefato opcional com `actions/upload-artifact@v4`

---
➡️ [Próxima página: Estratégia de Versionamento](estrategia-de-versionamento.md)
➡️ [Próxima página: Políticas de Pull Request (PR)](politica-de-pull-request.md)