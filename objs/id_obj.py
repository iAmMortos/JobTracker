
import uuid


class IdObj(object):
  def __init__(self, uuid=None):
    self._uuid = uuid.uuid4() if not uuid else uuid

  @property
  def uuid(self):
    return self._uuid

  @property
  def display_name(self):
    return self._uuid
