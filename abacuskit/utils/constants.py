'''
Date: 2021-05-12 00:33:51
LastEditors: jiyuyang
LastEditTime: 2021-11-08 19:47:25
Mail: jiyuyang@mail.ustc.edu.cn, 1041176461@qq.com
'''

import numpy as np
from scipy.constants import physical_constants

BOHR_TO_A = physical_constants["atomic unit of length"][0] / \
    physical_constants["Angstrom star"][0]
Hartree_TO_eV = physical_constants["Hartree energy in eV"][0]
Rydberg_TO_eV = physical_constants["Rydberg constant times hc in eV"]


angular_momentum_label = ['s', 'p', 'd', 'f', 'g']


def get_angular_momentum_label(l_index: int) -> str:
    """Atomic orbital angular momentum label from l_index

    :params l_index: 0 or 1 or 2 or 3 or 4
    """

    return angular_momentum_label[l_index]


angular_momentum_name = [
    ['$s$'],
    ['$p_x$', '$p_y$', '$p_z$'],
    ['$d_{3z^2-r^2}$', '$d_{xy}$', '$d_{xz}$', '$d_{x^2-y^2}$', '$d_{yz}$'],
    ['$f_{5z^2-3r^2}$', '$f_{5xz^2-xr^2}$', '$f_{5yz^2-yr^2}$',
        '$f_{zx^2-zy^2}$', '$f_{xyz}$', '$f_{x^3-3*xy^2}$', '$f_{3yx^2-y^3}$'],
    ['$g_1$', '$g_2$', '$g_3$', '$g_4$', '$g_5$', '$g_6$', '$g_7$', '$g_8$', '$g_9$']
]


def get_angular_momentum_name(l_index: int, m_index: int) -> str:
    """Atomic orbital angular momentum name from l_index and m_index

    :params l_index: 0 or 1 or 2 or 3 or 4
    :params m_index: 0 ... 2*l_index
    """

    return angular_momentum_name[l_index][m_index]


def get_angular_momentum_index(label: str) -> int:
    """Atomic orbital angular momentum index from label

    :params label: 's' or 'p' or 'd' or 'f'
    """

    if label == 's':
        return 0
    elif label == 'p':
        return 1
    elif label == 'd':
        return 2
    elif label == 'f':
        return 3
    elif label == 'g':
        return 4

LatticeType = {
    'P' : 'primitive',
    'I' : 'body centering',   # h+k+l=2n
    'F' : 'face centering',   # h,k,l all odd or even
    'A' : 'single face centering',  # k+l=2n
    'B' : 'single face centering',  # h+l=2n
    'C' : 'single face centering',  # h+k=2n
    'R' : 'rhombohedral centering'  # -h+k+l=3n (obverse); h-k+l=3n (reverse)
}

