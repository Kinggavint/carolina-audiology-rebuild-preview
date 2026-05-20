#!/usr/bin/env python3
"""Carolina Audiology Associates - static site builder.
Generates index.html, services.html, about.html, education.html, contact.html
with shared header/footer, full schema, and complete copy.
"""
import os, json, pathlib

OUT = pathlib.Path(__file__).parent

SITE = {
    "name": "Carolina Audiology Associates",
    "phone": "252-790-6649",
    "phone_tel": "+12527906649",
    "email": "info@carolinaaud.com",
    "address": "4065 Capital Drive",
    "city": "Rocky Mount",
    "state": "NC",
    "zip": "27804",
    "country": "US",
    "geo_lat": 35.9382,
    "geo_lng": -77.7905,
    "hours_text": "Mon–Thu 9:00 AM – 5:00 PM",
    "founder": "Dr. Melissa Palmer, Au.D.",
    "url": "https://kinggavint.github.io/carolina-audiology-proof",
}

# ---------------------------------------------------------------------------
# Shared partials
# ---------------------------------------------------------------------------

def head(title, description, canonical_path, extra_schema=None):
    canonical = f"{SITE['url']}{canonical_path}"
    base_schema = {
        "@context": "https://schema.org",
        "@type": "MedicalBusiness",
        "@id": f"{SITE['url']}/#business",
        "name": SITE["name"],
        "image": f"{SITE['url']}/og.png",
        "url": SITE["url"] + "/",
        "telephone": SITE["phone"],
        "email": SITE["email"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": SITE["address"],
            "addressLocality": SITE["city"],
            "addressRegion": SITE["state"],
            "postalCode": SITE["zip"],
            "addressCountry": SITE["country"],
        },
        "geo": {"@type": "GeoCoordinates", "latitude": SITE["geo_lat"], "longitude": SITE["geo_lng"]},
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"],
            "opens": "09:00", "closes": "17:00"
        }],
        "areaServed": [
            {"@type": "City", "name": "Rocky Mount, NC"},
            {"@type": "City", "name": "Tarboro, NC"},
            {"@type": "City", "name": "Wilson, NC"},
        ],
        "medicalSpecialty": "Audiology",
        "founder": {"@type": "Person", "name": SITE["founder"]},
        "priceRange": "$$",
    }
    schema_blocks = [json.dumps(base_schema, indent=2)]
    if extra_schema:
        for s in extra_schema:
            schema_blocks.append(json.dumps(s, indent=2))
    schema_html = "\n".join(f'<script type="application/ld+json">{s}</script>' for s in schema_blocks)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta name="theme-color" content="#0e3f4f">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/carolina-audiology-proof/css/base.css">
{schema_html}
</head>
<body>
<a href="#main" class="skip-link">Skip to main content</a>
"""

def header(active="home"):
    def cls(name): return ' class="active"' if name == active else ''
    return f"""<div class="utility-bar">
  <div class="container">
    <div>Serving Rocky Mount, Tarboro &amp; Wilson, NC</div>
    <div class="util-right">
      <a href="tel:{SITE['phone_tel']}">Call {SITE['phone']}</a>
      <span>{SITE['hours_text']}</span>
    </div>
  </div>
</div>
<header class="site-header">
  <div class="container header-inner">
    <a href="/carolina-audiology-proof/" class="brand" aria-label="Carolina Audiology Associates home">
      <div class="brand-mark">CA</div>
      <div class="brand-text">
        <span class="name">Carolina Audiology</span>
        <span class="tag">Associates · Rocky Mount, NC</span>
      </div>
    </a>
    <nav class="primary" aria-label="Primary">
      <a href="/carolina-audiology-proof/"{cls('home')}>Home</a>
      <a href="/carolina-audiology-proof/services.html"{cls('services')}>Services</a>
      <a href="/carolina-audiology-proof/about.html"{cls('about')}>About</a>
      <a href="/carolina-audiology-proof/education.html"{cls('education')}>Hearing Health</a>
      <a href="/carolina-audiology-proof/contact.html" class="btn btn-primary">Book Appointment</a>
    </nav>
    <button class="nav-toggle" aria-label="Open menu" onclick="document.querySelector('nav.primary').classList.toggle('open')">☰</button>
  </div>
