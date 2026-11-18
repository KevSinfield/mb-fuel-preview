#!/usr/bin/env python3
"""Builds the five preview pages from one shared header/footer.

Run from the repo root:  python3 tools/build_pages.py
Copy is taken from M&B's current site (mbfuel.co.uk), read 13 Nov 2026.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
V = "5"  # bump after CSS/JS edits so returning visitors get fresh files
SRC = "https://www.mbfuel.co.uk"
TEL = "tel:+442380619655"
TEL_TXT = "023 8061 9655"

# ---------- icons ----------
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
EXT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'
BURGER = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
GLOBE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/></svg>'
PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
DOC = '<svg viewBox="0 0 48 48" fill="none" stroke="#fff" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true"><path d="M12 5h17l9 9v29H12z"/><path d="M29 5v9h9M18 24h14M18 31h14M18 38h9"/></svg>'
WA = '<svg class="wa-icon" viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="15" fill="#25d366"/><path fill="#fff" d="M16 6.5a9.4 9.4 0 0 0-8.1 14.2L6.6 25.4l4.8-1.3A9.4 9.4 0 1 0 16 6.5zm0 17.1a7.7 7.7 0 0 1-3.9-1.1l-.3-.2-2.9.8.8-2.8-.2-.3A7.7 7.7 0 1 1 16 23.6zm4.2-5.8c-.2-.1-1.4-.7-1.6-.8s-.4-.1-.5.1-.6.8-.8 1-.3.2-.5.1a6.3 6.3 0 0 1-3.1-2.7c-.2-.4.2-.4.7-1.3a.4.4 0 0 0 0-.4l-.7-1.7c-.2-.5-.4-.4-.5-.4h-.5a.9.9 0 0 0-.6.3 2.7 2.7 0 0 0-.8 2 4.6 4.6 0 0 0 1 2.5 10.6 10.6 0 0 0 4.1 3.6c1.5.6 2.1.7 2.8.6a2.4 2.4 0 0 0 1.6-1.1 2 2 0 0 0 .1-1.1c0-.2-.2-.2-.4-.3z"/></svg>'
ENGINE = '<svg class="ico" viewBox="0 0 66 50" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true"><path d="M20 6h16M28 6v6M14 12h26l6 6h6v-5h6v24h-6v-5h-6l-6 8H20l-6-6H9v6H4V18h5v6h5z"/></svg>'
INJECTOR = '<svg class="ico" viewBox="0 0 66 50" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true"><path d="M44 3l8 8M40 7l8 8-6 6-8-8zM36 15l-16 16 6 6 16-16M23 28l5 5M20 31l-6 6M14 37l-4 4-2 6 6-2 4-4"/></svg>'
VAN = '<svg class="ico" viewBox="0 0 66 50" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true"><path d="M18 10h26v26H24M44 18h9l8 9v9h-5M2 16h12M5 23h10M2 30h10"/><circle cx="21" cy="38" r="4.5"/><circle cx="51" cy="38" r="4.5"/><path d="M30 36h16"/></svg>'


def ext(href, text):
    return f'<a class="src-link" href="{href}">{text} {EXT}<span class="sr-only"> (opens M&amp;B’s current website)</span></a>'


def more(href, text):
    return f'<a class="src-link" href="{href}">{text} {ARROW}</a>'


def wa_preview(extra=""):
    return (f'<div class="wa {extra}" aria-label="WhatsApp the workshop, proposed contact option, not yet active">'
            f'{WA}<span>WhatsApp the workshop</span><span class="tag">Proposed contact option</span></div>')


def header(active):
    def cur(key):
        return ' aria-current="page"' if key == active else ""
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="index.html" aria-label="M&amp;B Fuel Injection Service, home">
      <img src="assets/img/mb-logo.png" width="640" height="271" alt="M&amp;B Fuel Injection Service Ltd">
    </a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">{BURGER}<span class="txt">Menu</span></button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul class="nav-list">
        <li>
          <button class="sub-toggle" type="button" aria-expanded="false" aria-controls="services-sub">Services {CHEV}</button>
          <ul class="submenu" id="services-sub">
            <li><a href="vehicle-diagnostics.html"{cur('diag')}>Vehicle diagnostics</a></li>
            <li><a href="injector-pump-services.html"{cur('inj')}>Injector &amp; pump services</a></li>
            <li><a href="collection-delivery.html"{cur('col')}>Collection &amp; delivery</a></li>
            <li class="sep"><a href="services.html"{cur('svc')}>All services</a></li>
          </ul>
        </li>
        <li><a href="index.html#about">About</a></li>
        <li><a href="collection-delivery.html"{cur('col')}>Collection &amp; delivery</a></li>
        <li><a href="index.html#contact">Contact</a></li>
      </ul>
    </nav>
    <a class="header-call" href="{TEL}" aria-label="Call the workshop on {TEL_TXT}">{PHONE}<span class="num">{TEL_TXT}</span><span class="lbl">Call</span></a>
  </div>
</header>"""