# Convert Hermann-Mauguin symbol to Hall symbol
HM2Hall = {
    #   1
    'P1': 'P 1',
    #   2
    'P-1': '-P 1',
    #   3
    'P2': 'P 2y',
    'P2:b': 'P 2y',
    'P2b': 'P 2y',
    'P121': 'P 2y',
    'P2:c': 'P 2',
    'P2c': 'P 2',
    'P112': 'P 2',
    'P2:a': 'P 2x',
    'P2a': 'P 2x',
    'P211': 'P 2x',
    #   4
    'P21': 'P 2yb',
    'P21:b': 'P 2yb',
    'P21b': 'P 2yb',
    'P1211': 'P 2yb',
    'P21:c': 'P 2c',
    'P21c': 'P 2c',
    'P1121': 'P 2c',
    'P21:a': 'P 2xa',
    'P21a': 'P 2xa',
    'P2111': 'P 2xa',
    #   5
    'C2': 'C 2y',
    'C2:b1': 'C 2y',
    'C2b1': 'C 2y',
    'C121': 'C 2y',
    'C2:b2': 'A 2y',
    'C2b2': 'A 2y',
    'A121': 'A 2y',
    'A2': 'A 2y',
    'C2:b3': 'I 2y',
    'C2b3': 'I 2y',
    'I121': 'I 2y',
    'I2': 'I 2y',
    'C2:c1': 'A 2',
    'C2c1': 'A 2',
    'A112': 'A 2',
    'C2:c2': 'B 2',
    'C2c2': 'B 2',
    'B112': 'B 2',
    'B2': 'B 2',
    'C2:c3': 'I 2',
    'C2c3': 'I 2',
    'I112': 'I 2',
    'C2:a1': 'B 2x',
    'C2a1': 'B 2x',
    'B211': 'B 2x',
    'C2:a2': 'C 2x',
    'C2a2': 'C 2x',
    'C211': 'C 2x',
    'C2:a3': 'I 2x',
    'C2a3': 'I 2x',
    'I211': 'I 2x',
    #   6
    'Pm': 'P -2y',
    'Pm:b': 'P -2y',
    'Pmb': 'P -2y',
    'P1m1': 'P -2y',
    'Pm:c': 'P -2',
    'Pmc': 'P -2',
    'P11m': 'P -2',
    'Pm:a': 'P -2x',
    'Pma': 'P -2x',
    'Pm11': 'P -2x',
    #   7
    'Pc': 'P -2yc',
    'Pc:b1': 'P -2yc',
    'Pcb1': 'P -2yc',
    'P1c1': 'P -2yc',
    'Pc:b2': 'P -2yac',
    'Pcb2': 'P -2yac',
    'P1n1': 'P -2yac',
    'Pn': 'P -2yac',
    'Pc:b3': 'P -2ya',
    'Pcb3': 'P -2ya',
    'P1a1': 'P -2ya',
    'Pa': 'P -2ya',
    'Pc:c1': 'P -2a',
    'Pcc1': 'P -2a',
    'P11a': 'P -2a',
    'Pc:c2': 'P -2ab',
    'Pcc2': 'P -2ab',
    'P11n': 'P -2ab',
    'Pc:c3': 'P -2b',
    'Pcc3': 'P -2b',
    'P11b': 'P -2b',
    'Pb': 'P -2b',
    'Pc:a1': 'P -2xb',
    'Pca1': 'P -2xb',
    'Pb11': 'P -2xb',
    'Pc:a2': 'P -2xbc',
    'Pca2': 'P -2xbc',
    'Pn11': 'P -2xbc',
    'Pc:a3': 'P -2xc',
    'Pca3': 'P -2xc',
    'Pc11': 'P -2xc',
    'B1a1': 'B -2yc',
    #   8
    'Cm': 'C -2y',
    'Cm:b1': 'C -2y',
    'Cmb1': 'C -2y',
    'C1m1': 'C -2y',
    'Cm:b2': 'A -2y',
    'Cmb2': 'A -2y',
    'A1m1': 'A -2y',
    'Cm:b3': 'I -2y',
    'Cmb3': 'I -2y',
    'I1m1': 'I -2y',
    'Im': 'I -2y',
    'Cm:c1': 'A -2',
    'Cmc1': 'A -2',
    'A11m': 'A -2',
    'Cm:c2': 'B -2',
    'Cmc2': 'B -2',
    'B11m': 'B -2',
    'Bm': 'B -2',
    'Cm:c3': 'I -2',
    'Cmc3': 'I -2',
    'I11m': 'I -2',
    'Cm:a1': 'B -2x',
    'Cma1': 'B -2x',
    'Bm11': 'B -2x',
    'Cm:a2': 'C -2x',
    'Cma2': 'C -2x',
    'Cm11': 'C -2x',
    'Cm:a3': 'I -2x',
    'Cma3': 'I -2x',
    'Im11': 'I -2x',
    #   9
    'Cc': 'C -2yc',
    'Cc:b1': 'C -2yc',
    'Ccb1': 'C -2yc',
    'C1c1': 'C -2yc',
    'Cc:b2': 'A -2yac',
    'Ccb2': 'A -2yac',
    'A1n1': 'A -2yac',
    'Cc:b3': 'I -2ya',
    'Ccb3': 'I -2ya',
    'I1a1': 'I -2ya',
    'Ia': 'I -2ya',
    'Cc:-b1': 'A -2ya',
    'Cc-b1': 'A -2ya',
    'A1a1': 'A -2ya',
    'Aa': 'A -2ya',
    'Cc:-b2': 'C -2ybc',
    'Cc-b2': 'C -2ybc',
    'C1n1': 'C -2ybc',
    'Cc:-b3': 'I -2yc',
    'Cc-b3': 'I -2yc',
    'I1c1': 'I -2yc',
    'Cc:c1': 'A -2a',
    'Ccc1': 'A -2a',
    'A11a': 'A -2a',
    'Cc:c2': 'B -2bc',
    'B11n': 'B -2bc',
    'Cc:c3': 'I -2b',
    'Ccc3': 'I -2b',
    'I11b': 'I -2b',
    'Ib': 'I -2b',
    'Cc:-c1': 'B -2b',
    'Cc-c1': 'B -2b',
    'B11b': 'B -2b',
    'Bb': 'B -2b',
    'Cc:-c2': 'A -2ac',
    'Cc-c2': 'A -2ac',
    'A11n': 'A -2ac',
    'Cc:-c3': 'I -2a',
    'Cc-c3': 'I -2a',
    'I11a': 'I -2a',
    'Cc:a1': 'B -2xb',
    'Cca1': 'B -2xb',
    'Bb11': 'B -2xb',
    'Cc:a2': 'C -2xbc',
    'Cca2': 'C -2xbc',
    'Cn11': 'C -2xbc',
    'Cc:a3': 'I -2xc',
    'Cca3': 'I -2xc',
    'Ic11': 'I -2xc',
    'Cc:-a1': 'C -2xc',
    'Cc-a1': 'C -2xc',
    'Cc11': 'C -2xc',
    'Cc:-a2': 'B -2xbc',
    'Cc-a2': 'B -2xbc',
    'Bn11': 'B -2xbc',
    'Cc:-a3': 'I -2xb',
    'Cc-a3': 'I -2xb',
    'Ib11': 'I -2xb',
    #  10
    'P2/m': '-P 2y',
    'P2/m:b': '-P 2y',
    'P2/mb': '-P 2y',
    'P12/m1': '-P 2y',
    'P2/m:c': '-P 2',
    'P2/mc': '-P 2',
    'P112/m': '-P 2',
    'P2/m:a': '-P 2x',
    'P2/ma': '-P 2x',
    'P2/m11': '-P 2x',
    #  11
    'P21/m': '-P 2yb',
    'P21/m:b': '-P 2yb',
    'P21/mb': '-P 2yb',
    'P121/m1': '-P 2yb',
    'P21/m:c': '-P 2c',
    'P21/mc': '-P 2c',
    'P1121/m': '-P 2c',
    'P21/m:a': '-P 2xa',
    'P21/ma': '-P 2xa',
    'P21/m11': '-P 2xa',
    #  12
    'C2/m': '-C 2y',
    'C2/m:b1': '-C 2y',
    'C2/mb1': '-C 2y',
    'C12/m1': '-C 2y',
    'C2/m:b2': '-A 2y',
    'C2/mb2': '-A 2y',
    'A12/m1': '-A 2y',
    'A2/m': '-A 2y',
    'C2/m:b3': '-I 2y',
    'C2/mb3': '-I 2y',
    'I12/m1': '-I 2y',
    'I2/m': '-I 2y',
    'C2/m:c1': '-A 2',
    'C2/mc1': '-A 2',
    'A112/m': '-A 2',
    'C2/m:c2': '-B 2',
    'C2/mc2': '-B 2',
    'B112/m': '-B 2',
    'B2/m': '-B 2',
    'C2/m:c3': '-I 2',
    'C2/mc3': '-I 2',
    'I112/m': '-I 2',
    'C2/m:a1': '-B 2x',
    'C2/ma1': '-B 2x',
    'B2/m11': '-B 2x',
    'C2/m:a2': '-C 2x',
    'C2/ma2': '-C 2x',
    'C2/m11': '-C 2x',
    'C2/m:a3': '-I 2x',
    'C2/ma3': '-I 2x',
    'I2/m11': '-I 2x',
    #  13
    'P2/c': '-P 2yc',
    'P2/c:b1': '-P 2yc',
    'P2/cb1': '-P 2yc',
    'P12/c1': '-P 2yc',
    'P2/c:b2': '-P 2yac',
    'P2/cb2': '-P 2yac',
    'P12/n1': '-P 2yac',
    'P2/n': '-P 2yac',
    'P2/c:b3': '-P 2ya',
    'P2/cb3': '-P 2ya',
    'P12/a1': '-P 2ya',
    'P2/a': '-P 2ya',
    'P2/c:c1': '-P 2a',
    'P2/cc1': '-P 2a',
    'P112/a': '-P 2a',
    'P2/c:c2': '-P 2ab',
    'P2/cc2': '-P 2ab',
    'P112/n': '-P 2ab',
    'P2/c:c3': '-P 2b',
    'P2/cc3': '-P 2b',
    'P112/b': '-P 2b',
    'P2/b': '-P 2b',
    'P2/c:a1': '-P 2xb',
    'P2/ca1': '-P 2xb',
    'P2/b11': '-P 2xb',
    'P2/c:a2': '-P 2xbc',
    'P2/ca2': '-P 2xbc',
    'P2/n11': '-P 2xbc',
    'P2/c:a3': '-P 2xc',
    'P2/ca3': '-P 2xc',
    'P2/c11': '-P 2xc',
    #  14
    'P21/c': '-P 2ybc',
    'P21/c:b1': '-P 2ybc',
    'P21/cb1': '-P 2ybc',
    'P121/c1': '-P 2ybc',
    'P21/c:b2': '-P 2yn',
    'P21/cb2': '-P 2yn',
    'P121/n1': '-P 2yn',
    'P21/n': '-P 2yn',
    'P21/c:b3': '-P 2yab',
    'P21/cb3': '-P 2yab',
    'P121/a1': '-P 2yab',
    'P21/a': '-P 2yab',
    'P21/c:c1': '-P 2ac',
    'P21/cc1': '-P 2ac',
    'P1121/a': '-P 2ac',
    'P21/c:c2': '-P 2n',
    'P21/cc2': '-P 2n',
    'P1121/n': '-P 2n',
    'P21/c:c3': '-P 2bc',
    'P21/cc3': '-P 2bc',
    'P1121/b': '-P 2bc',
    'P21/b': '-P 2bc',
    'P21/c:a1': '-P 2xab',
    'P21/ca1': '-P 2xab',
    'P21/b11': '-P 2xab',
    'P21/c:a2': '-P 2xn',
    'P21/ca2': '-P 2xn',
    'P21/n11': '-P 2xn',
    'P21/c:a3': '-P 2xac',
    'P21/ca3': '-P 2xac',
    'P21/c11': '-P 2xac',
    'B121/c1': '-B 2ybc',
    #  15
    'C2/c': '-C 2yc',
    'C2/c:b1': '-C 2yc',
    'C2/cb1': '-C 2yc',
    'C12/c1': '-C 2yc',
    'C2/c:b2': '-A 2yac',
    'C2/cb2': '-A 2yac',
    'A12/n1': '-A 2yac',
    'A2/n': '-A 2yac',
    'C2/c:b3': '-I 2ya',
    'C2/cb3': '-I 2ya',
    'I12/a1': '-I 2ya',
    'I2/a': '-I 2ya',
    'C2/c:-b1': '-A 2ya',
    'C2/c-b1': '-A 2ya',
    'A12/a1': '-A 2ya',
    'A2/a': '-A 2ya',
    'C2/c:-b2': '-C 2ybc',
    'C2/c-b2': '-C 2ybc',
    'C12/n1': '-C 2ybc',
    'C2/c:-b3': '-I 2yc',
    'C2/c-b3': '-I 2yc',
    'I12/c1': '-I 2yc',
    'I2/c': '-I 2yc',
    'C2/c:c1': '-A 2a',
    'C2/cc1': '-A 2a',
    'A112/a': '-A 2a',
    'C2/c:c2': '-B 2bc',
    'C2/cc2': '-B 2bc',
    'B112/n': '-B 2bc',
    'B2/n': '-B 2bc',
    'C2/c:c3': '-I 2b',
    'C2/cc3': '-I 2b',
    'I112/b': '-I 2b',
    'I2/b': '-I 2b',
    'C2/c:-c1': '-B 2b',
    'C2/c-c1': '-B 2b',
    'B112/b': '-B 2b',
    'B2/b': '-B 2b',
    'C2/c:-c2': '-A 2ac',
    'C2/c-c2': '-A 2ac',
    'A112/n': '-A 2ac',
    'C2/c:-c3': '-I 2a',
    'C2/c-c3': '-I 2a',
    'I112/a': '-I 2a',
    'C2/c:a1': '-B 2xb',
    'C2/ca1': '-B 2xb',
    'B2/b11': '-B 2xb',
    'C2/c:a2': '-C 2xbc',
    'C2/ca2': '-C 2xbc',
    'C2/n11': '-C 2xbc',
    'C2/c:a3': '-I 2xc',
    'C2/ca3': '-I 2xc',
    'I2/c11': '-I 2xc',
    'C2/c:-a1': '-C 2xc',
    'C2/c-a1': '-C 2xc',
    'C2/c11': '-C 2xc',
    'C2/c:-a2': '-B 2xbc',
    'C2/c-a2': '-B 2xbc',
    'B2/n11': '-B 2xbc',
    'C2/c:-a3': '-I 2xb',
    'C2/c-a3': '-I 2xb',
    'I2/b11': '-I 2xb',
    #  16
    'P222': 'P 2 2',
    #  17
    'P2221': 'P 2c 2',
    'P2122': 'P 2a 2a',
    'P2212': 'P 2 2b',
    #  18
    'P21212': 'P 2 2ab',
    'P22121': 'P 2bc 2',
    'P21221': 'P 2ac 2ac',
    #  19
    'P212121': 'P 2ac 2ab',
    #  20
    'C2221': 'C 2c 2',
    'C2221S': 'C 2c 2',
    'A2122': 'A 2a 2a',
    'B2212': 'B 2 2b',
    #  21
    'C222': 'C 2 2',
    'A222': 'A 2 2',
    'B222': 'B 2 2',
    #  22
    'F222': 'F 2 2',
    #  23
    'I222': 'I 2 2',
    #  24
    'I212121': 'I 2b 2c',
    #  25
    'Pmm2': 'P 2 -2',
    'P2mm': 'P -2 2',
    'Pm2m': 'P -2 -2',
    #  26
    'Pmc21': 'P 2c -2',
    'Pcm21': 'P 2c -2c',
    'P21ma': 'P -2a 2a',
    'P21am': 'P -2 2a',
    'Pb21m': 'P -2 -2b',
    'Pm21b': 'P -2b -2',
    #  27
    'Pcc2': 'P 2 -2c',
    'P2aa': 'P -2a 2',
    'Pb2b': 'P -2b -2b',
    #  28
    'Pma2': 'P 2 -2a',
    'Pbm2': 'P 2 -2b',
    'P2mb': 'P -2b 2',
    'P2cm': 'P -2c 2',
    'Pc2m': 'P -2c -2c',
    'Pm2a': 'P -2a -2a',
    #  29
    'Pca21': 'P 2c -2ac',
    'Pbc21': 'P 2c -2b',
    'P21ab': 'P -2b 2a',
    'P21ca': 'P -2ac 2a',
    'Pc21b': 'P -2bc -2c',
    'Pb21a': 'P -2a -2ab',
    #  30
    'Pnc2': 'P 2 -2bc',
    'Pcn2': 'P 2 -2ac',
    'P2na': 'P -2ac 2',
    'P2an': 'P -2ab 2',
    'Pb2n': 'P -2ab -2ab',
    'Pn2b': 'P -2bc -2bc',
    #  31
    'Pmn21': 'P 2ac -2',
    'Pnm21': 'P 2bc -2bc',
    'P21mn': 'P -2ab 2ab',
    'P21nm': 'P -2 2ac',
    'Pn21m': 'P -2 -2bc',
    'Pm21n': 'P -2ab -2',
    #  32
    'Pba2': 'P 2 -2ab',
    'P2cb': 'P -2bc 2',
    'Pc2a': 'P -2ac -2ac',
    #  33
    'Pna21': 'P 2c -2n',
    'Pbn21': 'P 2c -2ab',
    'P21nb': 'P -2bc 2a',
    'P21cn': 'P -2n 2a',
    'Pc21n': 'P -2n -2ac',
    'Pn21a': 'P -2ac -2n',
    #  34
    'Pnn2': 'P 2 -2n',
    'P2nn': 'P -2n 2',
    'Pn2n': 'P -2n -2n',
    #  35
    'Cmm2': 'C 2 -2',
    'A2mm': 'A -2 2',
    'Bm2m': 'B -2 -2',
    #  36
    'Cmc21': 'C 2c -2',
    'Ccm21': 'C 2c -2c',
    'A21ma': 'A -2a 2a',
    'A21am': 'A -2 2a',
    'Bb21m': 'B -2 -2b',
    'Bm21b': 'B -2b -2',
    #  37
    'Ccc2': 'C 2 -2c',
    'A2aa': 'A -2a 2',
    'Bb2b': 'B -2b -2b',
    #  38
    'Amm2': 'A 2 -2',
    'Bmm2': 'B 2 -2',
    'B2mm': 'B -2 2',
    'C2mm': 'C -2 2',
    'Cm2m': 'C -2 -2',
    'Am2m': 'A -2 -2',
    #  39
    'Abm2': 'A 2 -2c',
    'Bma2': 'B 2 -2c',
    'B2cm': 'B -2c 2',
    'C2mb': 'C -2b 2',
    'Cm2a': 'C -2b -2b',
    'Ac2m': 'A -2c -2c',
    #  40
    'Ama2': 'A 2 -2a',
    'Bbm2': 'B 2 -2b',
    'B2mb': 'B -2b 2',
    'C2cm': 'C -2c 2',
    'Cc2m': 'C -2c -2c',
    'Am2a': 'A -2a -2a',
    #  41
    'Aba2': 'A 2 -2ac',
    'Bba2': 'B 2 -2bc',
    'B2cb': 'B -2bc 2',
    'C2cb': 'C -2bc 2',
    'Cc2a': 'C -2bc -2bc',
    'Ac2a': 'A -2ac -2ac',
    #  42
    'Fmm2': 'F 2 -2',
    'F2mm': 'F -2 2',
    'Fm2m': 'F -2 -2',
    #  43
    'Fdd2': 'F 2 -2d',
    'F2dd': 'F -2d 2',
    'Fd2d': 'F -2d -2d',
    #  44
    'Imm2': 'I 2 -2',
    'I2mm': 'I -2 2',
    'Im2m': 'I -2 -2',
    #  45
    'Iba2': 'I 2 -2c',
    'I2cb': 'I -2a 2',
    'Ic2a': 'I -2b -2b',
    #  46
    'Ima2': 'I 2 -2a',
    'Ibm2': 'I 2 -2b',
    'I2mb': 'I -2b 2',
    'I2cm': 'I -2c 2',
    'Ic2m': 'I -2c -2c',
    'Im2a': 'I -2a -2a',
    #  47
    'Pmmm': '-P 2 2',
    'P2/m2/m2/m': '-P 2 2',
    #  48
    'Pnnn': 'P 2 2 -1n',
    'Pnnn:1': 'P 2 2 -1n',
    'Pnnn1': 'P 2 2 -1n',
    'PnnnS': 'P 2 2 -1n',
    'Pnnn:2': '-P 2ab 2bc',
    'Pnnn2': '-P 2ab 2bc',
    'PnnnZ': '-P 2ab 2bc',
    #  49
    'Pccm': '-P 2 2c',
    'Pmaa': '-P 2a 2',
    'Pbmb': '-P 2b 2b',
    #  50
    'Pban': 'P 2 2 -1ab',
    'Pban:1': 'P 2 2 -1ab',
    'Pban1': 'P 2 2 -1ab',
    'PbanS': 'P 2 2 -1ab',
    'Pban:2': '-P 2ab 2b',
    'Pban2': '-P 2ab 2b',
    'PbanZ': '-P 2ab 2b',
    'Pncb': 'P 2 2 -1bc',
    'Pncb:1': 'P 2 2 -1bc',
    'Pncb1': 'P 2 2 -1bc',
    'PncbS': 'P 2 2 -1bc',
    'Pncb:2': '-P 2b 2bc',
    'Pncb2': '-P 2b 2bc',
    'PncbZ': '-P 2b 2bc',
    'Pcna': 'P 2 2 -1ac',
    'Pcna:1': 'P 2 2 -1ac',
    'Pcna1': 'P 2 2 -1ac',
    'PcnaS': 'P 2 2 -1ac',
    'Pcna:2': '-P 2a 2c',
    'Pcna2': '-P 2a 2c',
    'PcnaZ': '-P 2a 2c',
    #  51
    'Pmma': '-P 2a 2a',
    'Pmmb': '-P 2b 2',
    'Pbmm': '-P 2 2b',
    'Pcmm': '-P 2c 2c',
    'Pmcm': '-P 2c 2',
    'Pmam': '-P 2 2a',
    #  52
    'Pnna': '-P 2a 2bc',
    'Pnnb': '-P 2b 2n',
    'Pbnn': '-P 2n 2b',
    'Pcnn': '-P 2ab 2c',
    'Pncn': '-P 2ab 2n',
    'Pnan': '-P 2n 2bc',
    #  53
    'Pmna': '-P 2ac 2',
    'Pnmb': '-P 2bc 2bc',
    'Pbmn': '-P 2ab 2ab',
    'Pcnm': '-P 2 2ac',
    'Pncm': '-P 2 2bc',
    'Pman': '-P 2ab 2',
    #  54
    'Pcca': '-P 2a 2ac',
    'Pccb': '-P 2b 2c',
    'Pbaa': '-P 2a 2b',
    'Pcaa': '-P 2ac 2c',
    'Pbcb': '-P 2bc 2b',
    'Pbab': '-P 2b 2ab',
    #  55
    'Pbam': '-P 2 2ab',
    'Pmcb': '-P 2bc 2',
    'Pcma': '-P 2ac 2ac',
    #  56
    'Pccn': '-P 2ab 2ac',
    'Pnaa': '-P 2ac 2bc',
    'Pbnb': '-P 2bc 2ab',
    #  57
    'Pbcm': '-P 2c 2b',
    'Pcam': '-P 2c 2ac',
    'Pmca': '-P 2ac 2a',
    'Pmab': '-P 2b 2a',
    'Pbma': '-P 2a 2ab',
    'Pcmb': '-P 2bc 2c',
    #  58
    'Pnnm': '-P 2 2n',
    'Pmnn': '-P 2n 2',
    'Pnmn': '-P 2n 2n',
    #  59
    'Pmmn': 'P 2 2ab -1ab',
    'Pmmn:1': 'P 2 2ab -1ab',
    'Pmmn1': 'P 2 2ab -1ab',
    'PmmnS': 'P 2 2ab -1ab',
    'Pmmn:2': '-P 2ab 2a',
    'Pmmn2': '-P 2ab 2a',
    'PmmnZ': '-P 2ab 2a',
    'Pnmm': 'P 2bc 2 -1bc',
    'Pnmm:1': 'P 2bc 2 -1bc',
    'Pnmm1': 'P 2bc 2 -1bc',
    'PnmmS': 'P 2bc 2 -1bc',
    'Pnmm:2': '-P 2c 2bc',
    'Pnmm2': '-P 2c 2bc',
    'PnmmZ': '-P 2c 2bc',
    'Pmnm': 'P 2ac 2ac -1ac',
    'Pmnm:1': 'P 2ac 2ac -1ac',
    'Pmnm1': 'P 2ac 2ac -1ac',
    'PmnmS': 'P 2ac 2ac -1ac',
    'Pmnm:2': '-P 2c 2a',
    'Pmnm2': '-P 2c 2a',
    'PmnmZ': '-P 2c 2a',
    #  60
    'Pbcn': '-P 2n 2ab',
    'Pcan': '-P 2n 2c',
    'Pnca': '-P 2a 2n',
    'Pnab': '-P 2bc 2n',
    'Pbna': '-P 2ac 2b',
    'Pcnb': '-P 2b 2ac',
    #  61
    'Pbca': '-P 2ac 2ab',
    'P21/b21/c21/a': '-P 2ac 2ab',
    'Pcab': '-P 2bc 2ac',
    #  62
    'Pnma': '-P 2ac 2n',
    'Pmnb': '-P 2bc 2a',
    'Pbnm': '-P 2c 2ab',
    'Pcmn': '-P 2n 2ac',
    'Pmcn': '-P 2n 2a',
    'Pnam': '-P 2c 2n',
    #  63
    'Cmcm': '-C 2c 2',
    'Ccmm': '-C 2c 2c',
    'Amma': '-A 2a 2a',
    'Amam': '-A 2 2a',
    'Bbmm': '-B 2 2b',
    'Bmmb': '-B 2b 2',
    #  64
    'Cmca': '-C 2bc 2',
    'Cmce': '-C 2bc 2',
    'Ccmb': '-C 2bc 2bc',
    'Abma': '-A 2ac 2ac',
    'Acam': '-A 2 2ac',
    'Bbcm': '-B 2 2bc',
    'Bmab': '-B 2bc 2',
    #  65
    'Cmmm': '-C 2 2',
    'Ammm': '-A 2 2',
    'Bmmm': '-B 2 2',
    'C2/m2/m2/m': '-C 2 2',
    'A2/m2/m2/m': '-A 2 2',
    'B2/m2/m2/m': '-B 2 2',
    #  66
    'Cccm': '-C 2 2c',
    'Amaa': '-A 2a 2',
    'Bbmb': '-B 2b 2b',
    #  67
    'Cmma': '-C 2b 2',
    'Cmmb': '-C 2b 2b',
    'Abmm': '-A 2c 2c',
    'Acmm': '-A 2 2c',
    'Bmcm': '-B 2 2c',
    'Bmam': '-B 2c 2',
    #  68
    'Ccca': 'C 2 2 -1bc',
    'Ccca:1': 'C 2 2 -1bc',
    'Ccca1': 'C 2 2 -1bc',
    'CccaS': 'C 2 2 -1bc',
    'Ccca:2': '-C 2b 2bc',
    'Ccca2': '-C 2b 2bc',
    'CccaZ': '-C 2b 2bc',
    'Cccb': 'C 2 2 -1bc',
    'Cccb:1': 'C 2 2 -1bc',
    'Cccb1': 'C 2 2 -1bc',
    'CccbS': 'C 2 2 -1bc',
    'Cccb:2': '-C 2b 2c',
    'Cccb2': '-C 2b 2c',
    'CccbZ': '-C 2b 2c',
    'Abaa': 'A 2 2 -1ac',
    'Abaa:1': 'A 2 2 -1ac',
    'Abaa1': 'A 2 2 -1ac',
    'AbaaS': 'A 2 2 -1ac',
    'Abaa:2': '-A 2a 2c',
    'Abaa2': '-A 2a 2c',
    'AbaaZ': '-A 2a 2c',
    'Acaa': 'A 2 2 -1ac',
    'Acaa:1': 'A 2 2 -1ac',
    'Acaa1': 'A 2 2 -1ac',
    'AcaaS': 'A 2 2 -1ac',
    'Acaa:2': '-A 2ac 2c',
    'Acaa2': '-A 2ac 2c',
    'AcaaZ': '-A 2ac 2c',
    'Bbcb': 'B 2 2 -1bc',
    'Bbcb:1': 'B 2 2 -1bc',
    'Bbcb1': 'B 2 2 -1bc',
    'BbcbS': 'B 2 2 -1bc',
    'Bbcb:2': '-B 2bc 2b',
    'Bbcb2': '-B 2bc 2b',
    'BbcbZ': '-B 2bc 2b',
    'Bbab': 'B 2 2 -1bc',
    'Bbab:1': 'B 2 2 -1bc',
    'Bbab1': 'B 2 2 -1bc',
    'BbabS': 'B 2 2 -1bc',
    'Bbab:2': '-B 2b 2bc',
    'Bbab2': '-B 2b 2bc',
    'BbabZ': '-B 2b 2bc',
    #  69
    'Fmmm': '-F 2 2',
    'F2/m2/m2/m': '-F 2 2',
    #  70
    'Fddd': 'F 2 2 -1d',
    'Fddd:1': 'F 2 2 -1d',
    'Fddd1': 'F 2 2 -1d',
    'FdddS': 'F 2 2 -1d',
    'Fddd:2': '-F 2uv 2vw',
    'Fddd2': '-F 2uv 2vw',
    'FdddZ': '-F 2uv 2vw',
    #  71
    'Immm': '-I 2 2',
    'I2/m2/m2/m': '-I 2 2',
    #  72
    'Ibam': '-I 2 2c',
    'Imcb': '-I 2a 2',
    'Icma': '-I 2b 2b',
    #  73
    'Ibca': '-I 2b 2c',
    'Icab': '-I 2a 2b',
    #  74
    'Imma': '-I 2b 2',
    'Immb': '-I 2a 2a',
    'Ibmm': '-I 2c 2c',
    'Icmm': '-I 2 2b',
    'Imcm': '-I 2 2a',
    'Imam': '-I 2c 2',
    #  75
    'P4': 'P 4',
    #  76
    'P41': 'P 4w',
    #  77
    'P42': 'P 4c',
    #  78
    'P43': 'P 4cw',
    #  79
    'I4': 'I 4',
    #  80
    'I41': 'I 4bw',
    #  81
    'P-4': 'P -4',
    #  82
    'I-4': 'I -4',
    #  83
    'P4/m': '-P 4',
    #  84
    'P42/m': '-P 4c',
    #  85
    'P4/n': 'P 4ab -1ab',
    'P4/n:1': 'P 4ab -1ab',
    'P4/n1': 'P 4ab -1ab',
    'P4/nS': 'P 4ab -1ab',
    'P4/n:2': '-P 4a',
    'P4/n2': '-P 4a',
    'P4/nZ': '-P 4a',
    #  86
    'P42/n': 'P 4n -1n',
    'P42/n:1': 'P 4n -1n',
    'P42/n1': 'P 4n -1n',
    'P42/nS': 'P 4n -1n',
    'P42/n:2': '-P 4bc',
    'P42/n2': '-P 4bc',
    'P42/nZ': '-P 4bc',
    #  87
    'I4/m': '-I 4',
    #  88
    'I41/a': 'I 4bw -1bw',
    'I41/a:1': 'I 4bw -1bw',
    'I41/a1': 'I 4bw -1bw',
    'I41/aS': 'I 4bw -1bw',
    'I41/a:2': '-I 4ad',
    'I41/a2': '-I 4ad',
    'I41/aZ': '-I 4ad',
    #  89
    'P422': 'P 4 2',
    #  90
    'P4212': 'P 4ab 2ab',
    #  91
    'P4122': 'P 4w 2c',
    #  92
    'P41212': 'P 4abw 2nw',
    #  93
    'P4222': 'P 4c 2',
    #  94
    'P42212': 'P 4n 2n',
    #  95
    'P4322': 'P 4cw 2c',
    #  96
    'P43212': 'P 4nw 2abw',
    #  97
    'I422': 'I 4 2',
    #  98
    'I4122': 'I 4bw 2bw',
    #  99
    'P4mm': 'P 4 -2',
    # 100
    'P4bm': 'P 4 -2ab',
    # 101
    'P42cm': 'P 4c -2c',
    # 102
    'P42nm': 'P 4n -2n',
    # 103
    'P4cc': 'P 4 -2c',
    # 104
    'P4nc': 'P 4 -2n',
    # 105
    'P42mc': 'P 4c -2',
    # 106
    'P42bc': 'P 4c -2ab',
    # 107
    'I4mm': 'I 4 -2',
    # 108
    'I4cm': 'I 4 -2c',
    # 109
    'I41md': 'I 4bw -2',
    # 110
    'I41cd': 'I 4bw -2c',
    # 111
    'P-42m': 'P -4 2',
    # 112
    'P-42c': 'P -4 2c',
    # 113
    'P-421m': 'P -4 2ab',
    # 114
    'P-421c': 'P -4 2n',
    # 115
    'P-4m2': 'P -4 -2',
    # 116
    'P-4c2': 'P -4 -2c',
    # 117
    'P-4b2': 'P -4 -2ab',
    # 118
    'P-4n2': 'P -4 -2n',
    # 119
    'I-4m2': 'I -4 -2',
    # 120
    'I-4c2': 'I -4 -2c',
    # 121
    'I-42m': 'I -4 2',
    # 122
    'I-42d': 'I -4 2bw',
    # 123
    'P4/mmm': '-P 4 2',
    'P4/m2/m2/m': '-P 4 2',
    # 124
    'P4/mcc': '-P 4 2c',
    # 125
    'P4/nbm': 'P 4 2 -1ab',
    'P4/nbm:1': 'P 4 2 -1ab',
    'P4/nbm1': 'P 4 2 -1ab',
    'P4/nbmS': 'P 4 2 -1ab',
    'P4/nbm:2': '-P 4a 2b',
    'P4/nbm2': '-P 4a 2b',
    'P4/nbmZ': '-P 4a 2b',
    # 126
    'P4/nnc': 'P 4 2 -1n',
    'P4/nnc:1': 'P 4 2 -1n',
    'P4/nnc1': 'P 4 2 -1n',
    'P4/nncS': 'P 4 2 -1n',
    'P4/nnc:2': '-P 4a 2bc',
    'P4/nnc2': '-P 4a 2bc',
    'P4/nncZ': '-P 4a 2bc',
    # 127
    'P4/mbm': '-P 4 2ab',
    # 128
    'P4/mnc': '-P 4 2n',
    # 129
    'P4/nmm': 'P 4ab 2ab -1ab',
    'P4/nmm:1': 'P 4ab 2ab -1ab',
    'P4/nmm1': 'P 4ab 2ab -1ab',
    'P4/nmmS': 'P 4ab 2ab -1ab',
    'P4/n21/m2/m(originchoice2)': 'P 4ab 2ab -1ab',   # ? FINDSYM choice
    'P4/nmm:2': '-P 4a 2a',
    'P4/nmm2': '-P 4a 2a',
    'P4/nmmZ': '-P 4a 2a',
    # 130
    'P4/ncc': 'P 4ab 2n -1ab',
    'P4/ncc:1': 'P 4ab 2n -1ab',
    'P4/ncc1': 'P 4ab 2n -1ab',
    'P4/nccS': 'P 4ab 2n -1ab',
    'P4/ncc:2': '-P 4a 2ac',
    'P4/ncc2': '-P 4a 2ac',
    'P4/nccZ': '-P 4a 2ac',
    # 131
    'P42/mmc': '-P 4c 2',
    # 132
    'P42/mcm': '-P 4c 2c',
    # 133
    'P42/nbc': 'P 4n 2c -1n',
    'P42/nbc:1': 'P 4n 2c -1n',
    'P42/nbc1': 'P 4n 2c -1n',
    'P42/nbcS': 'P 4n 2c -1n',
    'P42/nbc:2': '-P 4ac 2b',
    'P42/nbc2': '-P 4ac 2b',
    'P42/nbcZ': '-P 4ac 2b',
    # 134
    'P42/nnm': 'P 4n 2 -1n',
    'P42/nnm:1': 'P 4n 2 -1n',
    'P42/nnm1': 'P 4n 2 -1n',
    'P42/nnmS': 'P 4n 2 -1n',
    'P42/nnm:2': '-P 4ac 2bc',
    'P42/nnm2': '-P 4ac 2bc',
    'P42/nnmZ': '-P 4ac 2bc',
    # 135
    'P42/mbc': '-P 4c 2ab',
    # 136
    'P42/mnm': '-P 4n 2n',
    # 137
    'P42/nmc': 'P 4n 2n -1n',
    'P42/nmc:1': 'P 4n 2n -1n',
    'P42/nmc1': 'P 4n 2n -1n',
    'P42/nmcS': 'P 4n 2n -1n',
    'P42/nmc:2': '-P 4ac 2a',
    'P42/nmc2': '-P 4ac 2a',
    'P42/nmcZ': '-P 4ac 2a',
    # 138
    'P42/ncm': 'P 4n 2ab -1n',
    'P42/ncm:1': 'P 4n 2ab -1n',
    'P42/ncm1': 'P 4n 2ab -1n',
    'P42/ncmS': 'P 4n 2ab -1n',
    'P42/ncm:2': '-P 4ac 2ac',
    'P42/ncm2': '-P 4ac 2ac',
    'P42/ncmZ': '-P 4ac 2ac',
    # 139
    'I4/mmm': '-I 4 2',
    'I4/m2/m2/m': '-I 4 2',
    # 140
    'I4/mcm': '-I 4 2c',
    # 141
    'I41/amd': 'I 4bw 2bw -1bw',
    'I41/amd:1': 'I 4bw 2bw -1bw',
    'I41/amd1': 'I 4bw 2bw -1bw',
    'I41/amdS': 'I 4bw 2bw -1bw',
    'I41/amd:2': '-I 4bd 2',
    'I41/amd2': '-I 4bd 2',
    'I41/amdZ': '-I 4bd 2',
    # 142
    'I41/acd': 'I 4bw 2aw -1bw',
    'I41/acd:1': 'I 4bw 2aw -1bw',
    'I41/acd1': 'I 4bw 2aw -1bw',
    'I41/acdS': 'I 4bw 2aw -1bw',
    'I41/acd:2': '-I 4bd 2c',
    'I41/acd2': '-I 4bd 2c',
    'I41/acdZ': '-I 4bd 2c',
    # 143
    'P3': 'P 3',
    # 144
    'P31': 'P 31',
    # 145
    'P32': 'P 32',
    # 146
    'R3': 'R 3',
    'R3:H': 'R 3',
    'R3H': 'R 3',
    'R3:R': 'P 3*',
    'R3R': 'P 3*',
    # 147
    'P-3': '-P 3',
    # 148
    'R-3': '-R 3',
    'R-3:H': '-R 3',
    'R-3H': '-R 3',
    'R-3:R': '-P 3*',
    'R-3R': '-P 3*',
    # 149
    'P312': 'P 3 2',
    # 150
    'P321': 'P 3 2"',
    # 151
    'P3112': 'P 31 2c (0 0 1)',
    # 152
    'P3121': 'P 31 2"',
    # 153
    'P3212': 'P 32 2c (0 0 -1)',
    # 154
    'P3221': 'P 32 2"',
    # 155
    'R32': 'R 3 2"',
    'R32:H': 'R 3 2"',
    'R32H': 'R 3 2"',
    'R32:R': 'P 3* 2',
    'R32R': 'P 3* 2',
    # 156
    'P3m1': 'P 3 -2"',
    # 157
    'P31m': 'P 3 -2',
    # 158
    'P3c1': 'P 3 -2"c',
    # 159
    'P31c': 'P 3 -2c',
    # 160
    'R3m': 'R 3 -2"',
    'R3m:H': 'R 3 -2"',
    'R3mH': 'R 3 -2"',
    'R3m:R': 'P 3* -2',
    'R3mR': 'P 3* -2',
    'R3mHR': 'T 3 -2"',
    # 161
    'R3c': 'R 3 -2"c',
    'R3c:H': 'R 3 -2"c',
    'R3cH': 'R 3 -2"c',
    'R3c:R': 'P 3* -2n',
    'R3cR': 'P 3* -2n',
    # 162
    'P-31m': '-P 3 2',
    # 163
    'P-31c': '-P 3 2c',
    # 164
    'P-3m1': '-P 3 2"',
    'P-32/m1': '-P 3 2"',
    # 165
    'P-3c1': '-P 3 2"c',
    # 166
    'R-3m': '-R 3 2"',
    'R-32/m': '-R 3 2"',
    'R-3m:H': '-R 3 2"',
    'R-3mH': '-R 3 2"',
    'R-32/m:H': '-R 3 2"',
    'R-32/mH': '-R 3 2"',
    'R-3m:R': '-P 3* 2',
    'R-3mR': '-P 3* 2',
    'R-32/m:R': '-P 3* 2',
    'R-32/mR': '-P 3* 2',
    'R-3mHR': '-T 3 2"',
    # 167
    'R-3c': '-R 3 2"c',
    'R-3c:H': '-R 3 2"c',
    'R-3cH': '-R 3 2"c',
    'R-3c:R': '-P 3* 2n',
    'R-3cR': '-P 3* 2n',
    # 168
    'P6': 'P 6',
    # 169
    'P61': 'P 61',
    # 170
    'P65': 'P 65',
    # 171
    'P62': 'P 62',
    # 172
    'P64': 'P 64',
    # 173
    'P63': 'P 6c',
    # 174
    'P-6': 'P -6',
    # 175
    'P6/m': '-P 6',
    # 176
    'P63/m': '-P 6c',
    # 177
    'P622': 'P 6 2',
    # 178
    'P6122': 'P 61 2 (0 0 -1)',
    # 179
    'P6522': 'P 65 2 (0 0 1)',
    # 180
    'P6222': 'P 62 2c (0 0 1)',
    # 181
    'P6422': 'P 64 2c (0 0 -1)',
    # 182
    'P6322': 'P 6c 2c',
    # 183
    'P6mm': 'P 6 -2',
    # 184
    'P6cc': 'P 6 -2c',
    # 185
    'P63cm': 'P 6c -2',
    # 186
    'P63mc': 'P 6c -2c',
    # 187
    'P-6m2': 'P -6 2',
    # 188
    'P-6c2': 'P -6c 2',
    # 189
    'P-62m': 'P -6 -2',
    # 190
    'P-62c': 'P -6c -2c',
    # 191
    'P6/mmm': '-P 6 2',
    'P6/m2/m2/m': '-P 6 2',
    # 192
    'P6/mcc': '-P 6 2c',
    # 193
    'P63/mcm': '-P 6c 2',
    # 194
    'P63/mmc': '-P 6c 2c',
    'P63/m2/m2/c': '-P 6c 2c',
    # 195
    'P23': 'P 2 2 3',
    # 196
    'F23': 'F 2 2 3',
    # 197
    'I23': 'I 2 2 3',
    # 198
    'P213': 'P 2ac 2ab 3',
    # 199
    'I213': 'I 2b 2c 3',
    # 200
    'Pm-3': '-P 2 2 3',
    'P2/m-3': '-P 2 2 3',
    'Pm3': '-P 2 2 3',
    # 201
    'Pn-3': 'P 2 2 3 -1n',
    'Pn-3:1': 'P 2 2 3 -1n',
    'Pn-31': 'P 2 2 3 -1n',
    'Pn-3S': 'P 2 2 3 -1n',
    'Pn-3:2': '-P 2ab 2bc 3',
    'Pn-32': '-P 2ab 2bc 3',
    'Pn-3Z': '-P 2ab 2bc 3',
    'Pn3': 'P 2 2 3 -1n',
    # 202
    'Fm-3': '-F 2 2 3',
    'F2/m-3': '-F 2 2 3',
    'Fm3': '-F 2 2 3',
    # 203
    'Fd-3': 'F 2 2 3 -1d',
    'Fd-3:1': 'F 2 2 3 -1d',
    'Fd-31': 'F 2 2 3 -1d',
    'Fd-3S': 'F 2 2 3 -1d',
    'Fd-3:2': '-F 2uv 2vw 3',
    'Fd-32': '-F 2uv 2vw 3',
    'Fd-3Z': '-F 2uv 2vw 3',
    'Fd3': 'F 2 2 3 -1d',
    # 204
    'Im-3': '-I 2 2 3',
    'I2/m-3': '-I 2 2 3',
    'Im3': '-I 2 2 3',
    # 205
    'Pa-3': '-P 2ac 2ab 3',
    'Pa3': '-P 2ac 2ab 3',
    # 206
    'Ia-3': '-I 2b 2c 3',
    'Ia3': '-I 2b 2c 3',
    # 207
    'P432': 'P 4 2 3',
    # 208
    'P4232': 'P 4n 2 3',
    # 209
    'F432': 'F 4 2 3',
    # 210
    'F4132': 'F 4d 2 3',
    # 211
    'I432': 'I 4 2 3',
    # 212
    'P4332': 'P 4acd 2ab 3',
    # 213
    'P4132': 'P 4bd 2ab 3',
    # 214
    'I4132': 'I 4bd 2c 3',
    # 215
    'P-43m': 'P -4 2 3',
    # 216
    'F-43m': 'F -4 2 3',
    # 217
    'I-43m': 'I -4 2 3',
    # 218
    'P-43n': 'P -4n 2 3',
    # 219
    'F-43c': 'F -4c 2 3',
    # 220
    'I-43d': 'I -4bd 2c 3',
    # 221
    'Pm-3m': '-P 4 2 3',
    'P4/m-32/m': '-P 4 2 3',
    'Pm3m': '-P 4 2 3',
    # 222
    'Pn-3n': 'P 4 2 3 -1n',
    'Pn-3n:1': 'P 4 2 3 -1n',
    'Pn-3n1': 'P 4 2 3 -1n',
    'Pn-3nS': 'P 4 2 3 -1n',
    'Pn-3n:2': '-P 4a 2bc 3',
    'Pn-3n2': '-P 4a 2bc 3',
    'Pn-3nZ': '-P 4a 2bc 3',
    # 223
    'Pm-3n': '-P 4n 2 3',
    'P2/m-3n': '-P 4n 2 3',
    'Pm3n': '-P 4n 2 3',
    # 224
    'Pn-3m': 'P 4n 2 3 -1n',
    'Pn-3m:1': 'P 4n 2 3 -1n',
    'Pn-3m1': 'P 4n 2 3 -1n',
    'Pn-3mS': 'P 4n 2 3 -1n',
    'Pn-3m:2': '-P 4bc 2bc 3',
    'Pn-3m2': '-P 4bc 2bc 3',
    'Pn-3mZ': '-P 4bc 2bc 3',
    'Pn3m': 'P 4n 2 3 -1n',
    # 225
    'Fm-3m': '-F 4 2 3',
    'F4/m-32/m': '-F 4 2 3',
    'Fm3m': '-F 4 2 3',
    # 226
    'Fm-3c': '-F 4c 2 3',
    'F2/m-3c': '-F 4c 2 3',
    'Fm3c': '-F 4c 2 3',
    # 227
    'Fd-3m': 'F 4d 2 3 -1d',
    'Fd-3m:1': 'F 4d 2 3 -1d',
    'Fd-3m1': 'F 4d 2 3 -1d',
    'Fd-3mS': 'F 4d 2 3 -1d',
    'Fd-3m:2': '-F 4vw 2vw 3',
    'Fd-3m2': '-F 4vw 2vw 3',
    'Fd-3mZ': '-F 4vw 2vw 3',
    'Fd3m': 'F 4d 2 3 -1d',
    # 228
    'Fd-3c': 'F 4d 2 3 -1cd',
    'Fd-3c:1': 'F 4d 2 3 -1cd',
    'Fd-3c1': 'F 4d 2 3 -1cd',
    'Fd-3cS': 'F 4d 2 3 -1cd',
    'Fd-3c:2': '-F 4cvw 2vw 3',
    'Fd-3c2': '-F 4cvw 2vw 3',
    'Fd-3cZ': '-F 4cvw 2vw 3',
    'Fd3c': 'F 4d 2 3 -1cd',
    # 229
    'Im-3m': '-I 4 2 3',
    'I4/m-32/m': '-I 4 2 3',
    'Im3m': '-I 4 2 3',
    # 230
    'Ia-3d': '-I 4bd 2c 3',
    'Ia3d': '-I 4bd 2c 3',
    #######################
    # Non-standard settings
    # 1
    'A1': 'A 1',
    'B1': 'B 1',
    'C1': 'C 1',
    'I1': 'I 1',
    'F1': 'F 1',
    # 2
    'A-1': '-A 1',
    'B-1': '-B 1',
    'C-1': '-C 1',
    'I-1': '-I 1',
    'F-1': '-F 1',
    # 5
    'F112': 'F 2',
    'F211': 'F 2x',
    'F121': 'F 2y',
    # 8
    'F11m': 'F -2',
    'Fm11': 'F -2x',
    'F1m1': 'F -2y',
    # 9
    'F11d': 'F -2d',
    'F1d1': 'F -2yd',
    'Fd11': 'F -2xd',
    # 12
    'F112/m': '-F 2',
    'F2/m11': '-F 2x',
    'F12/m1': '-F 2y',
    # 15
    'F12/d1': 'F 2ycuw -1c',
    # 70
    'Fddd': '-F 2 2 -1d',
    'Fddd:1': '-F 2 2 -1d',
    'Fddd1': '-F 2 2 -1d',
    'FdddS': '-F 2 2 -1d',
    'Fddd:2': '-F 2uv 2vw',
    'Fddd2': '-F 2uv 2vw',
    'FdddZ': '-F 2uv 2vw',
    # 139
    'F4/m2/m2/m': '-F 4 2',
    'F4/mmm': '-F 4 2'
}

