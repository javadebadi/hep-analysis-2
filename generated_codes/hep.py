import typing


class Hep:

	def __init__(
		self,
		acquisition_source: object  = None,
		new_record: object  = None,
		thesis_info: object  = None,
		export_to: object  = None,
		self_: object  = None,
		) -> None:
		self.acquisition_source = acquisition_source
		self.new_record = new_record
		self.thesis_info = thesis_info
		self.export_to = export_to
		self.self_ = self_
