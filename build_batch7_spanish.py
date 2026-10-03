# -*- coding: utf-8 -*-
"""Batch 7: 6 Spanish /es/ pages with hreflang to English equivalents."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_seo import build_page, write_page_subdir, DOMAIN

# Spanish UI label defaults
ES_LABELS = dict(
    lang="es",
    og_locale="es_ES",
    back_href="../index.html",
    back_label="Volver al inicio",
    faq_section_title="Preguntas frecuentes",
    faq_section_h2="Preguntas comunes, <em>respondidas.</em>",
    related_label="Lectura relacionada",
    related_h2="Contin&uacute;a donde <em>lo dejaste.</em>",
    cta_label="Cuando est&eacute;s listo",
    cta_btn_text="Escr&iacute;benos por WhatsApp &rarr;",
)

def hreflang_pair(es_slug, en_slug):
    """Build hreflang_alts for an es+en pair."""
    es_url = f"{DOMAIN}/es/{es_slug}.html"
    en_url = f"{DOMAIN}/{en_slug}.html"
    return [
        ("es", es_url),
        ("es-LA", es_url),
        ("en", en_url),
        ("en-IN", en_url),
        ("x-default", en_url),
    ]

def spanish_article_schema(canonical_url, title, description):
    return '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "Article",
        "headline": title, "description": description,
        "url": canonical_url,
        "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/founder.html"},
        "publisher": {"@type": "AccountingService", "name": "Bharat Quantum Prospera", "url": DOMAIN},
        "inLanguage": "es",
    }, separators=(',', ':'), ensure_ascii=False) + '</script>'


# -------- 1. Incorporacion Delaware para fundadores latinoamericanos --------
slug = "incorporacion-delaware-fundadores-latinoamericanos"
en_slug = "latin-america"
title = "Incorporación Delaware para fundadores latinoamericanos - BQP"
description = "Delaware C-Corp y Wyoming LLC para fundadores latinoamericanos. Costos, pasos, EIN sin SSN, apertura de cuenta bancaria. Firma CA con enfoque transfronterizo."
canonical_url = f"{DOMAIN}/es/{slug}.html"
write_page_subdir("es", slug, build_page(
    slug=slug,
    title=title,
    description=description,
    keywords="incorporacion Delaware latinoamerica, Delaware C-Corp fundadores latinos, Wyoming LLC Latinoamerica, abrir empresa Estados Unidos desde latinoamerica, EIN sin SSN, Mercury banco EEUU",
    hero_kicker="INCORPORACIÓN EN EE.UU. &middot; LATINOAMéRICA",
    hero_title_html="Delaware o Wyoming, <em>desde Latinoamérica.</em>",
    hero_lead="Delaware C-Corp o Wyoming LLC para fundadores latinoamericanos: formación de la entidad, EIN sin SSN, cuenta bancaria en Mercury o Brex, cumplimiento continuo y coordinación con tu asesor local en México, Brasil, Argentina, Chile, Colombia, Perú, Uruguay o Costa Rica.",
    sections=[
        ("Visión general", "Por qué incorporar en EE.UU. desde Latinoamérica",
         "<p>La mayoría de los fundadores latinoamericanos que forman una entidad en Estados Unidos lo hacen por tres razones operacionales: (i) aceptar pagos en Stripe, Mercury u otras plataformas financieras estadounidenses; (ii) cerrar contratos con clientes empresariales estadounidenses que prefieren contratar con una entidad local; (iii) levantar capital de fondos de venture capital de EE.UU. que exigen una estructura Delaware C-Corp.</p>"
         "<p>La decisión suele ser operativa, no una optimización tributaria pura. La tasa corporativa federal estadounidense (21%) es menor que la mexicana (30%), brasileña (34%), argentina (35%) o chilena (27%), pero el impacto tributario depende críticamente de las normas de CFC (Compañías Extranjeras Controladas) de tu país de residencia y del tratado tributario entre tu país y EE.UU. (si existe).</p>"),
        ("Delaware C-Corp vs Wyoming LLC", "Cómo elegir el vehículo",
         "<p><strong>Wyoming LLC:</strong> Nuestra recomendación típica para fundadores en etapa temprana, bootstrapped, o con negocios de SaaS, e-commerce y consultoría. Costo anual bajo (USD 60 de tasa estatal), estructura simple, Formulario 5472 + Formulario 1120 pro-forma como declaración principal. Para una LLC unipersonal de propiedad extranjera, el IRS trata la entidad como transparente para efectos fiscales federales pero exige la declaración informativa anual.</p>"
         "<p><strong>Delaware C-Corp:</strong> Requerido si planeas levantar capital de venture capital estadounidense. Estructura estándar con acciones de fundador, elección 83(b), vesting de 4 años. Impuesto de franquicia de Delaware (desde USD 400 anuales), Formulario 1120 federal, Formulario 5472 por partes relacionadas extranjeras.</p>"
         "<p><strong>Nuestra sugerencia pragmática:</strong> Comienza con Wyoming LLC durante los primeros 12-24 meses mientras validas tu modelo. Convierte a Delaware C-Corp (reorganización F bajo la Sección 368(a)(1)(F)) cuando una ronda con VC estadounidense sea concreta. Esto difiere los costos de C-Corp hasta cuando haya capital para cubrirlos.</p>"),
        ("Pasos prácticos", "De la decisión a la entidad operativa",
         "<ol>"
         "<li><strong>Semana 1-2:</strong> Elección de entidad, presentación ante el estado (Delaware o Wyoming), designación de agente registrado, redacción del Operating Agreement o Bylaws.</li>"
         "<li><strong>Semana 2-4:</strong> Solicitud del EIN mediante el Formulario SS-4 enviado por fax al IRS International (+1-855-215-1627). No se requiere SSN; el fundador latinoamericano aporta pasaporte y domicilio en su país de residencia.</li>"
         "<li><strong>Semana 4-6:</strong> Apertura de cuenta bancaria en Mercury o Brex. Pasaporte, EIN, documentos de formación y descripción del negocio.</li>"
         "<li><strong>Semana 6-8:</strong> Activación de Stripe si corresponde, lanzamiento operativo.</li>"
         "<li><strong>Paralelo:</strong> Cumplimiento del lado de tu país - CBE en Brasil, REFIPRES en México, Transparencia Fiscal en Argentina, DJ 1929 en Chile, Formulario 160 en Colombia, SUNAT en Perú, DGI en Uruguay, Hacienda en Costa Rica.</li>"
         "</ol>"
         "<p>Tiempo total hasta la entidad operativa con cuenta bancaria: 6-8 semanas desde el inicio.</p>"),
        ("Costos típicos año 1", "Qué pagas durante el primer año",
         "<p><strong>Wyoming LLC:</strong> aproximadamente USD 1.500-2.500 cubriendo formación, EIN, apertura de cuenta bancaria, preparación del Formulario 5472 + 1120 pro-forma, más cumplimiento local vía tu contador en el país de residencia.</p>"
         "<p><strong>Delaware C-Corp:</strong> aproximadamente USD 2.500-4.500 incluyendo Formulario 1120 federal e impuesto de franquicia de Delaware.</p>"
         "<p><strong>Documentación de precios de transferencia:</strong> suma USD 1.500-5.000 adicionales si existen transacciones entre partes relacionadas (México, Brasil, Chile, Colombia y Perú tienen requisitos específicos).</p>"
         "<p>Cifras indicativas; propuesta concreta en llamada de scoping.</p>"),
    ],
    faqs=[
        ("¿Puedo abrir una entidad estadounidense sin viajar a EE.UU.?",
         "Sí. El 100% del proceso - formación estatal, EIN, apertura de cuenta bancaria en Mercury o Brex, Stripe - puede completarse de forma remota desde tu país de residencia. No se requiere visa estadounidense ni presencia física."),
        ("¿Necesito un SSN estadounidense para solicitar el EIN?",
         "No. El EIN se obtiene mediante el Formulario SS-4 enviado por fax al IRS International. En la línea 7b se escribe 'Foreign / Non-US Applicant'. Ver nuestra guía detallada en /es/ein-sin-ssn.html."),
        ("¿Mercury o Brex aprueban cuentas para fundadores latinoamericanos?",
         "Sí, ambos. Mercury ha sido particularmente consistente desde 2022. Aprobación típica en 1-3 semanas tras recibir el EIN. Documentación: pasaporte, EIN, documentos de formación, descripción del negocio."),
        ("¿Cómo trato la entidad estadounidense en mi declaración tributaria local?",
         "Depende de tu país de residencia. Mex: SAT reporting + análisis REFIPRES. Bra: Receita Federal + CBE a BCB + CFC lucros no exterior. Arg: AFIP + análisis Transparencia Fiscal. Chi: SII DJ 1929. Col: DIAN Formulario 160. Ver nuestras guías por país (en inglés) linkeadas en latin-america.html."),
        ("¿Trabajan con un contador local en mi país?",
         "BQP maneja el lado estadounidense de extremo a extremo (formación, EIN, banca, Formulario 1120 / 5472, impuesto de franquicia, BOIR). Para el lado local - presentaciones ante SAT, Receita Federal, AFIP, SII, DIAN, SUNAT, DGI o Hacienda - coordinamos con tu contador local o te referimos a uno en nuestra red regional."),
        ("¿Ofrecen asesoría en español?",
         "Sí. Las sesiones de trabajo pueden conducirse en español. Las presentaciones formales ante entes reguladores estadounidenses se preparan en inglés por consistencia. Contenido escrito clave disponible en /es/."),
    ],
    related=[
        ("incorporacion-wyoming-llc.html", "Guía", "Incorporación Wyoming LLC"),
        ("ein-sin-ssn.html", "Guía", "Cómo obtener el EIN sin SSN"),
        ("mercury-vs-brex.html", "Comparación", "Mercury vs Brex"),
    ],
    cta_headline="¿Listo para abrir tu entidad estadounidense?",
    cta_body="20 minutos por WhatsApp y confirmamos la estructura correcta (Wyoming LLC o Delaware C-Corp) para tu negocio, los documentos que necesitamos de tu lado, y el cronograma hasta la entidad operativa con cuenta bancaria. Sin compromiso.",
    article=False,
    extra_schemas=[spanish_article_schema(canonical_url, title, description)],
    canonical_path=f"es/{slug}.html",
    hreflang_alts=hreflang_pair(slug, en_slug),
    **ES_LABELS,
))

# -------- 2. Incorporacion Wyoming LLC --------
slug = "incorporacion-wyoming-llc"
en_slug = "delaware-c-corp-vs-llc"
title = "Incorporación Wyoming LLC desde Latinoamérica - BQP"
description = "Cómo abrir una Wyoming LLC desde México, Brasil, Argentina, Chile, Colombia o cualquier país latinoamericano. Costos, pasos, Formulario 5472, apertura de cuenta bancaria."
canonical_url = f"{DOMAIN}/es/{slug}.html"
write_page_subdir("es", slug, build_page(
    slug=slug, title=title, description=description,
    keywords="Wyoming LLC Latinoamerica, abrir LLC Wyoming desde Mexico, Wyoming LLC desde Brasil, Wyoming LLC Colombia, costo Wyoming LLC fundador latino, LLC vs C-Corp",
    hero_kicker="GUÍA &middot; WYOMING LLC",
    hero_title_html="Wyoming LLC, <em>desde Latinoamérica.</em>",
    hero_lead="La LLC de Wyoming es la entidad estadounidense más eficiente en costo para fundadores latinoamericanos que no planean levantar venture capital estadounidense a corto plazo. Cómo abrirla, qué cuesta, qué debes declarar en tu país y los errores que enseña evitar.",
    sections=[
        ("Visión general", "Por qué Wyoming LLC",
         "<p>Wyoming es el estado estadounidense con el costo más bajo de mantenimiento anual para una LLC (USD 60 de tasa estatal), fuerte privacidad del registro de miembros y una ley de LLC moderna que admite estructuras de propiedad flexibles. Para fundadores latinoamericanos que operan negocios de SaaS, e-commerce, consultoría, servicios profesionales o propiedad de activos digitales en EE.UU., la Wyoming LLC es la entidad por defecto hasta que haya una ronda de VC estadounidense concreta en el horizonte.</p>"
         "<p>Delaware también admite LLCs, con costo anual mayor (USD 300 de tasa estatal) y mayor sofisticación para transacciones complejas. Para la mayoría de los casos de fundador individual latinoamericano, Wyoming es más eficiente.</p>"),
        ("Tratamiento tributario de la LLC", "Qué declara el IRS",
         "<p>Una LLC con un solo miembro de propiedad extranjera (fundador latinoamericano) es una <strong>entidad transparente</strong> (disregarded entity) para efectos del impuesto federal estadounidense. No hay declaración Form 1120 estándar. En cambio, se debe presentar anualmente el <strong>Formulario 5472</strong> con un <strong>Formulario 1120 pro-forma</strong> como cáscara, reportando transacciones entre la LLC y la parte relacionada extranjera (tú, el fundador).</p>"
         "<p>El castigo por omisión del Formulario 5472 es de USD 25.000 por año. No hay excepción para contribuyentes pequeños. Desde el año 1, incluso si solo hiciste el aporte inicial de capital, el Formulario 5472 aplica.</p>"
         "<p>Si la LLC genera ingresos efectivamente conectados con un comercio o negocio estadounidense (ECI), el fundador puede tener exposición fiscal estadounidense personal. Para la mayoría de los negocios latinoamericanos facturando a clientes estadounidenses sin establecimiento permanente en EE.UU., no hay ECI y no hay impuesto federal estadounidense sobre esos ingresos.</p>"),
        ("Pasos prácticos", "Cómo abrirla",
         "<ol>"
         "<li><strong>Nombre de la LLC:</strong> Verificar disponibilidad en el registro de Wyoming. Debe terminar en 'LLC', 'L.L.C.' o 'Limited Liability Company'.</li>"
         "<li><strong>Articles of Organization:</strong> Presentar ante el Wyoming Secretary of State. Costo USD 100. Procesamiento 1-2 días hábiles si es en línea, 7-10 días por correo.</li>"
         "<li><strong>Agente registrado:</strong> Designar un agente registrado con domicilio en Wyoming. Servicios profesionales desde USD 50/año.</li>"
         "<li><strong>Operating Agreement:</strong> Redactar el acuerdo de operación (reglas internas de la LLC). No se presenta ante el estado pero es crítico para el banco y para claridad de propiedad.</li>"
         "<li><strong>EIN:</strong> Solicitud mediante Formulario SS-4 por fax al IRS International. Ver /es/ein-sin-ssn.html.</li>"
         "<li><strong>Cuenta bancaria:</strong> Aplicar en Mercury o Brex con pasaporte, EIN y documentos de formación. Aprobación típica 1-3 semanas.</li>"
         "<li><strong>BOIR:</strong> Presentar el Beneficial Ownership Information Report ante FinCEN dentro de los 30 días de la formación (entidades creadas en 2024+).</li>"
         "</ol>"),
        ("Costos recurrentes", "Qué pagas cada año",
         "<ul>"
         "<li><strong>Tasa estatal Wyoming:</strong> USD 60 anuales (Annual Report).</li>"
         "<li><strong>Agente registrado:</strong> USD 50-150 anuales.</li>"
         "<li><strong>Preparación Formulario 5472 + 1120 pro-forma:</strong> USD 500-1.000 anuales con un preparador profesional.</li>"
         "<li><strong>BOIR actualizaciones:</strong> Sin cargo FinCEN; preparación profesional cuando hay cambios: USD 200-400.</li>"
         "<li><strong>Impuesto corporativo estatal:</strong> Wyoming no tiene impuesto corporativo estatal.</li>"
         "<li><strong>Impuesto federal:</strong> Depende de si hay ECI. Normalmente nulo para LLC extranjera-propietaria sin PE estadounidense.</li>"
         "</ul>"
         "<p>Costo recurrente típico total: USD 700-1.400 por año. Comparar con Delaware C-Corp que puede ser USD 2.000-4.000 anuales.</p>"),
    ],
    faqs=[
        ("¿Puedo convertir mi Wyoming LLC a Delaware C-Corp después?",
         "Sí, mediante una reorganización F (IRC Section 368(a)(1)(F)). Es un procedimiento estándar para startups latinoamericanas antes de una ronda de VC estadounidense. Costo legal típico USD 3.000-8.000. Tiempo 4-6 semanas."),
        ("¿La LLC puede aceptar pagos de Stripe?",
         "Sí. Stripe acepta Wyoming LLCs de propiedad extranjera con EIN, documentos de formación y verificación de identidad del fundador. La configuración es estándar tras completar el EIN y la cuenta bancaria."),
        ("¿Tengo que pagar impuesto corporativo estadounidense sobre las ganancias de la LLC?",
         "Para una LLC unipersonal de propiedad extranjera sin ingresos efectivamente conectados con un negocio estadounidense (ECI), no hay impuesto federal estadounidense sobre los ingresos. Si los servicios se prestan físicamente desde EE.UU. o hay un PE, la situación cambia. Analizamos caso por caso."),
        ("¿Dónde se tributa el ingreso de la LLC en mi país?",
         "Al ser transparente para EE.UU., el ingreso de la LLC fluye a ti como fundador y se declara en tu residencia fiscal. En México, Brasil, Argentina, Chile, Colombia, etc. aplican las normas locales de ingresos del exterior. Ver las guías por país para detalles."),
        ("¿La LLC necesita Formulario BOIR?",
         "Sí, bajo las reglas interinas actuales del Corporate Transparency Act (CTA). Las LLCs con propietarios extranjeros caen dentro del alcance. Verificar fincen.gov/boi por la posición actualizada."),
        ("¿Puedo tener socios latinoamericanos en la misma Wyoming LLC?",
         "Sí. Una LLC con múltiples miembros es una partnership para efectos fiscales estadounidenses (Formulario 1065, K-1 a cada miembro). Mecánicamente más compleja que una single-member LLC. Para startups con 2-4 cofundadores, factible pero requiere decisiones de reparto y distribución contemporáneas."),
    ],
    related=[
        ("incorporacion-delaware-fundadores-latinoamericanos.html", "Hub", "Incorporación Delaware - LatAm"),
        ("ein-sin-ssn.html", "Guía", "EIN sin SSN"),
        ("formulario-5472.html", "Guía", "Formulario 5472"),
    ],
    cta_headline="¿Listo para formar tu Wyoming LLC?",
    cta_body="20 minutos por WhatsApp y confirmamos si Wyoming LLC es la entidad correcta para tu modelo, los pasos exactos, el cronograma y los costos del primer año. Si Delaware C-Corp es mejor para tu caso, te lo decimos también.",
    article=False,
    extra_schemas=[spanish_article_schema(canonical_url, title, description)],
    canonical_path=f"es/{slug}.html",
    hreflang_alts=hreflang_pair(slug, en_slug),
    **ES_LABELS,
))

# -------- 3. EIN sin SSN --------
slug = "ein-sin-ssn"
en_slug = "how-to-get-ein-as-foreign-founder"
title = "Cómo obtener el EIN sin SSN (fundadores extranjeros) - BQP"
description = "Guía paso a paso para obtener el EIN del IRS sin SSN ni ITIN, desde Latinoamérica. Formulario SS-4, línea 7b 'Foreign Applicant', envío por fax, cronograma típico."
canonical_url = f"{DOMAIN}/es/{slug}.html"
write_page_subdir("es", slug, build_page(
    slug=slug, title=title, description=description,
    keywords="EIN sin SSN, EIN fundador extranjero, Formulario SS-4 Latinoamerica, EIN desde Mexico, EIN desde Brasil, como obtener EIN sin ITIN, IRS International EIN",
    hero_kicker="GUÍA &middot; EIN SIN SSN",
    hero_title_html="Obtener el EIN, <em>sin SSN requerido.</em>",
    hero_lead="El Employer Identification Number es el ID fiscal estadounidense que tu entidad necesita antes de abrir cuenta bancaria, firmar contratos o declarar impuestos. Los fundadores latinoamericanos pueden obtenerlo sin SSN ni ITIN. Así funciona el proceso real.",
    sections=[
        ("Visión general", "Qué es el EIN y por qué lo necesitas primero",
         "<p>El EIN es un número de identificación fiscal de 9 dígitos asignado por el IRS a cada entidad empresarial estadounidense. Es el equivalente corporativo del SSN. Toda LLC o C-Corp estadounidense lo necesita. Mercury, Brex y Stripe no abrirán una cuenta sin él. Los contratos piden que lo tengas en el W-9 o W-8. Es el segundo paso tras formar la entidad y la puerta de entrada a todo lo operativo.</p>"),
        ("Las cuatro vías de solicitud", "Y cuál aplica para fundadores sin SSN",
         "<p><strong>1. En línea (solo para personas con SSN/ITIN):</strong> El sistema online del IRS en irs.gov/ein emite el EIN en minutos. Pero requiere SSN o ITIN del responsable party. Los fundadores latinoamericanos sin estos documentos no pueden usar esta ruta.</p>"
         "<p><strong>2. Por fax (ruta más rápida para fundadores extranjeros):</strong> Completa el Formulario SS-4 a mano o en PDF, fírmalo, envíalo por fax al +1-855-215-1627 (International). El IRS típicamente devuelve el EIN por fax en 4-11 días hábiles.</p>"
         "<p><strong>3. Por correo:</strong> Envío postal del Formulario SS-4 al Internal Revenue Service, Attn: EIN International Operation, Cincinnati, OH 45999. Procesamiento 6-8 semanas. Solo usar si el fax falla.</p>"
         "<p><strong>4. Por teléfono (Línea International EIN):</strong> Llamar al +1-267-941-1099 Lunes-Viernes 06:00-23:00 ET. Un agente del IRS hace las preguntas del SS-4 verbalmente y emite el EIN en la llamada. Puede estar ocupada; marcar temprano en la mañana estadounidense ayuda.</p>"),
        ("Formulario SS-4 línea por línea", "La línea 7b es la clave",
         "<p>El Formulario SS-4 tiene campos específicos donde los fundadores latinoamericanos se traban. Esta es la respuesta correcta:</p>"
         "<ul>"
         "<li><strong>Línea 7a:</strong> Nombre del responsable party (fundador).</li>"
         "<li><strong>Línea 7b:</strong> Escribir exactamente <strong>'Foreign / Non-US Applicant'</strong>. NO inventar un SSN. NO dejar en blanco. Esta redacción específica es aceptada por la unidad International EIN del IRS y por todos los bancos estadounidenses que luego revisarán la carta del EIN.</li>"
         "<li><strong>Línea 9a:</strong> Tipo de entidad (Corporation para C-Corp, LLC para LLC con sub-clasificación según elección fiscal).</li>"
         "<li><strong>Línea 10:</strong> Razón de solicitud - 'Started a new business'.</li>"
         "<li><strong>Línea 11:</strong> Fecha de inicio del negocio.</li>"
         "<li><strong>Línea 18:</strong> Dejar en blanco (a menos que hayas tenido un EIN previo).</li>"
         "</ul>"),
        ("Qué recibes y cómo guardarlo", "La carta CP 575",
         "<p>Tras aprobación, el IRS emite la <strong>carta CP 575</strong> - el documento oficial que confirma el EIN. Guárdala permanentemente. Mercury, Brex, Stripe y cualquier futura instancia fiscal la pedirán. Si la pierdes, puedes solicitar una Letter 147C al IRS llamando al mismo número (+1-267-941-1099) - esta carta es funcionalmente equivalente para propósitos bancarios.</p>"
         "<p>El fax recibido con el EIN es también evidencia válida mientras llega la CP 575 por correo (puede tardar 2-4 semanas en llegar físicamente a tu domicilio en Latinoamérica, pero el EIN es válido desde el momento del fax).</p>"),
    ],
    faqs=[
        ("¿Puedo usar el sistema online del IRS si no tengo SSN?",
         "No. La solicitud online en irs.gov/ein requiere que el responsable party tenga SSN o ITIN válido. Los fundadores latinoamericanos sin SSN/ITIN deben usar fax, teléfono o correo postal."),
        ("¿Cuánto tarda realmente la ruta de fax?",
         "El IRS dice 4 días hábiles para solicitantes extranjeros; en la práctica 4-11 días es típico. Algunos reciben el EIN en 2-3 días cuando el backlog del IRS está bajo. Enviar el fax entre las 06:00-09:00 US ET suele acelerar."),
        ("¿Necesito solicitar un ITIN primero?",
         "No. NO solicites un ITIN solo para obtener el EIN - el EIN puede obtenerse con 'Foreign / Non-US Applicant' en la línea 7b. La solicitud de ITIN (Formulario W-7) toma 8-14 semanas y es innecesaria para propósitos de EIN."),
        ("¿Puede un agente registrado solicitar el EIN por mí?",
         "La mayoría de los agentes registrados (Stripe Atlas, Firstbase, Doola, Harvard Business Services) presentan el SS-4 en nombre del fundador usando Formulario 8821 (tax information authorization) o Formulario 2848 (power of attorney). Es práctica estándar y a veces más rápido que la auto-presentación."),
        ("¿Qué pasa si el fax falla?",
         "El IRS suspendió temporalmente la ruta de fax para solicitantes extranjeros en 2020-2021 y la restableció. Si falla al momento de tu solicitud, usar la ruta telefónica (+1-267-941-1099) o aceptar el retraso del correo postal. Los agentes registrados también pueden acelerar vía sus relaciones existentes con el IRS."),
        ("¿La entidad debe estar formada antes de solicitar el EIN?",
         "Sí. Necesitas el documento de formación emitido por el estado (Certificate of Incorporation, Articles of Organization) con nombre y fecha de formación antes de que el IRS emita el EIN. Formación primero, EIN segundo, cuenta bancaria tercero."),
    ],
    related=[
        ("incorporacion-delaware-fundadores-latinoamericanos.html", "Hub", "Incorporación Delaware - LatAm"),
        ("incorporacion-wyoming-llc.html", "Guía", "Wyoming LLC"),
        ("mercury-vs-brex.html", "Comparación", "Mercury vs Brex"),
    ],
    cta_headline="¿Tu EIN está atascado o lo necesitas rápido?",
    cta_body="Si estás trabado en la línea 7b, tu fax vuelve en blanco, o el cronograma está bloqueando tu apertura bancaria, nosotros corremos el proceso end-to-end y obtenemos el EIN típicamente en 5-7 días hábiles incluyendo la preparación del SS-4 y la gestión con el IRS.",
    article=False,
    extra_schemas=[spanish_article_schema(canonical_url, title, description)],
    canonical_path=f"es/{slug}.html",
    hreflang_alts=hreflang_pair(slug, en_slug),
    **ES_LABELS,
))

# -------- 4. Mercury vs Brex (es) --------
slug = "mercury-vs-brex"
en_slug = "mercury-vs-brex"
title = "Mercury vs Brex | Banca para fundadores latinoamericanos - BQP"
description = "Mercury vs Brex para fundadores latinoamericanos con entidad estadounidense: apertura de cuenta, saldos mínimos, comisiones de transferencia, treasury yield, cuál se adapta mejor a tu etapa."
canonical_url = f"{DOMAIN}/es/{slug}.html"
write_page_subdir("es", slug, build_page(
    slug=slug, title=title, description=description,
    keywords="Mercury vs Brex, Mercury banco Latinoamerica, Brex Latinoamerica, cuenta bancaria LLC EEUU, Mercury Mexico, Mercury Brasil, banca fintech EEUU fundador extranjero",
    hero_kicker="COMPARACIÓN &middot; BANCA EN EE.UU.",
    hero_title_html="Mercury vs Brex, <em>comparados.</em>",
    hero_lead="Las dos opciones más usadas de banca empresarial estadounidense para fundadores latinoamericanos con entidad en EE.UU. Apertura de cuenta, mínimos, transferencias, rendimiento de treasury y cuál se adapta a cada etapa.",
    sections=[
        ("Visión general", "Ambos son fintech, no bancos",
         "<p>Mercury y Brex son plataformas financieras tecnológicas, no bancos federalmente autorizados. Ambos se asocian con bancos miembros de la FDIC (Choice Financial Group, Column, Evolve para Mercury; JPMorgan y otros para Brex) para mantener los depósitos de clientes bajo programas de barrido que extienden la cobertura FDIC entre múltiples bancos socios. La experiencia de usuario es una aplicación web/móvil moderna; la cuenta subyacente está en el banco socio. Ambos abren cuentas para entidades estadounidenses propiedad de fundadores extranjeros (sujeto a su propio underwriting).</p>"),
        ("Abrir cuenta desde Latinoamérica", "Qué requiere cada uno",
         "<p>Ambas plataformas abren cuentas de forma remota para entidades estadounidenses. Los documentos requeridos son similares: certificate of incorporation, carta del EIN (IRS CP 575), operating agreement o bylaws, pasaporte del signatario autorizado, descripción del negocio.</p>"
         "<p><strong>Mercury:</strong> Históricamente la puerta más abierta para fundadores extranjeros y startups en etapa temprana. Underwriting enfocado en legitimidad del negocio, sin saldo mínimo, sin comisión mensual. Transferencias domésticas gratis, USD 5 por transferencia internacional saliente.</p>"
         "<p><strong>Brex:</strong> Underwriting históricamente más estricto, favorece startups respaldadas por VC con financiamiento visible, mayor profundidad de producto (Brex Cash, Brex Corporate Card, gestión de gastos). Transferencias domésticas e internacionales gratis. En 2022, Brex comenzó a desprior izar startups bootstrapped y pequeñas, reenfocándose en VC-backed y enterprise.</p>"
         "<p>Mercury tiene mejor tasa de aprobación para fundadores latinoamericanos sin ronda de VC visible. Brex es preferible si ya tienes capital levantado y necesitas gestión de gastos corporativos profundos.</p>"),
        ("Rendimiento, transferencias y comisiones", "Los términos comerciales que importan mensualmente",
         "<table><thead><tr><th>Feature</th><th>Mercury</th><th>Brex</th></tr></thead><tbody>"
         "<tr><td>Comisión mensual</td><td>Nula (Standard)</td><td>Nula</td></tr>"
         "<tr><td>Saldo mínimo</td><td>Nulo</td><td>Nulo (en general)</td></tr>"
         "<tr><td>Transferencia doméstica (out)</td><td>Nula</td><td>Nula</td></tr>"
         "<tr><td>Transferencia internacional (out)</td><td>USD 5</td><td>Nula</td></tr>"
         "<tr><td>Rendimiento Treasury</td><td>Mercury Treasury: fondo money market</td><td>Brex Cash: fondo money market</td></tr>"
         "<tr><td>Tarjeta corporativa</td><td>Mercury IO (limitada)</td><td>Brex Card (profunda)</td></tr>"
         "<tr><td>Gestión de gastos</td><td>Básica</td><td>Profunda (nativa)</td></tr>"
         "<tr><td>Cobertura FDIC (sweep)</td><td>Hasta USD 5M</td><td>Hasta USD 6M</td></tr>"
         "</tbody></table>"
         "<p>Las tasas y términos cambian; verifica los términos actuales en ambas plataformas antes de decidir.</p>"),
        ("Cuál se adapta a tu caso", "Marco de decisión",
         "<p><strong>Elige Mercury si:</strong> eres fundador en etapa temprana o bootstrapped, necesitas banca estadounidense confiable con transferencias simples, quieres barrido de tesorería sobre efectivo ocioso, y no necesitas gestión pesada de gastos. Mercury es el default más común para fundadores latinoamericanos formando una Delaware C-Corp o Wyoming LLC.</p>"
         "<p><strong>Elige Brex si:</strong> estás respaldado por VC, tienes tracción y financiamiento visible, quieres gestión de gastos e infraestructura de tarjeta corporativa profunda, y las transferencias internacionales son frecuentes (gratis en Brex vs USD 5 en Mercury).</p>"
         "<p><strong>Considera Ramp si:</strong> la necesidad primaria es tarjeta corporativa + gestión de gastos, no banca. Ramp es card-first con banca añadida después; el inverso de Mercury.</p>"),
    ],
    faqs=[
        ("¿Mercury y Brex aceptan entidades de propiedad de fundadores latinoamericanos?",
         "Sí, ambos aprueban entidades estadounidenses propiedad de fundadores latinoamericanos, sujeto a su propio underwriting. La tasa de aprobación de Mercury para fundadores latinoamericanos ha sido consistentemente alta desde 2022. Brex se ha vuelto más selectivo desde 2022, favoreciendo startups con VC."),
        ("¿Necesito un SSN estadounidense para abrir cuenta en Mercury o Brex?",
         "No. Ambos aceptan pasaporte del signatario autorizado. Sí necesitas una entidad estadounidense (Delaware, Wyoming u otro) con EIN válido emitido por el IRS. Mercury y Brex no abren cuentas para entidades extranjeras."),
        ("¿Qué es Mercury Treasury y cómo funciona?",
         "Mercury Treasury barre el efectivo ocioso a fondos de money market (Vanguard Federal Money Market, Morgan Stanley Government Institutional). No es FDIC asegurado (es un fondo registrado SEC) pero es considerado muy bajo riesgo. El rendimiento varía con las tasas vigentes. Los retiros se liquidan T+1."),
        ("¿Brex tiene un saldo mínimo?",
         "Brex removió la mayoría de los requisitos de saldo mínimo en 2023 pero sigue siendo más selectivo en underwriting. Saldos que caen a cero pueden gatillar revisión. Verificar términos actuales antes de abrir."),
        ("¿Ramp es mejor que Mercury o Brex?",
         "Ramp es una plataforma de tarjeta corporativa + gestión de gastos con producto bancario. Posicionamiento más cercano a Brex que a Mercury. Para operaciones intensivas en gastos con fuertes necesidades de control de tarjeta, Ramp es competitivo. Para banca pura, Mercury es más simple."),
        ("¿Si Mercury congela mi cuenta, qué pasa?",
         "Los congelamientos de cuentas fintech ocurren y los plazos de recuperación varían. Mercury ha sido más rápido que el promedio en desbloqueos cuando se proporciona documentación. Mejor defensa: mantener registros de clientes, facturas y documentación de proveedores organizados; responder a solicitudes de cumplimiento dentro de 48 horas; no usar la cuenta para transacciones personales."),
    ],
    related=[
        ("incorporacion-delaware-fundadores-latinoamericanos.html", "Hub", "Incorporación Delaware - LatAm"),
        ("incorporacion-wyoming-llc.html", "Guía", "Wyoming LLC"),
        ("ein-sin-ssn.html", "Guía", "EIN sin SSN"),
    ],
    cta_headline="¿Configurando banca estadounidense para tu entidad?",
    cta_body="La apertura es el paso visible; los invisibles son estructurar correctamente la entidad, el EIN, la documentación del signatario y el routing del capital inicial para que Mercury/Brex aprueben al primer intento. Nosotros lo hacemos end-to-end.",
    article=False,
    extra_schemas=[spanish_article_schema(canonical_url, title, description)],
    canonical_path=f"es/{slug}.html",
    hreflang_alts=hreflang_pair(slug, en_slug),
    **ES_LABELS,
))

# -------- 5. Formulario W-8BEN --------
slug = "formulario-w-8ben"
en_slug = "what-is-form-w-8ben"
title = "Formulario W-8BEN explicado | Para residentes latinoamericanos - BQP"
description = "Formulario W-8BEN y W-8BEN-E para residentes latinoamericanos: diferencia entre W-9 y W-8, cómo invocar el tratado tributario, errores comunes y guía línea por línea."
canonical_url = f"{DOMAIN}/es/{slug}.html"
write_page_subdir("es", slug, build_page(
    slug=slug, title=title, description=description,
    keywords="Formulario W-8BEN, W-8BEN-E Latinoamerica, W-8BEN Mexico, W-8BEN Brasil, W-8BEN Chile, W-8BEN vs W-9, invocar tratado tributario EEUU",
    hero_kicker="GUÍA &middot; FORMULARIO IRS",
    hero_title_html="Formulario W-8BEN, <em>desmitificado.</em>",
    hero_lead="Cada fundador latinoamericano, freelancer o entidad que recibe pago de un cliente estadounidense recibe la solicitud de completar un W-8. Qué versión, cómo llenarlo, y cómo invocar las tasas reducidas de tu tratado tributario con EE.UU.",
    sections=[
        ("Visión general", "Qué hace el Formulario W-8BEN",
         "<p>El Formulario W-8BEN (Certificate of Foreign Status of Beneficial Owner for US Tax Withholding and Reporting) es usado por personas no estadounidenses para certificar a un pagador en EE.UU. que son personas extranjeras, y reclamar una tasa de withholding reducida o nula bajo un tratado tributario de EE.UU. El Formulario W-8BEN-E es el equivalente para entidades extranjeras. Reemplazan al W-9 (usado por personas y entidades estadounidenses). El pagador estadounidense recoge el W-8 antes de hacer el pago y aplica la tasa de withholding correspondiente según la información del formulario.</p>"
         "<p>Sin W-8, el pagador estadounidense aplica el default de 30% sobre income de fuente estadounidense pagado a un receptor extranjero. Con un W-8 correctamente ejecutado invocando el tratado tributario entre tu país y EE.UU., la retención se reduce a cero o a la tasa reducida del tratado.</p>"),
        ("W-8BEN vs W-8BEN-E vs W-9", "Qué formulario para quién",
         "<table><thead><tr><th>Formulario</th><th>Para quién</th><th>Propósito</th></tr></thead><tbody>"
         "<tr><td>W-9</td><td>Personas estadounidenses (ciudadanos, residentes, entidades US)</td><td>Proveer TIN al pagador US; sin withholding en income de servicios</td></tr>"
         "<tr><td>W-8BEN</td><td>Personas individuales no estadounidenses</td><td>Certificar estatus extranjero; invocar beneficios de tratado</td></tr>"
         "<tr><td>W-8BEN-E</td><td>Entidades no estadounidenses (compañías, LLCs, partnerships)</td><td>Certificar estatus de entidad extranjera; invocar tratado + clasificación FATCA</td></tr>"
         "<tr><td>W-8IMY</td><td>Intermediarios extranjeros y entidades flow-through</td><td>Usado por partnerships y trusts extranjeros</td></tr>"
         "<tr><td>W-8ECI</td><td>Personas no US con comercio/negocio estadounidense</td><td>Income efectivamente conectado con comercio/negocio US</td></tr>"
         "</tbody></table>"
         "<p>Un individuo mexicano o chileno recibiendo pago de un cliente estadounidense completa W-8BEN. Una compañía SA de CV mexicana o una SpA chilena recibiendo pago completa W-8BEN-E. Este es el error de clasificación más común.</p>"),
        ("Línea por línea para claimants latinoamericanos", "Los campos que importan",
         "<p><strong>W-8BEN (individual):</strong></p>"
         "<ul>"
         "<li><strong>Línea 1:</strong> Nombre legal completo (coincidente con pasaporte).</li>"
         "<li><strong>Línea 2:</strong> País de ciudadanía (México, Brasil, Argentina, Chile, Colombia, etc.).</li>"
         "<li><strong>Línea 3:</strong> Dirección de residencia permanente (dirección local; no una dirección estadounidense).</li>"
         "<li><strong>Línea 5:</strong> US TIN si tienes uno (en blanco si no tienes ITIN).</li>"
         "<li><strong>Línea 6:</strong> Número de identificación fiscal extranjero - tu RFC (México), CPF (Brasil), CUIT (Argentina), RUT (Chile), NIT (Colombia), etc.</li>"
         "<li><strong>Línea 9:</strong> País que invoca beneficios del tratado - solo si tu país tiene tratado con EE.UU. México y Chile sí; Brasil, Argentina, Colombia, Perú, Uruguay, Costa Rica no tienen tratado tributario integral con EE.UU.</li>"
         "<li><strong>Línea 10:</strong> Artículo y párrafo del tratado invocado (ej. 'Artículo 7 for business profits'), tipo de income, y razón de la tasa reducida.</li>"
         "</ul>"
         "<p><strong>W-8BEN-E (entidad):</strong> La complejidad aumenta materialmente. Los campos críticos son la clasificación Capítulo 3 FATCA (línea 5 - usualmente 'Active NFFE' o 'Passive NFFE' para la mayoría de las operadoras latinoamericanas), y Parte III claim de beneficio de tratado (línea 14 con artículo del tratado, línea 15 con limitaciones especiales si aplican).</p>"),
        ("Cómo invocar beneficios de tratado US-México y US-Chile", "Artículo por artículo",
         "<p><strong>US-México (tratado 1992, protocolos 2002):</strong></p>"
         "<ul>"
         "<li>Artículo 7 (Business Profits): nula retención US si no hay PE estadounidense - usar para ingresos de servicios de una SA de CV o individual mexicano prestando desde México.</li>"
         "<li>Artículo 10 (Dividendos): tope 10% (5% para accionistas corporativos con 10%+).</li>"
         "<li>Artículo 11 (Intereses): tope 15% (10% para intereses bancarios).</li>"
         "<li>Artículo 12 (Regalías): tope 10%.</li>"
         "</ul>"
         "<p><strong>US-Chile (tratado 2010 en vigor 2024):</strong></p>"
         "<ul>"
         "<li>Artículo 7 (Business Profits): nula retención US si no hay PE estadounidense.</li>"
         "<li>Artículo 10 (Dividendos): tope 15% (5% para accionistas corporativos con 10%+ cumpliendo LOB).</li>"
         "<li>Artículo 11 (Intereses): tope 10% (4% intereses bancarios).</li>"
         "<li>Artículo 12 (Regalías): 2% para equipo industrial/comercial/científico; 10% otras.</li>"
         "<li>Artículo 12A (FTS): tope 10%.</li>"
         "</ul>"
         "<p><strong>Países sin tratado (Brasil, Argentina, Colombia, Perú, Uruguay, Costa Rica):</strong> No se puede invocar reducción de tratado. El W-8BEN se completa igualmente para certificar estatus extranjero y evitar backup withholding; la retención US de 30% aplica sobre income de fuente estadounidense (dividendos, intereses, regalías) sin reducción.</p>"),
    ],
    faqs=[
        ("Como freelancer mexicano en Upwork, ¿qué formulario llenó?",
         "W-8BEN. Eres un individuo no estadounidense prestando servicios desde México. Completa W-8BEN con tu dirección mexicana, RFC como foreign TIN, e invoca Artículo 7 (Business Profits) en línea 10 para nula retención sobre ingresos de servicios."),
        ("¿El W-8BEN expira?",
         "Sí. Generalmente válido desde la fecha de firma hasta el fin del tercer año calendario siguiente (aproximadamente 3 años). También expira al cambio de circunstancias que afecte la información proporcionada. Provee un W-8BEN fresco a cada pagador US cada 3 años."),
        ("¿Necesito un ITIN para completar el W-8BEN?",
         "No. No necesitas ITIN para completar el W-8BEN como individuo latinoamericano. Línea 5 (US TIN) puede quedar en blanco. Línea 6 (Foreign TIN) debe tener tu RFC/CPF/CUIT/RUT/NIT/etc."),
        ("¿Qué pasa si mi país no tiene tratado con EE.UU. (Brasil, Argentina, Colombia, Perú, Uruguay, Costa Rica)?",
         "Aún debes completar W-8BEN para certificar estatus extranjero. En línea 9-10 no se invoca tratado. La retención US aplica al default 30% sobre dividendos/intereses/regalías. Para business profits (Artículo 7), si no hay PE estadounidense, no hay retención incluso sin tratado - pero sin la Article 7 claim, el pagador puede ser más conservador."),
        ("Mi cliente US dice que necesita W-9 y no W-8BEN - ¿qué hago?",
         "El cliente está incorrecto. W-9 es solo para US persons. Si pide W-9 a un extranjero, está por hacer backup withholding incorrecto. Explica que el formulario correcto es W-8BEN (individual) o W-8BEN-E (entidad). Envía el correcto y referencia las instrucciones del IRS si es necesario."),
        ("¿Completar el W-8BEN elimina mi obligación fiscal en mi país?",
         "No. El W-8BEN afecta solo la retención estadounidense sobre pagos de fuente US. Tu obligación fiscal en México/Brasil/Argentina/Chile/Colombia sobre el mismo income permanece sin cambios. Pagas impuesto local sobre los ingresos como parte de tu ingreso mundial, y reclamas foreign tax credit por cualquier impuesto US retenido."),
    ],
    related=[
        ("incorporacion-delaware-fundadores-latinoamericanos.html", "Hub", "Incorporación Delaware - LatAm"),
        ("formulario-5472.html", "Guía", "Formulario 5472"),
        ("ein-sin-ssn.html", "Guía", "EIN sin SSN"),
    ],
    cta_headline="¿Facturando a clientes estadounidenses y el W-8BEN bloquea el pago?",
    cta_body="Una clasificación incorrecta del W-8BEN puede detener un pago por semanas o gatillar retención innecesaria del 30%. BQP prepara W-8BEN y W-8BEN-E, defiende la invocación del tratado si el pagador US o su banco presionan.",
    article=False,
    extra_schemas=[spanish_article_schema(canonical_url, title, description)],
    canonical_path=f"es/{slug}.html",
    hreflang_alts=hreflang_pair(slug, en_slug),
    **ES_LABELS,
))

# -------- 6. Formulario 5472 --------
slug = "formulario-5472"
en_slug = "how-to-file-form-5472"
title = "Cómo presentar el Formulario 5472 | LLC extranjero-propietaria - BQP"
description = "Guía paso a paso para presentar el Formulario 5472 con el Formulario 1120 pro-forma para una LLC estadounidense de un solo miembro de propiedad extranjera. Plazos, penalidades, transacciones reportables."
canonical_url = f"{DOMAIN}/es/{slug}.html"
write_page_subdir("es", slug, build_page(
    slug=slug, title=title, description=description,
    keywords="Formulario 5472, LLC extranjero propietaria 5472, Formulario 5472 Latinoamerica, penalidad 25000 formulario 5472, LLC Mexico declaracion IRS, formulario 1120 pro-forma",
    hero_kicker="GUÍA &middot; CUMPLIMIENTO FISCAL US",
    hero_title_html="Formulario 5472, <em>el playbook del propietario de LLC.</em>",
    hero_lead="Si eres fundador latinoamericano propietario de una LLC estadounidense de un solo miembro, el Formulario 5472 es anual. Omitirlo cuesta USD 25.000. Aquí está el proceso real, la carcasa 1120 pro-forma y los plazos que no se pueden perder.",
    sections=[
        ("Visión general", "Por qué existe y quién debe presentarlo",
         "<p>El Formulario 5472 (Information Return of a 25% Foreign-Owned US Corporation or Foreign Corporation Engaged in a US Trade or Business) es una declaración del IRS que reporta transacciones entre una corporación estadounidense (o LLC transparente de propiedad extranjera) y sus partes relacionadas extranjeras. Existe para que el IRS pueda monitorear operaciones transfronterizas entre partes relacionadas para fines de precios de transferencia y erosión de base.</p>"
         "<p>Desde 2017, las LLCs estadounidenses de un solo miembro de propiedad extranjera (disregarded entities para efectos fiscales US) son tratadas como corporaciones separadas solo para efectos del Formulario 5472, y deben declarar anualmente.</p>"
         "<p>Si eres residente latinoamericano propietario del 100% de una LLC de Delaware o Wyoming que tuvo cualquier transacción reportable (incluyendo la contribución inicial de capital en la formación, distribuciones, préstamos, servicios prestados) contigo u otra parte relacionada extranjera durante el año, el Formulario 5472 aplica.</p>"),
        ("La carcasa 1120 pro-forma", "Cómo declara una LLC transparente",
         "<p>Las LLCs transparentes normalmente no presentan declaración fiscal estadounidense - sus ingresos y gastos fluyen a la declaración del propietario. Pero el Formulario 5472 no puede presentarse solo; debe adjuntarse a un Formulario 1120. Entonces el proceso es:</p>"
         "<ol>"
         "<li>Presentar un <strong>Formulario 1120 pro-forma</strong> con el nombre de la LLC, dirección, EIN, y solo los campos de identificación superiores completados.</li>"
         "<li><strong>No</strong> llenar ingresos, deducciones o cifras fiscales en el 1120 - escribir 'Foreign-owned US DE' a través del encabezado del formulario y 'See attached Form 5472' donde corresponda.</li>"
         "<li>Adjuntar el Formulario 5472 completo por cada parte relacionada extranjera.</li>"
         "<li>Enviar el paquete por correo (la presentación electrónica es técnicamente disponible pero la carcasa pro-forma funciona más confiablemente en papel).</li>"
         "</ol>"
         "<p>Enviar a: Internal Revenue Service, 1973 Rulon White Blvd, M/S 6112, Attn: PIN Unit, Ogden, UT 84201. O fax a +1-855-887-7737. Retener el recibo de envío (correo registrado USPS o tracking FedEx).</p>"),
        ("Qué cuenta como transacción reportable", "Línea 4 del Formulario 5472",
         "<p>Transacciones reportables incluyen:</p>"
         "<ul>"
         "<li>Ventas de propiedad tangible entre partes relacionadas</li>"
         "<li>Rentas recibidas o pagadas</li>"
         "<li>Regalías recibidas o pagadas</li>"
         "<li>Servicios prestados o recibidos</li>"
         "<li>Comisiones</li>"
         "<li>Intereses recibidos o pagados</li>"
         "<li>Préstamos y pagos de préstamos (saldos de apertura y cierre)</li>"
         "<li>Contribuciones de capital y distribuciones</li>"
         "<li>Cualquier otra consideración</li>"
         "</ul>"
         "<p>El umbral: <strong>cero.</strong> Cualquier transacción reportable, por pequeña que sea, gatilla la obligación de presentar. Incluso la contribución inicial de capital cuando formaste la LLC es una transacción reportable del propietario extranjero a la LLC. Por eso virtualmente toda LLC estadounidense de propiedad extranjera tiene obligación del Formulario 5472 desde el año uno.</p>"),
        ("Plazos y penalidades", "El acantilado del 15 de abril",
         "<p><strong>Plazo:</strong> 15 de abril del año siguiente para contribuyentes de año calendario. Extensión automática hasta el 15 de octubre presentando el Formulario 7004 antes del 15 de abril.</p>"
         "<p><strong>Penalidad por omisión de presentación:</strong> USD 25.000 por Formulario 5472 por año. USD 25.000 adicionales por cada período de 30 días que la omisión continúe después de aviso del IRS. No hay de minimis. No hay excepción para contribuyentes pequeños.</p>"
         "<p><strong>Cura por presentación tardía:</strong> First-Time Abatement (FTA) puede aplicar si la LLC tiene historial de cumplimiento previo limpio. Abatement por causa razonable está disponible si puedes demostrar causa genuina (no desconocimiento de la regla - el IRS ha dicho explícitamente que desconocimiento no es causa razonable para una LLC extranjero-propietaria). Presentar prontamente al descubrir, con explicación, la mayoría de las primeras omisiones son abatidas. No ignores un aviso de penalidad del IRS por 5472.</p>"),
    ],
    faqs=[
        ("¿Debo presentar Formulario 5472 si mi LLC no tuvo ingresos?",
         "Sí, si hubo cualquier transacción reportable con partes relacionadas extranjeras - incluyendo tu contribución inicial de capital. Cero ingresos no exime la presentación. Toda LLC de un solo miembro extranjero-propietaria formada con contribución de capital tiene al menos una transacción reportable desde el día uno."),
        ("¿Qué es una 'parte relacionada extranjera' para el 5472?",
         "Cualquier persona o entidad que es (i) relacionada con la corporación reportante bajo IRC Section 267(b) o 707(b) - generalmente 25%+ propiedad común - y (ii) extranjera. Como propietario 100% extranjero de una LLC estadounidense, eres automáticamente una parte relacionada extranjera."),
        ("¿Puedo presentar el Formulario 5472 electrónicamente?",
         "El IRS acepta presentación electrónica del 5472 adjunto al 1120 mediante software fiscal profesional. Para el 1120 pro-forma con solo 5472 adjunto, la presentación en papel (o fax) es la ruta más confiable porque el e-file a menudo falla con los campos de ingresos/deducciones vacíos."),
        ("¿Qué pasa si omití el Formulario 5472 por años previos?",
         "Presentar lo antes posible con explicación de causa razonable. First-Time Abatement está disponible para un año previo si la LLC tiene cumplimiento previo limpio. El abatement por causa razonable requiere más que 'no sabía' - necesita demostrar diligencia y causa genuina. La mayoría de las primeras omisiones son abatidas si curas prontamente."),
        ("¿Una LLC multi-miembro formada en EE.UU. necesita Formulario 5472?",
         "Una LLC multi-miembro que es partnership para efectos US presenta Formulario 1065 (no 1120) y K-1s. Las reglas del 5472 aplican diferentemente - la partnership presenta 5472 solo si tiene 25%+ de propiedad extranjera a través de socios y transacciones reportables. Mismo principio, mecánica diferente."),
        ("¿Una Delaware C-Corp presenta Formulario 5472?",
         "Sí, si tiene 25%+ de propiedad extranjera y cualquier transacción reportable con partes relacionadas extranjeras. Se presenta como adjunto a su Formulario 1120 regular (no pro-forma). Estándar para todas las Delaware C-Corp propiedad de fundadores latinoamericanos que tuvieron contribución de capital del fundador."),
    ],
    related=[
        ("incorporacion-wyoming-llc.html", "Guía", "Wyoming LLC"),
        ("incorporacion-delaware-fundadores-latinoamericanos.html", "Hub", "Incorporación Delaware - LatAm"),
        ("formulario-w-8ben.html", "Guía", "Formulario W-8BEN"),
    ],
    cta_headline="¿LLC estadounidense de propiedad extranjera y dudas sobre el 5472?",
    cta_body="Si tienes una Wyoming o Delaware LLC y Atlas o Doola te dijeron 'nada más se necesita', eso es incorrecto. El Formulario 5472 aplica desde el año uno. BQP presenta el 5472 + 1120 pro-forma como parte estándar de nuestro mandato de cumplimiento para LLCs extranjero-propietarias.",
    article=False,
    extra_schemas=[spanish_article_schema(canonical_url, title, description)],
    canonical_path=f"es/{slug}.html",
    hreflang_alts=hreflang_pair(slug, en_slug),
    **ES_LABELS,
))

print("Batch 7 complete: 6 Spanish /es/ pages written")