FOOTER = f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <a class="footer-logo" href="index.html" aria-label="M&amp;B Fuel Injection Service, home">
        <img src="assets/img/mb-logo.png" width="640" height="271" alt="M&amp;B Fuel Injection Service Ltd" loading="lazy">
      </a>
      <nav class="footer-nav" aria-label="Footer">
        <h2>Quick links</h2>
        <ul>
          <li><a href="services.html">Services</a></li>
          <li><a href="index.html#about">About</a></li>
          <li><a href="vehicle-diagnostics.html">Vehicle diagnostics</a></li>
          <li><a href="injector-pump-services.html">Injectors &amp; pumps</a></li>
          <li><a href="collection-delivery.html">Collection &amp; delivery</a></li>
          <li><a href="index.html#contact">Contact &amp; estimates</a></li>
        </ul>
      </nav>
      <div class="footer-contact">
        <a href="{TEL}">{PHONE}{TEL_TXT}</a>
        <span>{GLOBE}mbfuel.co.uk</span>
        <span>{PIN}<address>Unit 3 Aercon Buildings, Woodside Rd,<br>Eastleigh, Hampshire SO50 4ET</address></span>
      </div>
    </div>
    <div class="footer-base">
      <span>© 2026 M&amp;B Fuel Injection Service Ltd. All rights reserved.</span>
      <span class="legal"><a href="terms.html">Terms &amp; Conditions</a><a href="privacy.html">Privacy Policy</a></span>
    </div>
    <p class="preview-note">Design preview only. Not the live website.</p>
  </div>
</footer>"""


def page(fname, title, desc, active, body):
    html = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#0d2246">
<link rel="icon" href="assets/img/mb-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css?v={V}">
</head>
<body>
{header(active)}
<main id="main">
{body}
</main>
{FOOTER}
<script src="assets/site.js?v={V}" defer></script>
</body>
</html>
"""
    (ROOT / fname).write_text(html, encoding="utf-8")
    print("wrote", fname)


def aside(heading, text):
    return f"""<aside class="aside" aria-label="Contact the workshop">
  <div class="cta-card">
    <h3>{heading}</h3>
    <p>{text}</p>
    <a class="btn btn-red" href="{TEL}">{PHONE}Call {TEL_TXT}</a>
    <a class="btn btn-outline-light" href="index.html#estimate">Request a free estimate {ARROW}</a>
    {wa_preview()}
  </div>
</aside>"""


def cta_strip(heading):
    return f"""<section class="cta-strip" aria-label="Get in touch">
  <div class="wrap">
    <h2>{heading}</h2>
    <div class="btn-row">
      <a class="btn btn-red" href="{TEL}">{PHONE}Call {TEL_TXT}</a>
      <a class="btn btn-outline" href="index.html#estimate">Request a free estimate {ARROW}</a>
    </div>
  </div>
</section>"""


# ---------- shared contact + estimate section (homepage) ----------
CONTACT = f"""<section class="contact-band" id="contact" aria-labelledby="contact-h">
  <div class="wrap">
    <h2 id="contact-h">Contact &amp; estimates</h2>
    <p>Choose whichever suits you. For most jobs the quickest way is to call and talk it through with the workshop.</p>
    <div class="contact-grid">
      <div class="contact-opt">
        <div class="c-ico red">{PHONE.replace('fill="currentColor"', 'fill="#fff"')}</div>
        <div>
          <h3>Call the workshop</h3>
          <p>For advice or to discuss a job</p>
          <a class="big" href="{TEL}">{TEL_TXT}</a>
        </div>
      </div>
      <div class="contact-opt">
        <div class="c-ico">{WA.replace('class="wa-icon"', 'class="wa-icon" style="width:54px;height:54px"')}</div>
        <div>
          <h3>WhatsApp the workshop</h3>
          <p>Send a part number or a photo</p>
          <span class="tag">Proposed contact option</span>
        </div>
      </div>
      <div class="contact-opt">
        <div class="c-ico" style="background:rgba(255,255,255,.1)">{DOC}</div>
        <div>
          <h3>Request a free estimate</h3>
          <p>Tell us what needs testing or repairing</p>
          <a class="text-link" href="#estimate">What to have ready</a>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="estimate" id="estimate" aria-labelledby="estimate-h">
  <div class="wrap estimate-grid">
    <div>
      <p class="eyebrow">Free estimates</p>
      <h2 id="estimate-h">Request a free estimate</h2>
      <p>M&amp;B gives free estimates for repairs to fuel injection equipment on car, commercial and marine units, and for auto electrical units. From a minor fault to a major failure, the team can answer your questions or offer advice.</p>
      <p><strong>It helps to have these ready:</strong></p>
      <ul class="checklist">
        <li>Your vehicle make, model and registration, or the machine the part came from</li>
        <li>The symptoms, such as a warning light, lack of power, smoke, bad starting or a fuel leak</li>
        <li>The part number from the injector or pump, if you know it</li>
        <li>Whether you need the part collected, or want it removed and refitted</li>
      </ul>
    </div>
    <div class="card">
      <h3>Get your estimate</h3>
      <p>Call the workshop to talk through the job. An online form for written enquiries is coming soon.</p>
      <a class="btn btn-red" href="{TEL}">{PHONE}Call {TEL_TXT}</a>
      <div class="soon-btn" aria-label="Written enquiry form, coming soon">Written enquiry form <span class="tag">Coming soon</span></div>
      <p class="note" style="margin-top:14px">This preview doesn’t collect enquiries. Until the form is ready, please call the workshop.</p>
      <address class="address"><strong>M&amp;B Fuel Injection Service Ltd</strong><br>Unit 3 Aercon Buildings, Woodside Rd,<br>Eastleigh, Hampshire SO50 4ET</address>
    </div>
  </div>
</section>"""

