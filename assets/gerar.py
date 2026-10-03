"""Gera os SVGs do README (claro e escuro) a partir de uma fonte só.

Uso: python3 assets/gerar.py
Edite PAPEIS e SISTEMAS abaixo e rode de novo. Fontes do sistema (sem webfont:
o GitHub serve o SVG como <img>, que não carrega fontes externas).
"""

from pathlib import Path
from xml.sax.saxutils import escape

PAPEIS = [
    "Founder &amp; Brand Designer",
    "Full-stack · Next.js + TypeScript",
    "Mobile · React Native",
    "SaaS B2B em produção",
]

# (nome, domínio) — o que aparece no "terminal" do banner.
SISTEMAS = [
    ("PitSpace", "pitspace.pazconcept.com.br"),
    ("DietSpace", "dietspace.com.br"),
    ("ElaraSpace", "elaraspace.pazconcept.com.br"),
    ("PerformX", "performx.pazconcept.com.br"),
    ("PazConcept", "pazconcept.com.br"),
]

TEMAS = {
    "dark": dict(
        fundo="#0d1117", grade="#ffffff", grade_op="0.035", brilho1="#7c3aed", brilho2="#2563eb",
        brilho_op="0.30", texto="#f0f6fc", texto2="#9198a1", mudo="#6e7681",
        card="#161b22", borda="#30363d", ok="#3fb950", destaque="#a78bfa",
    ),
    "light": dict(
        fundo="#ffffff", grade="#0d1117", grade_op="0.045", brilho1="#7c3aed", brilho2="#2563eb",
        brilho_op="0.14", texto="#1f2328", texto2="#59636e", mudo="#818b98",
        card="#f6f8fa", borda="#d1d9e0", ok="#1a7f37", destaque="#6d28d9",
    ),
}

W, H = 1200, 320
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace"


