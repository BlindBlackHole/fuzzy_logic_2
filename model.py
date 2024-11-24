input_lvs = [
    {
        'X': (0, 10, 1),
        'name': 'Proximity to Center',
        'terms': {
            'very close': {'umf': ('trapmf', 0, 0, 0.55, 4.61), 'lmf': ('trapmf', 0, 0, 0.09, 1.15, 1)},
            'close': {'umf': ('trapmf', 0.42, 2.25, 4.00, 5.41), 'lmf': ('trapmf', 2.79, 3.21, 3.21, 0.34, 3.71)},
            'moderately distant': {'umf': ('trapmf', 3.38, 5.50, 7.25, 9.02), 'lmf': ('trapmf', 5.79, 6.28, 6.28, 0.33, 6.67)},
            'far': {'umf': ('trapmf', 7.37, 9.36, 10, 10), 'lmf': ('trapmf', 8.68, 9.91, 10, 10, 1)},
        }
    },

    {
        'X': (0, 200, 1),
        'name': 'Area',
        'terms': {
            'low': {'umf': ('trapmf', 0, 0, 0.55, 4.61), 'lmf': ('trapmf', 0, 0, 0.09, 1.15, 1)},
            'medium': {'umf': ('trapmf', 0.42, 2.25, 4.00, 5.41), 'lmf': ('trapmf', 2.79, 3.21, 3.21, 0.34, 3.71)},
            'high': {'umf': ('trapmf', 3.38, 5.50, 7.25, 9.02), 'lmf': ('trapmf', 5.79, 6.28, 6.28, 0.33, 6.67)},
            'extremely high': {'umf': ('trapmf', 7.37, 9.36, 10, 10), 'lmf': ('trapmf', 8.68, 9.91, 10, 10, 1)},
        }
    },

    {
        'X': (1950, 2024, 1),
        'name': 'Modernity',
        'terms': {
            'very old': {'umf': ('trapmf', 0, 0, 0.55, 4.61), 'lmf': ('trapmf', 0, 0, 0.09, 1.15, 1)},
            'old': {'umf': ('trapmf', 0.42, 2.25, 4.00, 5.41), 'lmf': ('trapmf', 2.79, 3.21, 3.21, 0.34, 3.71)},
            'moderately outdated': {'umf': ('trapmf', 3.38, 5.50, 7.25, 9.02), 'lmf': ('trapmf', 5.79, 6.28, 6.28, 0.33, 6.67)},
            'new': {'umf': ('trapmf', 7.37, 9.36, 10, 10), 'lmf': ('trapmf', 8.68, 9.91, 10, 10, 1)},
        }
    }
]

output_lv = {
    'X': (10000, 1000000, 5000),
    'name': 'Cost',
    'terms': {
        'low': {'umf': ('trapmf', 0, 0, 0.55, 4.61), 'lmf': ('trapmf', 0, 0, 0.09, 1.15, 1)},
        'medium': {'umf': ('trapmf', 0.42, 2.25, 4.00, 5.41), 'lmf': ('trapmf', 2.79, 3.21, 3.21, 0.34, 3.71)},
        'high': {'umf': ('trapmf', 3.38, 5.50, 7.25, 9.02), 'lmf': ('trapmf', 5.79, 6.28, 6.28, 0.33, 6.67)},
        'extremely high': {'umf': ('trapmf', 7.37, 9.36, 10, 10), 'lmf': ('trapmf', 8.68, 9.91, 10, 10, 1)},
    }
}

rule_base = [
    (('very close', 'extremely high', 'new'), 'extremely high'),
    (('very close', 'high', 'new'), 'extremely high'),
    (('very close', 'medium', 'new'), 'high'),
    (('very close', 'low', 'new'), 'medium'),
    (('very close', 'extremely high', 'moderately outdated'), 'high'),
    (('very close', 'high', 'moderately outdated'), 'high'),
    (('very close', 'medium', 'moderately outdated'), 'medium'),
    (('very close', 'low', 'moderately outdated'), 'medium'),
    (('very close', 'extremely high', 'old'), 'high'),
    (('very close', 'high', 'old'), 'medium'),
    (('very close', 'medium', 'old'), 'medium'),
    (('very close', 'low', 'old'), 'medium'),
    (('very close', 'extremely high', 'very old'), 'medium'),
    (('very close', 'high', 'very old'), 'medium'),
    (('very close', 'medium', 'very old'), 'medium'),
    (('very close', 'low', 'very old'), 'low'),

    (('close', 'extremely high', 'high'), 'extremely high'),
    (('close', 'high', 'new'), 'high'),
    (('сlose', 'medium', 'new'), 'high'),
    (('close', 'low', 'new'), 'medium'),
    (('close', 'extremely high', 'moderately outdated'), 'extremely high'),
    (('close', 'high', 'moderately outdated'), 'high'),
    (('close', 'medium', 'moderately outdated'), 'high'),
    (('close', 'low', 'moderately outdated'), 'medium'),
    (('close', 'extremely high', 'old'), 'high'),
    (('close', 'high', 'old'), 'medium'),
    (('close', 'medium', 'old'), 'medium'),
    (('close', 'low', 'old'), 'low'),
    (('close', 'extremely high', 'very old'), 'medium'),
    (('close', 'high', 'very old'), 'medium'),
    (('close', 'medium', 'very old'), 'low'),
    (('close', 'low', 'very old'), 'low'),

    (('moderately distant', 'extremely high', 'new'), 'high'),
    (('moderately distant', 'high', 'new'), 'high'),
    (('moderately distant', 'medium', 'new'), 'high'),
    (('moderately distant', 'low', 'new'), 'medium'),
    (('moderately distant', 'extremely high', 'moderately outdated'), 'extremely high'),
    (('moderately distant', 'high', 'moderately outdated'), 'medium'),
    (('moderately distant', 'medium', 'moderately outdated'), 'medium'),
    (('moderately distant', 'low', 'moderately outdated'), 'low'),
    (('moderately distant', 'extremely high', 'old'), 'medium'),
    (('moderately distant', 'high', 'old'), 'medium'),
    (('moderately distant', 'medium', 'old'), 'low'),
    (('moderately distant', 'low', 'old'), 'low'),
    (('moderately distant', 'extremely high', 'very old'), 'medium'),
    (('moderately distant', 'high', 'very old'), 'low'),
    (('moderately distant', 'medium', 'very old'), 'low'),
    (('moderately distant', 'low', 'very old'), 'low'),

    (('far', 'extremely high', 'new'), 'high'),
    (('far', 'high', 'new'), 'medium'),
    (('far', 'medium', 'new'), 'medium'),
    (('far', 'low', 'new'), 'medium'),
    (('far', 'extremely high', 'moderately outdated'), 'medium'),
    (('far', 'high', 'moderately outdated'), 'medium'),
    (('far', 'medium', 'moderately outdated'), 'low'),
    (('far', 'low', 'moderately outdated'), 'low'),
    (('far', 'extremely high', 'old'), 'medium'),
    (('far', 'high', 'old'), 'low'),
    (('far', 'medium', 'old'), 'low'),
    (('far', 'low', 'old'), 'low'),
    (('far', 'extremely high', 'very old'), 'low'),
    (('far', 'high', 'very old'), 'low'),
    (('far', 'medium', 'very old'), 'low'),
    (('far', 'low', 'very old'), 'low'),
]
