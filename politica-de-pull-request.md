# Políticas de Pull Request (PR) e Integração

## 1. Tamanho das PRs (Adoção de Lotes Pequenos)
* **Regra:** As submissões (*Pull Requests*) devem ser atômicas e focadas na resolução de um único problema ou funcionalidade. O limite prático recomendado é de **300 a 400 linhas de código alteradas**.
* **Fundamentação Teórica:** Esta regra é fundamentada no conceito de *small batches* (lotes pequenos) detalhado no livro *Continuous Delivery* (**HUMBLE; FARLEY, 2010**). Entregar código em lotes reduzidos não apenas facilita a revisão e diminui a carga cognitiva dos desenvolvedores, mas também minimiza a divergência estrutural do código, permitindo que falhas sejam identificadas e revertidas rapidamente, reduzindo o risco geral da integração.

## 2. Revisão Obrigatória por Pares (Code Review)
* **Regra:** É estritamente proibida a autoaprovação (*Self-Approval*). Nenhuma alteração pode ser fundida à branch principal sem a revisão e aprovação de pelo menos 1 (um) outro desenvolvedor da equipe.
* **Foco da Revisão:** Uma vez que as verificações de sintaxe e estilo (*Linting*) são delegadas ao pipeline automatizado, o esforço humano deve ser direcionado exclusivamente à lógica de negócios, à segurança da aplicação e à precisão da conversão de dados do ERP. Essa prática vai ao encontro das descobertas apresentadas em *Accelerate* (**FORSGREN; HUMBLE; KIM, 2018**), que demonstram como a revisão colaborativa não apenas previne falhas, mas atua como um vetor crucial para disseminar conhecimento técnico e aumentar o desempenho organizacional da equipe.

## 3. Automação e Testes como Requisito (CI)
* **Regra:** A branch `main` atua como uma ramificação protegida (*Protected Branch*). A opção de "Merge" permanecerá bloqueada sistemicamente até que o pipeline de CI (via GitHub Actions) retorne **100% de sucesso**.
* **Critérios de Validação:** O código proposto deve superar a análise estática (`ruff`), a compilação de sintaxe (`compileall`) e a suíte de testes unitários (`pytest`). Como estabelecido por **FOWLER (2006)** em seu artigo seminal, uma das bases da Integração Contínua é que todo artefato seja validado por um *build* auto-testável. Automatizar essas etapas elimina o trabalho braçal (*toil*), uma premissa defendida na abordagem de *Site Reliability Engineering* (**SRE / O'REILLY, 2016**), garantindo um *feedback* rápido sem depender de intervenções manuais.

## 4. Critérios Finais de Aprovação e Merge
Para que a submissão seja considerada apta e o código seja incorporado à base de produção (conforme os modelos práticos dos **Material dos Módulos**), o seguinte *checklist* deve ser cumprido:

**Pipeline Verde:** Testes e *linting* aprovados integralmente pela automação do GitHub Actions.
**Revisão Humana:** Aprovação formal (via plataforma) por um colega revisor.
**Zero Conflitos:** Ausência total de conflitos de integração com a branch `main`. A responsabilidade de resolver divergências na branch de origem recai sobre o autor.
**Integridade do Histórico:** A incorporação deve utilizar a estratégia de **Squash and Merge**. Isso converte múltiplos *commits* de trabalho e ajustes em um único *commit* semântico, assegurando um histórico linear, auditável e limpo na ramificação principal.

---

## Referências Bibliográficas

* **FORSGREN, Nicole; HUMBLE, Jez; KIM, Gene.** *Accelerate: The Science of Lean Software and DevOps*. IT Revolution Press, 2018.
* **FOWLER, Martin.** *Continuous Integration*. 2006. Disponível em: martinfowler.com.
* **HUMBLE, Jez; FARLEY, David.** *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*. Addison-Wesley, 2010.
* **IFPE.** *Material do Módulo – Blocos 1 (Versionamento), 2 (Integração Contínua), 3 (Automação e Toil) e 4 (Métricas e Impacto)*. Jaboatão dos Guararapes: Instituto Federal de Pernambuco, 2026.
* **MURPHY, Niall R. et al. (Ed.).** *Site Reliability Engineering: How Google Runs Production Systems*. O'Reilly Media, 2016.