</header>
<main id="main">
"""

FOOTER = f"""</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <h4>Carolina Audiology Associates</h4>
        <p>Independent, doctor-led hearing care for adults in Rocky Mount, Tarboro, Wilson, and across eastern North Carolina.</p>
        <p style="margin-top:14px;"><strong style="color:#fff">{SITE['phone']}</strong><br>{SITE['address']}<br>{SITE['city']}, {SITE['state']} {SITE['zip']}</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="/carolina-audiology-proof/services.html#hearing-evaluation">Hearing Evaluation</a></li>
          <li><a href="/carolina-audiology-proof/services.html#tinnitus">Tinnitus Treatment</a></li>
          <li><a href="/carolina-audiology-proof/services.html#hearing-aids">Hearing Aids</a></li>
          <li><a href="/carolina-audiology-proof/services.html#earwax">Earwax Removal</a></li>
          <li><a href="/carolina-audiology-proof/services.html#hearing-protection">Hearing Protection</a></li>
        </ul>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="/carolina-audiology-proof/about.html">About Dr. Palmer</a></li>
          <li><a href="/carolina-audiology-proof/education.html">Hearing Health</a></li>
          <li><a href="/carolina-audiology-proof/contact.html">Book Appointment</a></li>
        </ul>
      </div>
      <div>
        <h4>Hours</h4>
        <ul>
          <li>Mon · 9:00 – 5:00</li>
          <li>Tue · 9:00 – 5:00</li>
          <li>Wed · 9:00 – 5:00</li>
          <li>Thu · 9:00 – 5:00</li>
          <li>Fri – Sun · Closed</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>© 2026 Carolina Audiology Associates · All rights reserved</div>
      <div>HIPAA-compliant care · Most major insurance accepted</div>
    </div>
  </div>
</footer>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# Page bodies
# ---------------------------------------------------------------------------

def page_home():
    title = "Audiologist in Rocky Mount, NC | Carolina Audiology Associates"
    desc = "Independent audiology practice in Rocky Mount, NC. Dr. Melissa Palmer offers hearing evaluations, tinnitus treatment, hearing aids, and earwax removal. Call 252-790-6649."

    extra = [{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type":"Question","name":"What are the signs I should see an audiologist?","acceptedAnswer":{"@type":"Answer","text":"Common signs include turning up the TV louder than family members like, asking people to repeat themselves, trouble following conversations in restaurants, ringing or buzzing in your ears, and feeling more tired after social gatherings. If any of these sound familiar, a baseline hearing evaluation is a smart next step."}},
            {"@type":"Question","name":"How long does a hearing evaluation take?","acceptedAnswer":{"@type":"Answer","text":"A complete adult diagnostic hearing evaluation at Carolina Audiology Associates takes about 60 minutes. That includes a health and lifestyle conversation, a full hearing test, a clear review of your results, and time to answer your questions."}},
            {"@type":"Question","name":"Do you accept insurance?","acceptedAnswer":{"@type":"Answer","text":"Yes. We work with Medicare, Blue Cross Blue Shield, UnitedHealthcare, Humana, and Aetna. We will verify your benefits before your visit so there are no surprises."}},
            {"@type":"Question","name":"What hearing aid brands do you fit?","acceptedAnswer":{"@type":"Answer","text":"Because we are independent, we fit several leading manufacturers and select the technology that best matches your hearing loss, lifestyle, and budget. We are never tied to one brand."}},
            {"@type":"Question","name":"Where do you serve?","acceptedAnswer":{"@type":"Answer","text":"Our office is in Rocky Mount, NC. We see patients from Rocky Mount, Tarboro, Wilson, Nashville, Wilson County, Edgecombe County, Nash County, and the surrounding communities in eastern North Carolina."}},
        ]
    }, {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".hero h1", ".hero p.lead", "#why-us p"]}
    }]

    body = """
<section class="hero">
  <div class="container">
    <span class="section-eyebrow" style="color:#ffd9c5">Welcome to Carolina Audiology Associates</span>
    <h1>Hearing care that listens first.</h1>
    <p class="lead">Independent, doctor-led audiology in Rocky Mount, NC. We take the time to understand your hearing — and your life — before we recommend anything.</p>
    <div class="hero-actions">
      <a href="/carolina-audiology-proof/contact.html" class="btn btn-primary">Book an Appointment</a>
      <a href="tel:""" + SITE['phone_tel'] + """" class="btn btn-ghost">Call """ + SITE['phone'] + """</a>
    </div>
    <p class="hero-meta">Serving <strong>Rocky Mount</strong>, <strong>Tarboro</strong>, and <strong>Wilson</strong> · Most major insurance accepted</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-header center">
      <span class="section-eyebrow">What we do</span>
      <h2>Comprehensive hearing care, under one roof.</h2>
      <p>From a first hearing screening to fitting, programming, and lifelong follow-up, every step of your hearing care happens with the same doctor who knows your story.</p>
    </div>
    <div class="service-grid">
      <div class="service-card">
        <div class="ico">🔍</div>
        <h3>Hearing Evaluations</h3>
        <p>Complete diagnostic hearing tests for adults. We measure how you hear in real-world listening — not just in a sound booth.</p>
        <a href="/carolina-audiology-proof/services.html#hearing-evaluation">Learn more →</a>
      </div>
      <div class="service-card">
        <div class="ico">🔔</div>
        <h3>Tinnitus Treatment</h3>
        <p>Personalized care plans to quiet ringing, buzzing, or hissing in your ears — including sound therapy and hearing aid integration.</p>
        <a href="/carolina-audiology-proof/services.html#tinnitus">Learn more →</a>
      </div>
      <div class="service-card">
        <div class="ico">🎧</div>
        <h3>Hearing Aids</h3>
        <p>Independent fitting from several leading manufacturers, programmed precisely to your hearing and your life.</p>
        <a href="/carolina-audiology-proof/services.html#hearing-aids">Learn more →</a>
      </div>
      <div class="service-card">
        <div class="ico">💧</div>
        <h3>Earwax Removal</h3>
        <p>Safe, gentle, professional earwax removal — performed by a doctor of audiology, not a guess at home.</p>
        <a href="/carolina-audiology-proof/services.html#earwax">Learn more →</a>
      </div>
      <div class="service-card">
        <div class="ico">🛡️</div>
        <h3>Hearing Protection</h3>
        <p>Custom hearing protection for musicians, hunters, swimmers, and anyone exposed to loud sound on the job.</p>
        <a href="/carolina-audiology-proof/services.html#hearing-protection">Learn more →</a>
      </div>
      <div class="service-card">
        <div class="ico">🛠️</div>
        <h3>Repair &amp; Programming</h3>
        <p>Cleaning, in-office repairs, and reprogramming for hearing aids you already own — even if you bought them elsewhere.</p>
        <a href="/carolina-audiology-proof/services.html#hearing-aids">Learn more →</a>
      </div>
    </div>
  </div>
</section>

<section class="alt" id="why-us">
  <div class="container">
    <div class="split">
      <div>
        <span class="section-eyebrow">Why patients choose us</span>
        <h2>Doctor-led care without the pressure.</h2>
        <p>We are an independent practice — not a chain. That means your appointments are unhurried, your questions get full answers, and the only person guiding your hearing care is the doctor sitting across from you.</p>
        <p>We will never push one brand, one device, or one price. We will recommend what is right for your hearing, your lifestyle, and your budget — and we will tell you honestly when you do not need a hearing aid yet.</p>
        <ul style="list-style:none;padding:0;margin-top:20px;">
          <li style="padding:8px 0;">✓ Time to actually talk with your audiologist</li>
          <li style="padding:8px 0;">✓ Independent — multiple manufacturers, no brand lock-in</li>
          <li style="padding:8px 0;">✓ Honest pricing and clear next steps</li>
          <li style="padding:8px 0;">✓ Most major insurance accepted</li>
          <li style="padding:8px 0;">✓ Lifetime aftercare on hearing aids fit at our office</li>
        </ul>
      </div>
      <div>
        <div style="background:#fff;padding:36px;border-radius:20px;box-shadow:var(--shadow-md);">
          <span class="section-eyebrow">Insurance accepted</span>
          <h3>We work with most major plans.</h3>
          <p>We verify your benefits before your visit so you know what is covered.</p>
          <div class="pill-row">
            <span class="pill">Medicare</span>
            <span class="pill">Blue Cross Blue Shield</span>
            <span class="pill">UnitedHealthcare</span>
            <span class="pill">Humana</span>
            <span class="pill">Aetna</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="deep">
  <div class="container">
    <div class="section-header center">
      <span class="section-eyebrow" style="color:#ffd9c5">The Carolina difference</span>
      <h2>Hearing care, built around you.</h2>
    </div>
    <div class="trust-bar">
      <div class="trust-item"><div class="num">60 min</div><div class="lbl">Unhurried evaluations</div></div>
      <div class="trust-item"><div class="num">5+</div><div class="lbl">Insurance plans accepted</div></div>
      <div class="trust-item"><div class="num">Au.D.</div><div class="lbl">Doctor-led visits, every time</div></div>
      <div class="trust-item"><div class="num">3</div><div class="lbl">Communities served</div></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-header center">
      <span class="section-eyebrow">Common questions</span>
      <h2>What patients ask before they call.</h2>
    </div>
    <div class="faq">
      <details><summary>What are the signs I should see an audiologist?</summary>
        <div class="content"><p>Common signs include turning up the TV louder than family members like, asking people to repeat themselves, trouble following conversations in restaurants, ringing or buzzing in your ears, and feeling more tired after social gatherings. If any of these sound familiar, a baseline hearing evaluation is a smart next step.</p></div>
      </details>
      <details><summary>How long does a hearing evaluation take?</summary>
        <div class="content"><p>A complete adult diagnostic hearing evaluation takes about 60 minutes. That includes a health and lifestyle conversation, a full hearing test, a clear review of your results, and time to answer your questions.</p></div>
      </details>
      <details><summary>Do you accept my insurance?</summary>
        <div class="content"><p>We work with Medicare, Blue Cross Blue Shield, UnitedHealthcare, Humana, and Aetna. We will verify your benefits before your visit so there are no surprises.</p></div>
      </details>
      <details><summary>What hearing aid brands do you fit?</summary>
        <div class="content"><p>Because we are independent, we fit several leading manufacturers and select the technology that best matches your hearing loss, lifestyle, and budget. We are never tied to one brand.</p></div>
      </details>
      <details><summary>Where do you serve?</summary>
        <div class="content"><p>Our office is in Rocky Mount, NC. We see patients from Rocky Mount, Tarboro, Wilson, Nashville, and the surrounding communities in eastern North Carolina.</p></div>
      </details>
    </div>
  </div>
</section>

<section class="cta-strip">
  <div class="container">
    <div>
      <h2>Ready to hear what you have been missing?</h2>
      <p>Book your hearing evaluation with Dr. Palmer today.</p>
    </div>
    <a href="/carolina-audiology-proof/contact.html" class="btn btn-primary">Book Appointment</a>
  </div>
</section>
"""
    return head(title, desc, "/", extra) + header("home") + body + FOOTER


