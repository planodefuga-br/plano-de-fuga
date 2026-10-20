# Plano de Fuga · o que só você pode fazer

Eu crio o repositório, o GitHub Pages e o agendador assim que o teu GitHub estiver conectado ao Claude.
Ficam 2 coisas contigo, uns 15 minutos no total.

## 1. Token do Instagram (10 min, no computador)
1. A conta do Plano de Fuga tem que ser **profissional** (Criador serve).
2. Entra em developers.facebook.com → Meus apps → **Criar app** → caso de uso "Outro" → tipo **Empresa**.
3. No painel do app: **Adicionar produto → Instagram → "API setup with Instagram login"**.
4. Em **"1. Generate access tokens"**: Add account → entra com o Instagram do Plano de Fuga → **Generate token**.
5. Copia o token. Ele vale 60 dias, ou seja, cobre a eleição e mais um mês e meio.

Não precisa de página do Facebook nem de App Review, porque o app só publica na tua própria conta.

## 2. Colar o token no GitHub (2 min)
No repositório `plano-de-fuga` → **Settings → Secrets and variables → Actions → New repository secret**
- Nome: `IG_TOKEN`
- Valor: o token

Não manda o token no chat. Ele dá acesso de publicação à conta.

## 3. Testar
Aba **Actions → Publicar no Instagram → Run workflow**, com **"Só testar"** marcado.
Se aparecer "conta: <teu usuário>", tá funcionando. Daí pra frente ele roda sozinho a cada 15 minutos.

## Todo dia, 30 segundos
O Reel do dia chega pra você (e também fica em `docs/reels/`). Posta pelo app às 20h de Brasília, com o áudio Happy Nation.

## Em dezembro
O token vence 60 dias depois de gerado. Gera outro do mesmo jeito e troca o secret.
