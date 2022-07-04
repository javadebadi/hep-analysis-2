import typing


class Abstract:

	def __init__(
		self,
		source: str  = None,
		value: str  = None,
		) -> None:
		self.source = source
		self.value = value

	@property
	def source(self) -> str:
		return self.source

	@source.setter
	def source(self, source) -> None:
		assert len(source) >= 1
		self._source = source

	@property
	def value(self) -> str:
		return self.value

	@value.setter
	def value(self, value) -> None:
		assert len(value) >= 1
		self._value = value



class AcquisitionSource:

	def __init__(
		self,
		datetime: str  = None,
		email: str  = None,
		method: str  = None,
		orcid: str  = None,
		source: str  = None,
		submission_number: str  = None,
		) -> None:
		self.datetime = datetime
		self.email = email
		self.method = method
		self.orcid = orcid
		self.source = source
		self.submission_number = submission_number

	@property
	def datetime(self) -> str:
		return self.datetime

	@datetime.setter
	def datetime(self, datetime) -> None:
		assert len(datetime) >= 1
		self._datetime = datetime

	@property
	def email(self) -> str:
		return self.email

	@email.setter
	def email(self, email) -> None:
		assert len(email) >= 1
		self._email = email

	@property
	def method(self) -> str:
		return self.method

	@method.setter
	def method(self, method) -> None:
		assert len(method) >= 1
		self._method = method

	@property
	def orcid(self) -> str:
		return self.orcid

	@orcid.setter
	def orcid(self, orcid) -> None:
		assert len(orcid) >= 1
		self._orcid = orcid

	@property
	def source(self) -> str:
		return self.source

	@source.setter
	def source(self, source) -> None:
		assert len(source) >= 1
		self._source = source

	@property
	def submission_number(self) -> str:
		return self.submission_number

	@submission_number.setter
	def submission_number(self, submission_number) -> None:
		assert len(submission_number) >= 1
		self._submission_number = submission_number



class Address:

	def __init__(
		self,
		country_code: str  = None,
		place_name: str  = None,
		postal_code: str  = None,
		state: str  = None,
		) -> None:
		self.country_code = country_code
		self.place_name = place_name
		self.postal_code = postal_code
		self.state = state

	@property
	def country_code(self) -> str:
		return self.country_code

	@country_code.setter
	def country_code(self, country_code) -> None:
		assert len(country_code) >= 2
		assert len(country_code) <= 2
		self._country_code = country_code

	@property
	def place_name(self) -> str:
		return self.place_name

	@place_name.setter
	def place_name(self, place_name) -> None:
		assert len(place_name) >= 1
		self._place_name = place_name

	@property
	def postal_code(self) -> str:
		return self.postal_code

	@postal_code.setter
	def postal_code(self, postal_code) -> None:
		assert len(postal_code) >= 1
		self._postal_code = postal_code

	@property
	def state(self) -> str:
		return self.state

	@state.setter
	def state(self, state) -> None:
		assert len(state) >= 1
		self._state = state



class NewRecord:

	def __init__(
		self,
		ref: str  = None,
		) -> None:
		self.ref = ref

	@property
	def ref(self) -> str:
		return self.ref

	@ref.setter
	def ref(self, ref) -> None:
		assert len(ref) >= 1
		self._ref = ref



class Title:

	def __init__(
		self,
		source: str  = None,
		subtitle: str  = None,
		title: str  = None,
		) -> None:
		self.source = source
		self.subtitle = subtitle
		self.title = title

	@property
	def source(self) -> str:
		return self.source

	@source.setter
	def source(self, source) -> None:
		assert len(source) >= 1
		self._source = source

	@property
	def subtitle(self) -> str:
		return self.subtitle

	@subtitle.setter
	def subtitle(self, subtitle) -> None:
		assert len(subtitle) >= 1
		self._subtitle = subtitle

	@property
	def title(self) -> str:
		return self.title

	@title.setter
	def title(self, title) -> None:
		assert len(title) >= 1
		self._title = title



class Self:

	def __init__(
		self,
		ref: str  = None,
		) -> None:
		self.ref = ref

	@property
	def ref(self) -> str:
		return self.ref

	@ref.setter
	def ref(self, ref) -> None:
		assert len(ref) >= 1
		self._ref = ref



class Seminars:

	def __init__(
		self,
		abstract: Abstract  = None,
		acquisition_source: AcquisitionSource  = None,
		address: Address  = None,
		captioned: bool  = None,
		core: bool  = None,
		deleted: bool  = None,
		end_datetime: str  = None,
		new_record: NewRecord  = None,
		start_datetime: str  = None,
		timezone: str  = None,
		title: Title  = None,
		schema: str  = None,
		self_: Self  = None,
		) -> None:
		self.abstract = abstract
		self.acquisition_source = acquisition_source
		self.address = address
		self.captioned = captioned
		self.core = core
		self.deleted = deleted
		self.end_datetime = end_datetime
		self.new_record = new_record
		self.start_datetime = start_datetime
		self.timezone = timezone
		self.title = title
		self.schema = schema
		self.self_ = self_

	@property
	def abstract(self) -> Abstract:
		return self.abstract

	@property
	def acquisition_source(self) -> AcquisitionSource:
		return self.acquisition_source

	@property
	def address(self) -> Address:
		return self.address

	@property
	def captioned(self) -> bool:
		return self.captioned

	@captioned.setter
	def captioned(self, captioned) -> None:
		self._captioned = captioned

	@property
	def core(self) -> bool:
		return self.core

	@core.setter
	def core(self, core) -> None:
		self._core = core

	@property
	def deleted(self) -> bool:
		return self.deleted

	@deleted.setter
	def deleted(self, deleted) -> None:
		self._deleted = deleted

	@property
	def end_datetime(self) -> str:
		return self.end_datetime

	@end_datetime.setter
	def end_datetime(self, end_datetime) -> None:
		assert len(end_datetime) >= 1
		self._end_datetime = end_datetime

	@property
	def new_record(self) -> NewRecord:
		return self.new_record

	@property
	def start_datetime(self) -> str:
		return self.start_datetime

	@start_datetime.setter
	def start_datetime(self, start_datetime) -> None:
		assert len(start_datetime) >= 1
		self._start_datetime = start_datetime

	@property
	def timezone(self) -> str:
		return self.timezone

	@timezone.setter
	def timezone(self, timezone) -> None:
		assert len(timezone) >= 1
		self._timezone = timezone

	@property
	def title(self) -> Title:
		return self.title

	@property
	def schema(self) -> str:
		return self.schema

	@schema.setter
	def schema(self, schema) -> None:
		assert len(schema) >= 1
		self._schema = schema

	@property
	def self_(self) -> Self:
		return self.self_