# Space group number for each Hall symbol
Hall2Number = {
    'Unknown': 0,
    #   1
    'P 1': 1,
    #   2
    '-P 1': 2,
    #   3
    'P 2y': 3,
    'P 2': 3,
    'P 2x': 3,
    #   4
    'P 2yb': 4,
    'P 2c': 4,
    'P 2xa': 4,
    #   5
    'C 2y': 5,
    'A 2y': 5,
    'I 2y': 5,
    'A 2': 5,
    'B 2': 5,
    'I 2': 5,
    'B 2x': 5,
    'C 2x': 5,
    'I 2x': 5,
    #   6
    'P -2y': 6,
    'P -2': 6,
    'P -2x': 6,
    #   7
    'P -2yc': 7,
    'P -2yac': 7,
    'P -2ya': 7,
    'P -2a': 7,
    'P -2ab': 7,
    'P -2b': 7,
    'P -2xb': 7,
    'P -2xbc': 7,
    'P -2xc': 7,
    #   8
    'C -2y': 8,
    'A -2y': 8,
    'I -2y': 8,
    'A -2': 8,
    'B -2': 8,
    'I -2': 8,
    'B -2x': 8,
    'C -2x': 8,
    'I -2x': 8,
    #   9
    'C -2yc': 9,
    'A -2yac': 9,
    'I -2ya': 9,
    'A -2ya': 9,
    'C -2ybc': 9,
    'I -2yc': 9,
    'A -2a': 9,
    'B -2bc': 9,
    'I -2b': 9,
    'B -2b': 9,
    'A -2ac': 9,
    'I -2a': 9,
    'B -2xb': 9,
    'C -2xbc': 9,
    'I -2xc': 9,
    'C -2xc': 9,
    'B -2xbc': 9,
    'I -2xb': 9,
    #  10
    '-P 2y': 10,
    '-P 2': 10,
    '-P 2x': 10,
    #  11
    '-P 2yb': 11,
    '-P 2c': 11,
    '-P 2xa': 11,
    #  12
    '-C 2y': 12,
    '-A 2y': 12,
    '-I 2y': 12,
    '-A 2': 12,
    '-B 2': 12,
    '-I 2': 12,
    '-B 2x': 12,
    '-C 2x': 12,
    '-I 2x': 12,
    #  13
    '-P 2yc': 13,
    '-P 2yac': 13,
    '-P 2ya': 13,
    '-P 2a': 13,
    '-P 2ab': 13,
    '-P 2b': 13,
    '-P 2xb': 13,
    '-P 2xbc': 13,
    '-P 2xc': 13,
    #  14
    '-P 2ybc': 14,
    '-P 2yn': 14,
    '-P 2yab': 14,
    '-P 2ac': 14,
    '-P 2n': 14,
    '-P 2bc': 14,
    '-P 2xab': 14,
    '-P 2xn': 14,
    '-P 2xac': 14,
    #  15
    '-C 2yc': 15,
    '-A 2yac': 15,
    '-I 2ya': 15,
    '-A 2ya': 15,
    '-C 2ybc': 15,
    '-I 2yc': 15,
    '-A 2a': 15,
    '-B 2bc': 15,
    '-I 2b': 15,
    '-B 2b': 15,
    '-A 2ac': 15,
    '-I 2a': 15,
    '-B 2xb': 15,
    '-C 2xbc': 15,
    '-I 2xc': 15,
    '-C 2xc': 15,
    '-B 2xbc': 15,
    '-I 2xb': 15,
    #  16
    'P 2 2': 16,
    #  17
    'P 2c 2': 17,
    'P 2a 2a': 17,
    'P 2 2b': 17,
    #  18
    'P 2 2ab': 18,
    'P 2bc 2': 18,
    'P 2ac 2ac': 18,
    #  19
    'P 2ac 2ab': 19,
    #  20
    'C 2c 2': 20,
    'A 2a 2a': 20,
    'B 2 2b': 20,
    #  21
    'C 2 2': 21,
    'A 2 2': 21,
    'B 2 2': 21,
    #  22
    'F 2 2': 22,
    #  23
    'I 2 2': 23,
    #  24
    'I 2b 2c': 24,
    #  25
    'P 2 -2': 25,
    'P -2 2': 25,
    'P -2 -2': 25,
    #  26
    'P 2c -2': 26,
    'P 2c -2c': 26,
    'P -2a 2a': 26,
    'P -2 2a': 26,
    'P -2 -2b': 26,
    'P -2b -2': 26,
    #  27
    'P 2 -2c': 27,
    'P -2a 2': 27,
    'P -2b -2b': 27,
    #  28
    'P 2 -2a': 28,
    'P 2 -2b': 28,
    'P -2b 2': 28,
    'P -2c 2': 28,
    'P -2c -2c': 28,
    'P -2a -2a': 28,
    #  29
    'P 2c -2ac': 29,
    'P 2c -2b': 29,
    'P -2b 2a': 29,
    'P -2ac 2a': 29,
    'P -2bc -2c': 29,
    'P -2a -2ab': 29,
    #  30
    'P 2 -2bc': 30,
    'P 2 -2ac': 30,
    'P -2ac 2': 30,
    'P -2ab 2': 30,
    'P -2ab -2ab': 30,
    'P -2bc -2bc': 30,
    #  31
    'P 2ac -2': 31,
    'P 2bc -2bc': 31,
    'P -2ab 2ab': 31,
    'P -2 2ac': 31,
    'P -2 -2bc': 31,
    'P -2ab -2': 31,
    #  32
    'P 2 -2ab': 32,
    'P -2bc 2': 32,
    'P -2ac -2ac': 32,
    #  33
    'P 2c -2n': 33,
    'P 2c -2ab': 33,
    'P -2bc 2a': 33,
    'P -2n 2a': 33,
    'P -2n -2ac': 33,
    'P -2ac -2n': 33,
    #  34
    'P 2 -2n': 34,
    'P -2n 2': 34,
    'P -2n -2n': 34,
    #  35
    'C 2 -2': 35,
    'A -2 2': 35,
    'B -2 -2': 35,
    #  36
    'C 2c -2': 36,
    'C 2c -2c': 36,
    'A -2a 2a': 36,
    'A -2 2a': 36,
    'B -2 -2b': 36,
    'B -2b -2': 36,
    #  37
    'C 2 -2c': 37,
    'A -2a 2': 37,
    'B -2b -2b': 37,
    #  38
    'A 2 -2': 38,
    'B 2 -2': 38,
    'B -2 2': 38,
    'C -2 2': 38,
    'C -2 -2': 38,
    'A -2 -2': 38,
    #  39
    'A 2 -2c': 39,
    'B 2 -2c': 39,
    'B -2c 2': 39,
    'C -2b 2': 39,
    'C -2b -2b': 39,
    'A -2c -2c': 39,
    #  40
    'A 2 -2a': 40,
    'B 2 -2b': 40,
    'B -2b 2': 40,
    'C -2c 2': 40,
    'C -2c -2c': 40,
    'A -2a -2a': 40,
    #  41
    'A 2 -2ac': 41,
    'B 2 -2bc': 41,
    'B -2bc 2': 41,
    'C -2bc 2': 41,
    'C -2bc -2bc': 41,
    'A -2ac -2ac': 41,
    #  42
    'F 2 -2': 42,
    'F -2 2': 42,
    'F -2 -2': 42,
    #  43
    'F 2 -2d': 43,
    'F -2d 2': 43,
    'F -2d -2d': 43,
    #  44
    'I 2 -2': 44,
    'I -2 2': 44,
    'I -2 -2': 44,
    #  45
    'I 2 -2c': 45,
    'I -2a 2': 45,
    'I -2b -2b': 45,
    #  46
    'I 2 -2a': 46,
    'I 2 -2b': 46,
    'I -2b 2': 46,
    'I -2c 2': 46,
    'I -2c -2c': 46,
    'I -2a -2a': 46,
    #  47
    '-P 2 2': 47,
    #  48
    'P 2 2 -1n': 48,
    '-P 2ab 2bc': 48,
    #  49
    '-P 2 2c': 49,
    '-P 2a 2': 49,
    '-P 2b 2b': 49,
    #  50
    'P 2 2 -1ab': 50,
    '-P 2ab 2b': 50,
    'P 2 2 -1bc': 50,
    '-P 2b 2bc': 50,
    'P 2 2 -1ac': 50,
    '-P 2a 2c': 50,
    #  51
    '-P 2a 2a': 51,
    '-P 2b 2': 51,
    '-P 2 2b': 51,
    '-P 2c 2c': 51,
    '-P 2c 2': 51,
    '-P 2 2a': 51,
    #  52
    '-P 2a 2bc': 52,
    '-P 2b 2n': 52,
    '-P 2n 2b': 52,
    '-P 2ab 2c': 52,
    '-P 2ab 2n': 52,
    '-P 2n 2bc': 52,
    #  53
    '-P 2ac 2': 53,
    '-P 2bc 2bc': 53,
    '-P 2ab 2ab': 53,
    '-P 2 2ac': 53,
    '-P 2 2bc': 53,
    '-P 2ab 2': 53,
    #  54
    '-P 2a 2ac': 54,
    '-P 2b 2c': 54,
    '-P 2a 2b': 54,
    '-P 2ac 2c': 54,
    '-P 2bc 2b': 54,
    '-P 2b 2ab': 54,
    #  55
    '-P 2 2ab': 55,
    '-P 2bc 2': 55,
    '-P 2ac 2ac': 55,
    #  56
    '-P 2ab 2ac': 56,
    '-P 2ac 2bc': 56,
    '-P 2bc 2ab': 56,
    #  57
    '-P 2c 2b': 57,
    '-P 2c 2ac': 57,
    '-P 2ac 2a': 57,
    '-P 2b 2a': 57,
    '-P 2a 2ab': 57,
    '-P 2bc 2c': 57,
    #  58
    '-P 2 2n': 58,
    '-P 2n 2': 58,
    '-P 2n 2n': 58,
    #  59
    'P 2 2ab -1ab': 59,
    '-P 2ab 2a': 59,
    'P 2bc 2 -1bc': 59,
    '-P 2c 2bc': 59,
    'P 2ac 2ac -1ac': 59,
    '-P 2c 2a': 59,
    #  60
    '-P 2n 2ab': 60,
    '-P 2n 2c': 60,
    '-P 2a 2n': 60,
    '-P 2bc 2n': 60,
    '-P 2ac 2b': 60,
    '-P 2b 2ac': 60,
    #  61
    '-P 2ac 2ab': 61,
    '-P 2bc 2ac': 61,
    #  62
    '-P 2ac 2n': 62,
    '-P 2bc 2a': 62,
    '-P 2c 2ab': 62,
    '-P 2n 2ac': 62,
    '-P 2n 2a': 62,
    '-P 2c 2n': 62,
    #  63
    '-C 2c 2': 63,
    '-C 2c 2c': 63,
    '-A 2a 2a': 63,
    '-A 2 2a': 63,
    '-B 2 2b': 63,
    '-B 2b 2': 63,
    #  64
    '-C 2bc 2': 64,
    '-C 2bc 2bc': 64,
    '-A 2ac 2ac': 64,
    '-A 2 2ac': 64,
    '-B 2 2bc': 64,
    '-B 2bc 2': 64,
    #  65
    '-C 2 2': 65,
    '-A 2 2': 65,
    '-B 2 2': 65,
    #  66
    '-C 2 2c': 66,
    '-A 2a 2': 66,
    '-B 2b 2b': 66,
    #  67
    '-C 2b 2': 67,
    '-C 2b 2b': 67,
    '-A 2c 2c': 67,
    '-A 2 2c': 67,
    '-B 2 2c': 67,
    '-B 2c 2': 67,
    #  68
    'C 2 2 -1bc': 68,
    '-C 2b 2bc': 68,
    'C 2 2 -1bc': 68,
    '-C 2b 2c': 68,
    'A 2 2 -1ac': 68,
    '-A 2a 2c': 68,
    'A 2 2 -1ac': 68,
    '-A 2ac 2c': 68,
    'B 2 2 -1bc': 68,
    '-B 2bc 2b': 68,
    'B 2 2 -1bc': 68,
    '-B 2b 2bc': 68,
    #  69
    '-F 2 2': 69,
    #  70
    'F 2 2 -1d': 70,
    '-F 2uv 2vw': 70,
    #  71
    '-I 2 2': 71,
    #  72
    '-I 2 2c': 72,
    '-I 2a 2': 72,
    '-I 2b 2b': 72,
    #  73
    '-I 2b 2c': 73,
    '-I 2a 2b': 73,
    #  74
    '-I 2b 2': 74,
    '-I 2a 2a': 74,
    '-I 2c 2c': 74,
    '-I 2 2b': 74,
    '-I 2 2a': 74,
    '-I 2c 2': 74,
    #  75
    'P 4': 75,
    #  76
    'P 4w': 76,
    #  77
    'P 4c': 77,
    #  78
    'P 4cw': 78,
    #  79
    'I 4': 79,
    #  80
    'I 4bw': 80,
    #  81
    'P -4': 81,
    #  82
    'I -4': 82,
    #  83
    '-P 4': 83,
    #  84
    '-P 4c': 84,
    #  85
    'P 4ab -1ab': 85,
    '-P 4a': 85,
    #  86
    'P 4n -1n': 86,
    '-P 4bc': 86,
    #  87
    '-I 4': 87,
    #  88
    'I 4bw -1bw': 88,
    '-I 4ad': 88,
    #  89
    'P 4 2': 89,
    #  90
    'P 4ab 2ab': 90,
    #  91
    'P 4w 2c': 91,
    #  92
    'P 4abw 2nw': 92,
    #  93
    'P 4c 2': 93,
    #  94
    'P 4n 2n': 94,
    #  95
    'P 4cw 2c': 95,
    #  96
    'P 4nw 2abw': 96,
    #  97
    'I 4 2': 97,
    #  98
    'I 4bw 2bw': 98,
    #  99
    'P 4 -2': 99,
    # 100
    'P 4 -2ab': 100,
    # 101
    'P 4c -2c': 101,
    # 102
    'P 4n -2n': 102,
    # 103
    'P 4 -2c': 103,
    # 104
    'P 4 -2n': 104,
    # 105
    'P 4c -2': 105,
    # 106
    'P 4c -2ab': 106,
    # 107
    'I 4 -2': 107,
    # 108
    'I 4 -2c': 108,
    # 109
    'I 4bw -2': 109,
    # 110
    'I 4bw -2c': 110,
    # 111
    'P -4 2': 111,
    # 112
    'P -4 2c': 112,
    # 113
    'P -4 2ab': 113,
    # 114
    'P -4 2n': 114,
    # 115
    'P -4 -2': 115,
    # 116
    'P -4 -2c': 116,
    # 117
    'P -4 -2ab': 117,
    # 118
    'P -4 -2n': 118,
    # 119
    'I -4 -2': 119,
    # 120
    'I -4 -2c': 120,
    # 121
    'I -4 2': 121,
    # 122
    'I -4 2bw': 122,
    # 123
    '-P 4 2': 123,
    # 124
    '-P 4 2c': 124,
    # 125
    'P 4 2 -1ab': 125,
    '-P 4a 2b': 125,
    # 126
    'P 4 2 -1n': 126,
    '-P 4a 2bc': 126,
    # 127
    '-P 4 2ab': 127,
    # 128
    '-P 4 2n': 128,
    # 129
    'P 4ab 2ab -1ab': 129,
    '-P 4a 2a': 129,
    # 130
    'P 4ab 2n -1ab': 130,
    '-P 4a 2ac': 130,
    # 131
    '-P 4c 2': 131,
    # 132
    '-P 4c 2c': 132,
    # 133
    'P 4n 2c -1n': 133,
    '-P 4ac 2b': 133,
    # 134
    'P 4n 2 -1n': 134,
    '-P 4ac 2bc': 134,
    # 135
    '-P 4c 2ab': 135,
    # 136
    '-P 4n 2n': 136,
    # 137
    'P 4n 2n -1n': 137,
    '-P 4ac 2a': 137,
    # 138
    'P 4n 2ab -1n': 138,
    '-P 4ac 2ac': 138,
    # 139
    '-I 4 2': 139,
    # 140
    '-I 4 2c': 140,
    # 141
    'I 4bw 2bw -1bw': 141,
    '-I 4bd 2': 141,
    # 142
    'I 4bw 2aw -1bw': 142,
    '-I 4bd 2c': 142,
    # 143
    'P 3': 143,
    # 144
    'P 31': 144,
    # 145
    'P 32': 145,
    # 146
    'R 3': 146,
    'P 3*': 146,
    # 147
    '-P 3': 147,
    # 148
    '-R 3': 148,
    '-P 3*': 148,
    # 149
    'P 3 2': 149,
    # 150
    'P 3 2"': 150,
    # 151
    'P 31 2c (0 0 1)': 151,
    # 152
    'P 31 2"': 152,
    # 153
    'P 32 2c (0 0 -1)': 153,
    # 154
    'P 32 2"': 154,
    # 155
    'R 3 2"': 155,
    'P 3* 2': 155,
    # 156
    'P 3 -2"': 156,
    # 157
    'P 3 -2': 157,
    # 158
    'P 3 -2"c': 158,
    # 159
    'P 3 -2c': 159,
    # 160
    'R 3 -2"': 160,
    'P 3* -2': 160,
    # 161
    'R 3 -2"c': 161,
    'P 3* -2n': 161,
    # 162
    '-P 3 2': 162,
    # 163
    '-P 3 2c': 163,
    # 164
    '-P 3 2"': 164,
    # 165
    '-P 3 2"c': 165,
    # 166
    '-R 3 2"': 166,
    '-P 3* 2': 166,
    # 167
    '-R 3 2"c': 167,
    '-P 3* 2n': 167,
    # 168
    'P 6': 168,
    # 169
    'P 61': 169,
    # 170
    'P 65': 170,
    # 171
    'P 62': 171,
    # 172
    'P 64': 172,
    # 173
    'P 6c': 173,
    # 174
    'P -6': 174,
    # 175
    '-P 6': 175,
    # 176
    '-P 6c': 176,
    # 177
    'P 6 2': 177,
    # 178
    'P 61 2 (0 0 -1)': 178,
    # 179
    'P 65 2 (0 0 1)': 179,
    # 180
    'P 62 2c (0 0 1)': 180,
    # 181
    'P 64 2c (0 0 -1)': 181,
    # 182
    'P 6c 2c': 182,
    # 183
    'P 6 -2': 183,
    # 184
    'P 6 -2c': 184,
    # 185
    'P 6c -2': 185,
    # 186
    'P 6c -2c': 186,
    # 187
    'P -6 2': 187,
    # 188
    'P -6c 2': 188,
    # 189
    'P -6 -2': 189,
    # 190
    'P -6c -2c': 190,
    # 191
    '-P 6 2': 191,
    # 192
    '-P 6 2c': 192,
    # 193
    '-P 6c 2': 193,
    # 194
    '-P 6c 2c': 194,
    # 195
    'P 2 2 3': 195,
    # 196
    'F 2 2 3': 196,
    # 197
    'I 2 2 3': 197,
    # 198
    'P 2ac 2ab 3': 198,
    # 199
    'I 2b 2c 3': 199,
    # 200
    '-P 2 2 3': 200,
    # 201
    'P 2 2 3 -1n': 201,
    '-P 2ab 2bc 3': 201,
    # 202
    '-F 2 2 3': 202,
    # 203
    'F 2 2 3 -1d': 203,
    '-F 2uv 2vw 3': 203,
    # 204
    '-I 2 2 3': 204,
    # 205
    '-P 2ac 2ab 3': 205,
    # 206
    '-I 2b 2c 3': 206,
    # 207
    'P 4 2 3': 207,
    # 208
    'P 4n 2 3': 208,
    # 209
    'F 4 2 3': 209,
    # 210
    'F 4d 2 3': 210,
    # 211
    'I 4 2 3': 211,
    # 212
    'P 4acd 2ab 3': 212,
    # 213
    'P 4bd 2ab 3': 213,
    # 214
    'I 4bd 2c 3': 214,
    # 215
    'P -4 2 3': 215,
    # 216
    'F -4 2 3': 216,
    # 217
    'I -4 2 3': 217,
    # 218
    'P -4n 2 3': 218,
    # 219
    'F -4c 2 3': 219,
    # 220
    'I -4bd 2c 3': 220,
    # 221
    '-P 4 2 3': 221,
    # 222
    'P 4 2 3 -1n': 222,
    '-P 4a 2bc 3': 222,
    # 223
    '-P 4n 2 3': 223,
    # 224
    'P 4n 2 3 -1n': 224,
    '-P 4bc 2bc 3': 224,
    # 225
    '-F 4 2 3': 225,
    # 226
    '-F 4c 2 3': 226,
    # 227
    'F 4d 2 3 -1d': 227,
    '-F 4vw 2vw 3': 227,
    # 228
    'F 4d 2 3 -1cd': 228,
    '-F 4cvw 2vw 3': 228,
    # 229
    '-I 4 2 3': 229,
    # 230
    '-I 4bd 2c 3': 230,
    #######################
    # Non-standard settings
    # 1
    'A 1': 1,
    'B 1': 1,
    'C 1': 1,
    'I 1': 1,
    'F 1': 1,
    # 2
    '-A 1': 2,
    '-B 1': 2,
    '-C 1': 2,
    '-I 1': 2,
    '-F 1': 2,
    # 5
    'F 2': 5,
    'F 2x': 5,
    'F 2y': 5,
    # 8
    'F -2': 8,
    'F -2x': 8,
    'F -2y': 8,
    # 9
    'F -2d': 9,
    'F -2yd': 9,
    'F -2xd': 9,
    # 12
    '-F 2': 12,
    '-F 2x': 12,
    '-F 2y': 12,
    # 15
    'F 2ycuw -1c': 15,
    # 70
    '-F 2 2 -1d': 70,
    '-F 2uv 2vw': 70,
    # 139
    '-F 4 2': 139
}

