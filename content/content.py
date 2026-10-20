# Plano de Fuga · conteúdo 20 a 25/10/2026
# Regras: perfil é marca, sem biografia pessoal. Política sempre com os dois lados na semana,
# manchetes reproduzidas LITERALMENTE com veículo e data. Horários em UTC (Brasília = UTC-3).

# ---------- Manchetes verificadas (texto literal) ----------
H = {
 "lula_entrega":  ("Lula se entrega à Polícia Federal", "O POVO", "07.04.2018"),
 "petrobras":     ("Petrobras perde R$ 6,2 bilhões com corrupção", "CONGRESSO EM FOCO", "22.04.2015"),
 "fachin":        ("Fachin anula as condenações de Lula na Lava Jato", "MIGALHAS", "08.03.2021"),
 "vorcaro_preso": ("Polícia Federal prende Daniel Vorcaro em escândalo do Banco Master", "O POVO", "04.03.2026"),
 "flavio_cobra":  ("Flávio Bolsonaro admite cobrança a Vorcaro, mas nega crime", "AGÊNCIA BRASIL", "13.05.2026"),
 "flavio_casa":   ("Daniel Vorcaro recebeu Flávio Bolsonaro em sua casa em 2025", "PODER360", "11.10.2026"),
 "lula_vorcaro":  ("Lula recebeu Vorcaro, dono do Master, sem registro na agenda", "PODER360", "26.01.2026"),
 "coveiro":       ("Bolsonaro sobre número de mortes por coronavírus: 'Não sou coveiro'", "A GAZETA", "21.04.2020"),
 "golpe":         ("STF condena Bolsonaro a 27 anos e três meses de prisão", "DIÁRIO DO COMÉRCIO", "11.09.2025"),
 "mansao":        ("Flávio Bolsonaro compra mansão em Brasília por R$ 6 milhões, diz site", "A GAZETA", "MAR.2021"),
 "rachadinha":    ("TJ do Rio arquiva denúncia do MP contra Flávio Bolsonaro em caso das “rachadinhas”", "INFOMONEY / REUTERS", "17.05.2022"),
 "dirceu":        ("Supremo condena Dirceu por compra de voto no Congresso", "FOLHA DE S.PAULO", "10.10.2012"),
 "inss":          ("Presidente do INSS é afastado em operação que apura fraude bilionária contra aposentados", "ITATIAIA", "23.04.2025"),
}
def clip(key, stamp=None, note=None, src=None):
    t, o, d = H[key]
    return {"t": "clip", "head": t, "outlet": o, "date": d, "stamp": stamp, "note": note, "src": src}

EXIT_NOTE = "Bolsa, visto e trabalho fora do Brasil. Todo dia aqui."

