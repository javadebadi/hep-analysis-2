import typing


class Jobs:

	def __init__(
		self,
		acquisition_source: object  = None,
		new_record: object  = None,
		reference_letters: object  = None,
		self_: object  = None,
		) -> None:
		self.acquisition_source = acquisition_source
		self.new_record = new_record
		self.reference_letters = reference_letters
		self.self_ = self_
