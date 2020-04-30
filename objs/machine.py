
from objs.id_obj import IdObj


class Machine (IdObj):
  def __init__(self, machine_id, machine_type, model, uuid=None):
    super.__init__(uuid)
    self._machine_id = machine_id
    self._type = machine_type
    self._model = model
    self._is_rental = False
    self._assigned_job_id = None

  @property
  def machine_id(self):
    return self._machine_id

  @machine_id.setter
  def machine_id(self, val):
    self._machine_id = val

  @property
  def type(self):
    return self._type

  @type.setter
  def type(self, val):
    self._type = val

  @property
  def model(self):
    return self._model

  @model.setter
  def model(self, val):
    self._model = val

  @property
  def is_rental(self):
    return self._is_rental

  @is_rental.setter
  def is_rental(self, val):
    self._is_rental = val

  @property
  def assigned_job_id(self):
    return self._assigned_job_id

  @assigned_job_id.setter
  def assigned_job_id(self, val):
    self._assigned_job_id = val