# The space groups that has only one possible "standard" setting
Number2Hall = {
    1: 'P 1',
    2: '-P 1',
    16: 'P 2 2',
    19: 'P 2ac 2ab',
    22: 'F 2 2',
    23: 'I 2 2',
    24: 'I 2b 2c',
    47: '-P 2 2',
    69: '-F 2 2',
    71: '-I 2 2',
    75: 'P 4',
    76: 'P 4w',
    77: 'P 4c',
    78: 'P 4cw',
    79: 'I 4',
    80: 'I 4bw',
    81: 'P -4',
    82: 'I -4',
    83: '-P 4',
    84: '-P 4c',
    87: '-I 4',
    89: 'P 4 2',
    90: 'P 4ab 2ab',
    91: 'P 4w 2c',
    92: 'P 4abw 2nw',
    93: 'P 4c 2',
    94: 'P 4n 2n',
    95: 'P 4cw 2c',
    96: 'P 4nw 2abw',
    97: 'I 4 2',
    98: 'I 4bw 2bw',
    99: 'P 4 -2',
    100: 'P 4 -2ab',
    101: 'P 4c -2c',
    102: 'P 4n -2n',
    103: 'P 4 -2c',
    104: 'P 4 -2n',
    105: 'P 4c -2',
    106: 'P 4c -2ab',
    107: 'I 4 -2',
    108: 'I 4 -2c',
    109: 'I 4bw -2',
    110: 'I 4bw -2c',
    111: 'P -4 2',
    112: 'P -4 2c',
    113: 'P -4 2ab',
    114: 'P -4 2n',
    115: 'P -4 -2',
    116: 'P -4 -2c',
    117: 'P -4 -2ab',
    118: 'P -4 -2n',
    119: 'I -4 -2',
    120: 'I -4 -2c',
    121: 'I -4 2',
    122: 'I -4 2bw',
    123: '-P 4 2',
    124: '-P 4 2c',
    127: '-P 4 2ab',
    128: '-P 4 2n',
    131: '-P 4c 2',
    132: '-P 4c 2c',
    135: '-P 4c 2ab',
    136: '-P 4n 2n',
    139: '-I 4 2',
    140: '-I 4 2c',
    143: 'P 3',
    144: 'P 31',
    145: 'P 32',
    147: '-P 3',
    149: 'P 3 2',
    150: 'P 3 2"',
    151: 'P 31 2c (0 0 1)',
    152: 'P 31 2"',
    153: 'P 32 2c (0 0 -1)',
    154: 'P 32 2"',
    156: 'P 3 -2"',
    157: 'P 3 -2',
    158: 'P 3 -2"c',
    159: 'P 3 -2c',
    162: '-P 3 2',
    163: '-P 3 2c',
    164: '-P 3 2"',
    165: '-P 3 2"c',
    168: 'P 6',
    169: 'P 61',
    170: 'P 65',
    171: 'P 62',
    172: 'P 64',
    173: 'P 6c',
    174: 'P -6',
    175: '-P 6',
    176: '-P 6c',
    177: 'P 6 2',
    178: 'P 61 2 (0 0 -1)',
    179: 'P 65 2 (0 0 1)',
    180: 'P 62 2c (0 0 1)',
    181: 'P 64 2c (0 0 -1)',
    182: 'P 6c 2c',
    183: 'P 6 -2',
    184: 'P 6 -2c',
    185: 'P 6c -2',
    186: 'P 6c -2c',
    187: 'P -6 2',
    188: 'P -6c 2',
    189: 'P -6 -2',
    190: 'P -6c -2c',
    191: '-P 6 2',
    192: '-P 6 2c',
    193: '-P 6c 2',
    194: '-P 6c 2c',
    195: 'P 2 2 3',
    196: 'F 2 2 3',
    197: 'I 2 2 3',
    198: 'P 2ac 2ab 3',
    199: 'I 2b 2c 3',
    200: '-P 2 2 3',
    202: '-F 2 2 3',
    204: '-I 2 2 3',
    205: '-P 2ac 2ab 3',
    206: '-I 2b 2c 3',
    207: 'P 4 2 3',
    208: 'P 4n 2 3',
    209: 'F 4 2 3',
    210: 'F 4d 2 3',
    211: 'I 4 2 3',
    212: 'P 4acd 2a 3',
    213: 'P 4bd 2ab 3',
    214: 'I 4bd 2c 3',
    215: 'P -4 2 3',
    216: 'F -4 2 3',
    217: 'I -4 2 3',
    218: 'P -4n 2 3',
    219: 'F -4c 2 3',
    220: 'I -4bd 2c 3',
    221: '-P 4 2 3',
    223: '-P 4n 2 3',
    225: '-F 4 2 3',
    226: '-F 4c 2 3',
    229: '-I 4 2 3',
    230: '-I 4bd 2c 3'
}

