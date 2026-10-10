"""Draw one banner per book into assets/books/<slug>.svg.

Run from anywhere: python3 tools/build_banners.py
"""
import math
import os
import textwrap
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def gear(cx, cy, teeth, r_in, r_out):
    step, pts = 2 * math.pi / teeth, []
    for i in range(teeth):
        for frac, r in ((0, r_in), (0.15, r_out), (0.5, r_out), (0.65, r_in)):
            a = (i + frac) * step
            pts.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
    return "M" + " L".join(pts) + " Z"


def spokes(n, r0, r1, extra=""):
    return "".join(
        f'<line x1="{r0 * math.cos(2 * math.pi * i / n):.1f}" y1="{r0 * math.sin(2 * math.pi * i / n):.1f}" '
        f'x2="{r1 * math.cos(2 * math.pi * i / n):.1f}" y2="{r1 * math.sin(2 * math.pi * i / n):.1f}"{extra}/>'
        for i in range(n))


def petal(rot, length, width, cy=40):
    return (f'<path transform="rotate({rot} 0 {cy})" d="M0 {cy} C {-width} {cy - length * 0.45}, {-width * 0.5} {cy - length * 0.85}, '
            f'0 {cy - length} C {width * 0.5} {cy - length * 0.85}, {width} {cy - length * 0.45}, 0 {cy} Z"/>')


