"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2025 Alain Bernard.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : demo formula
---------------------

Data module

updates
-------
- creation :   2025/02/22

$ DOC START

Data for formula module
"""

# ====================================================================================================
# LaTeX symbols

SYMBOLS = {
    'Alpha'     : 'A',
    'alpha'     : 'α',
    'Beta'      : 'B',
    'beta'      : 'β',
    'Gamma'     : 'Γ',
    'gamma'     : 'γ',
    'Delta'     : 'Δ',
    'delta'     : 'δ',
    'Epsilon'   : 'E',
    'epsilon'   : 'ϵ',
    'varepsilon': 'ε',
    'Zeta'      : 'Z',
    'zeta'      : 'ζ',
    'Eta'       : 'H',
    'eta'       : 'η',
    'Theta'     : 'Θ',
    'theta'     : 'θ',
    'vartheta'  : 'ϑ',
    'Iota'      : 'I',
    'iota'      : 'ι',
    'Kappa'     : 'K',
    'kappa'     : 'κ',
    'varkappa'  : 'ϰ',
    'Lambda'    : 'Λ',
    'lambda'    : 'λ',
    'Mu'        : 'M',
    'mu'        : 'μ',
    'Nu'        : 'N',
    'nu'        : 'ν',
    'Xi'        : 'Ξ',
    'xi'        : 'ξ',
    'Omicron'   : 'O',
    'omicron'   : 'o',
    'Pi'        : 'Π',
    'pi'        : 'π',
    'varpi'     : 'π',
    'Rho'       : 'P',
    'rho'       : 'ρ',
    'varrho'    : 'ϱ',
    'Sigma'     : 'Σ',
    'sigma'     : 'σ',
    'varsigma'  : 'ς',
    'Tau'       : 'T',
    'tau'       : 'τ',
    'Upsilon'   : 'Υ',
    'upsilon'   : 'υ',
    'Phi'       : 'Φ',
    'phi'       : 'ϕ',
    'varphi'    : 'φ',
    'Chi'       : 'X',
    'chi'       : 'χ',
    'Psi'       : 'Ψ',
    'psi'       : 'ψ',
    'Omega'     : 'Ω',
    'omega'     : 'ω',

    'geq'       : '≥',
    'geqslant'  : '⩾',
    'gg'        : '≫',
    'ggg'       : '⋙',
    'leq'       : '≤',
    'leqslant'  : '⩽',
    'll'        : '≪',
    'lll'       : '⋘',
    'ngeq'      : '≱',
    'ngeqslant' : '⪈',
    'ngtr'      : '≯',
    'nleq'      : '≰',
    'nleqslant' : '⪇',
    'nless'     : '≮',
    'notsubset' : '⊄',
    'notsupset' : '⊅',
    'nprec'     : '⊀',
    'npreceq'   : '⋠',
    'nsubseteq' : '⊈',
    'nsucc'     : '⊁',
    'nsucceq'   : '⋡',
    'nsupseteq' : '⊉',
    'prec'      : '≺',
    'preceq'    : '⪯',
    'sqsubset'  : '⊏',
    'sqsubseteq' : '⊑',
    'sqsupset'  : '⊐',
    'sqsupseteq' : '⊒',
    'subset'    : '⊂',
    'subseteq'  : '⊆',
    'succ'      : '≻',
    'succeq'    : '⪰',
    'supset'    : '⊃',
    'supseteq'  : '⊇',

    'doteq'     : '≐',
    'equiv'     : '≡',
    'approx'    : '≈',
    'cong'      : '≅',
    'simeq'     : '≃',
    'sim'       : '∼',
    'propto'    : '∝',
    'neq'       : '≠',
    'neq'       : '≠',

    'exists'    : '∃',
    'nexists'   : '∄',
    'forall'    : '∀',
    'neg'       : '¬',
    'lor'       : '∨',
    'land'      : '∧',
    'top'       : '⊤',
    'bot'       : '⊥',

    '{'         : '{',
    '|'         : '‖',
    'langle'    : '⟨',
    'rangle'    : '⟩',

    'rightarrow'     : '→',
    'to'             : '→',
    'longrightarrow' : '⟶',
    'mapsto'         : '↦',
    'longmapsto'     : '⟼',
    'leftarrow'      : '←',
    'gets'           : '←',
    'longleftarrow'  : '⟵',

    'implies'        : '⟹',
    'Longrightarrow' : '⟹',
    'Rightarrow'     : '⇒',
    'Longleftarrow'  : '⟸',
    'Leftarrow'      : '⇐',
    'iff'            : '⟺',
    'Leftrightarrow' : '⇔',

    'uparrow'       : '↑',
    'Uparrow'       : '⇑',
    'downarrow'     : '↓',
    'Downarrow'     : '⇓',
    'updownarrow'   : '↕',
    'Updownarrow'   : '⇕',

    'partial'       : '∂',
    'imath'         : 'ı',
    'Re'            : 'ℜ',
    'nabla'         : '∇',
    'eth'           : 'ð',
    'jmath'         : 'ȷ',
    'Im'            : 'ℑ',
    'hbar'          : 'ℏ',
    'ell'           : 'ℓ',
    'wp'            : '℘',
    'infty'         : '∞',
    'Box'           : '◻',
    }

# ====================================================================================================
# Dynamic Sqrt symbol (platform independent)

SQRT_CHAR = [
   [
    ( (0.5302241444587708, -0.13709531724452972), (0.5976977944374084, 0.3078262209892273), (0.41875767707824707, 0.10535694658756256) ),
    ( (0.1958247274160385, 0.5902614593505859), (0.3072912096977234, 0.34780919551849365), (0.15132802724838257, 0.5686520934104919) ),
    ( (0.06233461946249008, 0.525433361530304), (0.10683132708072662, 0.547042727470398), (0.05469376966357231, 0.5406311750411987) ),
    ( (0.03941207379102707, 0.5710267424583435), (0.04705292358994484, 0.5558289289474487), (0.10705604404211044, 0.6068840026855469) ),
    ( (0.2423439770936966, 0.6785984635353088), (0.17470000684261322, 0.6427412033081055), (0.333359956741333, 0.48316439986228943) ),
    ( (0.5153919458389282, 0.09229632467031479), (0.4243759512901306, 0.2877303957939148), (0.5738219618797302, 0.4781776964664459) ),
    ( (0.6906819343566895, 1.2499403953552246), (0.6322519183158875, 0.8640590310096741), (0.7073119878768921, 1.2499403953552246) ),
    ( (0.7405721545219421, 1.2499403953552246), (0.7239421010017395, 1.2499403953552246), (0.7776119709014893, 1.2499403953552246) ),
    ( (0.8516915440559387, 1.2499403953552246), (0.8146517276763916, 1.2499403953552246), (0.8516915440559387, 1.2325166463851929) ),
    ( (0.8516915440559387, 1.197669267654419), (0.8516915440559387, 1.2150930166244507), (0.8120093941688538, 1.197669267654419) ),
    ( (0.7326450943946838, 1.197669267654419), (0.7723272442817688, 1.197669267654419), (0.6651714444160461, 0.7527477145195007) ),
   ],
]


SIGMA_CHAR = [
   [
    ( (0.004803940653800964, 1.0001130104064941), (0.004803940653800964, 0.9912624359130859), (0.2548322081565857, 1.0001130104064941) ),
    ( (0.754888653755188, 1.0001130104064941), (0.5048604011535645, 1.0001130104064941), (0.7615265846252441, 0.9313485622406006) ),
    ( (0.7748024463653564, 0.7938196659088135), (0.7681645154953003, 0.862584114074707), (0.765460193157196, 0.7938196659088135) ),
    ( (0.74677574634552, 0.7938196659088135), (0.7561179995536804, 0.7938196659088135), (0.7433338165283203, 0.8377286791801453) ),
    ( (0.7216991186141968, 0.8945713639259338), (0.7349749803543091, 0.8713126182556152), (0.7084231972694397, 0.9178301692008972) ),
    ( (0.6671206951141357, 0.9451102614402771), (0.6902304887771606, 0.934676468372345), (0.6440109014511108, 0.9555440545082092) ),
    ( (0.557226300239563, 0.9607610106468201), (0.6073794364929199, 0.9607610106468201), (0.40998202562332153, 0.9607610106468201) ),
    ( (0.11549347639083862, 0.9607610106468201), (0.2627377510070801, 0.9607610106468201), (0.23441994190216064, 0.811996579170227) ),
    ( (0.4722728431224823, 0.5144677758216858), (0.3533463776111603, 0.6632322072982788), (0.3435424566268921, 0.3633303642272949) ),
    ( (0.08608169853687286, 0.061055608093738556), (0.21481208503246307, 0.21219301223754883), (0.24190066754817963, 0.061055608093738556) ),
    ( (0.5535385608673096, 0.061055608093738556), (0.3977195918560028, 0.061055608093738556), (0.6223762035369873, 0.061055608093738556) ),
    ( (0.7113734483718872, 0.08753041177988052), (0.67498779296875, 0.06988051533699036), (0.7477591037750244, 0.10518030822277069) ),
    ( (0.7932411432266235, 0.19813624024391174), (0.7750482559204102, 0.1420488804578781), (0.8025833964347839, 0.19637125730514526) ),
    ( (0.82126784324646, 0.1928412914276123), (0.8119255900382996, 0.19460627436637878), (0.8070086240768433, 0.1285608559846878) ),
    ( (0.7784901857376099, 0.0), (0.7927494049072266, 0.0642804354429245), (0.5205947756767273, 0.0) ),
    ( (0.004803940653800964, 0.0), (0.2626993656158447, 0.0), (0.004803940653800964, 0.00885055772960186) ),
    ( (0.004803940653800964, 0.02655167318880558), (0.004803940653800964, 0.01770111545920372), (0.13313701748847961, 0.17799456417560577) ),
    ( (0.3898031711578369, 0.4808802902698517), (0.26147007942199707, 0.32943740487098694), (0.26147007942199707, 0.6451073288917542) ),
    ( (0.004803940653800964, 0.9735613465309143), (0.13313701748847961, 0.8093343377113342), (0.004803940653800964, 0.9824119210243225) ),
   ],
]
