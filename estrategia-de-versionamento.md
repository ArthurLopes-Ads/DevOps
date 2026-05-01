## Justificativa Técnica

**Redução de Riscos e Aumento de Previsibilidade no IntegraVendas**

As diretrizes arquiteturais e operacionais adotadas para o middleware IntegraVendas resolvem diretamente os gargalos de desenvolvimento descritos no escopo do projeto, embasando-se nas melhores práticas da engenharia de software moderna.

### I. Branches curtas e merges frequentes
O modelo anterior de "branches separadas por semanas" resultava em incompatibilidades severas na integração ERP/E-commerce. Segundo Jez Humble e David Farley no livro ***Continuous Delivery***, trabalhar em pequenos lotes (*Small Batches*) e promover merges frequentes na branch principal diminui drasticamente a divergência do código. Isso evita o chamado *integration hell* (conflitos gigantescos) e mantém o sistema de estoque sempre passível de ser implantado.

### II. Feedback rápido via Pipeline Automatizado
Historicamente, erros de conversão de dados do IntegraVendas eram descobertos apenas em produção, causando alto impacto financeiro (ex: zerar estoque indevidamente). Conforme descrito no livro ***Acelerar (Accelerate)*** (Nicole Forsgren et al.), equipes de alta performance dependem da detecção antecipada de falhas. O pipeline configurado no GitHub Actions — executando `ruff` (lint), `compileall` e `pytest` — fornece feedback em poucos minutos. Se uma regra de negócio for violada, o erro é barrado logo após o commit.

### III. Builds reprodutíveis e controle de ambiente
O workflow YAML define explicitamente a versão do *runtime* (Python 3.13) e gerencia dependências estritas via `requirements.txt` armazenado em cache (`actions/setup-python@v5`). Este isolamento atende ao princípio de builds reprodutíveis citado em ***Continuous Delivery***. Ele elimina a falácia do "na minha máquina funciona", garantindo que a validação de código ocorra em um ambiente idêntico e consistente toda vez.

### IV. Redução de Toil e Alinhamento SRE
O processo antigo de implantação do IntegraVendas exigia acesso via SSH, parada manual do serviço e reinicialização, caracterizando alto nível de *toil* (trabalho manual, repetitivo e sem valor duradouro). As práticas de ***Site Reliability Engineering (SRE)*** do Google preconizam a automação severa do *toil*. Ao automatizar os testes e a publicação do artefato no CI (`upload-artifact`), a equipe garante que a branch `main` é segura, pavimentando o caminho para um Deploy Contínuo (CD) 100% automatizado, liberando o time para focar em novas integrações de varejo.

### V. Cultura de Qualidade através de PRs
A exigência de *Code Review* nas políticas de Pull Request transcende o aspecto punitivo ou de bloqueio. O livro ***Acelerar*** demonstra que a revisão assíncrona por pares eleva significativamente a qualidade do código. No caso de lógicas sensíveis como conciliação de vendas, isso promove o compartilhamento de conhecimento sobre as regras do negócio e evita a formação de silos de conhecimento técnico entre os desenvolvedores.
