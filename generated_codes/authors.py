import typing


class Authors:

	def __init__(
		self,
		acquisition_source: object  = None,
		name: object  = None,
		new_record: object  = None,
		self_: object  = None,
		) -> None:
		self.acquisition_source = acquisition_source
		self.name = name
		self.new_record = new_record
		self.self_ = self_
