# Plano de Fuga

Conteúdo e publicação automática do perfil @planodefuga.

- `content/content.py`: textos, manchetes e horários
- `render/build.py`: gera os carrosséis (`docs/<id>/*.jpg`) e os cards dos Reels
- `render/reels.py`: monta os Reels (`docs/reels/*.mp4`)
- `docs/`: o que vai pro ar, servido pelo GitHub Pages
- `publisher/publish.py` + `.github/workflows/publicar.yml`: publica a cada 15 min o que já passou do horário
- `projeto-claude/`: instruções do projeto no claude.ai e da tarefa agendada
- `SETUP.md`: o que precisa ser feito à mão (token do Instagram)