# =====================================================================
# CARROSSÉIS DE POLÍTICA (recorte de jornal) — publicação automática
# =====================================================================
POL = [
{"id": "c1-faltam-5", "publish_at": "2026-10-20T23:30:00Z", "slides": [
  {"t": "cover", "k": "FALTAM 5 DIAS", "h": "Dois processos. Nenhum julgamento. Os dois na tua urna."},
  clip("lula_entrega", note="580 dias preso em Curitiba, entre abril de 2018 e novembro de 2019."),
  clip("fachin", stamp="ANULADO", note="O STF decidiu que a Vara de Curitiba não podia julgar. Se as acusações procediam, ninguém decidiu."),
  clip("rachadinha", stamp="ARQUIVADO", note="Denúncia de 2020 por peculato, lavagem e organização criminosa. Caiu depois que STJ e STF anularam as provas por causa de foro."),
  {"t": "say", "h": "Um caiu por causa da vara. O outro, por causa do foro."},
  {"t": "say", "h": "Nos dois casos, o país nunca soube a resposta."},
  {"t": "exit", "h": "Faltam 5 dias. Todo dia, um lado de cada vez."},
 ],
 "caption": """Faltam 5 dias.

Lula: preso em 2018, condenações anuladas em 2021 porque a Vara de Curitiba não era competente. O mérito nunca foi julgado.
Flávio: denunciado por rachadinha em 2020, denúncia arquivada em 2022 depois que as provas foram anuladas por foro.

Aqui ninguém vai te dizer em quem votar. Só lembrar.

Fontes: O Povo, Migalhas, InfoMoney/Reuters, Poder360.

#eleicoes2026 #segundoturno #lula #flaviobolsonaro #planodefuga"""},

{"id": "c2-faltam-4", "publish_at": "2026-10-21T23:30:00Z", "slides": [
  {"t": "cover", "k": "FALTAM 4 DIAS", "h": "O banqueiro preso que tinha amigo dos dois lados."},
  clip("vorcaro_preso", stamp="PRESO", note="O Banco Master deixou R$ 40,6 bilhões em dívidas com uns 800 mil investidores."),
  {"t": "say", "h": "“Amigos de todos os poderes.”", "s": "Foi o que Vorcaro disse em depoimento à PF.", "src": "O Povo"},
  clip("lula_vorcaro", note="Dezembro de 2024, no Planalto. Lula diz que o assunto era do Banco Central."),
  clip("flavio_cobra", note="R$ 134 milhões pedidos pra um filme sobre Jair Bolsonaro. Ele diz que foi patrocínio privado."),
  clip("flavio_casa", note="Agosto de 2025. O que foi conversado não foi divulgado."),
  {"t": "exit", "h": "Faltam 4 dias. Amanhã, o resto da conta."},
 ],
 "caption": """Faltam 4 dias.

Daniel Vorcaro, dono do Banco Master, foi preso em março. Em depoimento disse ter "amigos de todos os poderes".
Lula o recebeu no Planalto em dezembro de 2024, sem registro na agenda.
Flávio admitiu ter cobrado dele R$ 134 milhões pra um filme sobre o pai, e nega crime.

Ninguém aqui está dizendo que alguém cometeu crime. Está dizendo que os dois sentaram com ele.

Fontes: O Povo, Poder360, Agência Brasil.

#eleicoes2026 #segundoturno #bancomaster #vorcaro #planodefuga"""},

{"id": "c3-faltam-3", "publish_at": "2026-10-22T23:30:00Z", "slides": [
  {"t": "cover", "k": "FALTAM 3 DIAS", "h": "Num governo compraram o Congresso. No outro, tentaram não sair."},
  clip("dirceu", stamp="CONDENADO", note="Mensalão. O STF entendeu que o esquema foi montado dentro do 1º governo Lula. Lula não foi réu."),
  clip("golpe", stamp="CONDENADO", note="Trama golpista depois da derrota em 2022. Hoje o candidato é o filho."),
  {"t": "say", "h": "Os dois lados dizem que o outro é a ameaça à democracia."},
  {"t": "say", "h": "Os dois têm condenação no STF pra mostrar."},
  {"t": "exit", "h": "Faltam 3 dias."},
 ],
 "caption": """Faltam 3 dias.

2012: o STF condena José Dirceu, chefe da Casa Civil do 1º governo Lula, pelo mensalão.
2025: o STF condena Jair Bolsonaro a 27 anos e 3 meses por tentativa de golpe.

Fontes: Folha de S.Paulo, Diário do Comércio, Congresso em Foco.

#eleicoes2026 #segundoturno #mensalao #tramagolpista #planodefuga"""},

{"id": "c4-faltam-2", "publish_at": "2026-10-23T23:30:00Z", "slides": [
  {"t": "cover", "k": "FALTAM 2 DIAS", "h": "O golpe que passou pelos dois governos. Quem pagou foi teu avô."},
  clip("inss", note="Operação Sem Desconto. Associações descontavam mensalidade da aposentadoria sem o aposentado autorizar."),
  {"t": "split", "h": "Agora olha as datas.",
   "l": {"tag": "GOVERNO BOLSONARO", "big": "2019–22", "txt": "4 anos de descontos"},
   "r": {"tag": "GOVERNO LULA", "big": "2023–24", "txt": "2 anos de descontos"}},
  {"t": "say", "h": "R$ 6,3 bilhões descontados de aposentados.", "s": "A CGU diz que nem todo desconto era fraude, mas a maioria provavelmente não tinha autorização.", "src": "PF / CGU via Itatiaia"},
  {"t": "say", "h": "Enquanto um culpa o outro, o aposentado pagou nos dois."},
  {"t": "exit", "h": "Faltam 2 dias."},
 ],
 "caption": """Faltam 2 dias.

R$ 6,3 bilhões descontados de aposentados e pensionistas entre 2019 e 2024, segundo a PF e a CGU. Parte nos anos de Bolsonaro, parte nos anos de Lula.

Fontes: Itatiaia, NSC Total, O Povo.

#eleicoes2026 #segundoturno #inss #aposentados #planodefuga"""},

{"id": "c5-falta-1", "publish_at": "2026-10-24T23:30:00Z", "slides": [
  {"t": "cover", "k": "FALTA 1 DIA", "h": "A semana inteira num slide."},
  {"t": "split", "h": "O que vai pra urna.",
   "l": {"tag": "LULA", "big": "", "txt": "Preso em 2018, condenações anuladas sem julgar o mérito\nMensalão no 1º governo\nR$ 6,2 bi de perda na Petrobras\nRecebeu Vorcaro fora da agenda"},
   "r": {"tag": "FLÁVIO BOLSONARO", "big": "", "txt": "Rachadinha arquivada depois de anularem as provas\nMansão de R$ 6 milhões\nCobrou R$ 134 mi de Vorcaro pra filme\nPai condenado a 27 anos por golpe"}},
  {"t": "say", "h": "Nos dois: R$ 6,3 bilhões descontados de aposentados."},
  {"t": "say", "h": "Amanhã você vota. Na segunda, os problemas continuam os mesmos."},
  {"t": "exit", "h": "O teu plano não precisa depender de domingo."},
 ],
 "caption": """Falta 1 dia.

Foi uma semana inteira, sempre dos dois lados. Se você ficou com raiva de um e concordou com outro, provavelmente você já tem lado, e tudo bem.

A partir de segunda o perfil volta pro que interessa: como sair, com bolsa, visto e trabalho.

Fontes de todos os dados nos posts anteriores.

#eleicoes2026 #segundoturno #planodefuga"""},

{"id": "c6-hoje", "publish_at": "2026-10-25T13:00:00Z", "slides": [
  {"t": "cover", "k": "HOJE · 25/10", "h": "Vai votar."},
  {"t": "say", "h": "Das 8h às 17h, horário de Brasília.", "s": "No 2º turno, quem vota no exterior escolhe só presidente e vice.", "src": "TSE"},
  {"t": "exit", "h": "Seja quem for que ganhe, amanhã a gente continua falando de como sair."},
 ],
 "caption": """Hoje é dia de votar. Das 8h às 17h, horário de Brasília.

Amanhã o Plano de Fuga volta pro que interessa: bolsa, visto e trabalho fora.

#eleicoes2026 #segundoturno #planodefuga"""},
]