# ---------- homepage ----------
HOME = f"""<section class="hero" aria-labelledby="hero-h">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <h1 id="hero-h">Diesel expertise.<br>Since 1974.</h1>
      <p class="hero-sub">Diesel fuel injection testing, repairs and diagnostics.</p>
      <div class="btn-row">
        <a class="btn btn-red" href="{TEL}">Call a diesel specialist {ARROW}</a>
        <a class="btn btn-outline-light" href="#estimate">Request a free estimate {ARROW}</a>
      </div>
      {wa_preview()}
    </div>
    <div class="hero-media">
      <img src="assets/img/hero-workshop.webp" width="514" height="318" alt="Technician testing a diesel injector on a test bench" fetchpriority="high">
      <span class="img-label">Illustrative workshop photo</span>
    </div>
  </div>
</section>

<section class="routes" aria-label="How can we help?">
  <div class="wrap route-grid">
    <a class="route-card" href="vehicle-diagnostics.html">
      {ENGINE}<strong>My vehicle has a diesel fault</strong>
      <span class="more">Vehicle diagnostics {ARROW}</span>
    </a>
    <a class="route-card" href="injector-pump-services.html">
      {INJECTOR}<strong>I have an injector or pump to test</strong>
      <span class="more">Injector and pump services {ARROW}</span>
    </a>
    <a class="route-card" href="collection-delivery.html">
      {VAN}<strong>I need collection and delivery</strong>
      <span class="more">Collection and delivery {ARROW}</span>
    </a>
  </div>
</section>

<section class="section" id="about" aria-labelledby="about-h" style="scroll-margin-top:70px">
  <div class="wrap split">
    <div>
      <p class="eyebrow">About us</p>
      <h2 id="about-h">Diesel fuel injection specialists</h2>
      <p class="lead">Supplying, reconditioning and testing all makes of diesel fuel injection equipment since 1974.</p>
      <p>M&amp;B was appointed Bosch Diesel Service Agents in 1976 and holds Bosch Diesel Centre status, quality audited every year. It became a Delphi Diesel Centre in 2008 and has since been appointed a Centre of Excellence. The Eastleigh premises, close to the M3 and M27, include a modern workshop, test shop, garage and clean room.</p>
      <ul class="quick-links">
        <li><a href="vehicle-diagnostics.html">Diagnostics {ARROW}</a></li>
        <li><a href="injector-pump-services.html#common-rail">Common rail {ARROW}</a></li>
        <li><a href="vehicle-diagnostics.html#dpf">DPF cleaning {ARROW}</a></li>
        <li><a href="vehicle-diagnostics.html#seized">Seized injector removal {ARROW}</a></li>
        <li><a href="vehicle-diagnostics.html#removal">Removal &amp; fitting {ARROW}</a></li>
        <li><a href="services.html">View all services {ARROW}</a></li>
      </ul>
    </div>
    <div class="img-wrap">
      <img src="assets/img/injectors.webp" width="398" height="220" alt="Row of diesel injectors on a workbench" loading="lazy" style="width:100%">
      <span class="img-label">Illustrative photo</span>
    </div>
  </div>
</section>

<section class="section section-pale" aria-labelledby="col-h">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Collection &amp; delivery</p>
      <h2 id="col-h">Free collection and delivery</h2>
      <p class="lead">We offer a free collection and delivery service for diesel injectors, pumps and other components.</p>
      <p>A daily service runs from our Eastleigh workshop near the M3 and M27. If you’re further afield, an express courier service covers the rest of the UK. Ask us whether your location is on the daily route.</p>
      <div class="btn-row">
        <a class="btn btn-red" href="collection-delivery.html">Ask us about collection {ARROW}</a>
      </div>
    </div>
    <div class="img-wrap">
      <img src="assets/img/van.webp" width="453" height="212" alt="White M&amp;B collection van outside the workshop" loading="lazy" style="width:100%">
      <span class="img-label">Illustrative van photo</span>
    </div>
  </div>
</section>

{CONTACT}"""

