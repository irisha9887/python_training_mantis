from sys import maxsize


class Project:

    def __init__(self, name=None, status=None, view_state=None, inherit_global=None, description=None, id=None):
        self.name = name
        self.status = status
        self.view_state = view_state
        self.inherit_global = inherit_global
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.name, self.status, self.view_state, self.inherit_global, self.description)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and\
        self.status == other.status and self.view_state == other.view_state and\
        self.inherit_global == other.inherit_global and self.description == other.description

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize