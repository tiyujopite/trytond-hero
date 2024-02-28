from trytond.pool import Pool
from . import hero


def register():
    Pool.register(
        hero.Hero,
        module='hero', type_='model')
