# -*- coding: utf-8 -*-
"""Batch 8: 4 Portuguese /pt/ pages with hreflang to English equivalents."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_seo import build_page, write_page_subdir, DOMAIN

PT_LABELS = dict(
    lang="pt-BR",
    og_locale="pt_BR",
    back_href="../index.html",
    back_label="Voltar ao início",
    faq_section_title="Perguntas frequentes",
    faq_section_h2="Perguntas comuns, <em>respondidas.</em>",
    related_label="Leitura relacionada",
    related_h2="Continue de onde <em>você parou.</em>",
    cta_label="Quando você estiver pronto",
    cta_btn_text="Fale conosco no WhatsApp &rarr;",
)

def hreflang_pair(pt_slug, en_slug):
    pt_url = f"{DOMAIN}/pt/{pt_slug}.html"
    en_url = f"{DOMAIN}/{en_slug}.html"
    return [
        ("pt", pt_url),
        ("pt-BR", pt_url),
        ("en", en_url),
        ("en-IN", en_url),
        ("x-default", en_url),
    ]

def pt_article_schema(canonical_url, title, description):
    return '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "Article",
        "headline": title, "description": description,
        "url": canonical_url,
        "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/founder.html"},
        "publisher": {"@type": "AccountingService", "name": "Bharat Quantum Prospera", "url": DOMAIN},
        "inLanguage": "pt-BR",
    }, separators=(',', ':'), ensure_ascii=False) + '</script>'


# -------- 1. Incorporação Delaware para fundadores brasileiros --------
slug = "incorporacao-delaware-fundadores-brasileiros"
en_slug = "us-incorporation-for-brazilian-founders"
title = "Incorporação Delaware para fundadores brasileiros - BQP"
description = "Delaware C-Corp ou Wyoming LLC para fundadores brasileiros: ausência de tratado Brasil-EUA, declaração CBE ao BCB, DEEE, lucros no exterior. Firma CA com foco transfronteiriço."
canonical_url = f"{DOMAIN}/pt/{slug}.html"
write_page_subdir("pt", slug, build_page(
    slug=slug, title=title, description=description,
    keywords="incorporacao Delaware do Brasil, Delaware C-Corp Brasil, Wyoming LLC do Brasil, CBE BCB declaracao, DEEE Brasil, abrir empresa Estados Unidos do Brasil, EIN sem SSN brasileiro",
    hero_kicker="INCORPORAÇÃO NOS EUA &middot; BRASIL",
    hero_title_html="Delaware ou Wyoming, <em>do Brasil.</em>",
    hero_lead="Delaware C-Corp ou Wyoming LLC para fundadores brasileiros. Ausência de tratado Brasil-EUA, declaração CBE ao BCB quando o capital no exterior ultrapassa o limite, registro DEEE, reporte à Receita Federal, regime de lucros no exterior - tudo tratado.",
    sections=[
        ("Visão geral", "Por que fundadores brasileiros usam entidades americanas",
         "<p>Os três motivadores mais comuns para startups e SaaS brasileiras formarem uma entidade nos EUA são: (i) aceitar o Stripe ou trilhos de pagamento americanos semelhantes que não estão disponíveis ou são limitados no Brasil; (ii) fechar clientes corporativos americanos que preferem contratar com uma entidade local por razões legais e de pagamento; (iii) captar de fundos de venture capital americanos que exigem uma estrutura Delaware C-Corp. O serviço prestado do Brasil (desenvolvimento, operação de plataforma SaaS, consultoria) permanece no Brasil - a entidade americana existe para receber receita e captar capital.</p>"
         "<p>A alíquota corporativa brasileira combinada (34% IRPJ + CSLL) é materialmente maior que a federal americana (21%). Mas as economias mecânicas da diferença de alíquota geralmente são anuladas pelo regime brasileiro de lucros no exterior (CFC), que normalmente captura os lucros da entidade americana na renda tributável da matriz brasileira a menos que condições específicas sejam atendidas. A decisão raramente é pura arbitragem fiscal.</p>"),
        ("Considerações do lado brasileiro", "O que torna o Brasil distintivo",
         "<p><strong>Ausência de tratado tributário Brasil-EUA abrangente.</strong> Diferente do México, Chile ou muitos países europeus, o Brasil não tem tratado bilateral de imposto de renda com os EUA. Consequência: não há redução de withholding por tratado sobre dividendos/royalties/juros americanos pagos a acionistas brasileiros. A tributação brasileira da renda americana é regida inteiramente pelas regras domésticas brasileiras.</p>"
         "<p><strong>Declaração CBE (Capitais Brasileiros no Exterior) ao BCB.</strong> Residentes brasileiros (pessoas físicas e empresas) com ativos fora do Brasil devem apresentar a CBE ao Banco Central do Brasil anualmente quando ativos no exterior ultrapassam USD 1 milhão (trimestral se acima de USD 100 milhões). Aporte de capital em uma Delaware C-Corp conta.</p>"
         "<p><strong>DEEE (Declaração Econômico-Financeira do Capital Estrangeiro) e BACEN.</strong> Investimento direto no exterior por empresas brasileiras requer registro no BACEN.</p>"
         "<p><strong>Reporte à Receita Federal.</strong> Pessoas físicas brasileiras: ficha de Bens e Direitos no Exterior na DIRPF declara a participação na entidade americana. Empresas brasileiras: ECF reporta subsidiária estrangeira.</p>"
         "<p><strong>Regime de lucros no exterior (Lei 12.973/2014).</strong> Para pessoas jurídicas brasileiras com subsidiárias estrangeiras, os lucros da subsidiária são geralmente incluídos na base tributária da matriz brasileira ao final do ano em regime de competência, independente de repatriação efetiva. Carve-outs estreitos aplicam-se a renda ativa de subsidiárias em países com tratado - mas não há tratado US.</p>"),
        ("Delaware C-Corp vs Wyoming LLC para brasileiros", "Escolhendo o veículo",
         "<p><strong>Delaware C-Corp:</strong> Obrigatório se captando venture capital americano. Estrutura padrão de founder stock, eleição 83(b), vesting de 4 anos. Imposto anual de franchise de USD 400+, Form 1120 federal, Form 5472 reportando partes relacionadas estrangeiras. Para fundadores brasileiros sem planos próximos de VC americano, o custo de cumprimento contínuo é substancial.</p>"
         "<p><strong>Wyoming LLC:</strong> Materialmente mais barato de operar (USD 60 taxa estadual, USD 50-150 agente registrado). LLC uni-membro de propriedade de indivíduo brasileiro é entidade transparente para fins fiscais US - sem Form 1120 - mas o Form 5472 com Form 1120 pro-forma ainda é obrigatório (multa de USD 25.000 se omitido). Boa escolha padrão para fundadores brasileiros solo em SaaS, e-commerce, consultoria com clientes americanos.</p>"
         "<p><strong>Nossa recomendação usual:</strong> Wyoming LLC para os primeiros 12-24 meses da presença americana de uma startup brasileira; converter para Delaware C-Corp (reorganização F) quando uma rodada de VC americano se tornar concreta. Isso difere o custo de franchise tax de Delaware e Form 1120 até que haja capital para pagá-los.</p>"),
        ("Cronograma do Brasil", "Workflow típico",
         "<p><strong>Semanas 1-2:</strong> Seleção de entidade, protocolo Delaware/Wyoming no estado, Operating Agreement ou Bylaws, nomeação de agente registrado.</p>"
         "<p><strong>Semanas 2-4:</strong> Pedido de EIN via Form SS-4 por fax ao IRS International (+1-855-215-1627). Fundador brasileiro fornece passaporte, CPF, endereço no Brasil, e o documento de formação Delaware/Wyoming.</p>"
         "<p><strong>Semanas 4-6:</strong> Abertura de conta bancária no Mercury ou Brex. Passaporte brasileiro, carta de EIN, documentos de formação, descrição do negócio. Aprovação geralmente em 1-3 semanas após receber o EIN.</p>"
         "<p><strong>Semanas 6-8:</strong> Ativação Stripe se for voltado a clientes US. Lançamento operacional.</p>"
         "<p><strong>Semanas 6-10:</strong> Reporte do lado brasileiro - avaliação CBE (apresentar na janela de fim de ano se o limite for ultrapassado), ficha DIRPF, DEEE/BACEN conforme aplicável.</p>"
         "<p>Tempo total até a entidade americana operacional com conta bancária: 6-8 semanas desde o início. Reportes brasileiros em curso continuam anualmente após isso.</p>"),
    ],
    faqs=[
        ("Preciso de um advogado brasileiro além da BQP?",
         "Para formação e cumprimento US, não - BQP cobre fim-a-fim. Para presentações regulatórias brasileiras (CBE, DEEE, registro BACEN, posições de IR brasileiro sobre resultados da entidade US), recomendamos um contador ou advogado tributário brasileiro trabalhando em paralelo. Coordenamos os dois lados."),
        ("O regime de lucros no exterior captura automaticamente a renda da minha Wyoming LLC?",
         "Se você é pessoa física brasileira detendo a LLC pessoalmente, a LLC é transparente para fins US (disregarded entity), então você reporta a renda da LLC na sua DIRPF como se ganha diretamente. Se você é empresa brasileira detendo a LLC, o regime de lucros no exterior aplica e os lucros da LLC são incluídos na base tributária da matriz brasileira ao final do ano. Importa materialmente quem é o titular."),
        ("Existe algum tratado Brasil-EUA no qual eu possa confiar?",
         "Não há tratado abrangente de imposto de renda. Há acordo de totalização previdenciária e arranjos não-tributários diversos, mas para imposto de renda (withholding sobre dividendos/royalties/juros/ganhos de capital), as regras domésticas brasileiras aplicam. Withholding US em pagamentos para brasileiros é a alíquota US doméstica padrão (30% em muitas categorias), sem redução por tratado disponível."),
        ("Posso pagar salário da LLC americana sem acionar tributação brasileira?",
         "Não. Como residente fiscal brasileiro, sua renda mundial é tributável no Brasil independentemente de onde é paga. Salário da LLC americana é renda tributável brasileira, reportada na DIRPF. O lado US também pode exigir withholding dependendo da caracterização. Discuta conosco antes de configurar fluxos de remuneração pessoal."),
        ("Qual é o custo total típico de ano 1 para um fundador brasileiro?",
         "Para Wyoming LLC: aproximadamente USD 1.500-2.500 cobrindo formação, EIN, abertura de conta bancária, preparação Form 5472 + 1120 pro-forma, taxa de franchise Delaware (se DE) ou taxas Wyoming, mais apresentações CBE e DIRPF do lado brasileiro via parceiro local. Para Delaware C-Corp: USD 2.500-4.500 incluindo Form 1120. Valores indicativos; orçamento concreto em call de scoping."),
        ("Vocês têm recursos em português?",
         "Sim. Veja /pt/incorporacao-wyoming-llc.html para Wyoming LLC em português, /pt/ein-sem-ssn.html para o processo de EIN, /pt/formulario-5472.html para o Form 5472. Sessões de trabalho em português disponíveis sob solicitação. Protocolos formais US permanecem em inglês."),
    ],
    related=[
        ("incorporacao-wyoming-llc.html", "Guia", "Wyoming LLC"),
        ("ein-sem-ssn.html", "Guia", "EIN sem SSN"),
        ("formulario-5472.html", "Guia", "Formulário 5472"),
    ],
    cta_headline="Fundador brasileiro considerando uma entidade americana?",
    cta_body="A ausência de tratado tributário torna ineficientes algumas abordagens comuns que funcionam para fundadores mexicanos ou chilenos. 20 minutos e definimos a estrutura correta para seu negócio - Wyoming LLC, Delaware C-Corp ou estrutura holding - incluindo o footprint de reporte brasileiro.",
    article=False,
    extra_schemas=[pt_article_schema(canonical_url, title, description)],
    canonical_path=f"pt/{slug}.html",
    hreflang_alts=hreflang_pair(slug, en_slug),
    **PT_LABELS,
))

# -------- 2. Incorporação Wyoming LLC --------
slug = "incorporacao-wyoming-llc"
en_slug = "delaware-c-corp-vs-llc"
title = "Incorporação Wyoming LLC do Brasil - BQP"
description = "Como abrir uma Wyoming LLC do Brasil. Custos, passos, Formulário 5472, abertura de conta bancária, cumprimento brasileiro paralelo."
canonical_url = f"{DOMAIN}/pt/{slug}.html"
write_page_subdir("pt", slug, build_page(
    slug=slug, title=title, description=description,
    keywords="Wyoming LLC Brasil, abrir LLC Wyoming brasileiro, Wyoming LLC do Brasil custo, LLC Estados Unidos brasileiro, LLC vs C-Corp Brasil",
    hero_kicker="GUIA &middot; WYOMING LLC",
    hero_title_html="Wyoming LLC, <em>do Brasil.</em>",
    hero_lead="A LLC de Wyoming é a entidade americana mais custo-eficiente para fundadores brasileiros sem planos de captar venture capital US a curto prazo. Como abrir, quanto custa, o que declarar no Brasil e os erros que ensinamos a evitar.",
    sections=[
        ("Visão geral", "Por que Wyoming LLC",
         "<p>Wyoming é o estado americano com o menor custo anual de manutenção de uma LLC (USD 60 de taxa estadual), forte privacidade do registro de membros e uma lei de LLC moderna que admite estruturas de propriedade flexíveis. Para fundadores brasileiros operando negócios de SaaS, e-commerce, consultoria, serviços profissionais ou propriedade de ativos digitais nos EUA, a Wyoming LLC é a entidade default até que haja uma rodada de VC americano concreta no horizonte.</p>"
         "<p>Delaware também admite LLCs, com custo anual maior (USD 300 de taxa estadual) e maior sofisticação para transações complexas. Para a maioria dos casos de fundador individual brasileiro, Wyoming é mais eficiente.</p>"),
        ("Tratamento tributário da LLC", "O que o IRS declara",
         "<p>Uma LLC com um único membro de propriedade estrangeira (fundador brasileiro) é uma <strong>entidade transparente</strong> (disregarded entity) para fins do imposto federal americano. Não há declaração Form 1120 padrão. Em vez disso, deve-se apresentar anualmente o <strong>Formulário 5472</strong> com um <strong>Formulário 1120 pro-forma</strong> como invólucro, reportando transações entre a LLC e a parte relacionada estrangeira (você, o fundador).</p>"
         "<p>A multa por omissão do Formulário 5472 é de USD 25.000 por ano. Não há exceção para contribuintes pequenos. Desde o ano 1, mesmo que você tenha apenas feito o aporte inicial de capital, o Formulário 5472 aplica.</p>"
         "<p>Se a LLC gera renda efetivamente conectada com comércio ou negócio americano (ECI), o fundador pode ter exposição fiscal americana pessoal. Para a maioria dos negócios brasileiros faturando clientes americanos sem estabelecimento permanente nos EUA, não há ECI e não há imposto federal americano sobre essa renda.</p>"
         "<p><strong>No Brasil</strong>, se você é pessoa física detentora da LLC, a transparência americana significa que você declara a renda da LLC na sua DIRPF como se ganhada diretamente. Se você é empresa brasileira (CNPJ) detentora, o regime de lucros no exterior aplica.</p>"),
        ("Passos práticos", "Como abrir",
         "<ol>"
         "<li><strong>Nome da LLC:</strong> Verificar disponibilidade no registro de Wyoming. Deve terminar em 'LLC', 'L.L.C.' ou 'Limited Liability Company'.</li>"
         "<li><strong>Articles of Organization:</strong> Protocolar junto ao Wyoming Secretary of State. Custo USD 100. Processamento 1-2 dias úteis online, 7-10 dias por correio.</li>"
         "<li><strong>Agente registrado:</strong> Nomear um agente registrado com endereço em Wyoming. Serviços profissionais a partir de USD 50/ano.</li>"
         "<li><strong>Operating Agreement:</strong> Redigir o acordo de operação (regras internas da LLC). Não se apresenta ao estado mas é crítico para o banco e para clareza de propriedade.</li>"
         "<li><strong>EIN:</strong> Solicitação via Formulário SS-4 por fax ao IRS International. Veja /pt/ein-sem-ssn.html.</li>"
         "<li><strong>Conta bancária:</strong> Aplicar no Mercury ou Brex com passaporte, EIN e documentos de formação. Aprovação típica 1-3 semanas.</li>"
         "<li><strong>BOIR:</strong> Apresentar o Beneficial Ownership Information Report ao FinCEN dentro de 30 dias da formação (entidades criadas em 2024+).</li>"
         "<li><strong>Lado brasileiro:</strong> CBE ao BCB se ativos no exterior ultrapassarem USD 1M; ficha DIRPF; registro BACEN se empresa brasileira investiu diretamente.</li>"
         "</ol>"),
        ("Custos recorrentes", "O que você paga por ano",
         "<ul>"
         "<li><strong>Taxa estadual Wyoming:</strong> USD 60 anuais (Annual Report).</li>"
         "<li><strong>Agente registrado:</strong> USD 50-150 anuais.</li>"
         "<li><strong>Preparação Formulário 5472 + 1120 pro-forma:</strong> USD 500-1.000 anuais com preparador profissional.</li>"
         "<li><strong>Atualizações BOIR:</strong> Sem taxa FinCEN; preparação profissional quando há mudanças: USD 200-400.</li>"
         "<li><strong>Imposto corporativo estadual:</strong> Wyoming não tem imposto corporativo estadual.</li>"
         "<li><strong>Imposto federal:</strong> Depende se há ECI. Normalmente nulo para LLC estrangeiro-proprietária sem PE americano.</li>"
         "<li><strong>Lado brasileiro:</strong> Honorários do seu contador para CBE, DIRPF, lançamentos. Varia conforme complexidade.</li>"
         "</ul>"
         "<p>Custo recorrente US típico total: USD 700-1.400 por ano. Comparar com Delaware C-Corp que pode ser USD 2.000-4.000 anuais.</p>"),
    ],
    faqs=[
        ("Posso converter minha Wyoming LLC em Delaware C-Corp depois?",
         "Sim, através de reorganização F (IRC Section 368(a)(1)(F)). É um procedimento padrão para startups brasileiras antes de uma rodada de VC americano. Custo legal típico USD 3.000-8.000. Tempo 4-6 semanas."),
        ("A LLC pode aceitar pagamentos do Stripe?",
         "Sim. Stripe aceita Wyoming LLCs de propriedade estrangeira com EIN, documentos de formação e verificação de identidade do fundador. A configuração é padrão após completar o EIN e a conta bancária."),
        ("Tenho que pagar imposto corporativo americano sobre lucros da LLC?",
         "Para uma LLC uni-membro de propriedade estrangeira sem renda efetivamente conectada com negócio americano (ECI), não há imposto federal americano sobre a renda. Se os serviços são prestados fisicamente dos EUA ou há PE, a situação muda. Analisamos caso a caso."),
        ("A LLC precisa de Formulário BOIR?",
         "Sim, sob as regras interinas atuais do Corporate Transparency Act. LLCs com proprietários estrangeiros estão dentro do escopo. Verificar fincen.gov/boi para posição atualizada."),
        ("Preciso declarar a LLC na minha DIRPF?",
         "Sim. A participação na LLC (quotas, valor investido, saldo em conta bancária da LLC) é um bem no exterior declarável na ficha de Bens e Direitos. Pessoa física brasileira detentora de LLC transparente também reporta a renda operacional da LLC como ganho próprio."),
        ("Posso ter sócios brasileiros na mesma Wyoming LLC?",
         "Sim. Uma LLC com múltiplos membros é partnership para fins fiscais americanos (Formulário 1065, K-1 para cada membro). Mecanicamente mais complexo que single-member LLC. Para startups com 2-4 co-fundadores, factível mas requer decisões contemporâneas de repartição e distribuição."),
    ],
    related=[
        ("incorporacao-delaware-fundadores-brasileiros.html", "Hub", "Delaware para Brasileiros"),
        ("ein-sem-ssn.html", "Guia", "EIN sem SSN"),
        ("formulario-5472.html", "Guia", "Formulário 5472"),
    ],
    cta_headline="Pronto para formar sua Wyoming LLC?",
    cta_body="20 minutos no WhatsApp e confirmamos se Wyoming LLC é a entidade correta para seu modelo, os passos exatos, o cronograma e os custos do primeiro ano. Se Delaware C-Corp for melhor, também dizemos.",
    article=False,
    extra_schemas=[pt_article_schema(canonical_url, title, description)],
    canonical_path=f"pt/{slug}.html",
    hreflang_alts=hreflang_pair(slug, en_slug),
    **PT_LABELS,
))

# -------- 3. EIN sem SSN --------
slug = "ein-sem-ssn"
en_slug = "how-to-get-ein-as-foreign-founder"
title = "Como obter o EIN sem SSN (fundadores brasileiros) - BQP"
description = "Guia passo a passo para obter o EIN do IRS sem SSN ou ITIN, do Brasil. Formulário SS-4, linha 7b 'Foreign Applicant', envio por fax, cronograma típico."
canonical_url = f"{DOMAIN}/pt/{slug}.html"
write_page_subdir("pt", slug, build_page(
    slug=slug, title=title, description=description,
    keywords="EIN sem SSN, EIN fundador brasileiro, Formulario SS-4 Brasil, EIN do Brasil, como obter EIN sem ITIN, IRS International EIN brasileiro",
    hero_kicker="GUIA &middot; EIN SEM SSN",
    hero_title_html="Obter o EIN, <em>sem SSN exigido.</em>",
    hero_lead="O Employer Identification Number é o ID fiscal americano que sua entidade precisa antes de abrir conta bancária, assinar contratos ou declarar impostos. Fundadores brasileiros podem obtê-lo sem SSN nem ITIN. Como o processo realmente funciona.",
    sections=[
        ("Visão geral", "O que é o EIN e por que você precisa primeiro",
         "<p>O EIN é um número de identificação fiscal de 9 dígitos atribuído pelo IRS a cada entidade empresarial americana. É o equivalente corporativo do SSN. Toda LLC ou C-Corp americana precisa dele. Mercury, Brex e Stripe não abrirão conta sem ele. Contratos pedem que você o tenha no W-9 ou W-8. É o segundo passo após formar a entidade e a porta de entrada para tudo operacional.</p>"),
        ("As quatro vias de solicitação", "E qual aplica para fundadores sem SSN",
         "<p><strong>1. Online (apenas para pessoas com SSN/ITIN):</strong> O sistema online do IRS em irs.gov/ein emite o EIN em minutos. Mas exige SSN ou ITIN do responsable party. Fundadores brasileiros sem esses documentos não podem usar essa rota.</p>"
         "<p><strong>2. Por fax (rota mais rápida para fundadores estrangeiros):</strong> Preencher o Formulário SS-4 à mão ou em PDF, assinar, enviar por fax para +1-855-215-1627 (International). O IRS tipicamente devolve o EIN por fax em 4-11 dias úteis.</p>"
         "<p><strong>3. Por correio:</strong> Envio postal do Formulário SS-4 para Internal Revenue Service, Attn: EIN International Operation, Cincinnati, OH 45999. Processamento 6-8 semanas. Usar só se o fax falhar.</p>"
         "<p><strong>4. Por telefone (Linha International EIN):</strong> Ligar para +1-267-941-1099 Segunda-Sexta 06:00-23:00 ET. Um agente do IRS faz as perguntas do SS-4 verbalmente e emite o EIN na ligação. Pode estar ocupada; ligar cedo na manhã americana ajuda.</p>"),
        ("Formulário SS-4 linha por linha", "A linha 7b é a chave",
         "<p>O Formulário SS-4 tem campos específicos onde fundadores brasileiros tropecam. Resposta correta:</p>"
         "<ul>"
         "<li><strong>Linha 7a:</strong> Nome do responsable party (fundador).</li>"
         "<li><strong>Linha 7b:</strong> Escrever exatamente <strong>'Foreign / Non-US Applicant'</strong>. NÃO inventar SSN. NÃO deixar em branco. Essa redação específica é aceita pela unidade International EIN do IRS e por todos os bancos americanos que depois revisarão a carta do EIN.</li>"
         "<li><strong>Linha 9a:</strong> Tipo de entidade (Corporation para C-Corp, LLC para LLC com sub-classificação conforme eleição fiscal).</li>"
         "<li><strong>Linha 10:</strong> Razão da solicitação - 'Started a new business'.</li>"
         "<li><strong>Linha 11:</strong> Data de início do negócio.</li>"
         "<li><strong>Linha 18:</strong> Deixar em branco (a menos que você tenha tido EIN prévio).</li>"
         "</ul>"),
        ("O que você recebe e como guardar", "A carta CP 575",
         "<p>Após aprovação, o IRS emite a <strong>carta CP 575</strong> - o documento oficial que confirma o EIN. Guarde permanentemente. Mercury, Brex, Stripe e qualquer futura instância fiscal a pedirão. Se perder, você pode solicitar uma Letter 147C ao IRS ligando no mesmo número (+1-267-941-1099) - esta carta é funcionalmente equivalente para fins bancários.</p>"
         "<p>O fax recebido com o EIN também é evidência válida enquanto a CP 575 chega por correio (pode levar 2-4 semanas para chegar fisicamente ao seu endereço no Brasil, mas o EIN é válido desde o momento do fax).</p>"),
    ],
    faqs=[
        ("Posso usar o sistema online do IRS se não tenho SSN?",
         "Não. A solicitação online em irs.gov/ein exige SSN ou ITIN válido do responsable party. Fundadores brasileiros sem SSN/ITIN devem usar fax, telefone ou correio."),
        ("Quanto tempo demora realmente a rota do fax?",
         "O IRS diz 4 dias úteis para solicitantes estrangeiros; na prática 4-11 dias úteis é típico. Alguns recebem em 2-3 dias quando o backlog do IRS está baixo. Enviar fax entre 06:00-09:00 US ET costuma acelerar."),
        ("Preciso de ITIN antes de solicitar o EIN?",
         "NÃO solicite ITIN só para obter EIN - o EIN pode ser obtido com 'Foreign / Non-US Applicant' na linha 7b. Solicitação de ITIN (Formulário W-7) leva 8-14 semanas e é desnecessária para fins de EIN."),
        ("Um agente registrado pode solicitar o EIN para mim?",
         "A maioria dos agentes registrados (Stripe Atlas, Firstbase, Doola, Harvard Business Services) protocola o SS-4 em nome do fundador usando Formulário 8821 (tax information authorization) ou Formulário 2848 (power of attorney). É prática padrão e às vezes mais rápido que auto-protocolo."),
        ("E se o fax falhar?",
         "O IRS suspendeu temporariamente a rota de fax para solicitantes estrangeiros em 2020-2021 e a restabeleceu. Se falhar no momento da sua solicitação, usar rota telefônica (+1-267-941-1099) ou aceitar o atraso do correio. Agentes registrados também podem acelerar via suas relações existentes com IRS."),
        ("A entidade precisa estar formada antes de pedir o EIN?",
         "Sim. Você precisa do documento de formação emitido pelo estado (Certificate of Incorporation, Articles of Organization) com nome e data de formação antes de o IRS emitir o EIN. Formação primeiro, EIN segundo, conta bancária terceiro."),
    ],
    related=[
        ("incorporacao-delaware-fundadores-brasileiros.html", "Hub", "Delaware para Brasileiros"),
        ("incorporacao-wyoming-llc.html", "Guia", "Wyoming LLC"),
        ("formulario-5472.html", "Guia", "Formulário 5472"),
    ],
    cta_headline="Seu EIN está travado ou você precisa rápido?",
    cta_body="Se está travado na linha 7b, seu fax volta em branco, ou o cronograma está bloqueando sua abertura bancária, nós rodamos o processo fim-a-fim e obtemos o EIN tipicamente em 5-7 dias úteis incluindo a preparação do SS-4 e a gestão com o IRS.",
    article=False,
    extra_schemas=[pt_article_schema(canonical_url, title, description)],
    canonical_path=f"pt/{slug}.html",
    hreflang_alts=hreflang_pair(slug, en_slug),
    **PT_LABELS,
))

# -------- 4. Formulário 5472 --------
slug = "formulario-5472"
en_slug = "how-to-file-form-5472"
title = "Como protocolar o Formulário 5472 | LLC proprietária estrangeira - BQP"
description = "Guia passo a passo para protocolar o Formulário 5472 com Formulário 1120 pro-forma para uma LLC americana uni-membro de propriedade estrangeira. Prazos, multas, transações reportáveis."
canonical_url = f"{DOMAIN}/pt/{slug}.html"
write_page_subdir("pt", slug, build_page(
    slug=slug, title=title, description=description,
    keywords="Formulario 5472, LLC estrangeiro proprietaria 5472, Formulario 5472 Brasil, multa 25000 formulario 5472, LLC Brasil declaracao IRS, formulario 1120 pro-forma",
    hero_kicker="GUIA &middot; CUMPRIMENTO FISCAL US",
    hero_title_html="Formulário 5472, <em>o playbook do proprietário de LLC.</em>",
    hero_lead="Se você é fundador brasileiro proprietário de uma LLC americana uni-membro, o Formulário 5472 é anual. Omitir custa USD 25.000. Aqui o processo real, o invólucro 1120 pro-forma e os prazos que não podem ser perdidos.",
    sections=[
        ("Visão geral", "Por que existe e quem deve protocolar",
         "<p>O Formulário 5472 (Information Return of a 25% Foreign-Owned US Corporation or Foreign Corporation Engaged in a US Trade or Business) é uma declaração do IRS que reporta transações entre uma corporação americana (ou LLC transparente de propriedade estrangeira) e suas partes relacionadas estrangeiras. Existe para que o IRS possa monitorar operações transfronteiriças entre partes relacionadas para fins de preços de transferência e erosão de base.</p>"
         "<p>Desde 2017, as LLCs americanas uni-membro de propriedade estrangeira (disregarded entities para fins fiscais US) são tratadas como corporações separadas apenas para fins do Formulário 5472, e devem declarar anualmente.</p>"
         "<p>Se você é residente brasileiro proprietário de 100% de uma LLC Delaware ou Wyoming que teve qualquer transação reportável (incluindo a contribuição inicial de capital na formação, distribuições, empréstimos, serviços prestados) com você ou outra parte relacionada estrangeira durante o ano, o Formulário 5472 aplica.</p>"),
        ("O invólucro 1120 pro-forma", "Como declara uma LLC transparente",
         "<p>LLCs transparentes normalmente não protocolam declaração fiscal americana - sua renda e despesas fluem para a declaração do proprietário. Mas o Formulário 5472 não pode ser protocolado sozinho; deve ser anexado a um Formulário 1120. Então o processo é:</p>"
         "<ol>"
         "<li>Protocolar um <strong>Formulário 1120 pro-forma</strong> com o nome da LLC, endereço, EIN e apenas os campos de identificação superiores completados.</li>"
         "<li><strong>Não</strong> preencher renda, deduções ou valores fiscais no 1120 - escrever 'Foreign-owned US DE' no cabeçalho do formulário e 'See attached Form 5472' onde relevante.</li>"
         "<li>Anexar o Formulário 5472 completo por cada parte relacionada estrangeira.</li>"
         "<li>Enviar o pacote por correio (protocolo eletrônico é tecnicamente disponível mas o invólucro pro-forma funciona mais confiávelmente em papel).</li>"
         "</ol>"
         "<p>Enviar para: Internal Revenue Service, 1973 Rulon White Blvd, M/S 6112, Attn: PIN Unit, Ogden, UT 84201. Ou fax para +1-855-887-7737. Guardar o recibo de envio (correio registrado USPS ou tracking FedEx).</p>"),
        ("O que conta como transação reportável", "Linha 4 do Formulário 5472",
         "<p>Transações reportáveis incluem:</p>"
         "<ul>"
         "<li>Vendas de propriedade tangível entre partes relacionadas</li>"
         "<li>Aluguel recebido ou pago</li>"
         "<li>Royalties recebidos ou pagos</li>"
         "<li>Serviços prestados ou recebidos</li>"
         "<li>Comissões</li>"
         "<li>Juros recebidos ou pagos</li>"
         "<li>Empréstimos e pagamentos (saldos de abertura e fechamento)</li>"
         "<li>Contribuições de capital e distribuições</li>"
         "<li>Qualquer outra consideração</li>"
         "</ul>"
         "<p>O limite: <strong>zero.</strong> Qualquer transação reportável, por menor que seja, aciona a obrigação de protocolar. Até a contribuição inicial de capital quando você formou a LLC é transação reportável do proprietário estrangeiro para a LLC. Por isso virtualmente toda LLC americana de propriedade estrangeira tem obrigação do Formulário 5472 desde o ano um.</p>"),
        ("Prazos e multas", "O penhasco do 15 de abril",
         "<p><strong>Prazo:</strong> 15 de abril do ano seguinte para contribuintes de ano calendário. Extensão automática até 15 de outubro protocolando o Formulário 7004 antes de 15 de abril.</p>"
         "<p><strong>Multa por omissão:</strong> USD 25.000 por Formulário 5472 por ano. USD 25.000 adicionais por cada período de 30 dias que a omissão continuar após aviso do IRS. Não há de minimis. Não há exceção para contribuintes pequenos.</p>"
         "<p><strong>Cura por protocolo atrasado:</strong> First-Time Abatement (FTA) pode aplicar se a LLC tem histórico de cumprimento prévio limpo. Abatement por causa razoável está disponível se você demonstrar causa genuína (não desconhecimento da regra - o IRS disse explicitamente que desconhecimento não é causa razoável para uma LLC estrangeiro-proprietária). Protocolando prontamente ao descobrir, com explicação, a maioria das primeiras omissões é abatida. Não ignore um aviso de multa 5472 do IRS.</p>"),
    ],
    faqs=[
        ("Devo protocolar Formulário 5472 se minha LLC não teve renda?",
         "Sim, se houve qualquer transação reportável com partes relacionadas estrangeiras - incluindo sua contribuição inicial de capital. Zero renda não isenta o protocolo. Toda LLC uni-membro estrangeiro-proprietária formada com contribuição de capital tem pelo menos uma transação reportável desde o dia um."),
        ("O que é 'parte relacionada estrangeira' para o 5472?",
         "Qualquer pessoa ou entidade que é (i) relacionada à corporação reportante sob IRC Section 267(b) ou 707(b) - geralmente 25%+ propriedade comum - e (ii) estrangeira. Como proprietário 100% estrangeiro de LLC americana, você é automaticamente parte relacionada estrangeira."),
        ("Posso protocolar o Formulário 5472 eletronicamente?",
         "O IRS aceita protocolo eletrônico do 5472 anexado ao 1120 via software fiscal profissional. Para 1120 pro-forma com apenas 5472 anexado, protocolo em papel (ou fax) é a rota mais confiável porque o e-file muitas vezes falha com os campos de renda/dedução vazios."),
        ("E se omiti o Formulário 5472 em anos anteriores?",
         "Protocolar o quanto antes com explicação de causa razoável. First-Time Abatement está disponível para um ano anterior se a LLC tem cumprimento prévio limpo. Abatement por causa razoável exige mais que 'não sabia' - precisa demonstrar diligência e causa genuína. A maioria das primeiras omissões é abatida se curar prontamente."),
        ("Uma LLC multi-membro formada nos EUA precisa de Formulário 5472?",
         "LLC multi-membro que é partnership para fins US protocola Formulário 1065 (não 1120) e K-1s. Regras do 5472 aplicam diferentemente - a partnership protocola 5472 só se tem 25%+ de propriedade estrangeira através de sócios e transações reportáveis. Mesmo princípio, mecânica diferente."),
        ("Uma Delaware C-Corp protocola Formulário 5472?",
         "Sim, se tem 25%+ de propriedade estrangeira e qualquer transação reportável com partes relacionadas estrangeiras. Protocolado como anexo ao Formulário 1120 regular (não pro-forma). Padrão para todas as Delaware C-Corp propriedade de fundadores brasileiros que tiveram contribuição de capital do fundador."),
    ],
    related=[
        ("incorporacao-wyoming-llc.html", "Guia", "Wyoming LLC"),
        ("incorporacao-delaware-fundadores-brasileiros.html", "Hub", "Delaware para Brasileiros"),
        ("ein-sem-ssn.html", "Guia", "EIN sem SSN"),
    ],
    cta_headline="LLC americana propriedade estrangeira e dúvidas sobre o 5472?",
    cta_body="Se você tem uma Wyoming ou Delaware LLC e Atlas ou Doola disseram 'nada mais é necessário', isso está errado. O Formulário 5472 aplica desde o ano um. BQP protocola 5472 + 1120 pro-forma como parte padrão do nosso mandato de cumprimento para LLCs estrangeiro-proprietárias.",
    article=False,
    extra_schemas=[pt_article_schema(canonical_url, title, description)],
    canonical_path=f"pt/{slug}.html",
    hreflang_alts=hreflang_pair(slug, en_slug),
    **PT_LABELS,
))

print("Batch 8 complete: 4 Portuguese /pt/ pages written")