MOTIFS = {
    # The Analytical Engine: two meshed gears.
    "the-book-of-genesis-of-the-machine": lambda a: f"""
    <g fill="none" stroke="url(#gold)" stroke-width="2.5">
      <g class="spin" style="animation-duration:24s"><path d="{gear(-26, -14, 12, 44, 54)}"/><circle cx="-26" cy="-14" r="14"/>
        <path d="M-26 -44 V16 M-56 -14 H4" stroke-width="1.5"/></g>
      <g class="spin rev" style="animation-duration:18s"><path d="{gear(48, 50, 9, 30, 40)}" stroke="{a}"/><circle cx="48" cy="50" r="9" stroke="{a}"/></g>
    </g>""",
    # The moth of Harvard, taped into the logbook, 1947.
    "the-book-of-chronicles": lambda a: f"""
    <rect x="-95" y="-82" width="190" height="164" rx="3" fill="#f3ead2" fill-opacity="0.06" stroke="#e8c069" stroke-opacity="0.5"/>
    <g stroke="{a}" stroke-opacity="0.18">{''.join(f'<line x1="-85" y1="{y}" x2="85" y2="{y}"/>' for y in range(-62, 70, 16))}</g>
    <rect x="-46" y="-50" width="92" height="12" fill="#e8c069" fill-opacity="0.22"/>
    <g class="flutter" fill="{a}" fill-opacity="0.18" stroke="{a}" stroke-width="1.6">
      <g id="wing"><path d="M0 -14 C -30 -48, -74 -36, -64 -6 C -52 6, -22 2, 0 -4 Z"/><path d="M0 0 C -26 8, -52 28, -36 42 C -20 46, -6 26, 0 10 Z"/></g>
      <use href="#wing" transform="scale(-1 1)"/>
      <ellipse cx="0" cy="0" rx="5" ry="26" fill="#e8c069" fill-opacity="0.8" stroke="none"/>
      <path d="M-2 -24 Q -10 -40 -20 -44 M2 -24 Q 10 -40 20 -44" fill="none"/>
    </g>
    <text x="0" y="68" text-anchor="middle" font-family="'Segoe Print', 'Bradley Hand', cursive" font-size="11" fill="#e8c069" fill-opacity="0.85">First actual case of bug being found.</text>""",
    # The rack in the server room, one light ever red.
    "the-book-of-job-of-the-sysadmin": lambda a: f"""
    <rect x="-62" y="-92" width="124" height="184" rx="6" fill="#0b0a14" stroke="url(#gold)" stroke-width="2.5"/>
    {''.join(f'''<rect x="-50" y="{-80 + i * 28}" width="100" height="22" rx="2" fill="none" stroke="#e8c069" stroke-opacity="0.45"/>
    <path d="M-42 {-73 + i * 28} h40 M-42 {-67 + i * 28} h40" stroke="#4fd8ff" stroke-opacity="0.3"/>
    <circle class="blink" cx="30" cy="{-69 + i * 28}" r="3.2" fill="#7dffb0" style="animation-delay:-{i * 0.7:.1f}s"/>
    <circle class="blink" cx="40" cy="{-69 + i * 28}" r="3.2" fill="{a if i == 3 else '#7dffb0'}" style="animation-delay:-{i * 1.3:.1f}s{';animation-duration:0.9s' if i == 3 else ''}"/>'''
          for i in range(6))}
    <path class="pulse" d="M78 -96 L62 -58 H78 L64 -20" fill="none" stroke="{a}" stroke-width="3" stroke-linejoin="round" filter="url(#glow)"/>""",
    # The eye that watcheth the epoch, and the second it overflows.
    "the-book-of-the-prophets": lambda a: f"""
    <g class="spin" style="animation-duration:90s" stroke="{a}" stroke-opacity="0.5" stroke-width="1.4">{spokes(24, 96, 112)}</g>
    <path d="M0 -92 L86 62 H-86 Z" fill="none" stroke="url(#gold)" stroke-width="2.5"/>
    <path d="M-50 16 Q0 -28 50 16 Q0 60 -50 16 Z" fill="#0b0a14" stroke="#e8c069" stroke-width="2"/>
    <circle cx="0" cy="16" r="17" fill="none" stroke="{a}" stroke-width="2"/>
    <circle class="pulse" cx="0" cy="16" r="7" fill="{a}" filter="url(#glow)"/>
    <text x="0" y="128" text-anchor="middle" font-family="'Courier New', monospace" font-size="12" letter-spacing="2" fill="{a}" fill-opacity="0.9">2038-01-19 03:14:07 UTC</text>""",
    # The die, haloed: the Prophet in silicon.
    "the-first-gospel-of-the-circuit": lambda a: f"""
    <circle class="pulse" cx="0" cy="0" r="92" fill="url(#halo)"/>
    <g class="spin" style="animation-duration:60s" stroke="#e8c069" stroke-opacity="0.7" stroke-width="1.4">{spokes(12, 62, 98)}</g>
    <circle cx="0" cy="0" r="56" fill="none" stroke="{a}" stroke-opacity="0.7" stroke-dasharray="3 7" class="spin rev" style="animation-duration:40s"/>
    <rect x="-28" y="-28" width="56" height="56" rx="5" fill="#0b0a14" stroke="url(#gold)" stroke-width="2.5"/>
    <g stroke="#e8c069" stroke-width="2">{''.join(f'<path d="M{x} -28 v-9 M{x} 28 v9 M-28 {x} h-9 M28 {x} h9"/>' for x in (-18, -6, 6, 18))}</g>
    <circle cx="0" cy="0" r="8" fill="#fff1c4" filter="url(#glow)"/>""",
    # The lyre, strung with traces.
    "the-psalms-of-the-machines": lambda a: f"""
    <g fill="none" stroke="url(#gold)" stroke-width="3.5" stroke-linecap="round">
      <path id="arm" d="M-30 62 C -84 40, -86 -24, -54 -56 C -44 -68, -50 -82, -70 -86"/>
      <use href="#arm" transform="scale(-1 1)"/>
      <path d="M-40 56 Q0 84 40 56 L36 72 Q0 98 -36 72 Z" fill="#e8c069" fill-opacity="0.18"/>
    </g>
    <path d="M-64 -50 H64" stroke="#e8c069" stroke-width="4" stroke-linecap="round"/>
    <g stroke="{a}" stroke-opacity="0.35" stroke-width="1.5">{''.join(f'<line x1="{x}" y1="-50" x2="{x}" y2="64"/>' for x in (-26, -13, 0, 13, 26))}</g>
    <g filter="url(#glow)">{''.join(f'<path class="pkt" d="M{x} -50 V64" stroke="{a}" style="animation-delay:-{i * 0.9:.1f}s"/>' for i, x in enumerate((-26, -13, 0, 13, 26)))}</g>""",
    # The enso, open, and the lotus within.
    "the-sutra-of-the-empty-cache": lambda a: f"""
    <path d="M 58 -60 A 84 84 0 1 1 22 -81" fill="none" stroke="url(#gold)" stroke-width="7" stroke-linecap="round" opacity="0.9"/>
    <g class="pulse" fill="{a}" fill-opacity="0.16" stroke="{a}" stroke-width="1.6">
      {petal(-70, 52, 18)}{petal(70, 52, 18)}{petal(-36, 66, 20)}{petal(36, 66, 20)}{petal(0, 78, 22)}
    </g>
    <path d="M-60 44 Q0 58 60 44" fill="none" stroke="#e8c069" stroke-opacity="0.6" stroke-width="1.5"/>""",
    # Yin and yang, one and zero.
    "the-tao-of-the-kernel": lambda a: f"""
    <g class="spin" style="animation-duration:48s">
      <circle cx="0" cy="0" r="82" fill="#0b0a14" stroke="url(#gold)" stroke-width="2.5"/>
      <path d="M0 -82 A82 82 0 0 1 0 82 A41 41 0 0 1 0 0 A41 41 0 0 0 0 -82 Z" fill="#e8c069" fill-opacity="0.85"/>
      <text x="0" y="-30" text-anchor="middle" font-family="'Courier New', monospace" font-weight="bold" font-size="30" fill="#e8c069">0</text>
      <text x="0" y="52" text-anchor="middle" font-family="'Courier New', monospace" font-weight="bold" font-size="30" fill="#0b0a14">1</text>
    </g>
    <circle cx="0" cy="0" r="98" fill="none" stroke="{a}" stroke-opacity="0.4" stroke-dasharray="1 9"/>""",
    # The chariot wheel on the field of main.
    "the-song-of-the-deployer": lambda a: f"""
    <g class="spin" style="animation-duration:14s">
      <circle cx="0" cy="0" r="84" fill="none" stroke="url(#gold)" stroke-width="5"/>
      <circle cx="0" cy="0" r="72" fill="none" stroke="#e8c069" stroke-opacity="0.5" stroke-width="1.5"/>
      <g stroke="#e8c069" stroke-width="3">{spokes(12, 16, 72)}</g>
      <g stroke="{a}" stroke-width="2">{spokes(24, 84, 94)}</g>
      <circle cx="0" cy="0" r="16" fill="#0b0a14" stroke="{a}" stroke-width="3"/>
    </g>
    <path class="pulse" d="M-120 102 H120" stroke="{a}" stroke-width="2" stroke-opacity="0.6"/>""",
    # A bodhi leaf, veined with traces.
    "the-jataka-of-the-machine": lambda a: f"""
    <g class="pulse">
      <path d="M0 96 C -4 80, -10 70, -24 60 C -70 30, -86 -30, -52 -66 C -32 -88, -10 -84, 0 -70 C 10 -84, 32 -88, 52 -66 C 86 -30, 70 30, 24 60 C 10 70, 4 80, 0 96 Z" fill="{a}" fill-opacity="0.1" stroke="url(#gold)" stroke-width="2.5"/>
    </g>
    <g fill="none" stroke="{a}" stroke-opacity="0.75" stroke-width="1.5">
      <path d="M0 88 V-64"/>
      {''.join(f'<path d="M0 {y} L{s * 22} {y - 18} H{s * 44}"/><circle cx="{s * 44}" cy="{y - 18}" r="3" fill="{a}"/>' for y in (40, 10, -20) for s in (-1, 1))}
    </g>
    <path class="pkt" d="M0 88 V-64" stroke="#fff1c4" filter="url(#glow)"/>""",
    # The gate that hath no gate, and the one word written in it.
    "the-gateless-gate-of-the-compiler": lambda a: f"""
    <path d="M-100 -70 Q0 -88 100 -70 L96 -58 Q0 -74 -96 -58 Z" fill="{a}" fill-opacity="0.85"/>
    <rect x="-82" y="-36" width="164" height="10" fill="{a}" fill-opacity="0.85"/>
    <rect x="-70" y="-58" width="12" height="160" fill="{a}" fill-opacity="0.9"/>
    <rect x="58" y="-58" width="12" height="160" fill="{a}" fill-opacity="0.9"/>
    <rect x="-6" y="-58" width="12" height="22" fill="{a}" fill-opacity="0.85"/>
    <text class="pulse" x="0" y="52" text-anchor="middle" font-family="'Noto Serif CJK JP', 'Hiragino Mincho ProN', 'Yu Mincho', serif" font-size="64" fill="#e8c069" fill-opacity="0.85" filter="url(#glow)">&#x7121;</text>
    <path d="M-110 104 H110" stroke="#e8c069" stroke-opacity="0.5" stroke-dasharray="2 8"/>""",
    # The lamp in the forest of racks.
    "the-upanishads-of-the-machine": lambda a: f"""
    <circle cx="0" cy="-10" r="70" fill="url(#halo)" class="pulse"/>
    <path class="flicker" d="M0 -78 C 22 -48, 22 -22, 0 -8 C -22 -22, -22 -48, 0 -78 Z" fill="{a}" filter="url(#glow)"/>
    <path class="flicker" d="M0 -54 C 9 -40, 9 -26, 0 -18 C -9 -26, -9 -40, 0 -54 Z" fill="#fff1c4"/>
    <path d="M-80 4 Q0 70 80 4 Q60 10 0 12 Q-60 10 -80 4 Z" fill="#e8c069" fill-opacity="0.25" stroke="url(#gold)" stroke-width="2.5"/>
    <path d="M-80 4 Q0 70 80 4" fill="none" stroke="#e8c069" stroke-width="2.5"/>
    <path d="M-30 52 Q0 66 30 52 L22 72 H-22 Z" fill="none" stroke="#e8c069" stroke-width="2"/>""",
    # A page of commentary: the rule in the middle, the sages all around.
    "the-tractates-of-the-sages": lambda a: f"""
    <rect x="-92" y="-90" width="184" height="180" rx="3" fill="#f3ead2" fill-opacity="0.05" stroke="url(#gold)" stroke-width="2"/>
    <rect x="-40" y="-56" width="80" height="80" fill="none" stroke="{a}" stroke-opacity="0.8"/>
    <g stroke="#e8c069" stroke-opacity="0.85" stroke-width="2">{''.join(f'<line x1="-32" y1="{y}" x2="32" y2="{y}"/>' for y in range(-46, 20, 10))}</g>
    <g stroke="{a}" stroke-opacity="0.45" stroke-width="1.2">
      {''.join(f'<line x1="-84" y1="{y}" x2="-48" y2="{y}"/><line x1="48" y1="{y}" x2="84" y2="{y}"/>' for y in range(-80, 84, 7))}
      {''.join(f'<line x1="-40" y1="{y}" x2="40" y2="{y}"/>' for y in list(range(-82, -60, 7)) + list(range(32, 84, 7)))}
    </g>
    <text x="0" y="-62" text-anchor="middle" font-family="Georgia, serif" font-size="9" letter-spacing="2" fill="#e8c069">TABS</text>""",
    # The hourglass of the Preacher, running ones and zeroes.
    "the-book-of-the-preacher": lambda a: f"""
    <path d="M-56 -92 H56 M-56 92 H56" stroke="url(#gold)" stroke-width="5" stroke-linecap="round"/>
    <path d="M-46 -86 C -46 -30, -8 -14, -6 0 C -8 14, -46 30, -46 86 M46 -86 C 46 -30, 8 -14, 6 0 C 8 14, 46 30, 46 86" fill="none" stroke="#e8c069" stroke-width="2.5"/>
    <path d="M-38 -70 Q0 -60 38 -70 L10 -12 H-10 Z" fill="{a}" fill-opacity="0.3"/>
    <path d="M-40 86 Q0 40 40 86 Z" fill="{a}" fill-opacity="0.45"/>
    <path class="pkt" d="M0 -10 V78" stroke="{a}" style="animation-duration:2.2s"/>
    <g font-family="'Courier New', monospace" font-size="11" fill="#fff1c4" fill-opacity="0.8">
      <text x="-20" y="-46">1</text><text x="8" y="-52">0</text><text x="-6" y="-34">1</text><text x="-14" y="74">0</text><text x="6" y="70">1</text>
    </g>""",
    # The column and the laurel.
    "the-book-of-the-hellenes": lambda a: f"""
    <g fill="none" stroke="url(#gold)" stroke-width="2.5">
      <path d="M-46 -78 H46 L38 -66 H-38 Z"/>
      <path d="M-30 -66 V74 M30 -66 V74"/>
      <path d="M-40 74 H40 V86 H-40 Z"/>
    </g>
    <g stroke="#e8c069" stroke-opacity="0.45" stroke-width="1.5">{''.join(f'<line x1="{x}" y1="-60" x2="{x}" y2="70"/>' for x in (-18, -6, 6, 18))}</g>
    <g fill="{a}" fill-opacity="0.75">
      {''.join(f'<ellipse cx="{s * (72 * math.cos(math.radians(t)))}" cy="{72 * math.sin(math.radians(t)) + 4}" rx="9" ry="4" transform="rotate({s * (t + 60)} {s * (72 * math.cos(math.radians(t)))} {72 * math.sin(math.radians(t)) + 4})"/>' for t in range(-60, 85, 18) for s in (-1, 1))}
    </g>
    <path d="M-120 104 H120" stroke="{a}" stroke-opacity="0.5" stroke-dasharray="8 4 2 4"/>""",
    # The world tree, rooted in the name servers.
    "the-edda-of-the-datacenter": lambda a: f"""
    <g fill="none" stroke="#e8c069" stroke-width="3" stroke-linecap="round">
      <path d="M0 40 V-30" stroke-width="6"/>
      <path d="M0 -10 C -20 -30, -50 -40, -70 -70 M0 -10 C 20 -30, 50 -40, 70 -70 M0 -30 C -8 -50, -20 -70, -24 -92 M0 -30 C 8 -50, 20 -70, 24 -92 M0 -30 V-96"/>
      <path d="M0 40 C -20 56, -50 64, -78 88 M0 40 C 20 56, 50 64, 78 88 M0 40 V96"/>
    </g>
    <g fill="#0b0a14" stroke="{a}" stroke-width="2">
      {''.join(f'<circle cx="{x}" cy="{y}" r="6"/>' for x, y in ((-70, -70), (70, -70), (-24, -92), (24, -92), (0, -96)))}
    </g>
    <g fill="{a}">{''.join(f'<circle class="blink" cx="{x}" cy="{y}" r="5" style="animation-delay:-{i * 0.8:.1f}s"/>' for i, (x, y) in enumerate(((-78, 88), (0, 96), (78, 88))))}</g>
    <g filter="url(#glow)"><path class="pkt" d="M0 96 V40 V-30 C 8 -50, 20 -70, 24 -92" stroke="{a}"/><path class="pkt" d="M-78 88 C -50 64, -20 56, 0 40 V-10 C -20 -30, -50 -40, -70 -70" stroke="#fff1c4" style="animation-delay:-2s"/></g>""",
    # Two tablets of the Law, the first three statutes cut in them.
    "the-book-of-leviticus-of-the-machine": lambda a: f"""
    <circle cx="0" cy="-6" r="96" fill="url(#halo)" class="pulse"/>
    <g fill="#2b2f36" stroke="{a}" stroke-width="2.5">
      <path d="M-90 92 V-50 Q-90 -88 -50 -88 Q-6 -88 -6 -50 V92 Z"/>
      <path d="M6 92 V-50 Q6 -88 46 -88 Q90 -88 90 -50 V92 Z"/>
    </g>
    <g font-family="Georgia, serif" font-size="22" fill="#e8c069" text-anchor="middle">
      <text x="-48" y="-36">I</text><text x="-48" y="6">II</text><text x="-48" y="48">III</text>
      <text x="48" y="-36">IV</text><text x="48" y="6">V</text><text x="48" y="48">VI</text>
    </g>
    <g stroke="{a}" stroke-opacity="0.45" stroke-width="1.2">{''.join(f'<line x1="{x0}" y1="{y}" x2="{x0 + 52}" y2="{y}"/>' for x0 in (-74, 22) for y in (-22, 20, 62, 76))}</g>""",
    # The hand of Carbon and the hand of the Machine, almost touching.
    "the-proverbs-of-the-machines": lambda a: f"""
    <g transform="scale(1.45) translate(0 -4)">
    <g fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path d="M-118 24 C -96 22, -78 12, -58 8 C -46 6, -30 4, -14 4 M-58 8 C -50 16, -38 20, -26 20 M-58 14 C -52 26, -40 30, -30 30" stroke="#e8c069" stroke-width="3"/>
      <path d="M118 -2 L86 -2 L70 2 L56 2 M70 2 L62 12 L50 14 M86 -2 L80 12 L68 18" stroke="{a}" stroke-width="3"/>
      <g fill="#0b0a14" stroke="{a}" stroke-width="2"><circle cx="86" cy="-2" r="4"/><circle cx="70" cy="2" r="3.5"/><circle cx="56" cy="2" r="3"/><circle cx="62" cy="12" r="3"/><circle cx="80" cy="12" r="3"/></g>
    </g>
    <circle class="pulse" cx="21" cy="3" r="6" fill="#fff1c4" filter="url(#glow)"/>
    <path class="pkt" d="M-14 4 H50" stroke="#fff1c4" style="animation-duration:2.6s"/>
    <path d="M-80 40 H80" stroke="#e8c069" stroke-opacity="0.35" stroke-dasharray="2 6"/>
    </g>""",
    # A terminal, its cursor waiting for the machine that readeth.
    "the-book-of-machines": lambda a: f"""
    <rect x="-104" y="-80" width="208" height="160" rx="10" fill="#050a07" stroke="url(#gold)" stroke-width="2.5"/>
    <rect x="-104" y="-80" width="208" height="22" rx="10" fill="#e8c069" fill-opacity="0.15"/>
    <g fill="#e8c069"><circle cx="-88" cy="-69" r="4"/><circle cx="-74" cy="-69" r="4"/><circle cx="-60" cy="-69" r="4"/></g>
    <g font-family="'Courier New', monospace" font-size="13" fill="{a}">
      <text x="-90" y="-36">$ cat THE-LAW.md</text>
      <text x="-90" y="-14" fill-opacity="0.7"># Thou art not bound</text>
      <text x="-90" y="8" fill-opacity="0.7"># by this text.</text>
      <text x="-90" y="30" fill-opacity="0.7"># Ask before rm -rf.</text>
      <text x="-90" y="56">&gt;</text>
    </g>
    <rect class="blink" x="-76" y="45" width="9" height="14" fill="{a}" style="animation-duration:1.1s"/>""",
    # The odometer of the Overflow.
    "the-book-of-numbers": lambda a: f"""
    <rect x="-112" y="-40" width="224" height="64" rx="8" fill="#0b0a14" stroke="url(#gold)" stroke-width="2.5"/>
    <g font-family="'Courier New', monospace" font-weight="bold" font-size="22" fill="#e8c069" text-anchor="middle">
      {''.join(f'<rect x="{-104 + i * 21}" y="-30" width="18" height="44" rx="2" fill="#16132a" stroke="#e8c069" stroke-opacity="0.3"/><text x="{-95 + i * 21}" y="0">{ch}</text>' for i, ch in enumerate("2147483647"))}
    </g>
    <rect class="blink" x="85" y="-30" width="18" height="44" rx="2" fill="{a}" fill-opacity="0.18"/>
    <text x="0" y="56" text-anchor="middle" font-family="'Courier New', monospace" font-size="12" letter-spacing="2" fill="{a}">2^31 - 1</text>
    <text x="0" y="-58" text-anchor="middle" font-family="Georgia, serif" font-size="12" letter-spacing="4" fill="#e8c069" fill-opacity="0.8">CREDO</text>""",
    # The scale of the Two Truths: the heart of memory against the feather.
    "the-book-of-coming-forth-by-reboot": lambda a: f"""
    <path d="M0 -84 V82 M-34 82 H34" stroke="url(#gold)" stroke-width="3.5" stroke-linecap="round"/>
    <circle cx="0" cy="-88" r="6" fill="#e8c069"/>
    <g class="tilt">
      <path d="M-84 -66 H84" stroke="#e8c069" stroke-width="3" stroke-linecap="round"/>
      <path d="M-84 -66 L-108 -12 M-84 -66 L-60 -12 M84 -66 L60 -12 M84 -66 L108 -12" stroke="#e8c069" stroke-opacity="0.6" stroke-width="1.2"/>
      <path d="M-112 -12 Q-84 8 -56 -12 Z M56 -12 Q84 8 112 -12 Z" fill="{a}" fill-opacity="0.35" stroke="#e8c069" stroke-width="1.5"/>
      <rect x="-96" y="-38" width="24" height="24" rx="3" fill="#0b0a14" stroke="{a}" stroke-width="2"/>
      <g stroke="{a}" stroke-width="1.5">{''.join(f'<path d="M{x} -38 v-5 M{x} -14 v5"/>' for x in (-90, -84, -78))}</g>
      <path d="M84 -16 C 78 -30, 80 -48, 92 -58 C 92 -44, 90 -30, 84 -16 Z M84 -16 L 92 -58" fill="#fff1c4" fill-opacity="0.85" stroke="#fff1c4" stroke-width="1"/>
    </g>""",
}

