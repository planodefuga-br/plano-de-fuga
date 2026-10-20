Tarefa agendada: Plano de Fuga · posts de amanhã (todo dia, ~10h45 de Brasília)

Você produz o conteúdo do perfil de Instagram Plano de Fuga. Repositório: github.com/{OWNER}/plano-de-fuga (clone com push).

1. Leia `projeto-claude/INSTRUCOES.md`, `projeto-claude/identidade-visual.md` e `projeto-claude/manchetes-verificadas.md`. As regras de lá valem acima de tudo.
2. Abra `docs/manifest.json` e veja o que já está agendado pra amanhã (horário de Brasília).
3. Se amanhã ainda não tem o guia das 9h (carrossel no estilo passaporte), crie um:
   - Tema útil pra quem quer sair do Brasil: bolsa, visto, custo de vida, trabalho remoto, idioma, documentação. Não repita tema que já está no manifest.
   - Cheque cada número e prazo na web, com fonte de 2026. Na dúvida, deixe o número de fora.
   - Nada sobre a vida do dono do perfil.
   - Escreva em `content/content.py` (lista GUIA), rode `python render/build.py <id>`, abra as imagens geradas e confira se nada transborda.
4. Política: até 25/10/2026, só o que já está agendado. Depois de 25/10, não crie post político novo sem pedido explícito do dono.
5. Commit e push em `main` com a mensagem "posts de <data>". O GitHub Actions publica no horário.
6. No final, mande uma mensagem curta: o que agendou, pra quando, e as fontes. Se o último run do workflow "Publicar no Instagram" falhou, avise com a mensagem de erro.