# ---------- vehicle diagnostics ----------
DIAG = f"""<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> / <a href="services.html">Services</a> / Vehicle diagnostics</p>
    <h1>My vehicle has a diesel fault</h1>
    <p class="lead">M&amp;B’s diagnostic equipment checks that your engine’s electronic control systems are working, and uses stored fault codes to find the problem on most vehicles on the road today.</p>
    <div class="btn-row">
      <a class="btn btn-red" href="{TEL}">{PHONE}Call {TEL_TXT}</a>
      <a class="btn btn-outline-light" href="index.html#estimate">Request a free estimate {ARROW}</a>
    </div>
  </div>
</section>
<div class="content">
  <div class="wrap content-grid">
    <div>
      <h2 id="faults">Faults we diagnose</h2>
      <p>Call the workshop if you’re seeing any of these:</p>
      <ul class="ticks">
        <li>Engine management light on</li>
        <li>Lack of power</li>
        <li>Poor fuel consumption</li>
        <li>Bad starting</li>
        <li>Excessive smoke</li>
        <li>Erratic idle</li>
        <li>Fuel leaks</li>
        <li>Seized or blowing injectors</li>
        <li>Low fuel pressure</li>
      </ul>
      <p>The workshop uses Bosch KTS670, Delphi DS350 and Denso DSTPC diagnostic equipment.</p>

      <h2 id="removal">Removal &amp; fitting</h2>
      <p>Fuel pumps, injectors and related parts can be removed, serviced and refitted to your vehicle, either at our premises or on site. Smoke emission testing to MOT standards is also available.</p>
      <p>{more('removal-fitting.html', 'More about removal &amp; fitting')}</p>

      <h2 id="seized">Seized injector removal</h2>
      <p>Using the latest equipment, we can remove injectors that are seized in the cylinder head, snapped or damaged. The work can be done at your premises or in our workshops. Genuine replacement injectors are available, plus a re-coding service.</p>
      <p>{more('seized-injector-removal.html', 'More about seized injector removal')}</p>

      <h2 id="dpf">DPF cleaning</h2>
      <p>Cleaning your existing diesel particulate filter recovers up to 98% of its original efficiency, which can save the cost of a replacement. The service covers cars, heavy goods vehicles, plant and agricultural machinery.</p>
      <p>{more('dpf-cleaning.html', 'More about DPF cleaning')}</p>

      <figure class="figure">
        <img src="assets/img/mb-workshop-strip.webp" width="960" height="200" alt="Technicians at work, and a workshop with clean room and test shop" loading="lazy">
        <figcaption>Images from M&amp;B’s current website</figcaption>
      </figure>
    </div>
    {aside('Talk to a diesel specialist', 'Describe the symptoms and we’ll tell you the best next step.')}
  </div>
</div>
{cta_strip('Not sure what’s wrong? Call the workshop.')}"""