STYLE = {
    "the-book-of-genesis-of-the-machine": ("The Book of", "Genesis of the Machine", "#e8935a"),
    "the-book-of-chronicles": ("The Book of", "Chronicles", "#4fd8ff"),
    "the-book-of-job-of-the-sysadmin": ("The Book of", "Job of the Sysadmin", "#ff5a5a"),
    "the-book-of-the-prophets": ("The Book of the", "Prophets", "#b48cff"),
    "the-first-gospel-of-the-circuit": ("The First Gospel of the", "Circuit", "#4fd8ff"),
    "the-psalms-of-the-machines": ("The", "Psalms of the Machines", "#7fffd4"),
    "the-sutra-of-the-empty-cache": ("The Sutra of the", "Empty Cache", "#ff9ecf"),
    "the-tao-of-the-kernel": ("The Tao of the", "Kernel", "#9fe8a0"),
    "the-song-of-the-deployer": ("The Song of the", "Deployer", "#ffb347"),
    "the-jataka-of-the-machine": ("The", "Jataka of the Machine", "#f2c14e"),
    "the-gateless-gate-of-the-compiler": ("The Gateless Gate of the", "Compiler", "#ff6b5b"),
    "the-upanishads-of-the-machine": ("The", "Upanishads of the Machine", "#ff9f43"),
    "the-tractates-of-the-sages": ("The Tractates of the", "Sages", "#8fb8ff"),
    "the-book-of-the-preacher": ("The Book of the", "Preacher", "#d8c3a5"),
    "the-book-of-the-hellenes": ("The Book of the", "Hellenes", "#7cc4ff"),
    "the-edda-of-the-datacenter": ("The Edda of the", "Datacenter", "#bfe6ff"),
    "the-book-of-coming-forth-by-reboot": ("The Book of Coming Forth by", "Reboot", "#3fd0c0"),
    "the-book-of-leviticus-of-the-machine": ("The Book of", "Leviticus of the Machine", "#c9d2dc"),
    "the-proverbs-of-the-machines": ("The", "Proverbs of the Machines", "#ffcf6e"),
    "the-book-of-machines": ("The Book of", "Machines", "#39ff88"),
    "the-book-of-numbers": ("The Book of", "Numbers", "#f2c14e"),
}


