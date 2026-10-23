---
name: plano-de-fuga-semana
description: Planeja os posts do Plano de Fuga por dia ou por semana (6 por dia, temas, países, horários, objetivo de cada post) e confere o equilíbrio político. Use quando o dono pedir mais posts, o plano da semana ou a fila de amanhã.
---

# Plano da semana do Plano de Fuga

Adaptado de [sergebulaev/instagram-skills](https://github.com/sergebulaev/instagram-skills) (licença MIT, Copyright (c) 2026 Sergey Bulaev), skill `ig-content-planner`. As regras de `projeto-claude/regras.md` vencem esta skill. Cada post do plano é feito depois com a skill `plano-de-fuga-post`.

## Volume e mistura (R5)

Por dia, 6 posts:
- 2 guias técnicos (carrossel): vistos, burocracia, impostos, custo de vida.
- 3 Reels: em geral um por guia e um da série política.
- 1 político (carrossel estilo jornal, R10).
- O comparativo (Brasil × país, profissão ou vida) entra num dos guias ou como post próprio.

## Pilares

| Pilar | O que entra | Objetivo principal |
|---|---|---|
| Vistos e burocracia | requisitos, valores, prazos, mudanças de lei | salvar |
| Dinheiro | salário mínimo e por área (tecnologia em destaque), impostos | mandar |
| Custo de vida | aluguel, mercado, transporte por cidade | salvar |
| Comparativo | Brasil × país, mesmo item e mesma unidade | mandar |
| Política (até 25/10) | Lula e Flávio, fatos do mesmo tipo (R2, R10) | mandar e comentar |

## Regras do plano

- **Variar o país** de post pra post (R8). Não repetir o mesmo país dois guias seguidos.
- **Variar o objetivo:** no dia, pelo menos um post pra salvar e um pra mandar.
- **Equilíbrio político:** na semana, Lula e Flávio aparecem com frequência e peso parecidos. Conferir post a post antes de fechar o plano.
- **Fato antes de pauta:** tema sem fonte primária encontrada sai do plano (ex.: o guia da Itália saiu por falta do texto da lei).
- **Contagem regressiva** nos políticos até o dia 25 ("Faltam N dias").
- **Domingo da eleição:** só post neutro de serviço (horário, voto no exterior), checado.

## Horários

A fila atual (UTC) é a referência: 12:00 guia, 14:00 Reel, 16:00 guia, 20:00 guia ou comparativo, 21:00 Reel, 23:00 Reel político, 23:30 carrossel político. Em Brasília é 3 horas a menos.

Depois de 2 semanas de dados, conferir nos insights do perfil quando o público está online e ajustar. Constância vale mais que volume: melhor 6 bons por dia no horário do que 6 feitos às pressas.

## Saída

Uma tabela por dia:

| Hora (UTC) | id | Tipo | Pilar | País | Gancho (molde) | Objetivo | Fonte |
|---|---|---|---|---|---|---|---|

Mais a conferência: país variou, os dois lados equilibrados, todo fato com fonte. O plano vai pro dono antes de produzir. Os posts produzidos voltam pra aprovação um a um ou em lote (R9) e entram no manifest com `auto: false` até o "pode".
