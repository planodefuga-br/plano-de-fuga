# Regras do Plano de Fuga

Regras ditadas pelo dono. Valem pra todo texto do projeto (slide, legenda, roteiro de Reel, guia, bio, resposta a comentário) e ficam acima de qualquer padrão de estilo. Quando uma regra daqui conflitar com outro arquivo, esta vence, a menos que o dono diga o contrário.

## R1 · Nada de escrita com cara de IA (20/10/2026)

**Regra:** nenhum texto pode ter linguagem genérica de IA. A informação continua toda lá: corta o enfeite, não o fato. No lugar de abstração, verbo concreto.

**Proibido:**
- **Travessão (U+2014 ou U+2013): NUNCA, sem exceção.** Nem em slide, legenda, roteiro ou manchete de jornal. Hífen ("-") pode. Manchete que vem com travessão é reproduzida com hífen no lugar (decisão do dono, 20/10/2026).
- Abertura panorâmica: "Em um mundo cada vez mais...", "Nos últimos anos...", "Quando se fala em...".
- Metáfora vaga: "abrir portas", "um mar de oportunidades", "a jornada", "o divisor de águas", "peça-chave".
- Paralelismo negativo: "não é apenas X, é Y", "não se trata de X, mas de Y", "mais do que X, é Y" (também quando vem em duas frases).
- Excesso de conectivos: "além disso", "ademais", "no entanto", "por outro lado", "vale ressaltar", "é importante destacar", "nesse sentido".
- Adjetivo abstrato e inflado: "fundamental", "crucial", "essencial", "incrível", "transformador", "rico", "vibrante", "único".

**Também vigiar (verbete da Wikipedia):**
- Simbolismo inflado: "é um marco", "desempenha papel vital", "consolida", "profundamente enraizado".
- Tom de folheto turístico: "de tirar o fôlego", "imperdível", "rica herança cultural".
- Opinião disfarçada de informação: "vale notar que", "não podemos deixar de mencionar".
- Gerúndio de comentário vazio no fim da frase: "..., garantindo mais segurança", "..., destacando a importância de...".
- Atribuição vaga: "especialistas apontam", "estudos mostram", "críticos dizem" (sem dizer quem). Sempre nomear a fonte.
- Trio automático de adjetivos ou itens ("rápido, simples e eficiente") só pra dar ritmo.
- Negrito em excesso e lista com rótulo em negrito que só repete o rótulo na frase seguinte.
- Fecho de moral: "No fim das contas...", "Em resumo...", "O futuro é promissor".

**Como fazer:**
- Sujeito + verbo concreto + fato. "A bolsa paga €1.400 por mês", e não "a bolsa oferece um apoio financeiro significativo".
- Número, data, nome e fonte no lugar de adjetivo.
- Frase curta. Uma ideia por frase.
- Antes de entregar, reler procurando cada item da lista acima.

**Skill:** a regra virou a skill `plano-de-fuga-escrita` (cópia em `projeto-claude/skill-escrita/SKILL.md`), feita a partir do verbete completo. Ela é a referência detalhada. Dois acréscimos que vieram do verbete:
- Sem travessão, varie a pontuação (dois-pontos, parênteses, pergunta) e o tamanho das frases. Texto só com vírgula e ponto, tudo com 8 a 15 palavras, também denuncia IA.
- Escrita humana usa "é", "tem", "há", verbo comum, afirmação definitiva quando a fonte sustenta, e repete a palavra certa em vez de trocar por sinônimo.

**Base:** [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)

## R2 · Mesmo rigor, nenhum lado melhor (20/10/2026)

**Regra (palavras do dono):** os dois lados têm que ter o mesmo rigor, mas nunca fazendo parecer que um lado é melhor, ou menos pior, que o outro. E sem falsa equivalência.

**Na prática:**
- Equilíbrio pela escolha dos fatos, não por emparelhar coisas desiguais. Cada lado recebe os seus fatos mais fortes, cada um com o tamanho e o status jurídico reais.
- Só comparar lado a lado o que é do mesmo tipo (condenação com condenação, anulação com anulação, o próprio político com o próprio político). Se não é do mesmo tipo, não vira "os dois fizeram igual".
- Dizer a diferença quando ela existe: quem foi réu e quem não foi, valor, tribunal, se é o candidato ou um parente.
- Ao longo do dia e da semana, os dois lados aparecem com frequência e intensidade parecidas. Nenhum post termina deixando um lado com cara de opção menos pior.
- Substitui a regra antiga "os dois lados com o mesmo peso" das instruções.

## R3 · Reel não é carrossel (20/10/2026)

**Regra:** Reel é vídeo vertical nativo, não apresentação de slides. Proibido reaproveitar a arte do carrossel como frame de Reel.

**Na prática:**
- Nada de rodapé, nota pequena, número de página, linha MRZ ou fonte em letra miúda dentro do Reel. Fonte vai na legenda (ou um selo curto e legível, se for indispensável).
- Texto grande, poucas palavras por tela, na área segura.
- Movimento de verdade: vídeo real, corte no ritmo da música, zoom, texto que entra e sai.
- Uma ideia por tela. Se precisa de parágrafo, é carrossel, não Reel.

## R4 · Nada manual (20/10/2026)