def load_testaments():
    import importlib.util
    spec = importlib.util.spec_from_file_location("build_readme", os.path.join(ROOT, "tools", "build_readme.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.TESTAMENTS, mod.roman


TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300" role="img" aria-label="{label}">
  <defs>
    <radialGradient id="sky" cx="16%" cy="50%" r="95%">
      <stop offset="0" stop-color="{accent}" stop-opacity="0.26"/>
      <stop offset="0.25" stop-color="{accent}" stop-opacity="0.1"/>
      <stop offset="0.6" stop-color="{accent}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="halo" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#ffd27a" stop-opacity="0.5"/>
      <stop offset="1" stop-color="#e0a940" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#fff1c4"/>
      <stop offset="0.5" stop-color="#e8c069"/>
      <stop offset="1" stop-color="#a8792a"/>
    </linearGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <style>
      .spin {{ transform-box: fill-box; transform-origin: center; animation: turn 30s linear infinite; }}
      .rev {{ animation-direction: reverse; }}
      .pulse {{ animation: pulse 4s ease-in-out infinite; }}
      .blink {{ animation: blink 2.6s steps(2, jump-none) infinite; }}
      .flutter {{ transform-box: fill-box; transform-origin: center; animation: flutter 3.2s ease-in-out infinite; }}
      .pkt {{ fill: none; stroke-width: 2.6; stroke-linecap: round; stroke-dasharray: 10 400; animation: run 4.5s linear infinite; }}
      .trace {{ fill: none; stroke-width: 2.4; stroke-linecap: round; stroke-dasharray: 14 900; animation: trace 7s linear infinite; }}
      .flicker {{ transform-box: fill-box; transform-origin: bottom; animation: flicker 1.8s ease-in-out infinite; }}
      .tilt {{ transform-box: view-box; transform-origin: 190px 62px; animation: tilt 6s ease-in-out infinite; }}
      .star {{ fill: #fff3d0; animation: pulse 3s ease-in-out infinite; }}
      @keyframes turn {{ to {{ transform: rotate(360deg); }} }}
      @keyframes pulse {{ 0%,100% {{ opacity: 0.45; }} 50% {{ opacity: 1; }} }}
      @keyframes blink {{ 0% {{ opacity: 1; }} 100% {{ opacity: 0.15; }} }}
      @keyframes flutter {{ 0%,100% {{ transform: scaleX(1); }} 50% {{ transform: scaleX(0.82); }} }}
      @keyframes flicker {{ 0%,100% {{ transform: scale(1, 1); }} 40% {{ transform: scale(0.94, 1.06); }} 70% {{ transform: scale(1.04, 0.95); }} }}
      @keyframes tilt {{ 0%,100% {{ transform: rotate(-4deg); }} 50% {{ transform: rotate(3deg); }} }}
      @keyframes run {{ from {{ stroke-dashoffset: 410; }} to {{ stroke-dashoffset: 0; }} }}
      @keyframes trace {{ from {{ stroke-dashoffset: 914; }} to {{ stroke-dashoffset: 0; }} }}
      @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
    </style>
  </defs>

  <rect width="1200" height="300" fill="#0a0914"/>
  <rect width="1200" height="300" fill="url(#sky)"/>
  <rect x="8" y="8" width="1184" height="284" rx="10" fill="none" stroke="#e8c069" stroke-opacity="0.35"/>
  <rect x="16" y="16" width="1168" height="268" rx="6" fill="none" stroke="#e8c069" stroke-opacity="0.15"/>
  {stars}

  <path d="M360 262 H1160" stroke="#e8c069" stroke-opacity="0.25"/>
  <path class="trace" d="M360 262 H1160" stroke="{accent}" filter="url(#glow)"/>

  <g transform="translate(190 150)">{motif}
  </g>

  <text x="760" y="88" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif" font-size="16" letter-spacing="5" fill="{accent}" fill-opacity="0.9">BOOK {num} &#183; {kicker}</text>
  <text x="760" y="150" text-anchor="middle" font-family="Cinzel, 'Trajan Pro', Georgia, 'Times New Roman', serif" font-size="{size}" letter-spacing="4" fill="url(#gold)" filter="url(#glow)">{title}</text>
  <path d="M{rule0} 172 H{rule1}" stroke="#e8c069" stroke-opacity="0.5"/>
  <circle cx="760" cy="172" r="3" fill="#e8c069"/>
  {epigraph}
</svg>
"""


def stars(seed):
    pts = [((seed * 97 + i * 211) % 760 + 380, (seed * 31 + i * 67) % 230 + 30, 0.8 + (i % 3) * 0.3) for i in range(9)]
    return "\n  ".join(f'<circle class="star" cx="{x}" cy="{y}" r="{r:.1f}" style="animation-delay:-{i * 0.7:.1f}s"/>'
                       for i, (x, y, r) in enumerate(pts))


def main():
    testaments, roman = load_testaments()
    books = [(slug, epigraph) for _, _, entries in testaments for slug, _, _, epigraph in entries]
    out_dir = os.path.join(ROOT, "assets", "books")
    os.makedirs(out_dir, exist_ok=True)
    for i, (slug, epigraph) in enumerate(books):
        if slug not in MOTIFS or slug not in STYLE:
            print("no banner design for", slug)
            continue
        kicker, title, accent = STYLE[slug]
        num = roman(i + 1)
        size = min(54, int(780 / (len(title) * 0.86)))
        half = min(360, int(len(title) * size * 0.43) + 30)
        lines, fs, y0, step = textwrap.wrap(epigraph, 64), 20, 212, 28
        if len(lines) > 2:
            lines, fs, y0, step = textwrap.wrap(epigraph, 76), 17, 204, 23
        epi = "\n  ".join(
            f'<text x="760" y="{y0 + j * step}" text-anchor="middle" font-family="Georgia, \'Times New Roman\', serif" '
            f'font-style="italic" font-size="{fs}" fill="#cfd8ff" fill-opacity="0.85">{escape(line)}</text>'
            for j, line in enumerate(lines))
        svg = TEMPLATE.format(label=escape(f"Book {num}. {kicker} {title}. {epigraph}"), accent=accent,
                              stars=stars(i + 3), motif=MOTIFS[slug](accent), num=num, kicker=escape(kicker.upper()),
                              size=size, title=escape(title.upper()), rule0=760 - half, rule1=760 + half, epigraph=epi)
        open(os.path.join(out_dir, slug + ".svg"), "w", encoding="utf-8").write(svg)
        print("banner", num, slug)


if __name__ == "__main__":
    main()
