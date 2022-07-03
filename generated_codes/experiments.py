import typing


class Experiments:

	def __init__(
		self,
		accelerator: object  = None,
		collaboration: object  = None,
		experiment: object  = None,
		new_record: object  = None,
		self_: object  = None,
		) -> None:
		self.accelerator = accelerator
		self.collaboration = collaboration
		self.experiment = experiment
		self.new_record = new_record
		self.self_ = self_
