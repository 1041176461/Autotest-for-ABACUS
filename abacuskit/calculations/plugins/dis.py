'''
Date: 2021-04-28 21:26:54
LastEditors: jiyuyang
LastEditTime: 2021-05-06 16:17:30
Mail: jiyuyang@mail.ustc.edu.cn, 1041176461@qq.com
'''
distance = {
    "H":	[	0.6,	0.75,	0.9,	1.2,	1.5	],
    "He":	[	1.25,	1.75,	2.4,	3.25	],
    "Li":	[	1.5,	2.1,	2.5,	2.8,	3.2,	3.5,	4.2	],
    "Be":	[	1.75,	2,	2.375,	3,	4	],
    "B":	[	1.25,	1.625,	2.5,	3.5	],
    "C":	[	1,	1.25,	1.5,	2,	3	],
    "N":	[	1,	1.1,	1.5,	2,	3	],
    "O":	[	1,	1.208,	1.5,	2,	3	],
    "F":	[	1.2,	1.418,	1.75,	2.25,	3.25	],
    "Ne":	[	1.5,	1.75,	2.25,	2.625,	3,	3.5	],
    "Na":	[	2.05,	2.4,	2.8,	3.1,	3.3,	3.8,	4.3	],
    "Mg":	[	2.125,	2.375,	2.875,	3.375,	4.5	],
    "Al":	[	2,	2.5,	3,	3.75,	4.5	],
    "Si":	[	1.75,	2,	2.25,	2.75,	3.75	],
    "P":	[	1.625,	1.875,	2.5,	3.25,	4	],
    "S":	[	1.6,	1.9,	2.5,	3.25,	4	],
    "Cl":	[	1.65,	2,	2.5,	3.25,	4	],
    "Ar":	[	2.25,	2.625,	3,	3.375,	4	],
    "K":	[	1.8,	2.6,	3.4,	3.8,	4,	4.4,	4.8	],
    "Ca":	[	2.5,	3,	3.5,	4,	5	],
    "Sc":	[	1.75,	2.15,	2.75,	3.5,	4.5	],
    "Ti":	[	1.6,	1.85,	2.5,	3.25,	4.25	],
    "V":	[	1.45,	1.65,	2.25,	3,	4	],
    "Cr":	[	1.375,	1.55,	2,	2.75,	3.75	],
    "Mn":	[	1.4,	1.6,	2.1,	2.75,	3.75	],
    "Fe":	[	1.45,	1.725,	2.25,	3,	4	],
    "Co":	[	1.8,	2,	2.5,	3.5	],
    "Ni":	[	1.65,	2,	2.5,	3,	4	],
    "Cu":	[	1.8,	2.2,	3,	4	],
    "Zn":	[	2,	2.3,	2.85,	3.5,	4.25	],
    "Ga":	[	1.85,	2.1,	2.45,	3,	4	],
    "Ge":	[	1.8,	2,	2.35,	3,	4	],
    "As":	[	1.75,	2.1,	2.5,	3,	4	],
    "Se":	[	1.85,	2.15,	2.5,	3,	4	],
    "Br":	[	1.9,	2.25,	2.75,	3.25,	4	],
    "Kr":	[	2.4,	3,	3.675,	4.25,	5	],
    "Rb":	[	2.45,	3,	4,	5	],
    "Sr":	[	2.75,	3.5,	4.4,	5	],
    "Y":	[	2.125,	2.5,	2.875,	3.25,	4,	5	],
    "Zr":	[	1.9,	2.25,	3,	4	],
    "Nb":	[	1.75,	2.05,	2.4,	3,	4	],
    "Mo":	[	1.675,	1.9,	2.375,	3,	4	],
    "Tc":	[	1.7,	1.915,	2.375,	3,	4	],
    "Ru":	[	1.725,	1.925,	2.375,	3,	4	],
    "Rh":	[	1.8,	2.1,	2.5,	3,	4	],
    "Pd":	[	2,	2.275,	2.75,	3.75	],
    "Ag":	[	2.1,	2.45,	3,	4	],
    "Cd":	[	2.15,	2.5,	3.1,	4,	5	],
    "In":	[	2.15,	2.5,	3,	3.75,	4.75	],
    "Sn":	[	2.1,	2.4,	3.75,	3.5,	4.5	],
    "Sb":	[	2.1,	2.5,	3,	3.5,	4.5	],
    "Te":	[	2.15,	2.55,	3.1,	3.6,	4.5	],
    "I":	[	2.22,	2.65,	3.25,	4.25	],
    "Xe":	[	3,	3.5,	4.06,	4.5,	5.25	],
    "Cs":	[	2.7,	3.5,	4.5,	5.5	],
    "Ba":	[	2.65,	3,	3.5,	4.4,	5.5	],
    "La":	[	2.2,	2.6,	3.25,	4,	5	],
    "Ce":	[	2,	2.375,	2.875,	3.5,	4.5	],
    "Pr":	[	1.9,	2.25,	2.75,	3.5,	4.5	],
    "Nd":	[	1.8,	2.125,	2.625,	3.375,	4.5	],
    "Pm":	[	1.775,	2.05,	2.5,	3.25,	4.25	],
    "Sm":	[	1.775,	2.05,	2.5,	3.25,	4.25	],
    "Eu":	[	1.775,	2.075,	2.5,	3.25,	4.25	],
    "Gd":	[	1.8,	2.11,	2.625,	3.375,	4.1,	5	],
    "Tb":	[	1.825,	2.16,	2.625,	3.375,	4.1,	5	],
    "Dy":	[	1.85,	2.24,	2.625,	3.375,	4.1,	5	],
    "Ho":	[	1.93,	2.375,	3,	4.1,	5	],
    "Er":	[	2.025,	2.5,	3.125,	4.1,	5	],
    "Tm":	[	2.2,	2.625,	3.25,	4.1,	5	],
    "Yb":	[	2.5,	3,	3.5,	4.1,	5	],
    "Lu":	[	2.2,	2.5,	3.04,	4,	5	],
    "Hf":	[	1.975,	2.49,	3.25,	4.5	],
    "Ta":	[	1.85,	2.12,	2.625,	3.25,	4.5	],
    "W":	[	1.775,	1.99,	2.5,	3.25,	4.5	],
    "Re":	[	1.775,	2.01,	2.5,	3.25,	4.25	],
    "Os":	[	1.8,	2.04,	2.5,	3.25,	4.5	],
    "Ir":	[	1.85,	2.125,	2.5,	3.25,	4.25	],
    "Pt":	[	2,	2.275,	2.75,	3.75	],
    "Au":	[	2.1,	2.45,	3,	4	],
    "Hg":	[	2.225,	2.5,	3.04,	4,	5	],
    "Tl":	[	2.21,	2.6,	3.11,	3.75,	4.75	],
    "Pb":	[	2.225,	2.5,	2.88,	3.625,	4.5	],
    "Bi":	[	2.225,	2.61,	3.125,	3.75,	4.75	],
    "Po":	[	2.3,	2.72,	3.25,	3.875,	4.75	],
    "At":	[	2.375,	2.83,	3.5,	4.5	],
    "Rn":	[	2.8,	3.5,	4.17,	4.75,	5.5	],
    "Fr":	[	2.85,	3.5,	4.43,	5.5	],
    "Ra":	[	3.15,	3.5,	4.25,	5.12,	6	],
    "Ac":	[	2.48,	3.1,	3.72,	4.25,	5	],
    "Th":	[	2.25,	2.65,	3.25,	4,	5	],
    "Pa":	[	2.04,	2.3,	3,	3.75,	4.75	],
    "U":	[	1.89,	2.09,	2.75,	3.5,	4.5	],
    "Np":	[	1.84,	2.05,	2.625,	3.375,	4.5	],
    "Pu":	[	1.81,	2.02,	2.5,	3.25,	4.25	],
    "Am":	[	1.81,	2.03,	2.5,	3.25,	4.25	],
    "Cm":	[	1.83,	2.07,	2.5,	3.25,	4.25	],
    "Bk":	[	1.86,	2.12,	2.5,	3,	4	],
    "Cf":	[	1.89,	2.19,	2.625,	3.125,	4	],
    "Es":	[	1.93,	2.29,	2.625,	3.125,	4	],
    "Fm":	[	1.98,	2.375,	2.75,	3.25,	4.25	],
    "Md":	[	2.08,	2.5,	3,	3.43,	4.25	],
    "No":	[	2.6,	3.125,	3.75,	4.27,	5	]
}