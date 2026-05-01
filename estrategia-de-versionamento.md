# Estratégia de Versionamento

## 1. Estratégia de Branching (GitHub Flow)

Baseando-se nas diretrizes abordadas no **Material do Módulo (Bloco 1)**, adotamos o **GitHub Flow** por ser leve e orientado à Integração Contínua (CI). 

Esta escolha rechaça o uso de *branches* de longa duração. Como argumentado por **Humble e Farley (2010)** em *Continuous Delivery*, isolar desenvolvedores em ramificações por semanas gera o "inferno da integração" (*integration hell*). Para evitar isso, seguimos a "Regra da Mainline" definida por **Fowler (2006)**, onde o código é integrado frequentemente a um tronco principal único.

| Tipo de Branch | Nomenclatura | Origem | Destino | Regra de Uso e Fundamentação |
| :--- | :--- | :--- | :--- | :--- |
| **Principal** | `main` | - | - | Atua como a **fonte única da verdade** (Fowler, 2006). Deve estar sempre estável e pronta para produção. Commits diretos são estritamente bloqueados. |
| **Trabalho** | `feature/*` ou `fix/*` | `main` | `main` | Branches de vida curta (horas/dias). A pesquisa de **Forsgren et al. (2018)** comprova que ramificações com vida útil inferior a um dia são indicadores chave de equipes de alta performance. |

## 2. Políticas de Pull Request (PR)

Todo o código desenvolvido nas *branches* de trabalho deve retornar à `main` exclusivamente via submissão de um *Pull Request* (PR), regido pelas seguintes normativas:

* **Lotes Pequenos (*Small Batches*):** As alterações devem ser atômicas e focadas em uma única tarefa funcional (limite ideal de 300 a 400 linhas). Segundo **Humble e Farley (2010)**, processar lotes pequenos reduz drasticamente o risco de quebras críticas, pois falhas menores são mais fáceis de isolar e reverter.
* **Revisão Obrigatória (*Peer Review*):** É proibida a autoaprovação (*self-approval*). Todo PR exige revisão de pelo menos um colega. Como evidenciado no livro *Accelerate* (**Forsgren et al., 2018**), essa prática não é apenas um portão de segurança, mas o principal mecanismo para quebrar silos técnicos e compartilhar conhecimento sobre a lógica de conversão do IntegraVendas.
* **Validação Automatizada:** A abertura da PR aciona automaticamente o pipeline de CI no GitHub Actions. **Fowler (2006)** estabelece que um código só está integrado se passar por um *build* auto-testável, garantindo a integridade antes do olhar humano.

## 3. Critérios de Merge e Integração

O aceite do código na ramificação principal só será habilitado se cumprir 100% do seguinte *checklist* de qualidade:

1. **Pipeline Verde e Feedback Rápido:** O status do CI deve estar totalmente aprovado (análise com `ruff` e testes com `pytest`). O bloqueio imediato de código falho fornece o "feedback rápido" essencial citado em *Accelerate* (**Forsgren et al., 2018**), impedindo degradações no sistema.
2. **Eliminação de *Toil* (Build Reprodutível):** A execução limpa do pipeline garante que as dependências estão controladas. Alinhado aos princípios de *Site Reliability Engineering* (**SRE / O'Reilly, 2016**), automatizar essa verificação elimina o *toil* (trabalho manual sem valor), e garante que o artefato não sofra da síndrome "na minha máquina funciona" (**Humble; Farley, 2010**).
3. **Aprovação Humana e Resolução de Conflitos:** Ausência total de conflitos estruturais com a `main` e validação semântica pelo revisor.
4. **Estratégia *Squash and Merge*:** O *merge* aglutinará os *commits* de desenvolvimento em um único *commit* final semântico, mantendo o histórico rastreável e facilitando auditorias futuras.

## 4. Política de Versionamento (Release Management)

A evolução do middleware segue o **Versionamento Semântico (SemVer)** no formato `MAJOR.MINOR.PATCH` (Exemplo: `v2.1.0`). Esta padronização apoia o gerenciamento seguro de configurações defendido em *Continuous Delivery*:
* **MAJOR:** Mudanças estruturais e quebras de compatibilidade na arquitetura (ex: troca no modelo de dados do ERP).
* **MINOR:** Novas funcionalidades compatíveis com a versão atual (ex: suporte a uma nova API Shopify).
* **PATCH:** Correções de *bugs* de sincronização e ajustes internos inertes ao cliente.

---

## 5. Referências Bibliográficas

* **FORSGREN, N.; HUMBLE, J.; KIM, G.** *Accelerate: The Science of Lean Software and DevOps*. IT Revolution Press, 2018.
* **FOWLER, M.** *Continuous Integration*. 2006. Disponível em: martinfowler.com/articles/continuousIntegration.html. 
* **HUMBLE, J.; FARLEY, D.** *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*. Addison-Wesley, 2010.
* **IFPE.** *Material do Módulo – Blocos 1 (Versionamento), 2 (Integração Contínua), 3 (Automação e Toil) e 4 (Métricas e Impacto)*. Jaboatão dos Guararapes: Instituto Federal de Pernambuco, 2026.
* **MURPHY, N. R. et al.** (Ed.). *Site Reliability Engineering: How Google Runs Production Systems*. O'Reilly Media, 2016.