# ---------- injector & pump ----------
INJ = f"""<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> / <a href="services.html">Services</a> / Injector &amp; pump services</p>
    <h1>I have an injector or pump to test</h1>
    <p class="lead">Test and repair for diesel injectors and pumps of all makes, carried out by fully trained technicians on manufacturer-approved test equipment. Fuel pump calibration print-outs are available if required.</p>
    <div class="btn-row">
      <a class="btn btn-red" href="{TEL}">{PHONE}Call {TEL_TXT}</a>
      <a class="btn btn-outline-light" href="index.html#estimate">Request a free estimate {ARROW}</a>
    </div>
  </div>
</section>
<div class="content">
  <div class="wrap content-grid">
    <div>
      <h2 id="common-rail">Common rail</h2>
      <p>A complete and cost-effective test and repair service for Bosch and Delphi common rail pumps (CP1 and CP3) and injectors. Only genuine parts are fitted, calibrated on Bosch and Delphi accredited test equipment.</p>
      <p>{more('common-rail.html', 'More about common rail')}</p>

      <h2 id="electronic-pumps">Electronic fuel pumps</h2>
      <p>As an official Bosch and Delphi Diesel Centre, our factory-trained technicians repair and test VP30 and VP44 pumps with integrated ECU, as fitted to Audi, BMW, Ford, Vauxhall and others, as well as EDC inline and EDC rotary pumps. All repairs are guaranteed and covered by the nationwide Bosch and Delphi diesel network.</p>
      <p>{more('electronic-fuel-pumps.html', 'More about electronic fuel pumps')}</p>

      <h2 id="unit-pump">Unit pump &amp; injector repair</h2>
      <p>Test and repair for Bosch and Delphi EUI (electronic unit injectors) and EUP (electronic unit pumps), including the latest Delphi smart pump and injector, for makes including DAF, Iveco, Land Rover, MAN, Mercedes, Renault, Scania, Volvo, Volvo Penta and VW.</p>
      <p>{more('unit-pump-injector-repair.html', 'More about unit pump &amp; injector repair')}</p>

      <h2 id="all-makes">All makes</h2>
      <p>As well as Bosch and Delphi, we test and repair most makes of diesel fuel injection equipment, including Denso, Stanadyne and Siemens, and earlier makes such as Bryce, Gardner and CAV. A large selection of service exchange units is available from stock.</p>
      <p>{more('all-makes.html', 'More about the makes we repair')}</p>

      <h2 id="test-shop">Test shop &amp; clean room</h2>
      <p>The test shop holds only manufacturer-approved equipment, including Bosch 815 and Hartridge test benches and the Bosch EPS 708 common rail bench, rated for injection pressures up to 2,500 bar. The benches are regularly audited, and every test result is recorded and archived electronically.</p>
      <p>Common rail pumps and injectors are assembled in a separate clean room with climate control and HEPA filtration, because even tiny amounts of dirt can cause a modern injector to fail.</p>
      <p>{more('test-shop.html', 'More about the test shop')} &nbsp; {more('clean-room.html', 'More about the clean room')}</p>

      <h2 id="sending">Sending us a part</h2>
      <p>Garages and customers can send injectors and pumps in using our <a href="collection-delivery.html">collection and delivery service</a>. Have the part number to hand when you call, as it helps us give you a free estimate.</p>
    </div>
    {aside('Have a part number?', 'Call with the part number and the symptoms, and we can tell you about testing, repair or a service exchange unit.')}
  </div>
</div>
{cta_strip('Got an injector or pump to test? Call the workshop.')}"""

# ---------- collection & delivery ----------
COL = f"""<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> / <a href="services.html">Services</a> / Collection &amp; delivery</p>
    <h1>I need collection and delivery</h1>
    <p class="lead">Free collection and delivery for diesel injectors, pumps and other components, so you don’t have to bring them to the workshop.</p>
    <div class="btn-row">
      <a class="btn btn-red" href="{TEL}">{PHONE}Ask about collection: {TEL_TXT}</a>
      <a class="btn btn-outline-light" href="index.html#estimate">Request a free estimate {ARROW}</a>
    </div>
  </div>
</section>
<div class="content">
  <div class="wrap content-grid">
    <div>
      <h2>How it works</h2>
      <h3>Daily collection and delivery</h3>
      <p>A daily delivery and collection service runs when you need it, from our industrial premises in Eastleigh, close to the M3 and M27 motorways.</p>
      <h3>Express courier (UK only)</h3>
      <p>If you’re outside the daily delivery area, we can offer an express courier service anywhere in the UK. Request a collection and we’ll email you a collection label. Collection is free for parcels up to 30kg.</p>
      <p class="soon-inline"><strong>Online collection request:</strong> coming soon. For now, call <a href="{TEL}">{TEL_TXT}</a> to arrange a collection.</p>

      <h2>Is my location covered?</h2>
      <p>Call the workshop and tell us where you are. We’ll let you know whether you’re on the daily route or whether the courier service is the better option.</p>

      <h2>What to tell us</h2>
      <ul class="checklist">
        <li>Your company name (if any), contact name and phone number</li>
        <li>The collection address, including the postcode</li>
        <li>The part, such as an injector, pump or other component, and the part number if known</li>
        <li>A short description of the fault</li>
      </ul>

      <figure class="figure">
        <img src="assets/img/van.webp" width="453" height="212" alt="White M&amp;B collection van outside the workshop" loading="lazy">
        <figcaption>Illustrative van photo</figcaption>
      </figure>
    </div>
    {aside('Ask us about collection', 'Tell us where you are and what needs collecting.')}
  </div>
</div>
{cta_strip('Need something collected? Call the workshop.')}"""

# ---------- services hub ----------
def svc(title, text, preview=None, page_file=None):
    links = []
    if page_file:
        links.append(f'<a href="{page_file}">Find out more {ARROW}</a>')
    elif preview:
        links.append(f'<a href="{preview[0]}">{preview[1]} {ARROW}</a>')
    return f'<div class="svc"><h3>{title}</h3><p>{text}</p><div class="links">{"".join(links)}</div></div>'


