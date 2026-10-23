---
name: plano-de-fuga-perfil
description: Revisa e reescreve o perfil do @planodefuga_br (foto, campo Nome, bio, link, categoria, destaques, primeira grade e posts fixados). Use quando o dono pedir pra mexer na bio ou no perfil.
---

# Perfil do Plano de Fuga

Adaptado de [sergebulaev/instagram-skills](https://github.com/sergebulaev/instagram-skills) (licença MIT, Copyright (c) 2026 Sergey Bulaev), skill `ig-profile-optimizer`. Vale tudo de `projeto-claude/regras.md` e da skill `plano-de-fuga-escrita` por cima disto.

A decisão de seguir acontece no topo do perfil: foto, Nome, bio, link e as primeiras linhas da grade. É isso que esta skill arruma.

## O que entregar

1. Nota das 9 partes (ok, melhorar, ruim).
2. As correções em ordem de impacto (Nome, bio e fixados primeiro).
3. Antes e depois de cada parte reescrita.
4. Plano de destaques e escolha dos fixados, com o motivo.

O dono aplica no app (a API não muda bio nem nome). Sempre mandar o texto pronto pra colar.

## As 9 partes

| # | Parte | Passa quando |
|---|---|---|
| 1 | **Foto** | o logo (avião saindo da bandeira) lê bem pequeno, com contraste. Sem rosto: o perfil é marca |
| 2 | **Nome** | marca + palavra que a pessoa digita na busca, até 30 caracteres. É o campo que a busca do Instagram indexa (o @ não é) |
| 3 | **@** | `planodefuga_br`, já definido |
| 4 | **Bio** | até 150 caracteres: o que a pessoa ganha + do que o perfil fala + um fato. Sem frase motivacional |
| 5 | **Link** | o grupo do Telegram, direto (R11: o objetivo do perfil é a comunidade no Telegram) |
| 6 | **Categoria** | um rótulo que reforça a bio sem repetir |
| 7 | **Destaques** | 4 a 6, na ordem da próxima pergunta de quem chega, capas no mesmo estilo, nome curto que não corta |
| 8 | **Primeira grade (9 posts)** | parece um conjunto: mesmo tom, legível de longe, mostra os temas (vistos, salários, política) |
| 9 | **Fixados (até 3)** | os 3 que melhor mostram o que a pessoa vai receber |

## Regras

- **Nome:** exemplo de formato "Plano de Fuga | Morar fora" (26 caracteres; contar com código antes de mandar).
- **Bio:** começa pelo que a pessoa ganha, não por quem somos. Sem travessão, sem emoji, sem "transforme sua vida". Fato concreto vale mais que promessa ("vistos, salários e impostos de cada país da Europa").
- A bio termina chamando pro grupo do Telegram (R11). O dono cola a bio no app.
- Nunca dado pessoal do dono, nem nome, nem cidade.
- Nunca entregar bio cortada ou nome de destaque que corta.
- **Destaques sugeridos:** Comece aqui, Vistos, Salários, Custo de vida, Eleição (temporário).
- **Fixados:** um guia que funcionou (o mais salvo), um comparativo, e na semana da eleição um post político.
- **Teste final:** olhando só foto, Nome, bio, link e a primeira linha da grade, um desconhecido sabe pra quem é o perfil e teria motivo pra seguir?

Antes de mandar pro dono, passar a bio pela checagem da skill de escrita e contar os caracteres com código, não de cabeça.
