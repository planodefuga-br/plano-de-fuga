# Plano de Fuga · contexto do projeto (até 20/10/2026)

## O que é
Perfil de Instagram **Plano de Fuga**, reativado pra semana do 2º turno (25/10/2026, **Lula × Flávio Bolsonaro**). O objetivo é chegar no dia da eleição com o perfil cheio de post viral de política e de post útil sobre como sair do Brasil (bolsa, visto, trabalho fora). Depois da eleição, o perfil vira só conteúdo de "sair do Brasil".

## Decisões já tomadas
- **Perfil é marca, não pessoa.** Nada de dados pessoais do dono por enquanto: USP, empregos, cidade, valores de bolsa, YouTube pessoal. Fala como "a gente" ou de forma impessoal.
- **Política ataca os dois lados com o mesmo peso**, pra atrair o máximo de gente. Ataca político, nunca eleitor. Cada post ou Reel termina puxando o outro lado.
- **Fato sempre completo.** Lula: condenações anuladas por incompetência da Vara de Curitiba, sem julgamento do mérito. Flávio: denúncia da rachadinha arquivada depois que as provas foram anuladas por foro. Flávio/Vorcaro: ele admite que cobrou R$ 134 mi pra um filme sobre o pai e nega crime. Se a pessoa nega, dizer que nega.
- **Manchetes reproduzidas LITERALMENTE**, com veículo e data, na nossa tipografia. Nada de print ou logo de jornal, nada de imagem gerada de político.
- **Estética em dois mundos com paralelo mínimo:**
  - Marca e guias: página de passaporte (verde-água, guilhoché, azul-marinho, carimbos).
  - Política: recorte de jornal sombrio (fundo quase preto, papel rasgado, carimbo vermelho ANULADO / ARQUIVADO / PRESO / CONDENADO).
  - Os dois compartilham a linha MRZ de passaporte no rodapé e o carimbo "SAÍDA · PLANO DE FUGA" no fim.
- **Vídeo dá mais engajamento que carrossel.** Por enquanto os Reels são simples: manchetes que entram com impacto no ritmo de **Happy Nation** (Ace of Base). Mais pra frente o dono vai gravar vídeos com o próprio rosto.
- **Música:** a API do Instagram não coloca música da biblioteca e a faixa tem direito autoral. Por isso os Reels saem mudos e o dono **posta à mão pelo app**, escolhendo Happy Nation (30 s por dia). Carrosséis e guias saem automáticos.
- **Publicação via GitHub Actions** (não N8N, pra não misturar com servidor de trabalho). Imagens servidas pelo GitHub Pages. Token do Instagram com "API com Login do Instagram", sem precisar de página do Facebook.
- Quer **tarefa agendada diária** no Claude que gere os guias do dia seguinte e suba pro repositório.

## Calendário (horário de Brasília)
| Dia | 9h guia (auto) | 20h Reel (manual, Happy Nation) | 20h30 carrossel (auto) |
|---|---|---|---|
| Ter 20/10 | nada | Faltam 5: Lula, Lava Jato, anulação | Dois processos, nenhum julgamento |
| Qua 21/10 | Visto de procura de trabalho acabou | Faltam 4: Flávio + Vorcaro (+ Lula recebeu Vorcaro) | Vorcaro, "amigos de todos os poderes" |
| Qui 22/10 | Erasmus Mundus | Faltam 3: Bolsonaro, coveiro, golpe, mansão, rachadinha | Mensalão × trama golpista |
| Sex 23/10 | Fundación Carolina | Faltam 2: mensalão, Petrobras, INSS | INSS nos dois governos |
| Sáb 24/10 | Visto D8 nômade digital | Falta 1: montagem dos dois lados | A semana num slide |
| Dom 25/10 | 8h: voto no exterior | nada | 10h: "Hoje" |

## Estado atual
- **Pronto:** 16 posts (11 carrosséis + 5 Reels), legendas com fontes, publicador, workflow do GitHub, instruções do projeto. Está tudo em `~/Documents/plano-de-fuga`.
- **Revisão:** existe uma página de aprovação como artifact ("Plano de Fuga · Semana do 2º turno").
- **Hoje (20/10):** Reel e carrossel mandados pro celular pra postar à mão.