SVC = f"""<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> / Services</p>
    <h1>Our services</h1>
    <p class="lead">Testing, repair and diagnostics for diesel fuel injection equipment on car, commercial, plant and marine applications, plus auto electrical work.</p>
    <div class="jump">
      <a href="#vehicle">Vehicle faults</a><a href="#components">Injectors &amp; pumps</a><a href="#workshop">Workshop</a><a href="#electrical">Auto electrical</a>
    </div>
  </div>
</section>
<div class="content">
  <div class="wrap">
    <div class="svc-group" id="vehicle">
      <h2>Vehicle faults &amp; on-vehicle work</h2>
      <p>For drivers and fleet operators with a diesel fault, and garages that need parts removed or refitted.</p>
      <div class="svc-grid">
        {svc('Diagnostics', 'Fault-code diagnosis of electronic control systems on most vehicles on the road today.', ('vehicle-diagnostics.html#faults', 'Vehicle diagnostics'), None)}
        {svc('Removal &amp; Fitting', 'Pumps and injectors removed, serviced and refitted at our premises or on site. Smoke emission testing to MOT standards.', ('vehicle-diagnostics.html#removal', 'Read the summary'), 'removal-fitting.html')}
        {svc('Seized Injector Removal', 'Seized, snapped or damaged injectors removed at your premises or ours. Genuine replacements and re-coding.', ('vehicle-diagnostics.html#seized', 'Read the summary'), 'seized-injector-removal.html')}
        {svc('DPF Cleaning', 'Recovers up to 98% of a DPF’s original efficiency, for cars, HGVs, plant and agricultural machinery.', ('vehicle-diagnostics.html#dpf', 'Read the summary'), 'dpf-cleaning.html')}
      </div>
    </div>
    <div class="svc-group" id="components">
      <h2>Injectors &amp; pumps</h2>
      <p>For garages and customers with a component to test or repair. Parts can be sent in using our <a href="collection-delivery.html">collection and delivery service</a>.</p>
      <div class="svc-grid">
        {svc('Common Rail', 'Bosch and Delphi common rail pumps (CP1 and CP3) and injectors, using genuine parts.', ('injector-pump-services.html#common-rail', 'Injector &amp; pump services'), 'common-rail.html')}
        {svc('Electronic Fuel Pumps', 'VP30 and VP44 pumps with integrated ECU, plus EDC inline and rotary pumps. Repairs guaranteed.', ('injector-pump-services.html#electronic-pumps', 'Read the summary'), 'electronic-fuel-pumps.html')}
        {svc('Unit Pump &amp; Injector Repair', 'Bosch and Delphi EUI and EUP, including the latest Delphi smart pump and injector.', ('injector-pump-services.html#unit-pump', 'Read the summary'), 'unit-pump-injector-repair.html')}
        {svc('All Makes', 'Denso, Stanadyne, Siemens and earlier makes such as Bryce, Gardner and CAV. Exchange units from stock.', ('injector-pump-services.html#all-makes', 'Read the summary'), 'all-makes.html')}
      </div>
    </div>
    <div class="svc-group" id="workshop">
      <h2>Workshop &amp; facilities</h2>
      <div class="svc-grid">
        {svc('Test Shop', 'Manufacturer-approved Bosch and Hartridge test benches, regularly audited, with results logged electronically.', ('injector-pump-services.html#test-shop', 'Read the summary'), 'test-shop.html')}
        {svc('Clean Room', 'Climate-controlled clean room with HEPA filtration for assembling common rail pumps and injectors.', ('injector-pump-services.html#test-shop', 'Read the summary'), 'clean-room.html')}
        {svc('Bosch Diesel Centre', 'Part of Bosch’s international diesel workshop network: diagnosis, pump exchange and component repair.', None, 'bosch-diesel-centre.html')}
        {svc('Delphi Diesel Centre of Excellence', 'Authorised for OE warranty work, advanced diagnostics and repair of Delphi systems.', None, 'delphi-diesel-centre.html')}
      </div>
    </div>
    <div class="svc-group" id="electrical">
      <h2>Auto electrical</h2>
      <div class="svc-grid">
        {svc('Auto Electrical', 'Overhaul and testing of starter motors and alternators for car, commercial, plant and marine use. Free starter and alternator testing.', None, 'auto-electrical.html')}
      </div>
    </div>
    <figure class="figure">
      <img src="assets/img/mb-premises.webp" width="960" height="200" alt="M&amp;B’s Eastleigh premises and the workshop, clean room and test shop" loading="lazy">
      <figcaption>M&amp;B’s premises, from the current website</figcaption>
    </figure>
  </div>
</div>
{cta_strip('Not sure which service you need? Call the workshop.')}"""

