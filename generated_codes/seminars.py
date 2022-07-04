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
		return self._source

	@source.setter
	def source(self, source) -> None:
		if source is not None:
			assert len(source) >= 1
			pass
		self._source = source

	@property
	def value(self) -> str:
		return self._value

	@value.setter
	def value(self, value) -> None:
		if value is not None:
			assert len(value) >= 1
			pass
		self._value = value

	def set_from_dict(self, data: dict):
		if data is not None:
			return Abstract(
				source=data.get('source', None),
				value=data.get('value', None),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'source:  '
		s += self.source.__str__() if (self.source is not None) else ''
		s += '\n'
		s += 'value:  '
		s += self.value.__str__() if (self.value is not None) else ''
		s += '\n'
		return s


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
		return self._datetime

	@datetime.setter
	def datetime(self, datetime) -> None:
		if datetime is not None:
			assert len(datetime) >= 1
			pass
		self._datetime = datetime

	@property
	def email(self) -> str:
		return self._email

	@email.setter
	def email(self, email) -> None:
		if email is not None:
			assert len(email) >= 1
			pass
		self._email = email

	@property
	def method(self) -> str:
		return self._method

	@method.setter
	def method(self, method) -> None:
		if method is not None:
			assert len(method) >= 1
			pass
		self._method = method

	@property
	def orcid(self) -> str:
		return self._orcid

	@orcid.setter
	def orcid(self, orcid) -> None:
		if orcid is not None:
			assert len(orcid) >= 1
			pass
		self._orcid = orcid

	@property
	def source(self) -> str:
		return self._source

	@source.setter
	def source(self, source) -> None:
		if source is not None:
			assert len(source) >= 1
			pass
		self._source = source

	@property
	def submission_number(self) -> str:
		return self._submission_number

	@submission_number.setter
	def submission_number(self, submission_number) -> None:
		if submission_number is not None:
			assert len(submission_number) >= 1
			pass
		self._submission_number = submission_number

	def set_from_dict(self, data: dict):
		if data is not None:
			return AcquisitionSource(
				datetime=data.get('datetime', None),
				email=data.get('email', None),
				method=data.get('method', None),
				orcid=data.get('orcid', None),
				source=data.get('source', None),
				submission_number=data.get('submission_number', None),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'datetime:  '
		s += self.datetime.__str__() if (self.datetime is not None) else ''
		s += '\n'
		s += 'email:  '
		s += self.email.__str__() if (self.email is not None) else ''
		s += '\n'
		s += 'method:  '
		s += self.method.__str__() if (self.method is not None) else ''
		s += '\n'
		s += 'orcid:  '
		s += self.orcid.__str__() if (self.orcid is not None) else ''
		s += '\n'
		s += 'source:  '
		s += self.source.__str__() if (self.source is not None) else ''
		s += '\n'
		s += 'submission_number:  '
		s += self.submission_number.__str__() if (self.submission_number is not None) else ''
		s += '\n'
		return s


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
		return self._country_code

	@country_code.setter
	def country_code(self, country_code) -> None:
		if country_code is not None:
			assert len(country_code) >= 2
			assert len(country_code) <= 2
			pass
		self._country_code = country_code

	@property
	def place_name(self) -> str:
		return self._place_name

	@place_name.setter
	def place_name(self, place_name) -> None:
		if place_name is not None:
			assert len(place_name) >= 1
			pass
		self._place_name = place_name

	@property
	def postal_code(self) -> str:
		return self._postal_code

	@postal_code.setter
	def postal_code(self, postal_code) -> None:
		if postal_code is not None:
			assert len(postal_code) >= 1
			pass
		self._postal_code = postal_code

	@property
	def state(self) -> str:
		return self._state

	@state.setter
	def state(self, state) -> None:
		if state is not None:
			assert len(state) >= 1
			pass
		self._state = state

	def set_from_dict(self, data: dict):
		if data is not None:
			return Address(
				country_code=data.get('country_code', None),
				place_name=data.get('place_name', None),
				postal_code=data.get('postal_code', None),
				state=data.get('state', None),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'country_code:  '
		s += self.country_code.__str__() if (self.country_code is not None) else ''
		s += '\n'
		s += 'place_name:  '
		s += self.place_name.__str__() if (self.place_name is not None) else ''
		s += '\n'
		s += 'postal_code:  '
		s += self.postal_code.__str__() if (self.postal_code is not None) else ''
		s += '\n'
		s += 'state:  '
		s += self.state.__str__() if (self.state is not None) else ''
		s += '\n'
		return s


class NewRecord:

	def __init__(
		self,
		ref: str  = None,
		) -> None:
		self.ref = ref

	@property
	def ref(self) -> str:
		return self._ref

	@ref.setter
	def ref(self, ref) -> None:
		if ref is not None:
			assert len(ref) >= 1
			pass
		self._ref = ref

	def set_from_dict(self, data: dict):
		if data is not None:
			return NewRecord(
				ref=data.get('$ref', None),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'ref:  '
		s += self.ref.__str__() if (self.ref is not None) else ''
		s += '\n'
		return s


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
		return self._source

	@source.setter
	def source(self, source) -> None:
		if source is not None:
			assert len(source) >= 1
			pass
		self._source = source

	@property
	def subtitle(self) -> str:
		return self._subtitle

	@subtitle.setter
	def subtitle(self, subtitle) -> None:
		if subtitle is not None:
			assert len(subtitle) >= 1
			pass
		self._subtitle = subtitle

	@property
	def title(self) -> str:
		return self._title

	@title.setter
	def title(self, title) -> None:
		if title is not None:
			assert len(title) >= 1
			pass
		self._title = title

	def set_from_dict(self, data: dict):
		if data is not None:
			return Title(
				source=data.get('source', None),
				subtitle=data.get('subtitle', None),
				title=data.get('title', None),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'source:  '
		s += self.source.__str__() if (self.source is not None) else ''
		s += '\n'
		s += 'subtitle:  '
		s += self.subtitle.__str__() if (self.subtitle is not None) else ''
		s += '\n'
		s += 'title:  '
		s += self.title.__str__() if (self.title is not None) else ''
		s += '\n'
		return s


class Self:

	def __init__(
		self,
		ref: str  = None,
		) -> None:
		self.ref = ref

	@property
	def ref(self) -> str:
		return self._ref

	@ref.setter
	def ref(self, ref) -> None:
		if ref is not None:
			assert len(ref) >= 1
			pass
		self._ref = ref

	def set_from_dict(self, data: dict):
		if data is not None:
			return Self(
				ref=data.get('$ref', None),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'ref:  '
		s += self.ref.__str__() if (self.ref is not None) else ''
		s += '\n'
		return s


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
		return self._abstract

	@abstract.setter
	def abstract(self, abstract) -> None:
		pass
		self._abstract = abstract

	@property
	def acquisition_source(self) -> AcquisitionSource:
		return self._acquisition_source

	@acquisition_source.setter
	def acquisition_source(self, acquisition_source) -> None:
		pass
		self._acquisition_source = acquisition_source

	@property
	def address(self) -> Address:
		return self._address

	@address.setter
	def address(self, address) -> None:
		pass
		self._address = address

	@property
	def captioned(self) -> bool:
		return self._captioned

	@captioned.setter
	def captioned(self, captioned) -> None:
		if captioned is not None:
			pass
		self._captioned = captioned

	@property
	def core(self) -> bool:
		return self._core

	@core.setter
	def core(self, core) -> None:
		if core is not None:
			pass
		self._core = core

	@property
	def deleted(self) -> bool:
		return self._deleted

	@deleted.setter
	def deleted(self, deleted) -> None:
		if deleted is not None:
			pass
		self._deleted = deleted

	@property
	def end_datetime(self) -> str:
		return self._end_datetime

	@end_datetime.setter
	def end_datetime(self, end_datetime) -> None:
		if end_datetime is not None:
			assert len(end_datetime) >= 1
			pass
		self._end_datetime = end_datetime

	@property
	def new_record(self) -> NewRecord:
		return self._new_record

	@new_record.setter
	def new_record(self, new_record) -> None:
		pass
		self._new_record = new_record

	@property
	def start_datetime(self) -> str:
		return self._start_datetime

	@start_datetime.setter
	def start_datetime(self, start_datetime) -> None:
		if start_datetime is not None:
			assert len(start_datetime) >= 1
			pass
		self._start_datetime = start_datetime

	@property
	def timezone(self) -> str:
		return self._timezone

	@timezone.setter
	def timezone(self, timezone) -> None:
		if timezone is not None:
			assert len(timezone) >= 1
			pass
		self._timezone = timezone

	@property
	def title(self) -> Title:
		return self._title

	@title.setter
	def title(self, title) -> None:
		pass
		self._title = title

	@property
	def schema(self) -> str:
		return self._schema

	@schema.setter
	def schema(self, schema) -> None:
		if schema is not None:
			assert len(schema) >= 1
			pass
		self._schema = schema

	@property
	def self_(self) -> Self:
		return self._self_

	@self_.setter
	def self_(self, self_) -> None:
		pass
		self._self_ = self_

	def set_from_dict(self, data: dict):
		if data is not None:
			return Seminars(
				abstract=Abstract().set_from_dict(data=data.get('abstract', None)),
				acquisition_source=AcquisitionSource().set_from_dict(data=data.get('acquisition_source', None)),
				address=Address().set_from_dict(data=data.get('address', None)),
				captioned=data.get('captioned', None),
				core=data.get('core', None),
				deleted=data.get('deleted', None),
				end_datetime=data.get('end_datetime', None),
				new_record=NewRecord().set_from_dict(data=data.get('new_record', None)),
				start_datetime=data.get('start_datetime', None),
				timezone=data.get('timezone', None),
				title=Title().set_from_dict(data=data.get('title', None)),
				schema=data.get('$schema', None),
				self_=Self().set_from_dict(data=data.get('self', None)),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'abstract:  '
		s += self.abstract.__str__() if (self.abstract is not None) else ''
		s += '\n'
		s += 'acquisition_source:  '
		s += self.acquisition_source.__str__() if (self.acquisition_source is not None) else ''
		s += '\n'
		s += 'address:  '
		s += self.address.__str__() if (self.address is not None) else ''
		s += '\n'
		s += 'captioned:  '
		s += self.captioned.__str__() if (self.captioned is not None) else ''
		s += '\n'
		s += 'core:  '
		s += self.core.__str__() if (self.core is not None) else ''
		s += '\n'
		s += 'deleted:  '
		s += self.deleted.__str__() if (self.deleted is not None) else ''
		s += '\n'
		s += 'end_datetime:  '
		s += self.end_datetime.__str__() if (self.end_datetime is not None) else ''
		s += '\n'
		s += 'new_record:  '
		s += self.new_record.__str__() if (self.new_record is not None) else ''
		s += '\n'
		s += 'start_datetime:  '
		s += self.start_datetime.__str__() if (self.start_datetime is not None) else ''
		s += '\n'
		s += 'timezone:  '
		s += self.timezone.__str__() if (self.timezone is not None) else ''
		s += '\n'
		s += 'title:  '
		s += self.title.__str__() if (self.title is not None) else ''
		s += '\n'
		s += 'schema:  '
		s += self.schema.__str__() if (self.schema is not None) else ''
		s += '\n'
		s += 'self_:  '
		s += self.self_.__str__() if (self.self_ is not None) else ''
		s += '\n'
		return s