def page_services():
    title = "Audiology Services in Rocky Mount, NC | Carolina Audiology Associates"
    desc = "Hearing evaluations, tinnitus treatment, hearing aid fitting and repair, earwax removal, and custom hearing protection in Rocky Mount, NC."
    extra = [{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type":"Question","name":"How much do hearing aids cost?","acceptedAnswer":{"@type":"Answer","text":"Hearing aid pricing typically ranges from about $1,500 to $7,000 for a pair, depending on technology level and features. We will walk you through exactly what each option does and what it costs before you decide anything."}},
            {"@type":"Question","name":"How long does a hearing aid fitting take?","acceptedAnswer":{"@type":"Answer","text":"Your hearing aid fitting appointment typically takes 60 to 90 minutes. We program your devices to your unique hearing prescription, show you how to use them, and confirm they sound right before you leave."}},
            {"@type":"Question","name":"Can you treat tinnitus?","acceptedAnswer":{"@type":"Answer","text":"Yes. We provide tinnitus evaluations and personalized treatment plans, which may include sound therapy, hearing aids with tinnitus features, counseling, and lifestyle strategies."}},
            {"@type":"Question","name":"Should I remove earwax at home?","acceptedAnswer":{"@type":"Answer","text":"We do not recommend cotton swabs or at-home ear candles. They can push wax deeper or injure the ear canal. Professional earwax removal is safer and only takes a few minutes."}},
        ]
    }]
    body = """
<section class="page-hero">
  <div class="container">
    <span class="section-eyebrow" style="color:#ffd9c5">Our services</span>
    <h1>Complete hearing care for adults.</h1>
    <p>From your first evaluation to lifelong follow-up, every service is delivered by a doctor of audiology who knows your hearing.</p>
  </div>
</section>

<section id="hearing-evaluation">
  <div class="container">
    <div class="split">
      <div>
        <span class="section-eyebrow">Step one</span>
        <h2>Diagnostic Hearing Evaluation</h2>
        <p>A complete adult hearing evaluation is the foundation of everything we do. It tells us how you hear — and how you hear in real life, not just in a quiet sound booth.</p>
        <p>Your appointment includes a conversation about your lifestyle and concerns, otoscopy to check the health of your ear canal, pure-tone testing, speech-in-noise testing, and a clear, plain-English explanation of your results. You leave with a baseline you can compare to in future years.</p>
        <p><strong>Time:</strong> About 60 minutes · <strong>Most insurance accepted.</strong></p>
      </div>
      <div>
        <div style="background:#fff;padding:32px;border-radius:20px;box-shadow:var(--shadow-md);">
          <h3 style="margin-top:0;">What you'll learn</h3>
          <ul style="list-style:none;padding:0;">
            <li style="padding:6px 0;">✓ The type and degree of your hearing loss</li>
            <li style="padding:6px 0;">✓ How your hearing compares to expected for your age</li>
            <li style="padding:6px 0;">✓ Whether hearing aids will help</li>
            <li style="padding:6px 0;">✓ A clear plan — even if that plan is "watch and wait"</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="alt" id="tinnitus">
  <div class="container">
    <div class="split">
      <div>
        <div style="background:#fff;padding:32px;border-radius:20px;box-shadow:var(--shadow-md);">
          <h3 style="margin-top:0;">Tinnitus treatments we offer</h3>
          <ul style="list-style:none;padding:0;">
            <li style="padding:6px 0;">✓ Tinnitus assessment and matching</li>
            <li style="padding:6px 0;">✓ Sound therapy and masking</li>
            <li style="padding:6px 0;">✓ Hearing aids with tinnitus relief features</li>
            <li style="padding:6px 0;">✓ Counseling and coping strategies</li>
            <li style="padding:6px 0;">✓ Referral to ENT when medically indicated</li>
          </ul>
        </div>
      </div>
      <div>
        <span class="section-eyebrow">For ringing, buzzing, or hissing</span>
        <h2>Tinnitus Evaluation &amp; Treatment</h2>
        <p>Tinnitus is the perception of sound — ringing, buzzing, hissing, or roaring — when no outside sound is present. It is incredibly common, and it is treatable. There is no single cure, but with the right plan, most people get meaningful, lasting relief.</p>
        <p>We start by understanding your tinnitus: when it started, what it sounds like, and how it affects your sleep, focus, and mood. Then we build a personalized plan combining sound therapy, hearing aids if appropriate, and practical coping strategies.</p>
      </div>
    </div>
  </div>
</section>

<section id="hearing-aids">
  <div class="container">
    <div class="section-header">
      <span class="section-eyebrow">Independent. Always.</span>
      <h2>Hearing Aid Fitting, Programming &amp; Repair</h2>
      <p>We fit several leading manufacturers and select the device that fits your hearing, your lifestyle, and your budget — not the device that gives us the best margin.</p>
    </div>
    <div class="service-grid">
      <div class="service-card">
        <h3>Fitting &amp; Programming</h3>
        <p>Every hearing aid is programmed to your unique hearing prescription using real-ear measurement, so you hear what you should be hearing — not a factory default.</p>
      </div>
      <div class="service-card">
        <h3>Follow-Up &amp; Aftercare</h3>
        <p>Hearing aids need fine-tuning. We include follow-up visits so we can adjust the programming as your brain adapts and as your needs change.</p>
      </div>
      <div class="service-card">
        <h3>Repair (Any Brand)</h3>
        <p>Cleaning, in-office repairs, and reprogramming — even for hearing aids you bought somewhere else. Bring them in and we will take a look.</p>
      </div>
    </div>
    <p style="margin-top:30px;color:var(--c-ink-soft);"><strong>Investment range:</strong> Hearing aids typically range from $1,500 to $7,000 per pair depending on technology level. We will walk you through every option clearly before you decide anything.</p>
  </div>
</section>

<section class="alt" id="earwax">
  <div class="container">
    <div class="split">
      <div>
        <span class="section-eyebrow">Safe and gentle</span>
        <h2>Professional Earwax Removal</h2>
        <p>Wax build-up is one of the most common — and most easily treated — causes of hearing trouble. We safely remove cerumen in the office using methods chosen for your ear, including curette, suction, or irrigation.</p>
        <p>Please do not use cotton swabs at home — they push wax deeper. And please skip the ear candles. Five minutes in our chair is safer and more effective.</p>
      </div>
      <div>
        <div style="background:#fff;padding:32px;border-radius:20px;box-shadow:var(--shadow-md);">
          <h3 style="margin-top:0;">When to come in</h3>
          <ul style="list-style:none;padding:0;">
            <li style="padding:6px 0;">✓ Sudden muffled hearing in one ear</li>
            <li style="padding:6px 0;">✓ A feeling of fullness or pressure</li>
            <li style="padding:6px 0;">✓ Itching or mild discomfort</li>
            <li style="padding:6px 0;">✓ Before a hearing evaluation if you know you build up wax</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="hearing-protection">
  <div class="container">
    <div class="section-header">
      <span class="section-eyebrow">Protect what you have</span>
      <h2>Custom Hearing Protection</h2>
      <p>The cheapest way to take care of your hearing is to not damage it in the first place. We make custom hearing protection for musicians, hunters, motorcyclists, factory workers, and anyone who spends time around loud sound.</p>
    </div>
    <div class="service-grid">
      <div class="service-card">
        <h3>Musicians</h3>
        <p>Filtered earplugs that lower volume evenly, so music still sounds like music — just safer.</p>
      </div>
      <div class="service-card">
        <h3>Hunters &amp; Shooters</h3>
        <p>Electronic and passive options that protect against gunshots while letting you hear conversation and surroundings.</p>
      </div>
      <div class="service-card">
        <h3>Industrial &amp; Workplace</h3>
        <p>Custom-molded protection for high-noise environments — comfortable enough to wear all shift.</p>
      </div>
      <div class="service-card">
        <h3>Swimmers</h3>
        <p>Custom swim plugs that keep water out of the ear canal, helpful for people prone to swimmer's ear or with tubes.</p>
      </div>
    </div>
  </div>
</section>

<section class="cta-strip">
  <div class="container">
    <div>
      <h2>Not sure where to start?</h2>
      <p>Start with a hearing evaluation. We will go from there together.</p>
    </div>
    <a href="/carolina-audiology-proof/contact.html" class="btn btn-primary">Book Appointment</a>
  </div>
</section>
"""
    return head(title, desc, "/services.html", extra) + header("services") + body + FOOTER