**Regra:** o dono não posta nada à mão. Todo post (carrossel e Reel) sai pela publicação automática. O máximo que o dono faz é baixar vídeos e colocar na pasta. Preferência: material de licença aberta pesquisado por nós.

## R5 · Volume e pilares até a eleição (20/10/2026)

- Por dia: 2 guias técnicos, 3 Reels, 1 post político, mais 1 post de comparação (Brasil × outro país, profissão, vida). Total: 6 posts por dia (confirmado pelo dono em 20/10/2026).
- Comparação não precisa ter "Brasil vs Europa" no título. Qualquer post que compare.
- Reels de vídeo real: simples e sombrios. Cenas da Lava Jato, Lula e Bolsonaro presos, 8 de janeiro, discursos polêmicos dos dois (pandemia, mulheres, gays, economia), cortados no ritmo de música sombria e em alta.
- Todos os 16 posts atuais serão substituídos pelos formatos novos, só quando o dono mandar.
- Ordem: primeiro destravar a publicação automática.

## R6 · Música dentro do vídeo (20/10/2026)

- A Happy Nation vai embutida no MP4 dos Reels. O dono confia que o Instagram reconhece a faixa (já aconteceu com vídeos dele).
- O publicador tenta a Audio API primeiro. Se ela achar a música, anexa pela API. Se não, sai com a faixa do vídeo.
- Um teste diário (workflow "Testar Audio API", 11h17 UTC) confere se a API já libera catálogo. Resultado em `publisher/teste.json` no repositório.
- O arquivo de áudio é fornecido pelo dono e fica em `assets/audio/` (não vai pro repositório público).

## R7 · Nada com cara de slide ou colagem (20/10/2026)

- Nem carrossel nem Reel pode parecer apresentação de slides ou "post de IA/Canva": nada de composição diagramada, forma geométrica no lugar de foto, adesivo, fita, papel inclinado, cartão com rótulo.
- Vivo = parece visto ou vivido por alguém, não diagramado.
- Política: formato mini documentário (fotos reais grandes, sangrando, uma linha de texto por foto, tom escuro e frio, desilusão).
- Guias e comparativos: testar câmera de celular e mini documentário. "Tela do celular" (bloco de notas, print) foi DESCARTADA em 20/10: parece improvisado, como se o dono tivesse postado às pressas.
- Ajuste do dono em 20/10: pra carrossel, o visual desenhado antigo (passaporte, recorte de jornal) era "bem melhor". A meta é melhorar aquilo, mais visual, e não abandonar o design. O que sai: rodapé com titulozinho, número de página, linha MRZ e outros enfeites de apresentação.
- A marca (logo, perfil) é mínima. A identidade vem do tom das fotos e do texto.
- Fotos de banco com licença livre pra uso comercial (Unsplash, Pexels, Wikimedia, Agência Brasil) quando não houver foto própria.

## R8 · Europa inteira, vários temas (20/10/2026)

- O perfil fala de todos os países da Europa (Portugal, Espanha, Itália, Alemanha, Irlanda, França, Holanda etc.), não só Portugal. Variar o país de post pra post.
- Temas, além de salário mínimo: salário médio por área (com destaque pra tecnologia, que é a área do dono), vistos, burocracia, impostos, custo de vida, vida no dia a dia.
- Brasil × país X pode ser um país por post ou vários países no mesmo post.

## R9 · Nada vai ao ar sem aprovação (20/10/2026)

- Todo post novo (imagens finais e legenda) é mostrado ao dono ANTES de entrar no manifest com `auto: true`. Só publica depois de um "pode" explícito dele.
- Rascunho, teste de formato e exemplo nunca vão pro manifest.
- Motivo: em 20/10 o post n1-salario-minimo (bloco de notas) foi publicado sem o dono ver; ele achou que era rascunho.

## R10 · Política: Lula e Flávio no mesmo post (20/10/2026)

- De preferência, todo post político traz Lula e Flávio juntos, com fatos do mesmo tipo (R2: sem falsa equivalência, diferença dita quando existe).
- Fecho padrão, nas palavras do dono: "Um desses dois vai nos governar pelos próximos 4 anos. Você já pensou no seu plano de fuga?"
- Vorcaro: deixado de lado por enquanto (post m1 pausado).
- Linha editorial: o "clichê que todo mundo já sabe mas não quer aceitar", só com fato documentado.

## Skills do Instagram (23/10/2026)

- Adaptadas de sergebulaev/instagram-skills (MIT) a pedido do dono: `projeto-claude/skills/plano-de-fuga-post`, `plano-de-fuga-perfil` e `plano-de-fuga-semana`.
- Decisões do dono: travessão continua proibido (a skill original aceitava 1 ou 2), publicação só pela nossa API do Instagram (sem Publora), tudo em português por ora.

## R11 · Objetivo do perfil: comunidade no Telegram (23/10/2026)

- Palavras do dono: o objetivo do Plano de Fuga é criar uma comunidade de pessoas que querem sair do Brasil no Telegram e, em algum momento, vender algo.
- O Instagram é a porta de entrada. O link do perfil leva pro grupo do Telegram.
- O pedido no fim de um post pode ser entrar no grupo, com motivo concreto, sem virar isca em todo post.
- A bio da eleição foi descartada. A bio o dono coloca ele mesmo no app.