# =====================================================================
# GUIAS (passaporte) — publicação automática, 9h de Brasília
# =====================================================================
GUIA = [
{"id": "g1-visto-procura", "publish_at": "2026-10-21T12:00:00Z", "stamp": ("PORTUGAL", "SAÍDA ENCERRADA"), "slides": [
  {"t": "cover", "k": "GUIA · PORTUGAL", "h": "O visto mais pedido por brasileiro acabou. Quase ninguém percebeu."},
  {"t": "page", "lab": "O QUE ERA", "h": "Visto de procura de trabalho.", "s": "Você entrava, tinha 120 dias pra achar emprego e podia estender por mais 60.", "src": "Bem Paraná"},
  {"t": "page", "lab": "QUANTOS", "h": "Uns 12 mil brasileiros usaram em 2024.", "s": "Era o visto mais pedido no Brasil.", "src": "DN Brasil"},
  {"t": "page", "lab": "O QUE MUDOU", "h": "Acabou em 23 de outubro de 2025.", "s": "No lugar, um visto só pra trabalho altamente qualificado. Depois da mudança, foram emitidos 110.", "src": "DN Brasil · Lei 61/2025"},
  {"t": "page", "lab": "E AGORA", "h": "O novo ainda esperava regulamentação em julho de 2026.", "s": "A regra prevista pede comprovar €2.760, 3 vezes o salário mínimo português.", "src": "Cidadania e Visto · Eurodicas"},
  {"t": "cta", "h": "Entrar sem nada já não é plano. Segue que a gente mostra os caminhos que ainda funcionam."},
 ],
 "caption": """Se o teu plano era ir pra Portugal e procurar emprego lá, esse caminho acabou em outubro de 2025.

A Lei 61/2025 acabou com o visto de procura de trabalho no formato antigo. Em 2024 foram cerca de 12 mil pra brasileiros. Depois da mudança, 110.

Antes de seguir qualquer guia antigo, confere no portal de vistos do MNE.

Fontes: DN Brasil, Cidadania e Visto, Eurodicas, Bem Paraná.

#vistoportugal #morarfora #morarememportugal #planodefuga"""},

{"id": "g2-erasmus", "publish_at": "2026-10-22T12:00:00Z", "stamp": ("UNIÃO EUROPEIA", "ERASMUS MUNDUS"), "slides": [
  {"t": "cover", "k": "GUIA · BOLSAS", "h": "A bolsa europeia que paga pra você morar em 2 países."},
  {"t": "page", "lab": "O QUE É", "h": "Erasmus Mundus.", "s": "Mestrado conjunto, com diploma de mais de uma universidade."},
  {"t": "page", "lab": "QUANTO PAGA", "h": "Até €1.400 por mês.", "s": "Até €33.600 num mestrado de 24 meses, além dos custos do curso.", "src": "Comissão Europeia"},
  {"t": "page", "lab": "QUANTAS", "h": "Umas 3.000 bolsas por ano, em mais de 160 mestrados.", "src": "Comissão Europeia"},
  {"t": "page", "lab": "O DETALHE", "h": "Não é uma inscrição só.", "s": "Cada mestrado tem o próprio processo e o próprio prazo, normalmente entre o fim do ano e fevereiro."},
  {"t": "cta", "h": "Quer começar em 2027? A hora de olhar é agora.", "s": "Salva e manda pra quem tá na faculdade."},
 ],
 "caption": """Erasmus Mundus é a bolsa de mestrado da União Europeia. Você estuda em pelo menos 2 países e recebe até €1.400 por mês.

Cada programa tem prazo próprio, e muitos fecham entre o fim do ano e fevereiro.

Fonte: Comissão Europeia. Confere o catálogo oficial antes de aplicar.

#erasmusmundus #bolsadeestudos #mestradonaeuropa #planodefuga"""},

{"id": "g3-carolina", "publish_at": "2026-10-23T12:00:00Z", "stamp": ("ESPANHA", "ENTRADA"), "slides": [
  {"t": "cover", "k": "GUIA · BOLSAS", "h": "A Espanha tem uma bolsa feita pra latino-americano. E brasileiro esquece."},
  {"t": "page", "lab": "O QUE É", "h": "Fundación Carolina.", "s": "Pós-graduação, mestrado e doutorado na Espanha."},
  {"t": "page", "lab": "QUANTO PAGA", "h": "Referência de €1.200 por mês.", "s": "Pra viver na Espanha durante o curso.", "src": "Fundación Carolina"},
  {"t": "page", "lab": "ONDE", "h": "Umas 60 universidades espanholas conveniadas."},
  {"t": "page", "lab": "QUANDO", "h": "Prazos entre março e abril.", "s": "Na edição 2026–27, mestrado fechou em 2 de março e doutorado em 9 de abril."},
  {"t": "cta", "h": "Salva pra quando abrir a próxima convocatória."},
 ],
 "caption": """A Fundación Carolina é uma das poucas bolsas espanholas pensadas pra quem é da América Latina.

Mestrado, doutorado e estadias curtas, com referência de €1.200/mês. Os prazos costumam ser em março e abril.

Fonte: Fundación Carolina. Confere a convocatória do ano.

#fundacioncarolina #bolsadeestudos #espanha #planodefuga"""},

{"id": "g4-nomade", "publish_at": "2026-10-24T12:00:00Z", "stamp": ("PORTUGAL", "VISTO D8"), "slides": [
  {"t": "cover", "k": "GUIA · TRABALHO REMOTO", "h": "Quanto você precisa ganhar pra morar em Portugal trabalhando pra fora."},
  {"t": "page", "lab": "O VALOR", "h": "€3.680 por mês.", "s": "Mínimo do visto D8, de nômade digital, em 2026.", "src": "MNE Portugal via Cidadania e Visto"},
  {"t": "page", "lab": "A CONTA", "h": "4 vezes o salário mínimo português.", "s": "Que em 2026 é €920."},
  {"t": "page", "lab": "A REGRA", "h": "A renda tem que vir de fora de Portugal.", "s": "Contrato com empresa estrangeira ou clientes de fora, como PJ."},
  {"t": "page", "lab": "O PROCESSO", "h": "Pedido presencial no Brasil desde abril de 2026.", "s": "Análise de 30 a 60 dias úteis, em média.", "src": "Cidadania e Visto"},
  {"t": "cta", "h": "Antes do visto vem o trabalho remoto. Esse é o próximo guia."},
 ],
 "caption": """O visto de nômade digital de Portugal (D8) pede renda mínima de €3.680/mês em 2026, vinda de fora do país.

Na prática, o visto é a parte fácil. O difícil é o trabalho remoto que paga isso.

Fontes: MNE Portugal, Cidadania e Visto.

#nomadedigital #vistoportugal #trabalhoremoto #planodefuga"""},

{"id": "g5-voto-exterior", "publish_at": "2026-10-25T11:00:00Z", "stamp": ("BRASIL", "ELEIÇÃO 2026"), "slides": [
  {"t": "cover", "k": "HOJE TEM ELEIÇÃO", "h": "Quase 1 milhão de brasileiros votam hoje de fora do Brasil."},
  {"t": "page", "lab": "QUANTOS", "h": "Cerca de 918 mil eleitores no exterior.", "src": "Agrolink, com dados do TSE"},
  {"t": "page", "lab": "EM QUEM", "h": "No 2º turno, só presidente e vice.", "src": "TSE"},
  {"t": "cta", "h": "Sair do Brasil não é deixar de ser brasileiro."},
 ],
 "caption": """Cerca de 918 mil brasileiros estavam habilitados pra votar no exterior em 2026. No 2º turno eles votam só pra presidente.

Fontes: TSE, Agrolink.

#eleicoes2026 #brasileirosnoexterior #planodefuga"""},
]