def page_about():
    title = "About Dr. Melissa Palmer | Carolina Audiology Associates, Rocky Mount NC"
    desc = "Meet Dr. Melissa Palmer, Au.D. — independent audiologist in Rocky Mount, NC. Learn about her approach to hearing care and the practice she built."
    body = """
<section class="page-hero">
  <div class="container">
    <span class="section-eyebrow" style="color:#ffd9c5">About the practice</span>
    <h1>Independent hearing care, built for eastern North Carolina.</h1>
    <p>Carolina Audiology Associates was founded on a simple idea: hearing care works best when the person across the desk has time to listen.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="split">
      <div>
        <span class="section-eyebrow">Meet your audiologist</span>
        <h2>Dr. Melissa Palmer, Au.D.</h2>
        <p>Dr. Palmer is the founding audiologist at Carolina Audiology Associates. She built the practice around the kind of hearing care she wished her own family could find — unhurried, honest, and independent.</p>
        <p>Every patient who walks into Carolina Audiology Associates sees Dr. Palmer. Not a technician. Not a sales associate. The same doctor handles your evaluation, your fitting, and your follow-up care — so nothing gets lost in handoffs and every decision is informed by your whole story.</p>
        <p>Dr. Palmer serves patients across Rocky Mount, Tarboro, Wilson, and the surrounding communities of Edgecombe, Nash, and Wilson counties.</p>
      </div>
      <div>
        <div style="background:var(--c-sand-200);padding:36px;border-radius:20px;">
          <h3 style="margin-top:0;">Our approach in one paragraph</h3>
          <p>We never push a brand. We never push a price. We never push you to buy anything before you are ready. We test, we listen, we explain, and we recommend only what fits your hearing and your life. If you do not need a hearing aid yet, we will tell you — and we will see you back next year for a check.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <div class="section-header center">
      <span class="section-eyebrow">Our values</span>
      <h2>How we work — every visit, every patient.</h2>
    </div>
    <div class="service-grid">
      <div class="service-card">
        <h3>Time</h3>
        <p>Hearing care that is rushed is hearing care that misses things. Our visits are scheduled to give you room to ask, room to think, and room to decide.</p>
      </div>
      <div class="service-card">
        <h3>Independence</h3>
        <p>We are not owned by a hearing aid manufacturer. We fit what works for you, not what we are contracted to push.</p>
      </div>
      <div class="service-card">
        <h3>Honesty</h3>
        <p>We will tell you exactly what your hearing test shows, exactly what each option costs, and exactly what to expect. No surprises.</p>
      </div>
      <div class="service-card">
        <h3>Continuity</h3>
        <p>The same audiologist sees you every visit. Your hearing story is never restarted with someone new.</p>
      </div>
      <div class="service-card">
        <h3>Patience</h3>
        <p>Adjusting to better hearing takes time. We schedule the follow-ups it takes to get it right — and we never charge per visit when you are fit at our office.</p>
      </div>
      <div class="service-card">
        <h3>Local</h3>
        <p>We live and work in eastern North Carolina. When you call, you reach the people who actually work here.</p>
      </div>
    </div>
  </div>
</section>

<section class="cta-strip">
  <div class="container">
    <div>
      <h2>Have a question for Dr. Palmer?</h2>
      <p>The fastest way to get an answer is to come in for a hearing evaluation.</p>
    </div>
    <a href="/carolina-audiology-proof/contact.html" class="btn btn-primary">Book Appointment</a>
  </div>
</section>
"""
    return head(title, desc, "/about.html") + header("about") + body + FOOTER


