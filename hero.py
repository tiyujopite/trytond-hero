from trytond.model import ModelSQL, ModelView, fields, avatar_mixin


class Hero(avatar_mixin(250), ModelSQL, ModelView):
    "Hero"
    __name__ = 'hero'

    name = fields.Char("Name", required=True)
    party = fields.Many2One('party.party', "Party", required=True)
    tagline = fields.Text("Tagline")

    @classmethod
    def __setup__(cls):
        super().__setup__()
        cls._buttons.update({
                'search_avatar': {}
                })

    @classmethod
    @ModelView.button
    def search_avatar(cls, heroes):
        pass
