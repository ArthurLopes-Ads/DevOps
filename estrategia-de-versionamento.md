## 1. Estratégia de Branching (GitHub Flow)
Baseando-se nas diretrizes de versionamento abordadas no **Material do Módulo (Bloco 1)**, adotamos o GitHub Flow para garantir um ciclo de entregas contínuo e focado na estabilidade do middleware.

| Tipo de Branch | Nomenclatura | Origem | Destino | Regra de Uso |
| :--- | :--- | :--- | :--- | :--- |
| **Principal** | `main` | - | - | Representa a fonte única da verdade e deve estar sempre pronta para produção. Commits diretos são estritamente bloqueados. |
| **Trabalho** | `feature/*` ou `fix/*` | `main` | `main` | Branches de vida curta (horas/dias). Utilizadas para desenvolver integrações de ERP/E-commerce ou corrigir bugs, retornando à origem via Pull Request rapidamente. |

## 2. Políticas de Pull Request (PR)
Todo código desenvolvido nas branches de trabalho deve retornar à `main` exclusivamente via Pull Request, seguindo as regras:
* **Lotes Pequenos (Small Batches):** As alterações devem ser curtas e focadas em uma única tarefa funcional (limite ideal de 300 a 400 linhas de código).
* **Revisão Obrigatória (Peer Review):** É proibida a autoaprovação (*self-approval*). Todo PR exige revisão de pelo menos 1 (um) desenvolvedor da equipe, com foco exclusivo na lógica de negócio e segurança da sincronização dos dados.
* **Validação Automatizada:** A abertura da PR aciona automaticamente o pipeline de CI (GitHub Actions) para garantir a integridade do código antes da avaliação humana.

## 3. Critérios de Merge
A integração do código para a branch principal só será habilitada se cumprir 100% do seguinte checklist:
**Pipeline Verde:** Status do pipeline de CI totalmente aprovado (análise estática com `ruff` e testes com `pytest` passando sem falhas).
**Aprovação Humana:** Aprovação formal recebida de um revisor.
**Resolução de Conflitos:** Ausência total de conflitos de código com a branch `main`.
**Estratégia de Integração:** O merge deve ser feito obrigatoriamente utilizando **Squash and merge**, aglutinando os commits de desenvolvimento em um único commit semântico para manter o histórico linear e rastreável.

## 4. Política de Versionamento
Adota-se o **Versionamento Semântico (SemVer)** no formato `MAJOR.MINOR.PATCH` (Exemplo: `v2.1.0`):
* **MAJOR:** Mudanças estruturais e quebras de compatibilidade na arquitetura de integração.
* **MINOR:** Novas funcionalidades compatíveis com a versão atual (ex: suporte a uma nova API de E-commerce).
* **PATCH:** Correções de bugs e ajustes internos que não afetam integrações externas.