# =====================================================================
# REELS (recorte de jornal, vertical) — publicação manual com Happy Nation
# =====================================================================
REELS = [
{"id": "r1-faltam-5-lula", "post_at_brt": "20/10 20h", "cards": [
  {"t": "title", "k": "FALTAM 5 DIAS", "h": "Relembrando o que você esqueceu."},
  clip("petrobras"),
  clip("lula_entrega", stamp="PRESO"),
  {"t": "say", "h": "580 dias em Curitiba."},
  clip("fachin", stamp="ANULADO"),
  {"t": "say", "h": "Anulado por causa da vara. O mérito nunca foi julgado."},
  {"t": "say", "h": "Domingo ele pede o 4º mandato."},
  {"t": "exit", "h": "Amanhã é a vez do outro lado."},
 ],
 "caption": """Faltam 5 dias. Amanhã é a vez do outro lado.

Petrobras: R$ 6,2 bi em perdas com corrupção (balanço de 2014). Lula: 580 dias preso, condenações anuladas em 2021 por incompetência da Vara de Curitiba, sem julgamento do mérito.

Fontes: Congresso em Foco, O Povo, Migalhas.

#eleicoes2026 #lula #lavajato #segundoturno #planodefuga"""},

{"id": "r2-faltam-4-vorcaro", "post_at_brt": "21/10 20h", "cards": [
  {"t": "title", "k": "FALTAM 4 DIAS", "h": "O banqueiro que tinha amigo em todo lugar."},
  clip("vorcaro_preso", stamp="PRESO"),
  {"t": "say", "h": "R$ 40,6 bilhões em dívidas. 800 mil investidores."},
  clip("flavio_cobra"),
  {"t": "say", "h": "R$ 134 milhões pedidos pra um filme sobre o pai."},
  clip("flavio_casa"),
  clip("lula_vorcaro"),
  {"t": "say", "h": "Ele mesmo disse que tinha “amigos de todos os poderes”."},
  {"t": "exit", "h": "Faltam 4 dias."},
 ],
 "caption": """Faltam 4 dias.

Vorcaro, dono do Banco Master, preso em março de 2026. Flávio admitiu cobrar dele R$ 134 milhões pra um filme sobre Jair Bolsonaro e nega crime. Lula o recebeu no Planalto sem registro na agenda. E Vorcaro disse à PF que tinha "amigos de todos os poderes".

Fontes: O Povo, Agência Brasil, Poder360.

#eleicoes2026 #bancomaster #vorcaro #flaviobolsonaro #planodefuga"""},

{"id": "r3-faltam-3-bolsonaro", "post_at_brt": "22/10 20h", "cards": [
  {"t": "title", "k": "FALTAM 3 DIAS", "h": "O sobrenome na urna é o mesmo."},
  clip("coveiro"),
  {"t": "say", "h": "A pandemia passou de 700 mil mortos no Brasil."},
  clip("golpe", stamp="CONDENADO"),
  clip("mansao"),
  clip("rachadinha", stamp="ARQUIVADO"),
  {"t": "say", "h": "Provas anuladas por foro. Nunca houve julgamento."},
  {"t": "exit", "h": "Amanhã, o outro lado de novo."},
 ],
 "caption": """Faltam 3 dias. Amanhã, o outro lado de novo.

Jair: "não sou coveiro" em 2020, condenado a 27 anos e 3 meses por trama golpista em 2025. Flávio: mansão de R$ 6 milhões em 2021, denúncia da rachadinha arquivada em 2022 depois que as provas foram anuladas.

Fontes: A Gazeta, Diário do Comércio, InfoMoney/Reuters, Ministério da Saúde.

#eleicoes2026 #bolsonaro #flaviobolsonaro #segundoturno #planodefuga"""},

{"id": "r4-faltam-2-pt", "post_at_brt": "23/10 20h", "cards": [
  {"t": "title", "k": "FALTAM 2 DIAS", "h": "Não é a primeira vez."},
  clip("dirceu", stamp="CONDENADO"),
  {"t": "say", "h": "Chefe da Casa Civil do 1º governo Lula."},
  clip("petrobras"),
  clip("inss"),
  {"t": "say", "h": "R$ 6,3 bilhões descontados de aposentados."},
  {"t": "say", "h": "De 2019 a 2024. Passou pelos dois governos."},
  {"t": "exit", "h": "Faltam 2 dias."},
 ],
 "caption": """Faltam 2 dias.

Mensalão: Dirceu condenado pelo STF em 2012. Petrobras: R$ 6,2 bi em perdas com corrupção. INSS: R$ 6,3 bi descontados de aposentados entre 2019 e 2024, nos dois governos.

Fontes: Folha de S.Paulo, Congresso em Foco, Itatiaia.

#eleicoes2026 #mensalao #inss #segundoturno #planodefuga"""},

{"id": "r5-falta-1-tudo", "post_at_brt": "24/10 20h", "fast": True, "cards": [
  {"t": "title", "k": "FALTA 1 DIA", "h": "A semana inteira em 20 segundos."},
  clip("lula_entrega"), clip("rachadinha", stamp="ARQUIVADO"),
  clip("petrobras"), clip("mansao"),
  clip("dirceu", stamp="CONDENADO"), clip("golpe", stamp="CONDENADO"),
  clip("lula_vorcaro"), clip("flavio_cobra"),
  clip("inss"),
  {"t": "say", "h": "Amanhã você vota."},
  {"t": "exit", "h": "Seja quem for, o teu plano B continua de pé."},
 ],
 "caption": """Falta 1 dia. A semana inteira, dos dois lados.

Amanhã você vota. Seja quem for que ganhe, o teu plano B continua de pé.

Fontes: O Povo, InfoMoney/Reuters, Congresso em Foco, A Gazeta, Folha de S.Paulo, Diário do Comércio, Poder360, Agência Brasil, Itatiaia.

#eleicoes2026 #segundoturno #planodefuga"""},
]


