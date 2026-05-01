## Políticas de Pull Request (PR)

## 1. Tamanho das PRs (Lotes Pequenos)
* **Regra:** As PRs devem ser curtas e focadas em resolver apenas um problema (uma única funcionalidade ou correção de bug). Recomenda-se um limite prático de **300 a 400 linhas de código alteradas**.
* **Justificativa:** Alinhado ao princípio de *Continuous Delivery*, trabalhar em lotes pequenos (*small batches*) facilita a revisão cognitiva por parte dos outros desenvolvedores, reduz a divergência estrutural do código e torna a identificação de falhas muito mais rápida.

## 2. Revisão Obrigatória (Code Review)
* **Regra:** Nenhuma PR pode ser aprovada pelo seu próprio autor (**Proibido Self-Approval**). É exigida a revisão e aprovação de pelo menos 1 (um) outro desenvolvedor da equipe.
* **Foco da Revisão:** Como a verificação de sintaxe e formatação (*Linting*) é automatizada pelo pipeline, o revisor humano deve focar exclusivamente na lógica de negócios, segurança e na eficiência da conversão de dados do ERP para o E-commerce.

## 3. Testes Automatizados como Requisito (CI)
* **Regra:** A branch `main` é configurada como protegida (*Protected Branch*). O botão de "Merge" fica permanentemente bloqueado até que o pipeline de Integração Contínua (GitHub Actions) seja concluído com **status 100% de sucesso**.
* **Critérios de CI:** O código submetido na PR deve passar obrigatoriamente pela análise estática (`ruff`), compilação da sintaxe (`compileall`) e pelos testes automatizados (`pytest`). Se um novo código quebrar a lógica de conversão do estoque, o merge é imediatamente impedido.

## 4. Critérios Finais de Aprovação e Merge
Para que uma PR seja considerada "Aprovada" e seu código integrado à branch `main`, ela deve cumprir rigorosamente o seguinte checklist:

**Pipeline de CI aprovado:** Testes e Linting sem nenhuma falha ("verdes").
**Aprovação manual:** Pelo menos um *Code Review* favorável realizado por um colega.
**Sem conflitos de base:** Ausência total de conflitos de merge com a branch `main` (se houver, devem ser resolvidos na branch de origem pelo autor).
**Histórico Limpo:** O merge deve ser feito utilizando a estratégia **Squash and merge**, garantindo que o histórico da `main` permaneça linear, limpo e sem commits desnecessários de trabalho em andamento (WIP).