def page_education():
    title = "Hearing Health Education | Carolina Audiology Associates"
    desc = "Learn the signs of hearing loss, the link between hearing and brain health, tinnitus basics, and how hearing aids actually work — from Dr. Palmer in Rocky Mount, NC."
    extra = [{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type":"Question","name":"Is there a link between hearing loss and dementia?","acceptedAnswer":{"@type":"Answer","text":"Yes. Research from Johns Hopkins and the Lancet Commission identifies untreated hearing loss as one of the largest modifiable risk factors for cognitive decline in older adults. Treating hearing loss early supports brain health, social connection, and quality of life."}},
            {"@type":"Question","name":"How do I know if I have hearing loss?","acceptedAnswer":{"@type":"Answer","text":"Often, the people around you notice it before you do. Common early signs are turning the TV up louder than others, struggling to follow conversation in restaurants, asking for repeats, and feeling exhausted after social events. A baseline hearing test removes the guesswork."}},
            {"@type":"Question","name":"Will hearing aids make my ears lazy?","acceptedAnswer":{"@type":"Answer","text":"No. Modern hearing aids do not weaken your ears. In fact, going untreated puts more strain on your brain, because it has to work harder to fill in the missing sounds. Properly fit hearing aids help your brain stay sharp."}},
        ]
    }]
    body = """
<section class="page-hero">
  <div class="container">
    <span class="section-eyebrow" style="color:#ffd9c5">Hearing health</span>
    <h1>Everything we wish every patient knew.</h1>
    <p>Plain-English guides to hearing loss, tinnitus, hearing aids, and the connection between hearing and overall health.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-header">
      <span class="section-eyebrow">Signs of hearing loss</span>
      <h2>The signs almost everyone misses at first.</h2>
      <p>Hearing loss is gradual. Most people do not wake up one morning with it — they slowly lose a few sounds at a time, and the brain adapts so well that the change is hard to see from the inside.</p>
    </div>
    <div class="service-grid">
      <div class="service-card">
        <h3>You turn the TV up</h3>
        <p>If others ask you to turn the TV down, or you need captions, your high-frequency hearing is probably starting to drop.</p>
      </div>
      <div class="service-card">
        <h3>Restaurants got harder</h3>
        <p>Noisy rooms are the first place hearing loss shows up. If you find yourself dreading busy restaurants, it is not the restaurant — it is your hearing.</p>
      </div>
      <div class="service-card">
        <h3>You ask for repeats</h3>
        <p>Saying "what?" or "huh?" more often, especially with women's or children's voices, is a classic early sign.</p>
      </div>
      <div class="service-card">
        <h3>You feel exhausted</h3>
        <p>Straining to listen all day uses real mental energy. People with untreated hearing loss are tired in ways they cannot explain.</p>
      </div>
      <div class="service-card">
        <h3>Ringing in the ears</h3>
        <p>Tinnitus and hearing loss are deeply linked. Ringing, buzzing, or hissing is often the first symptom you notice.</p>
      </div>
      <div class="service-card">
        <h3>People are mumbling</h3>
        <p>If it sounds like everyone around you has started mumbling, the problem is rarely the world. It is usually high-frequency hearing.</p>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <div class="split">
      <div>
        <span class="section-eyebrow">Hearing &amp; the brain</span>
        <h2>The hearing-cognition connection.</h2>
        <p>Research from Johns Hopkins and the 2024 Lancet Commission on dementia prevention found that untreated hearing loss is one of the largest modifiable risk factors for cognitive decline in older adults.</p>
        <p>The reason is straightforward. When sound stops reaching the brain clearly, the brain works harder to fill in the gaps. Over time, that effort takes a toll. The good news: treating hearing loss with properly fit hearing aids is associated with reduced cognitive decline and lower dementia risk.</p>
        <p>That is one of the reasons we take hearing care seriously — even mild hearing loss is worth understanding early.</p>
      </div>
      <div>
        <div style="background:#fff;padding:36px;border-radius:20px;box-shadow:var(--shadow-md);">
          <h3 style="margin-top:0;">What the research says</h3>
          <ul style="list-style:none;padding:0;">
            <li style="padding:8px 0;">✓ Untreated hearing loss is a leading modifiable risk factor for dementia</li>
            <li style="padding:8px 0;">✓ Mild hearing loss roughly doubles dementia risk</li>
            <li style="padding:8px 0;">✓ Moderate hearing loss roughly triples it</li>
            <li style="padding:8px 0;">✓ Hearing aid use is associated with slower cognitive decline</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-header">
      <span class="section-eyebrow">How hearing aids work</span>
      <h2>A modern hearing aid is not your grandfather's.</h2>
      <p>Today's hearing aids are tiny, on-board computers. They sit behind or inside the ear, listen to the world thousands of times a second, and selectively amplify the speech sounds you are missing while keeping background noise from overwhelming you.</p>
    </div>
    <div class="service-grid">
      <div class="service-card">
        <h3>1. We measure</h3>
        <p>Your hearing aids are programmed to your unique hearing prescription using real-ear measurement, the gold standard in audiology.</p>
      </div>
      <div class="service-card">
        <h3>2. They listen</h3>
        <p>Microphones pick up speech and ambient sound, then the on-board chip decides what to amplify, what to soften, and what to filter out.</p>
      </div>
      <div class="service-card">
        <h3>3. They adapt</h3>
        <p>Modern devices change settings automatically as you move from quiet to noisy environments, so you do not have to fiddle with them.</p>
      </div>
      <div class="service-card">
        <h3>4. They connect</h3>
        <p>Most devices stream directly from your phone, TV, or car — turning your hearing aids into the highest-quality earbuds you have ever owned.</p>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <div class="section-header center">
      <span class="section-eyebrow">Common myths</span>
      <h2>Quick answers to what we hear most often.</h2>
    </div>
    <div class="faq">
      <details><summary>Will hearing aids make my ears "lazy"?</summary>
        <div class="content"><p>No. Modern hearing aids do not weaken your ears. The opposite is true — leaving hearing loss untreated puts more strain on your brain, not less.</p></div>
      </details>
      <details><summary>Aren't hearing aids huge and obvious?</summary>
        <div class="content"><p>Most modern hearing aids are small enough that people will not notice them unless you point them out. Some sit invisibly inside the ear canal.</p></div>
      </details>
      <details><summary>If I can still hear, do I really need treatment?</summary>
        <div class="content"><p>Hearing loss is rarely silence. It is usually missing certain frequencies — often the consonants in speech — which is why everything sounds "mumbled." Treating it early is easier than catching up later.</p></div>
      </details>
      <details><summary>Can I just buy hearing aids online?</summary>
        <div class="content"><p>You can — but without a real hearing test and professional programming, you are guessing. A properly fit hearing aid is dialed in to your specific hearing prescription, not a guess.</p></div>
      </details>
    </div>
  </div>
</section>

<section class="cta-strip">
  <div class="container">
    <div>
      <h2>Ready to find out where your hearing stands?</h2>
      <p>Book a baseline hearing evaluation with Dr. Palmer.</p>
    </div>
    <a href="/carolina-audiology-proof/contact.html" class="btn btn-primary">Book Appointment</a>
  </div>
</section>
"""
    return head(title, desc, "/education.html", extra) + header("education") + body + FOOTER


