
from objs.id_obj import IdObj


class Employee (IdObj):
  def __init__(self, first_name, last_name, uuid=None):
    super.__init__(uuid)
    self._first_name = first_name
    self._last_name = last_name
    self._assigned_job_id = None
    self._phone_number = None

  @property
  def first_name(self):
    return self._first_name

  @first_name.setter
  def first_name(self, val):
    self._first_name = val

  @property
  def last_name(self):
    return self._last_name

  @last_name.setter
  def last_name(self, val):
    self.last_name = val

  @property
  def full_name(self):
    return '{} {}'.format(self._first_name, self._last_name)

  @property
  def assigned_job_id(self):
    return self._assigned_job_id

  @assigned_job_id.setter
  def assigned_job_id(self, val):
    self._assigned_job_id = val

  @property
  def phone_number(self):
    return self._phone_number

  @phone_number.setter
  def phone_number(self, val):
    self._phone_number = val

  @property
  def display_name(self):
    return self.full_name
