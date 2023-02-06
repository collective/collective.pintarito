from collective.pintarito import _
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class SelectionsVocabulary:
    voc = SimpleVocabulary(
        [
            SimpleTerm(value=key, token=key, title=value)
            for key, value in {
                "default": _("Default"),
                "red": _("Red"),
                "green": _("Green"),
                "blue": _("Blue"),
                "yellow": _("Yellow"),
                "orange": _("Orange"),
                "purple": _("Purple"),
            }.items()
        ]
    )

    def __call__(self, context=None):
        return self.voc


selections_factory = SelectionsVocabulary()
