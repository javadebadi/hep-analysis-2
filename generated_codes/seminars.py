import typing


class Seminars:

	def __init__(
		self,
		abstract: object  = None,
		acquisition_source: object  = None,
		address: object  = None,
		new_record: object  = None,
		title: object  = None,
		self_: object  = None,
		) -> None:
		self.abstract = abstract
		self.acquisition_source = acquisition_source
		self.address = address
		self.new_record = new_record
		self.title = title
		self.self_ = self_