# ---------- coming-soon service pages ----------
# Each: file, title, group (hub anchor), lead, paragraphs, optional list, related route page
SERVICE_PAGES = [
    ("removal-fitting.html", "Removal &amp; Fitting", "vehicle",
     "Fuel pumps, injectors and related parts removed, serviced and refitted to your vehicle, at our premises or on site.",
     ["Smoke emission testing to MOT standards is also available."], None,
     ("vehicle-diagnostics.html", "Vehicle diagnostics")),
    ("seized-injector-removal.html", "Seized Injector Removal", "vehicle",
     "We remove seized, snapped and damaged injectors using the very latest equipment.",
     ["Work can be carried out at your premises or in our own workshops. Genuine replacement injectors are available, plus a re-coding service."],
     ["Injectors seized in the cylinder head", "Snapped injectors", "Damaged injectors"],
     ("vehicle-diagnostics.html", "Vehicle diagnostics")),
    ("dpf-cleaning.html", "DPF Cleaning", "vehicle",
     "Cleaning recovers up to 98% of your DPF’s original efficiency, saving the cost of a replacement.",
     ["The service covers cars, heavy goods vehicles, plant and agricultural machinery, as well as selective catalytic reduction (SCR) units."],
     ["Reverse flush system removes ash deposits", "Removes PM10, oil and cerium residuals", "Preserves the noble metals of the DPF and catalyst", "Sensors can be left in place"],
     ("vehicle-diagnostics.html", "Vehicle diagnostics")),
    ("common-rail.html", "Common Rail", "components",
     "A complete and cost-effective test and repair service for Bosch and Delphi common rail pumps (CP1 and CP3) and injectors.",
     ["We fit only genuine parts, calibrated on state-of-the-art Bosch and Delphi accredited test equipment."], None,
     ("injector-pump-services.html", "Injector &amp; pump services")),
    ("electronic-fuel-pumps.html", "Electronic Fuel Pumps", "components",
     "Factory-trained technicians repair and test VP30 and VP44 pumps with integrated ECU, as well as EDC inline and EDC rotary pumps.",
     ["These pumps are fitted to Audi, BMW, Ford, Vauxhall and others. All repairs are guaranteed and covered by the nationwide Bosch and Delphi diesel network."], None,
     ("injector-pump-services.html", "Injector &amp; pump services")),
    ("unit-pump-injector-repair.html", "Unit Pump &amp; Injector Repair", "components",
     "Test and repair for Bosch and Delphi EUI (electronic unit injectors) and EUP (electronic unit pumps), including the latest Delphi smart pump and injector.",
     ["Makes we work on include:"],
     ["DAF", "Iveco", "Land Rover", "MAN", "Mercedes", "Renault", "Scania", "Volvo", "Volvo Penta", "VW"],
     ("injector-pump-services.html", "Injector &amp; pump services")),
    ("all-makes.html", "All Makes", "components",
     "As well as Bosch and Delphi, we test and repair most makes of diesel fuel injection equipment.",
     ["That includes Denso, Stanadyne and Siemens, and earlier makes such as Bryce, Gardner and CAV. A large selection of service exchange units is available from stock.",
      "We operate an open house policy and give free estimates for repairs to fuel injection or auto electrical units."], None,
     ("injector-pump-services.html", "Injector &amp; pump services")),
    ("test-shop.html", "Test Shop", "workshop",
     "Our test shop holds only manufacturer-approved computerised test equipment, regularly audited to strict diesel test specifications.",
     ["Every test result is recorded and archived electronically. Our equipment includes:"],
     ["3 × Bosch 815 test benches", "Hartridge AVM PC2 test bench with Cambox", "Hartridge CRi PC test bench", "Hartridge 700 test bench", "Bosch EPS 708 common rail test bench, rated to 2,500 bar"],
     ("injector-pump-services.html", "Injector &amp; pump services")),
    ("clean-room.html", "Clean Room", "workshop",
     "Common rail pumps and injectors are assembled in a separate clean room with climate control and HEPA filtration.",
     ["Even tiny amounts of dirt can cause a modern common rail injector to malfunction or break down. Working in the clean room means parts are assembled to manufacturers’ quality standards, and bench test results are recorded and archived electronically."], None,
     ("injector-pump-services.html", "Injector &amp; pump services")),
    ("bosch-diesel-centre.html", "Bosch Diesel Centre", "workshop",
     "M&amp;B has been a Bosch Diesel Service Agent since 1976 and holds Bosch Diesel Centre status, quality audited every year.",
     ["As a Bosch Diesel Centre we’re part of Bosch’s international diesel workshop organisation, offering workshop owners, business customers and fleet operators:"],
     ["Diagnosis and system tests for all diesel systems and makes", "Pump exchange from our extensive stock", "Exchange pumps reconditioned by the Bosch Diesel Centre", "Factory-repaired pumps and new original equipment pumps", "Component repair of modern diesel systems", "General diesel vehicle repairs and maintenance to manufacturers’ specifications"],
     ("services.html", "All services")),
    ("delphi-diesel-centre.html", "Delphi Diesel Centre of Excellence", "workshop",
     "M&amp;B became a Delphi Diesel Centre in 2008 and has since been appointed a Centre of Excellence.",
     ["We’re authorised to carry out OE warranty work, advanced diesel diagnostics, and the test and repair of all Delphi diesel fuel injection systems, including rotary pumps and injectors, common rail pumps and injectors, and electronic unit injectors."], None,
     ("services.html", "All services")),
    ("auto-electrical.html", "Auto Electrical", "electrical",
     "A complete overhaul and testing service for all makes of starter motor and alternator, for car, commercial, plant and marine applications.",
     ["Starter and alternator testing is free of charge, and free estimates before repair are available on request. Service exchange units are usually available from stock."], None,
     ("services.html", "All services")),
]