def page_contact():
    title = "Book an Appointment | Carolina Audiology Associates, Rocky Mount NC"
    desc = "Schedule a hearing evaluation with Dr. Melissa Palmer at Carolina Audiology Associates in Rocky Mount, NC. Call 252-790-6649 or request an appointment online."
    body = """
<section class="page-hero">
  <div class="container">
    <span class="section-eyebrow" style="color:#ffd9c5">Contact us</span>
    <h1>Book your appointment.</h1>
    <p>Call us, or send us a few details and we will call you back within one business day.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="split">
      <div>
        <h2>Request an appointment</h2>
        <p>Tell us a little about what you would like help with. A team member will reach out to confirm a time.</p>
        <form class="book" action="mailto:""" + SITE['email'] + """" method="post" enctype="text/plain">
          <label>Full name<input type="text" name="name" required></label>
          <label>Phone<input type="tel" name="phone" required></label>
          <label>Email<input type="email" name="email" required></label>
          <label>Reason for visit
            <select name="reason">
              <option>Hearing evaluation</option>
              <option>Tinnitus consultation</option>
              <option>Hearing aid consultation</option>
              <option>Earwax removal</option>
              <option>Hearing aid repair / programming</option>
              <option>Custom hearing protection</option>
              <option>Something else</option>
            </select>
          </label>
          <label>Anything we should know?<textarea name="notes"></textarea></label>
          <button type="submit" class="btn btn-primary">Send request</button>
        </form>
      </div>
      <div>
        <h2>Reach us directly</h2>
        <div class="contact-info">
          <div class="row">
            <div class="ico">📞</div>
            <div><strong>Phone</strong><a href="tel:""" + SITE['phone_tel'] + """">""" + SITE['phone'] + """</a></div>
          </div>
          <div class="row">
            <div class="ico">✉️</div>
            <div><strong>Email</strong><a href="mailto:""" + SITE['email'] + """">""" + SITE['email'] + """</a></div>
          </div>
          <div class="row">
            <div class="ico">📍</div>
            <div><strong>Office</strong>""" + SITE['address'] + """<br>""" + SITE['city'] + """, """ + SITE['state'] + """ """ + SITE['zip'] + """</div>
          </div>
        </div>
        <div class="hours-block" style="margin-top:24px;">
          <h3 style="margin-top:0;">Office hours</h3>
          <div class="hours-row"><span class="day">Monday</span><span class="time">9:00 AM – 5:00 PM</span></div>
          <div class="hours-row"><span class="day">Tuesday</span><span class="time">9:00 AM – 5:00 PM</span></div>
          <div class="hours-row"><span class="day">Wednesday</span><span class="time">9:00 AM – 5:00 PM</span></div>
          <div class="hours-row"><span class="day">Thursday</span><span class="time">9:00 AM – 5:00 PM</span></div>
          <div class="hours-row closed"><span class="day">Friday</span><span class="time">Closed</span></div>
          <div class="hours-row closed"><span class="day">Saturday</span><span class="time">Closed</span></div>
          <div class="hours-row closed"><span class="day">Sunday</span><span class="time">Closed</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <div class="section-header center">
      <span class="section-eyebrow">Insurance accepted</span>
      <h2>We work with most major plans.</h2>
      <p>Medicare · Blue Cross Blue Shield · UnitedHealthcare · Humana · Aetna. We verify your benefits before your visit.</p>
    </div>
  </div>
</section>
"""
    return head(title, desc, "/contact.html") + header("contact") + body + FOOTER


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

PAGES = {
    "index.html": page_home,
    "services.html": page_services,
    "about.html": page_about,
    "education.html": page_education,
    "contact.html": page_contact,
}

ROBOTS = f"""User-agent: *
Allow: /

Sitemap: {SITE['url']}/sitemap.xml
"""

def sitemap():
    urls = ["/", "/services.html", "/about.html", "/education.html", "/contact.html"]
    items = "\n".join(f"  <url><loc>{SITE['url']}{u}</loc><changefreq>monthly</changefreq><priority>{'1.0' if u=='/' else '0.8'}</priority></url>" for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{items}\n</urlset>\n'

def main():
    for fname, fn in PAGES.items():
        (OUT / fname).write_text(fn())
        print(f"  wrote {fname} ({(OUT/fname).stat().st_size:,} bytes)")
    (OUT / "robots.txt").write_text(ROBOTS)
    (OUT / "sitemap.xml").write_text(sitemap())
    (OUT / ".nojekyll").write_text("")
    print("  wrote robots.txt, sitemap.xml, .nojekyll")

if __name__ == "__main__":
    main()