# ===================== 21/10/2026: formatos aprovados =====================
GUIA.append({"id": "g-salario-minimo", "publish_at": "2099-01-01T00:00:00Z", "stamp": ("PORTUGAL", "SALÁRIO MÍNIMO"), "slides": [
  {"t": "cover", "k": "BRASIL × PORTUGAL", "h": "Quanto vale o salário mínimo de Portugal em reais."},
  {"t": "page", "lab": "NO BRASIL", "h": "R$ 1.621 por mês.", "s": "Valor de 2026. São 13 salários no ano, contando o 13º.", "src": "Decreto 12.797/2025"},
  {"t": "page", "lab": "EM PORTUGAL", "h": "€ 920 por mês.", "s": "Valor de 2026 no continente. São 14 salários no ano.", "src": "Diário da República, 29/12/2025"},
  {"t": "page", "lab": "EM REAIS", "h": "R$ 5.180 por mês.", "s": "€ 920 × R$ 5,63, o euro de 20/10/2026. Dá 3,2 vezes o mínimo brasileiro.", "src": "Banco Central (PTAX)"},
  {"t": "page", "lab": "NO ANO", "h": "R$ 21.073 no Brasil. R$ 72.521 em Portugal.", "s": "13 e 14 salários, no câmbio de 20/10/2026."},
  {"t": "page", "lab": "MÉDIA OU MEDIANA", "h": "Mediana é o salário do meio.", "s": "Metade das pessoas ganha menos que ela, metade ganha mais. A média soma tudo e divide, e poucos salários altos puxam ela pra cima."},
  {"t": "page", "lab": "SALÁRIO NO BRASIL", "h": "Média: R$ 3.738 por mês.", "s": "O IBGE não publica a mediana. Mas 69% dos trabalhadores ganham até R$ 3.242, então a mediana fica abaixo disso.", "src": "IBGE, 2º tri 2026 · 4intelligence/PNAD"},
  {"t": "page", "lab": "SALÁRIO EM PORTUGAL", "h": "Média: € 1.436 por mês.", "s": "São R$ 8.085, sem os subsídios de férias e Natal. A mediana mais recente do INE é de 2021: € 996 no setor privado.", "src": "INE, junho de 2026 e 2021"},
  {"t": "cta", "h": "Aluguel e mercado também custam mais em Portugal.", "s": "O próximo guia compara o custo de vida."},
 ],
 "caption": ""})

REELS.append({"id": "r-p1-processos", "post_at_brt": "21/10 20h", "cards": [
  {"t": "title", "k": "FALTAM 4 DIAS", "h": "Lula e Flávio já responderam a processo."},
  clip("lula_entrega", stamp="PRESO"),
  {"t": "say", "h": "Lula ficou 580 dias preso em Curitiba."},
  clip("fachin", stamp="ANULADO"),
  {"t": "say", "h": "O STF anulou porque a Vara de Curitiba não podia julgar o caso."},
  clip("rachadinha", stamp="ARQUIVADO"),
  {"t": "say", "h": "O STJ considerou as provas ilícitas. O mérito nunca foi julgado."},
  {"t": "say", "h": "Um desses dois vai nos governar pelos próximos 4 anos."},
  {"t": "exit", "h": "Você já pensou no seu plano de fuga?"},
 ],
 "caption": ""})
