import typing


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



class Name:

	def __init__(
		self,
		numeration: str  = None,
		preferred_name: str  = None,
		title: str  = None,
		value: str  = None,
		) -> None:
		self.numeration = numeration
		self.preferred_name = preferred_name
		self.title = title
		self.value = value

	@property
	def numeration(self) -> str:
		return self.numeration

	@numeration.setter
	def numeration(self, numeration) -> None:
		assert len(numeration) >= 1
		self._numeration = numeration

	@property
	def preferred_name(self) -> str:
		return self.preferred_name

	@preferred_name.setter
	def preferred_name(self, preferred_name) -> None:
		assert len(preferred_name) >= 1
		self._preferred_name = preferred_name

	@property
	def title(self) -> str:
		return self.title

	@title.setter
	def title(self, title) -> None:
		assert len(title) >= 1
		self._title = title

	@property
	def value(self) -> str:
		return self.value

	@value.setter
	def value(self, value) -> None:
		assert len(value) >= 1
		self._value = value



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



class Authors:

	def __init__(
		self,
		acquisition_source: AcquisitionSource  = None,
		birth_date: str  = None,
		death_date: str  = None,
		deleted: bool  = None,
		legacy_creation_date: str  = None,
		legacy_version: str  = None,
		name: Name  = None,
		new_record: NewRecord  = None,
		status: str  = None,
		stub: bool  = None,
		schema: str  = None,
		bucket: str  = None,
		self_: Self  = None,
		) -> None:
		self.acquisition_source = acquisition_source
		self.birth_date = birth_date
		self.death_date = death_date
		self.deleted = deleted
		self.legacy_creation_date = legacy_creation_date
		self.legacy_version = legacy_version
		self.name = name
		self.new_record = new_record
		self.status = status
		self.stub = stub
		self.schema = schema
		self.bucket = bucket
		self.self_ = self_

	@property
	def acquisition_source(self) -> AcquisitionSource:
		return self.acquisition_source

	@property
	def birth_date(self) -> str:
		return self.birth_date

	@birth_date.setter
	def birth_date(self, birth_date) -> None:
		assert len(birth_date) >= 1
		self._birth_date = birth_date

	@property
	def death_date(self) -> str:
		return self.death_date

	@death_date.setter
	def death_date(self, death_date) -> None:
		assert len(death_date) >= 1
		self._death_date = death_date

	@property
	def deleted(self) -> bool:
		return self.deleted

	@deleted.setter
	def deleted(self, deleted) -> None:
		self._deleted = deleted

	@property
	def legacy_creation_date(self) -> str:
		return self.legacy_creation_date

	@legacy_creation_date.setter
	def legacy_creation_date(self, legacy_creation_date) -> None:
		assert len(legacy_creation_date) >= 1
		self._legacy_creation_date = legacy_creation_date

	@property
	def legacy_version(self) -> str:
		return self.legacy_version

	@legacy_version.setter
	def legacy_version(self, legacy_version) -> None:
		assert len(legacy_version) >= 1
		self._legacy_version = legacy_version

	@property
	def name(self) -> Name:
		return self.name

	@property
	def new_record(self) -> NewRecord:
		return self.new_record

	@property
	def status(self) -> str:
		return self.status

	@status.setter
	def status(self, status) -> None:
		assert len(status) >= 1
		self._status = status

	@property
	def stub(self) -> bool:
		return self.stub

	@stub.setter
	def stub(self, stub) -> None:
		self._stub = stub

	@property
	def schema(self) -> str:
		return self.schema

	@schema.setter
	def schema(self, schema) -> None:
		assert len(schema) >= 1
		self._schema = schema

	@property
	def bucket(self) -> str:
		return self.bucket

	@bucket.setter
	def bucket(self, bucket) -> None:
		assert len(bucket) >= 1
		self._bucket = bucket

	@property
	def self_(self) -> Self:
		return self.self_