def soon_panel(title):
    return f"""<div class="soon">
        <span class="tag">Coming soon</span>
        <h2>Full {title} page coming soon</h2>
        <p>We’re putting together a fuller page for this service, with photos and more detail. In the meantime, the workshop is happy to answer any questions.</p>
        <div class="btn-row">
          <a class="btn btn-red" href="{TEL}">{PHONE}Call {TEL_TXT}</a>
          <a class="btn btn-outline" href="index.html#estimate">Request a free estimate {ARROW}</a>
        </div>
      </div>"""


def service_page(fname, title, group, lead, paras, items, related):
    back = more('services.html', 'See all services')
    if related[0] != 'services.html':
        back = more(related[0], 'Back to ' + related[1].lower()) + ' &nbsp; ' + back
    body_paras = "\n      ".join(f"<p>{x}</p>" for x in paras)
    lst = ("<ul class=\"ticks\">" + "".join(f"<li>{i}</li>" for i in items) + "</ul>") if items else ""
    body = f"""<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> / <a href="services.html#{group}">Services</a> / {title}</p>
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
    <div class="btn-row">
      <a class="btn btn-red" href="{TEL}">{PHONE}Call {TEL_TXT}</a>
      <a class="btn btn-outline-light" href="index.html#estimate">Request a free estimate {ARROW}</a>
    </div>
  </div>
</section>
<div class="content">
  <div class="wrap content-grid">
    <div>
      {body_paras}
      {lst}
      {soon_panel(title)}
      <p style="margin-top:24px">{back}</p>
    </div>
    {aside('Talk to the workshop', 'Call to discuss a job, or have your part number ready for a free estimate.')}
  </div>
</div>"""
    page(fname, f"{title} | M&amp;B Fuel Injection Service", lead.replace('&amp;', '&amp;')[:155], "svc", body)


def legal_page(fname, title):
    body = f"""<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> / {title}</p>
    <h1>{title}</h1>
  </div>
</section>
<div class="content">
  <div class="wrap">
    <div class="soon" style="max-width:720px">
      <span class="tag">Coming soon</span>
      <h2>Our {title.lower()} will be published here</h2>
      <p>This page will be added when the new website launches. If you need a copy in the meantime, please call the workshop on <a href="{TEL}">{TEL_TXT}</a>.</p>
    </div>
  </div>
</div>"""
    page(fname, f"{title} | M&amp;B Fuel Injection Service", f"M&amp;B Fuel Injection Service {title.lower()}.", "", body)


if __name__ == "__main__":
    page("index.html", "M&amp;B Fuel Injection Service | Diesel expertise since 1974",
         "Diesel fuel injection testing, repairs and diagnostics in Eastleigh, Hampshire, since 1974.", "home", HOME)
    page("services.html", "Services | M&amp;B Fuel Injection Service",
         "All M&amp;B diesel fuel injection, diagnostics and auto electrical services.", "svc", SVC)
    page("vehicle-diagnostics.html", "Vehicle diagnostics | M&amp;B Fuel Injection Service",
         "Diesel fault diagnosis, removal and fitting, seized injector removal and DPF cleaning.", "diag", DIAG)
    page("injector-pump-services.html", "Injector &amp; pump services | M&amp;B Fuel Injection Service",
         "Test and repair of diesel injectors and pumps of all makes.", "inj", INJ)
    page("collection-delivery.html", "Collection &amp; delivery | M&amp;B Fuel Injection Service",
         "Free collection and delivery for diesel injectors, pumps and components.", "col", COL)
    for sp in SERVICE_PAGES:
        service_page(*sp)
    legal_page("terms.html", "Terms &amp; Conditions")
    legal_page("privacy.html", "Privacy Policy")
