# 📌 Sistema de Controle de EPIs

## 1) Escopo resumido
*Objetivo:* controlar cadastro de EPIs, colaboradores e o empréstimo/devolução de itens.  

*Perfis de usuário:*  
- ADMIN  
- TECNICO_SST  
- ALMOXARIFE  
- COLABORADOR  

(campo perfil em *usuario*)  

---

## 2) DER (conforme as 5 tabelas)
![Image](https://github.com/user-attachments/assets/ea2f7309-7610-4c5a-9db0-429bc6bc41e5)

--- 
## 3) Diagrama de Casos de Uso
flowchart LR
  subgraph Atores
    U1[Administrador]
    U2[Técnico de SST]
    U3[Almoxarife]
    U4[Colaborador]
  end

  UC1[(Autenticar-se)]
  UC2[(Gerir Usuários)]
  UC3[(Gerir Colaboradores)]
  UC4[(Gerir EPIs)]
  UC5[(Registrar Empréstimo)]
  UC6[(Registrar Devolução)]
  UC7[(Consultar Pendências/Histórico)]

  U1 --- UC1
  U2 --- UC1
  U3 --- UC1
  U4 --- UC1

  U1 --- UC2
  U2 --- UC4
  U3 --- UC3
  U3 --- UC4
  U3 --- UC5
  U3 --- UC6
  U2 --- UC7
  U3 --- UC7
  U4 --- UC7

Fluxos principais (resumidos)

Empréstimo: selecionar colaborador → adicionar EPIs/quantidades → salvar (gera emprestimo + emprestimo_item e baixa simples em epi.estoque).

Devolução: localizar empréstimo/itens pendentes → informar retornos → atualizar devolvido_em e somar no epi.estoque.

---

## 4) Requisitos Funcionais

RF01 — Autenticação e perfil: login por e-mail/senha; acesso conforme perfil.

RF02 — Cadastro de colaboradores: CRUD básico; validações de CPF e matrícula únicos.

RF03 — Cadastro de EPIs: CRUD básico; controle simples de estoque (inteiro), ca_numero e ca_validade (opcional).

RF04 — Empréstimo: criar cabeçalho (emprestimo) e itens (emprestimo_item) com quantidade; reduzir epi.estoque.

RF05 — Devolução: registrar devolvido_em por item; somar de volta no epi.estoque.

RF06 — Consulta: listar pendências de devolução por colaborador e histórico por período.

RF07 — Alertas simples (opcional): destacar itens com previsão vencida ou CA expirado.

---

## 5) Requisitos Não Funcionais

RNF01 — Usabilidade: até 3 cliques para registrar empréstimo; layout responsivo.

RNF02 — Segurança: senha com hash; perfis aplicados no backend; sessões expiram por inatividade.

RNF03 — Desempenho: listagens comuns em até 2s em rede local.

RNF04 — Disponibilidade: uso em horário comercial; backup diário do banco.

RNF05 — Manutenibilidade: arquitetura em camadas (API, serviço, persistência) + logs mínimos de erro.

RNF06 — Portabilidade: MySQL 8.0+, compatível com Workbench.

---

## 6) Wireframes (mínimos)
Login
+-------------------------+
|  LOGO                   |
|  Email: [_]   |
|  Senha: [_]   |
|  [ Entrar ]             |
+-------------------------+

Dashboard
+----------------------------------------------------+
| Pendentes de Devolução: [12]  | Empréstimos hoje: 5|
| CA(s) de EPI vencidos: 2 (alerta)                  |
| Busca rápida: [ Colaborador / EPI ]                |
+----------------------------------------------------+

EPIs (CRUD + estoque simples)
[ + Novo EPI ]  [Buscar: __________ ]
| Código | Nome | Tamanho | CA | Validade | Estoque | Ações |

Colaboradores
[ + Novo Colaborador ] [Buscar: _______ ]
| Matrícula | Nome | CPF | Ativo | Ações |

Empréstimos
[ + Novo Empréstimo ] [Buscar por colaborador: ______ ]
| Nº | Colaborador | Itens Pendentes | Prev. Devolução | Status | Ações |

Novo Empréstimo
Colaborador: [selecionar]
Itens:
  [ + Adicionar EPI ]
   -> EPI [select]  Quantidade []  [Remover]
Previsão devolução: [data/hora]
[ Confirmar ]  [ Cancelar ]

Devolução
Filtro: [Colaborador] [Somente pendentes]
| Empréstimo | EPI | Qtde | Entregue em | Devolver [] | Ação |
[ Confirmar devolução ]

--- 

## 7) Regras de Negócio

RB01: quantidade > 0 em emprestimo_item.

RB02: Não permitir saída se epi.estoque < quantidade.

RB03: Devolução soma quantidade ao epi.estoque e preenche devolvido_em.

RB04: Se ca_validade existir e estiver vencida, exibir aviso (não bloqueia no mínimo).

RB05: status do empréstimo vai para FECHADO quando todos os itens forem devolvidos.

---

## 8) Critérios de Aceite (MVP)

✅ Cadastrar usuários, colaboradores e EPIs.
✅ Criar empréstimo com 1..N itens e reduzir estoque.
✅ Registrar devolução total/parcial e recompor estoque.
✅ Listar pendências por colaborador e fechar empréstimo quando não houver mais pendências.
✅ Exportar listagens em CSV (opcional).