# Convert Hall symbol to Hermann-Mauguin symbol
Hall2HM = {
    'Unknown': 'Unknown',
    #   1
    'P 1': 'P1',
    #   2
    '-P 1': 'P-1',
    #   3
    'P 2y': 'P121',
    'P 2': 'P112',
    'P 2x': 'P211',
    #   4
    'P 2yb': 'P1211',
    'P 2c': 'P1121',
    'P 2xa': 'P2111',
    #   5
    'C 2y': 'C121',
    'A 2y': 'A121',
    'I 2y': 'I121',
    'A 2': 'A112',
    'B 2': 'B112',
    'I 2': 'I112',
    'B 2x': 'B211',
    'C 2x': 'C211',
    'I 2x': 'I211',
    #   6
    'P -2y': 'P1m1',
    'P -2': 'P11m',
    'P -2x': 'Pm11',
    #   7
    'P -2yc': 'P1c1',
    'P -2yac': 'P1n1',
    'P -2ya': 'P1a1',
    'P -2a': 'P11a',
    'P -2ab': 'P11n',
    'P -2b': 'P11b',
    'P -2xb': 'Pb11',
    'P -2xbc': 'Pn11',
    'P -2xc': 'Pc11',
    #   8
    'C -2y': 'C1m1',
    'A -2y': 'A1m1',
    'I -2y': 'I1m1',
    'A -2': 'A11m',
    'B -2': 'B11m',
    'I -2': 'I11m',
    'B -2x': 'Bm11',
    'C -2x': 'Cm11',
    'I -2x': 'Im11',
    #   9
    'C -2yc': 'C1c1',
    'A -2yac': 'A1n1',
    'I -2ya': 'I1a1',
    'A -2ya': 'A1a1',
    'C -2ybc': 'C1n1',
    'I -2yc': 'I1c1',
    'A -2a': 'A11a',
    'B -2bc': 'B11n',
    'I -2b': 'I11b',
    'B -2b': 'B11b',
    'A -2ac': 'A11n',
    'I -2a': 'I11a',
    'B -2xb': 'Bb11',
    'C -2xbc': 'Cn11',
    'I -2xc': 'Ic11',
    'C -2xc': 'Cc11',
    'B -2xbc': 'Bn11',
    'I -2xb': 'Ib11',
    #  10
    '-P 2y': 'P12/m1',
    '-P 2': 'P112/m',
    '-P 2x': 'P2/m11',
    #  11
    '-P 2yb': 'P121/m1',
    '-P 2c': 'P1121/m',
    '-P 2xa': 'P21/m11',
    #  12
    '-C 2y': 'C12/m1',
    '-A 2y': 'A12/m1',
    '-I 2y': 'I12/m1',
    '-A 2': 'A112/m',
    '-B 2': 'B112/m',
    '-I 2': 'I112/m',
    '-B 2x': 'B2/m11',
    '-C 2x': 'C2/m11',
    '-I 2x': 'I2/m11',
    #  13
    '-P 2yc': 'P12/c1',
    '-P 2yac': 'P12/n1',
    '-P 2ya': 'P12/a1',
    '-P 2a': 'P112/a',
    '-P 2ab': 'P112/n',
    '-P 2b': 'P112/b',
    '-P 2xb': 'P2/b11',
    '-P 2xbc': 'P2/n11',
    '-P 2xc': 'P2/c11',
    #  14
    '-P 2ybc': 'P121/c1',
    '-P 2yn': 'P121/n1',
    '-P 2yab': 'P121/a1',
    '-P 2ac': 'P1121/a',
    '-P 2n': 'P1121/n',
    '-P 2bc': 'P1121/b',
    '-P 2xab': 'P21/b11',
    '-P 2xn': 'P21/n11',
    '-P 2xac': 'P21/c11',
    #  15
    '-C 2yc': 'C12/c1',
    '-A 2yac': 'A12/n1',
    '-I 2ya': 'I12/a1',
    '-A 2ya': 'A12/a1',
    '-C 2ybc': 'C12/n1',
    '-I 2yc': 'I12/c1',
    '-A 2a': 'A112/a',
    '-B 2bc': 'B112/n',
    '-I 2b': 'I112/b',
    '-B 2b': 'B112/b',
    '-A 2ac': 'A112/n',
    '-I 2a': 'I112/a',
    '-B 2xb': 'B2/b11',
    '-C 2xbc': 'C2/n11',
    '-I 2xc': 'I2/c11',
    '-C 2xc': 'C2/c11',
    '-B 2xbc': 'B2/n11',
    '-I 2xb': 'I2/b11',
    #  16
    'P 2 2': 'P222',
    #  17
    'P 2c 2': 'P2221',
    'P 2a 2a': 'P2122',
    'P 2 2b': 'P2212',
    #  18
    'P 2 2ab': 'P21212',
    'P 2bc 2': 'P22121',
    'P 2ac 2ac': 'P21221',
    #  19
    'P 2ac 2ab': 'P212121',
    #  20
    'C 2c 2': 'C2221',
    'A 2a 2a': 'A2122',
    'B 2 2b': 'B2212',
    #  21
    'C 2 2': 'C222',
    'A 2 2': 'A222',
    'B 2 2': 'B222',
    #  22
    'F 2 2': 'F222',
    #  23
    'I 2 2': 'I222',
    #  24
    'I 2b 2c': 'I212121',
    #  25
    'P 2 -2': 'Pmm2',
    'P -2 2': 'P2mm',
    'P -2 -2': 'Pm2m',
    #  26
    'P 2c -2': 'Pmc21',
    'P 2c -2c': 'Pcm21',
    'P -2a 2a': 'P21ma',
    'P -2 2a': 'P21am',
    'P -2 -2b': 'Pb21m',
    'P -2b -2': 'Pm21b',
    #  27
    'P 2 -2c': 'Pcc2',
    'P -2a 2': 'P2aa',
    'P -2b -2b': 'Pb2b',
    #  28
    'P 2 -2a': 'Pma2',
    'P 2 -2b': 'Pbm2',
    'P -2b 2': 'P2mb',
    'P -2c 2': 'P2cm',
    'P -2c -2c': 'Pc2m',
    'P -2a -2a': 'Pm2a',
    #  29
    'P 2c -2ac': 'Pca21',
    'P 2c -2b': 'Pbc21',
    'P -2b 2a': 'P21ab',
    'P -2ac 2a': 'P21ca',
    'P -2bc -2c': 'Pc21b',
    'P -2a -2ab': 'Pb21a',
    #  30
    'P 2 -2bc': 'Pnc2',
    'P 2 -2ac': 'Pcn2',
    'P -2ac 2': 'P2na',
    'P -2ab 2': 'P2an',
    'P -2ab -2ab': 'Pb2n',
    'P -2bc -2bc': 'Pn2b',
    #  31
    'P 2ac -2': 'Pmn21',
    'P 2bc -2bc': 'Pnm21',
    'P -2ab 2ab': 'P21mn',
    'P -2 2ac': 'P21nm',
    'P -2 -2bc': 'Pn21m',
    'P -2ab -2': 'Pm21n',
    #  32
    'P 2 -2ab': 'Pba2',
    'P -2bc 2': 'P2cb',
    'P -2ac -2ac': 'Pc2a',
    #  33
    'P 2c -2n': 'Pna21',
    'P 2c -2ab': 'Pbn21',
    'P -2bc 2a': 'P21nb',
    'P -2n 2a': 'P21cn',
    'P -2n -2ac': 'Pc21n',
    'P -2ac -2n': 'Pn21a',
    #  34
    'P 2 -2n': 'Pnn2',
    'P -2n 2': 'P2nn',
    'P -2n -2n': 'Pn2n',
    #  35
    'C 2 -2': 'Cmm2',
    'A -2 2': 'A2mm',
    'B -2 -2': 'Bm2m',
    #  36
    'C 2c -2': 'Cmc21',
    'C 2c -2c': 'Ccm21',
    'A -2a 2a': 'A21ma',
    'A -2 2a': 'A21am',
    'B -2 -2b': 'Bb21m',
    'B -2b -2': 'Bm21b',
    #  37
    'C 2 -2c': 'Ccc2',
    'A -2a 2': 'A2aa',
    'B -2b -2b': 'Bb2b',
    #  38
    'A 2 -2': 'Amm2',
    'B 2 -2': 'Bmm2',
    'B -2 2': 'B2mm',
    'C -2 2': 'C2mm',
    'C -2 -2': 'Cm2m',
    'A -2 -2': 'Am2m',
    #  39
    'A 2 -2c': 'Abm2',
    'B 2 -2c': 'Bma2',
    'B -2c 2': 'B2cm',
    'C -2b 2': 'C2mb',
    'C -2b -2b': 'Cm2a',
    'A -2c -2c': 'Ac2m',
    #  40
    'A 2 -2a': 'Ama2',
    'B 2 -2b': 'Bbm2',
    'B -2b 2': 'B2mb',
    'C -2c 2': 'C2cm',
    'C -2c -2c': 'Cc2m',
    'A -2a -2a': 'Am2a',
    #  41
    'A 2 -2ac': 'Aba2',
    'B 2 -2bc': 'Bba2',
    'B -2bc 2': 'B2cb',
    'C -2bc 2': 'C2cb',
    'C -2bc -2bc': 'Cc2a',
    'A -2ac -2ac': 'Ac2a',
    #  42
    'F 2 -2': 'Fmm2',
    'F -2 2': 'F2mm',
    'F -2 -2': 'Fm2m',
    #  43
    'F 2 -2d': 'Fdd2',
    'F -2d 2': 'F2dd',
    'F -2d -2d': 'Fd2d',
    #  44
    'I 2 -2': 'Imm2',
    'I -2 2': 'I2mm',
    'I -2 -2': 'Im2m',
    #  45
    'I 2 -2c': 'Iba2',
    'I -2a 2': 'I2cb',
    'I -2b -2b': 'Ic2a',
    #  46
    'I 2 -2a': 'Ima2',
    'I 2 -2b': 'Ibm2',
    'I -2b 2': 'I2mb',
    'I -2c 2': 'I2cm',
    'I -2c -2c': 'Ic2m',
    'I -2a -2a': 'Im2a',
    #  47
    '-P 2 2': 'Pmmm',
    #  48
    'P 2 2 -1n': 'Pnnn:1',
    '-P 2ab 2bc': 'Pnnn:2',
    #  49
    '-P 2 2c': 'Pccm',
    '-P 2a 2': 'Pmaa',
    '-P 2b 2b': 'Pbmb',
    #  50
    'P 2 2 -1ab': 'Pban:1',
    '-P 2ab 2b': 'Pban:2',
    'P 2 2 -1bc': 'Pncb:1',
    '-P 2b 2bc': 'Pncb:2',
    'P 2 2 -1ac': 'Pcna:1',
    '-P 2a 2c': 'Pcna:2',
    #  51
    '-P 2a 2a': 'Pmma',
    '-P 2b 2': 'Pmmb',
    '-P 2 2b': 'Pbmm',
    '-P 2c 2c': 'Pcmm',
    '-P 2c 2': 'Pmcm',
    '-P 2 2a': 'Pmam',
    #  52
    '-P 2a 2bc': 'Pnna',
    '-P 2b 2n': 'Pnnb',
    '-P 2n 2b': 'Pbnn',
    '-P 2ab 2c': 'Pcnn',
    '-P 2ab 2n': 'Pncn',
    '-P 2n 2bc': 'Pnan',
    #  53
    '-P 2ac 2': 'Pmna',
    '-P 2bc 2bc': 'Pnmb',
    '-P 2ab 2ab': 'Pbmn',
    '-P 2 2ac': 'Pcnm',
    '-P 2 2bc': 'Pncm',
    '-P 2ab 2': 'Pman',
    #  54
    '-P 2a 2ac': 'Pcca',
    '-P 2b 2c': 'Pccb',
    '-P 2a 2b': 'Pbaa',
    '-P 2ac 2c': 'Pcaa',
    '-P 2bc 2b': 'Pbcb',
    '-P 2b 2ab': 'Pbab',
    #  55
    '-P 2 2ab': 'Pbam',
    '-P 2bc 2': 'Pmcb',
    '-P 2ac 2ac': 'Pcma',
    #  56
    '-P 2ab 2ac': 'Pccn',
    '-P 2ac 2bc': 'Pnaa',
    '-P 2bc 2ab': 'Pbnb',
    #  57
    '-P 2c 2b': 'Pbcm',
    '-P 2c 2ac': 'Pcam',
    '-P 2ac 2a': 'Pmca',
    '-P 2b 2a': 'Pmab',
    '-P 2a 2ab': 'Pbma',
    '-P 2bc 2c': 'Pcmb',
    #  58
    '-P 2 2n': 'Pnnm',
    '-P 2n 2': 'Pmnn',
    '-P 2n 2n': 'Pnmn',
    #  59
    'P 2 2ab -1ab': 'Pmmn:1',
    '-P 2ab 2a': 'Pmmn:2',
    'P 2bc 2 -1bc': 'Pnmm:1',
    '-P 2c 2bc': 'Pnmm:2',
    'P 2ac 2ac -1ac': 'Pmnm:1',
    '-P 2c 2a': 'Pmnm:2',
    #  60
    '-P 2n 2ab': 'Pbcn',
    '-P 2n 2c': 'Pcan',
    '-P 2a 2n': 'Pnca',
    '-P 2bc 2n': 'Pnab',
    '-P 2ac 2b': 'Pbna',
    '-P 2b 2ac': 'Pcnb',
    #  61
    '-P 2ac 2ab': 'Pbca',
    '-P 2bc 2ac': 'Pcab',
    #  62
    '-P 2ac 2n': 'Pnma',
    '-P 2bc 2a': 'Pmnb',
    '-P 2c 2ab': 'Pbnm',
    '-P 2n 2ac': 'Pcmn',
    '-P 2n 2a': 'Pmcn',
    '-P 2c 2n': 'Pnam',
    #  63
    '-C 2c 2': 'Cmcm',
    '-C 2c 2c': 'Ccmm',
    '-A 2a 2a': 'Amma',
    '-A 2 2a': 'Amam',
    '-B 2 2b': 'Bbmm',
    '-B 2b 2': 'Bmmb',
    #  64
    '-C 2bc 2': 'Cmca',
    '-C 2bc 2bc': 'Ccmb',
    '-A 2ac 2ac': 'Abma',
    '-A 2 2ac': 'Acam',
    '-B 2 2bc': 'Bbcm',
    '-B 2bc 2': 'Bmab',
    #  65
    '-C 2 2': 'Cmmm',
    '-A 2 2': 'Ammm',
    '-B 2 2': 'Bmmm',
    #  66
    '-C 2 2c': 'Cccm',
    '-A 2a 2': 'Amaa',
    '-B 2b 2b': 'Bbmb',
    #  67
    '-C 2b 2': 'Cmma',
    '-C 2b 2b': 'Cmmb',
    '-A 2c 2c': 'Abmm',
    '-A 2 2c': 'Acmm',
    '-B 2 2c': 'Bmcm',
    '-B 2c 2': 'Bmam',
    #  68
    'C 2 2 -1bc': 'Ccca:1',
    '-C 2b 2bc': 'Ccca:2',
    'C 2 2 -1bc': 'Cccb:1',
    '-C 2b 2c': 'Cccb:2',
    'A 2 2 -1ac': 'Abaa:1',
    '-A 2a 2c': 'Abaa:2',
    'A 2 2 -1ac': 'Acaa:1',
    '-A 2ac 2c': 'Acaa:2',
    'B 2 2 -1bc': 'Bbcb:1',
    '-B 2bc 2b': 'Bbcb:2',
    'B 2 2 -1bc': 'Bbab:1',
    '-B 2b 2bc': 'Bbab:2',
    #  69
    '-F 2 2': 'Fmmm',
    #  70
    'F 2 2 -1d': 'Fddd:1',
    '-F 2uv 2vw': 'Fddd:2',
    #  71
    '-I 2 2': 'Immm',
    #  72
    '-I 2 2c': 'Ibam',
    '-I 2a 2': 'Imcb',
    '-I 2b 2b': 'Icma',
    #  73
    '-I 2b 2c': 'Ibca',
    '-I 2a 2b': 'Icab',
    #  74
    '-I 2b 2': 'Imma',
    '-I 2a 2a': 'Immb',
    '-I 2c 2c': 'Ibmm',
    '-I 2 2b': 'Icmm',
    '-I 2 2a': 'Imcm',
    '-I 2c 2': 'Imam',
    #  75
    'P 4': 'P4',
    #  76
    'P 4w': 'P41',
    #  77
    'P 4c': 'P42',
    #  78
    'P 4cw': 'P43',
    #  79
    'I 4': 'I4',
    #  80
    'I 4bw': 'I41',
    #  81
    'P -4': 'P-4',
    #  82
    'I -4': 'I-4',
    #  83
    '-P 4': 'P4/m',
    #  84
    '-P 4c': 'P42/m',
    #  85
    'P 4ab -1ab': 'P4/n:1',
    '-P 4a': 'P4/n:2',
    #  86
    'P 4n -1n': 'P42/n:1',
    '-P 4bc': 'P42/n:2',
    #  87
    '-I 4': 'I4/m',
    #  88
    'I 4bw -1bw': 'I41/a:1',
    '-I 4ad': 'I41/a:2',
    #  89
    'P 4 2': 'P422',
    #  90
    'P 4ab 2ab': 'P4212',
    #  91
    'P 4w 2c': 'P4122',
    #  92
    'P 4abw 2nw': 'P41212',
    #  93
    'P 4c 2': 'P4222',
    #  94
    'P 4n 2n': 'P42212',
    #  95
    'P 4cw 2c': 'P4322',
    #  96
    'P 4nw 2abw': 'P43212',
    #  97
    'I 4 2': 'I422',
    #  98
    'I 4bw 2bw': 'I4122',
    #  99
    'P 4 -2': 'P4mm',
    # 100
    'P 4 -2ab': 'P4bm',
    # 101
    'P 4c -2c': 'P42cm',
    # 102
    'P 4n -2n': 'P42nm',
    # 103
    'P 4 -2c': 'P4cc',
    # 104
    'P 4 -2n': 'P4nc',
    # 105
    'P 4c -2': 'P42mc',
    # 106
    'P 4c -2ab': 'P42bc',
    # 107
    'I 4 -2': 'I4mm',
    # 108
    'I 4 -2c': 'I4cm',
    # 109
    'I 4bw -2': 'I41md',
    # 110
    'I 4bw -2c': 'I41cd',
    # 111
    'P -4 2': 'P-42m',
    # 112
    'P -4 2c': 'P-42c',
    # 113
    'P -4 2ab': 'P-421m',
    # 114
    'P -4 2n': 'P-421c',
    # 115
    'P -4 -2': 'P-4m2',
    # 116
    'P -4 -2c': 'P-4c2',
    # 117
    'P -4 -2ab': 'P-4b2',
    # 118
    'P -4 -2n': 'P-4n2',
    # 119
    'I -4 -2': 'I-4m2',
    # 120
    'I -4 -2c': 'I-4c2',
    # 121
    'I -4 2': 'I-42m',
    # 122
    'I -4 2bw': 'I-42d',
    # 123
    '-P 4 2': 'P4/mmm',
    # 124
    '-P 4 2c': 'P4/mcc',
    # 125
    'P 4 2 -1ab': 'P4/nbm:1',
    '-P 4a 2b': 'P4/nbm:2',
    # 126
    'P 4 2 -1n': 'P4/nnc:1',
    '-P 4a 2bc': 'P4/nnc:2',
    # 127
    '-P 4 2ab': 'P4/mbm',
    # 128
    '-P 4 2n': 'P4/mnc',
    # 129
    'P 4ab 2ab -1ab': 'P4/nmm:1',
    '-P 4a 2a': 'P4/nmm:2',
    # 130
    'P 4ab 2n -1ab': 'P4/ncc:1',
    '-P 4a 2ac': 'P4/ncc:2',
    # 131
    '-P 4c 2': 'P42/mmc',
    # 132
    '-P 4c 2c': 'P42/mcm',
    # 133
    'P 4n 2c -1n': 'P42/nbc:1',
    '-P 4ac 2b': 'P42/nbc:2',
    # 134
    'P 4n 2 -1n': 'P42/nnm:1',
    '-P 4ac 2bc': 'P42/nnm:2',
    # 135
    '-P 4c 2ab': 'P42/mbc',
    # 136
    '-P 4n 2n': 'P42/mnm',
    # 137
    'P 4n 2n -1n': 'P42/nmc:1',
    '-P 4ac 2a': 'P42/nmc:2',
    # 138
    'P 4n 2ab -1n': 'P42/ncm:1',
    '-P 4ac 2ac': 'P42/ncm:2',
    # 139
    '-I 4 2': 'I4/mmm',
    # 140
    '-I 4 2c': 'I4/mcm',
    # 141
    'I 4bw 2bw -1bw': 'I41/amd:1',
    '-I 4bd 2': 'I41/amd:2',
    # 142
    'I 4bw 2aw -1bw': 'I41/acd:1',
    '-I 4bd 2c': 'I41/acd:2',
    # 143
    'P 3': 'P3',
    # 144
    'P 31': 'P31',
    # 145
    'P 32': 'P32',
    # 146
    'R 3': 'R3:H',
    'P 3*': 'R3:R',
    # 147
    '-P 3': 'P-3',
    # 148
    '-R 3': 'R-3:H',
    '-P 3*': 'R-3:R',
    # 149
    'P 3 2': 'P312',
    # 150
    'P 3 2"': 'P321',
    # 151
    'P 31 2c (0 0 1)': 'P3112',
    # 152
    'P 31 2"': 'P3121',
    # 153
    'P 32 2c (0 0 -1)': 'P3212',
    # 154
    'P 32 2"': 'P3221',
    # 155
    'R 3 2"': 'R32:H',
    'P 3* 2': 'R32:R',
    # 156
    'P 3 -2"': 'P3m1',
    # 157
    'P 3 -2': 'P31m',
    # 158
    'P 3 -2"c': 'P3c1',
    # 159
    'P 3 -2c': 'P31c',
    # 160
    'R 3 -2"': 'R3m:H',
    'P 3* -2': 'R3m:R',
    # 161
    'R 3 -2"c': 'R3c:H',
    'P 3* -2n': 'R3c:R',
    # 162
    '-P 3 2': 'P-31m',
    # 163
    '-P 3 2c': 'P-31c',
    # 164
    '-P 3 2"': 'P-3m1',
    # 165
    '-P 3 2"c': 'P-3c1',
    # 166
    '-R 3 2"': 'R-3m:H',
    '-P 3* 2': 'R-3m:R',
    # 167
    '-R 3 2"c': 'R-3c:H',
    '-P 3* 2n': 'R-3c:R',
    # 168
    'P 6': 'P6',
    # 169
    'P 61': 'P61',
    # 170
    'P 65': 'P65',
    # 171
    'P 62': 'P62',
    # 172
    'P 64': 'P64',
    # 173
    'P 6c': 'P63',
    # 174
    'P -6': 'P-6',
    # 175
    '-P 6': 'P6/m',
    # 176
    '-P 6c': 'P63/m',
    # 177
    'P 6 2': 'P622',
    # 178
    'P 61 2 (0 0 -1)': 'P6122',
    # 179
    'P 65 2 (0 0 1)': 'P6522',
    # 180
    'P 62 2c (0 0 1)': 'P6222',
    # 181
    'P 64 2c (0 0 -1)': 'P6422',
    # 182
    'P 6c 2c': 'P6322',
    # 183
    'P 6 -2': 'P6mm',
    # 184
    'P 6 -2c': 'P6cc',
    # 185
    'P 6c -2': 'P63cm',
    # 186
    'P 6c -2c': 'P63mc',
    # 187
    'P -6 2': 'P-6m2',
    # 188
    'P -6c 2': 'P-6c2',
    # 189
    'P -6 -2': 'P-62m',
    # 190
    'P -6c -2c': 'P-62c',
    # 191
    '-P 6 2': 'P6/mmm',
    # 192
    '-P 6 2c': 'P6/mcc',
    # 193
    '-P 6c 2': 'P63/mcm',
    # 194
    '-P 6c 2c': 'P63/mmc',
    # 195
    'P 2 2 3': 'P23',
    # 196
    'F 2 2 3': 'F23',
    # 197
    'I 2 2 3': 'I23',
    # 198
    'P 2ac 2ab 3': 'P213',
    # 199
    'I 2b 2c 3': 'I213',
    # 200
    '-P 2 2 3': 'Pm-3',
    # 201
    'P 2 2 3 -1n': 'Pn-3:1',
    '-P 2ab 2bc 3': 'Pn-3:2',
    # 202
    '-F 2 2 3': 'Fm-3',
    # 203
    'F 2 2 3 -1d': 'Fd-3:1',
    '-F 2uv 2vw 3': 'Fd-3:2',
    # 204
    '-I 2 2 3': 'Im-3',
    # 205
    '-P 2ac 2ab 3': 'Pa-3',
    # 206
    '-I 2b 2c 3': 'Ia-3',
    # 207
    'P 4 2 3': 'P432',
    # 208
    'P 4n 2 3': 'P4232',
    # 209
    'F 4 2 3': 'F432',
    # 210
    'F 4d 2 3': 'F4132',
    # 211
    'I 4 2 3': 'I432',
    # 212
    'P 4acd 2ab 3': 'P4332',
    # 213
    'P 4bd 2ab 3': 'P4132',
    # 214
    'I 4bd 2c 3': 'I4132',
    # 215
    'P -4 2 3': 'P-43m',
    # 216
    'F -4 2 3': 'F-43m',
    # 217
    'I -4 2 3': 'I-43m',
    # 218
    'P -4n 2 3': 'P-43n',
    # 219
    'F -4c 2 3': 'F-43c',
    # 220
    'I -4bd 2c 3': 'I-43d',
    # 221
    '-P 4 2 3': 'Pm-3m',
    # 222
    'P 4 2 3 -1n': 'Pn-3n:1',
    '-P 4a 2bc 3': 'Pn-3n:2',
    # 223
    '-P 4n 2 3': 'Pm-3n',
    # 224
    'P 4n 2 3 -1n': 'Pn-3m:1',
    '-P 4bc 2bc 3': 'Pn-3m:2',
    # 225
    '-F 4 2 3': 'Fm-3m',
    # 226
    '-F 4c 2 3': 'Fm-3c',
    # 227
    'F 4d 2 3 -1d': 'Fd-3m:1',
    '-F 4vw 2vw 3': 'Fd-3m:2',
    # 228
    'F 4d 2 3 -1cd': 'Fd-3c:1',
    '-F 4cvw 2vw 3': 'Fd-3c:2',
    # 229
    '-I 4 2 3': 'Im-3m',
    # 230
    '-I 4bd 2c 3': 'Ia-3d',
    #######################
    # Non-standard settings
    # 1
    'A 1': 'A1',
    'B 1': 'B1',
    'C 1': 'C1',
    'I 1': 'I1',
    'F 1': 'F1',
    # 2
    '-A 1': 'A-1',
    '-B 1': 'B-1',
    '-C 1': 'C-1',
    '-I 1': 'I-1',
    '-F 1': 'F-1',
    # 5
    'F 2': 'F112',
    'F 2x': 'F211',
    'F 2y': 'F121',
    # 8
    'F -2': 'F11m',
    'F -2x': 'Fm11',
    'F -2y': 'F1m1',
    # 9
    'F -2d': 'F11d',
    'F -2yd': 'F1d1',
    'F -2xd': 'Fd11',
    # 12
    '-F 2': 'F112/m',
    '-F 2x': 'F2/m11',
    '-F 2y': 'F12/m1',
    # 15
    'F 2ycuw -1c': 'F12/d1',
    # 70
    '-F 2 2 -1d': 'Fddd:1',
    '-F 2uv 2vw': 'Fddd:2',
    # 139
    '-F 4 2': 'F4/mmm'
}

CrySysNumber = {
    'triclinic': np.arange(1, 3, 1),
    'monoclinic': np.arange(3, 16, 1),
    'orthorhombic': np.arange(16, 75, 1),
    'tetragonal': np.arange(75, 143, 1),
    'trigonal': np.arange(143, 168, 1),
    'hexagonal': np.arange(168, 195, 1),
    'cubic': np.arange(195, 231, 1)
}