def banner(t: dict) -> str:
    n = len(PAPEIS)
    ciclo = n * 3  # 3s por papel
    papeis = []
    for i, p in enumerate(PAPEIS):
        papeis.append(
            f'<text class="papel{" primeiro" if i == 0 else ""}" style="animation-delay:{i * 3}s" x="64" y="214">{p}</text>'
        )

    linhas = []
    y0 = 128
    for i, (nome, dom) in enumerate(SISTEMAS):
        y = y0 + i * 30
        linhas.append(f"""
    <g class="linha" style="animation-delay:{0.4 + i * 0.25:.2f}s">
      <circle class="pulso" style="animation-delay:{i * 0.4:.1f}s" cx="{742}" cy="{y - 5}" r="4" fill="{t['ok']}"/>
      <text x="758" y="{y}" class="mono" fill="{t['texto']}">{escape(nome)}</text>
      <text x="868" y="{y}" class="mono" fill="{t['mudo']}">{escape(dom)}</text>
    </g>""")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Daniel Paz — Founder da PazConcept, designer e desenvolvedor full-stack">
  <title>Daniel Paz — Founder da PazConcept, designer e desenvolvedor full-stack</title>
  <defs>
    <pattern id="grade" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="{t['grade']}" stroke-opacity="{t['grade_op']}"/>
    </pattern>
    <radialGradient id="b1" cx="0.12" cy="0.1" r="0.6">
      <stop offset="0" stop-color="{t['brilho1']}" stop-opacity="{t['brilho_op']}"/>
      <stop offset="1" stop-color="{t['brilho1']}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="b2" cx="0.85" cy="1" r="0.55">
      <stop offset="0" stop-color="{t['brilho2']}" stop-opacity="{t['brilho_op']}"/>
      <stop offset="1" stop-color="{t['brilho2']}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="nome" x1="0" x2="1">
      <stop offset="0" stop-color="{t['texto']}"/>
      <stop offset="1" stop-color="{t['destaque']}"/>
    </linearGradient>
    <clipPath id="borda"><rect width="{W}" height="{H}" rx="16"/></clipPath>
  </defs>
  <style>
    .sans {{ font-family: {SANS}; }}
    .mono {{ font-family: {MONO}; font-size: 14px; }}
    .papel {{ font-family: {SANS}; font-size: 22px; font-weight: 500; fill: {t['texto2']}; opacity: 0; }}
    .papel.primeiro {{ opacity: 1; }}
    @media (prefers-reduced-motion: no-preference) {{
      .papel, .papel.primeiro {{ animation: papel {ciclo}s infinite backwards; }}
    }}
    @keyframes papel {{
      0% {{ opacity: 0; transform: translateY(6px); }}
      {100 / n * 0.12:.2f}% {{ opacity: 1; transform: translateY(0); }}
      {100 / n * 0.88:.2f}% {{ opacity: 1; transform: translateY(0); }}
      {100 / n:.2f}%, 100% {{ opacity: 0; transform: translateY(-6px); }}
    }}
    .linha {{ animation: entra 0.5s ease-out backwards; }}
    @keyframes entra {{ from {{ opacity: 0; transform: translateX(8px); }} to {{ opacity: 1; transform: none; }} }}
    .pulso {{ animation: pulso 2.4s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
    @keyframes pulso {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.35; }} }}
    .cursor {{ animation: pisca 1.1s steps(1) infinite; }}
    @keyframes pisca {{ 50% {{ opacity: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .linha, .pulso, .cursor {{ animation: none; }}
    }}
  </style>

  <g clip-path="url(#borda)">
    <rect width="{W}" height="{H}" fill="{t['fundo']}"/>
    <rect width="{W}" height="{H}" fill="url(#grade)"/>
    <rect width="{W}" height="{H}" fill="url(#b1)"/>
    <rect width="{W}" height="{H}" fill="url(#b2)"/>
  </g>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="15.5" fill="none" stroke="{t['borda']}"/>

  <text x="64" y="92" class="mono" fill="{t['destaque']}" letter-spacing="2">PAZCONCEPT · DESIGN + CÓDIGO</text>
  <text x="62" y="160" class="sans" font-size="64" font-weight="700" letter-spacing="-1.5" fill="url(#nome)">Daniel Paz</text>
  {''.join(papeis)}
  <text x="64" y="262" class="sans" font-size="15" fill="{t['mudo']}">Do branding ao deploy: identidade visual, produto e código no mesmo lugar.</text>

  <g>
    <rect x="712" y="56" width="424" height="{56 + len(SISTEMAS) * 30 + 22}" rx="12" fill="{t['card']}" stroke="{t['borda']}"/>
    <circle cx="736" cy="80" r="5" fill="#ff5f57"/><circle cx="752" cy="80" r="5" fill="#febc2e"/><circle cx="768" cy="80" r="5" fill="#28c840"/>
    <text x="1112" y="85" class="mono" font-size="12" fill="{t['mudo']}" text-anchor="end">~/producao</text>
    <line x1="712" x2="1136" y1="98" y2="98" stroke="{t['borda']}"/>
    {''.join(linhas)}
    <text x="736" y="{y0 + len(SISTEMAS) * 30 + 4}" class="mono" fill="{t['mudo']}">$ <tspan class="cursor" fill="{t['texto']}">▍</tspan></text>
  </g>
</svg>
"""


# ─── Card de stack ──────────────────────────────────────────────────────────
# Só o que aparece de verdade nos repositórios (levantamento de 03/10/2026).
STACK = [
    ("Web", ["TypeScript", "React 19", "Next.js 16", "Vite", "Tailwind CSS 4", "shadcn/ui · Radix", "TanStack Query", "Zustand", "Motion", "PWA · Web Push"]),
    ("Mobile", ["React Native CLI", "React Navigation", "Reanimated", "Android · iOS", "op-sqlite", "Lottie"]),
    ("Backend & dados", ["PostgreSQL", "Prisma 7", "Supabase", "RLS · Realtime", "Edge Functions", "Neon", "Auth.js", "Zod", "Node.js", "Express"]),
    ("Integrações", ["Pix · Mercado Pago", "NFC-e", "WhatsApp", "Telegram bots", "Resend", "MCP"]),
    ("Qualidade", ["Vitest", "Playwright", "pgTAP", "Jest", "Maestro", "Testing Library", "ESLint", "Prettier"]),
    ("Infra", ["Vercel", "GitHub Actions", "Docker", "Sentry", "Vercel Cron · Blob"]),
    ("Design", ["Identidade visual", "Branding", "Figma", "Illustrator", "Photoshop"]),
]


def largura_texto(txt: str, px: float = 13) -> float:
    # Estimativa para a fonte do sistema: estreitas/largas ajustadas, com folga.
    estreitas = sum(c in "il.,:;·|' " for c in txt)
    largas = sum(c in "MWmw@" for c in txt)
    return (len(txt) - estreitas - largas) * px * 0.58 + estreitas * px * 0.32 + largas * px * 0.85


SW = 900  # mais estreito que o banner: no GitHub o card é reduzido menos e o texto fica legível


def stack(t: dict) -> str:
    x0, rot_w, pad_x, gap, chip_h, linha_h = 32, 138, 11, 7, 28, 36
    max_x = SW - 32
    corpo = []
    y = 74
    for cat, itens in STACK:
        corpo.append(f'<text x="{x0}" y="{y + 18}" class="cat">{escape(cat)}</text>')
        x = x0 + rot_w
        linhas = 1
        for item in itens:
            w = largura_texto(item) + pad_x * 2
            if x + w > max_x:
                x = x0 + rot_w
                y += linha_h
                linhas += 1
            corpo.append(
                f'<g><rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{chip_h}" rx="8" fill="{t["card"]}" stroke="{t["borda"]}"/>'
                f'<text x="{x + w / 2:.1f}" y="{y + 18.5}" class="chip" text-anchor="middle">{escape(item)}</text></g>'
            )
            x += w + gap
        y += linha_h + 14
    h = y + 10
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{SW}" height="{h}" viewBox="0 0 {SW} {h}" role="img" aria-label="Tecnologias usadas nos projetos">
  <title>Tecnologias usadas nos projetos</title>
  <style>
    .cat {{ font-family: {SANS}; font-size: 14px; font-weight: 600; fill: {t['texto2']}; }}
    .chip {{ font-family: {SANS}; font-size: 13px; fill: {t['texto']}; }}
    .titulo {{ font-family: {MONO}; font-size: 13px; letter-spacing: 2px; fill: {t['destaque']}; }}
  </style>
  <rect x="0.5" y="0.5" width="{SW - 1}" height="{h - 1}" rx="15.5" fill="{t['fundo']}" stroke="{t['borda']}"/>
  <text x="{x0}" y="44" class="titulo">STACK · O QUE ESTÁ RODANDO NOS MEUS REPOSITÓRIOS</text>
  {''.join(corpo)}
</svg>
"""


def main():
    pasta = Path(__file__).parent
    for nome, t in TEMAS.items():
        (pasta / f"banner-{nome}.svg").write_text(banner(t), encoding="utf-8")
        (pasta / f"stack-{nome}.svg").write_text(stack(t), encoding="utf-8")
        print("ok", f"banner-{nome}.svg", f"stack-{nome}.svg")


if __name__ == "__main__":
    main()
