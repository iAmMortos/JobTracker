
from objs.id_obj import IdObj


class Job (IdObj):
  def __init__(self, job_name, job_number, uuid=None):
    super.__init__(uuid)
    self._job_name = job_name
    self._job_number = job_number

  @property
  def job_name(self):
    return self._job_name

  @job_name.setter
  def job_name(self, val):
    self._job_name = val

  @property
  def job_number(self):
    return self._job_number

  @job_number.setter
  def job_number(self, val):
    self._job_number = val

  @property
  def display_name(self):
    return self._job_name
