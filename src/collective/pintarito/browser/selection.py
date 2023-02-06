from plone import api
from plone.app.layout.viewlets import ViewletBase


class SelectionViewlet(ViewletBase):
    @property
    def selection(self):
        return api.portal.get_registry_record(
            "pintarito.settings.selection", default="red"
        )