## Pendências
1. **Conectar o GitHub ao Claude** (claude.ai → Configurações → Conectores → GitHub). Depois disso: criar o repo `plano-de-fuga`, ligar o Pages em `/docs`, configurar a variável `PAGES_URL` e dar push.
2. **Gerar o token do Instagram** e colar como secret `IG_TOKEN` no repo (passo a passo em `SETUP.md`). Conta do Plano de Fuga como profissional (Criador).
3. **Criar a tarefa agendada diária** com o texto de `projeto-claude/tarefa-diaria.md`, trocando `{OWNER}` pelo usuário do GitHub.
4. O dono tem uma **lista de mudanças** pra fazer nos posts e no visual (ainda não passou).

## Como a pasta funciona
- `content/content.py`: todos os textos. `H` = manchetes literais; `POL` = carrosséis de política; `GUIA` = guias; `REELS` = roteiros dos vídeos.
- `render/templates.py`: visual (HTML/CSS dos dois mundos). `render/build.py`: gera os JPEGs em `docs/<id>/` e os cards dos Reels. `render/reels.py`: monta os MP4 em `docs/reels/` (corte a cada ~2,8 s, grão, carimbo que "bate", áudio mudo).
- Pra regerar: `python render/build.py [ids]` e depois `python render/reels.py [ids]`. Precisa de Python com Playwright/Chromium, numpy, Pillow e ffmpeg. **Rode os Reels um de cada vez**, porque rodar em paralelo corrompeu os MP4 uma vez.
- `docs/manifest.json`: horário (UTC), tipo, legenda e mídia de cada post. `auto: false` nos Reels.
- `publisher/publish.py` + `.github/workflows/publicar.yml`: a cada 15 min publica o que passou do horário (1 por execução). Pula post com mais de 6 h de atraso e para depois de 3 falhas.

## Fatos de apoio (checados em out/2026)
- Datafolha de 13 a 15/10: Flávio 47%, Lula 45% (válidos 51% × 49%), margem de 2 pontos.
- Vorcaro (Banco Master): preso em 04/03/2026; R$ 40,6 bi em dívidas, ~800 mil investidores; disse ter "amigos de todos os poderes".
- Lula recebeu Vorcaro no Planalto em 04/12/2024, sem registro na agenda (Poder360).
- Flávio: reunião na casa de Vorcaro em 20/08/2025 (Poder360). Foi noticiada uma decisão judicial mandando apagar conteúdo FALSO que ligava Flávio ao caso Master, então usar só fato admitido ou publicado por veículo grande.
- Visto de procura de trabalho de Portugal acabou em 23/10/2025 (Lei 61/2025); D8 pede €3.680/mês em 2026; Erasmus Mundus paga até €1.400/mês; Fundación Carolina tem referência de €1.200/mês.
- Lista completa de manchetes em `projeto-claude/manchetes-verificadas.md`.
## Descoberto em 20/10/2026
- Existe a Instagram Audio API: busca música e som em alta e anexa ao Reel na publicação (`audio_configuration`). Exige conta Business ou Criador **com página do Facebook ligada** e app no modo "API com Login do Facebook" (não funciona com "Login do Instagram", que era o plano no SETUP.md). O catálogo pode ser diferente do app, então Happy Nation precisa ser testada. Fonte: developers.facebook.com/docs/instagram-platform/content-publishing/audio-api/
- GitHub conectado. Repositório: github.com/planodefuga-br/plano-de-fuga (org separada, pra não expor a conta pessoal). Subido em 20/10 só o código, com manifest vazio e agendador desligado (cron comentado no workflow). Pages: https://planodefuga-br.github.io/plano-de-fuga (ligar em Settings > Pages, o Claude não tem acesso a essa API). Página do Facebook já ligada ao Instagram.
- 20/10 22h56: teste do publicador ok. Token (API com Login do Facebook, app "Plano de Fuga Publisher", caso de uso Instagram) enxerga a conta planodefuga_br ligada à página Plano de Fuga. Limite: 100 publicações por 24h. GitHub Pages ligado. Teste roda sozinho a cada push em publisher/publish.py e grava publisher/teste.json no repo.
- Audio API devolve lista VAZIA pra qualquer busca, até a de músicas em alta (sem erro). Música automática via API não funciona por enquanto. Decidido (R6): Happy Nation embutida no vídeo + teste diário da API.
- 20/10 19h34 BRT: primeiro post no ar (n1-salario-minimo, formato tela do celular, media_id 17997461142030932). Agendador ligado (cron a cada 15 min) e push no manifest publica na hora. Próximo: m1-vorcaro (manchete de jornal) às 23h45 UTC.
- Promessa feita no post n1: "no próximo post a gente faz essa conta" (custo de vida). Cumprir.
