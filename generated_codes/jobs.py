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



class ReferenceLetters:

	def __init__(
		self,
		) -> None:
		pass



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



class Jobs:

	def __init__(
		self,
		acquisition_source: AcquisitionSource  = None,
		deadline_date: str  = None,
		deleted: bool  = None,
		description: str  = None,
		external_job_identifier: str  = None,
		legacy_creation_date: str  = None,
		legacy_version: str  = None,
		new_record: NewRecord  = None,
		position: str  = None,
		reference_letters: ReferenceLetters  = None,
		status: str  = None,
		schema: str  = None,
		bucket: str  = None,
		self_: Self  = None,
		) -> None:
		self.acquisition_source = acquisition_source
		self.deadline_date = deadline_date
		self.deleted = deleted
		self.description = description
		self.external_job_identifier = external_job_identifier
		self.legacy_creation_date = legacy_creation_date
		self.legacy_version = legacy_version
		self.new_record = new_record
		self.position = position
		self.reference_letters = reference_letters
		self.status = status
		self.schema = schema
		self.bucket = bucket
		self.self_ = self_

	@property
	def acquisition_source(self) -> AcquisitionSource:
		return self.acquisition_source

	@property
	def deadline_date(self) -> str:
		return self.deadline_date

	@deadline_date.setter
	def deadline_date(self, deadline_date) -> None:
		assert len(deadline_date) >= 1
		self._deadline_date = deadline_date

	@property
	def deleted(self) -> bool:
		return self.deleted

	@deleted.setter
	def deleted(self, deleted) -> None:
		self._deleted = deleted

	@property
	def description(self) -> str:
		return self.description

	@description.setter
	def description(self, description) -> None:
		assert len(description) >= 1
		self._description = description

	@property
	def external_job_identifier(self) -> str:
		return self.external_job_identifier

	@external_job_identifier.setter
	def external_job_identifier(self, external_job_identifier) -> None:
		assert len(external_job_identifier) >= 1
		self._external_job_identifier = external_job_identifier

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
	def new_record(self) -> NewRecord:
		return self.new_record

	@property
	def position(self) -> str:
		return self.position

	@position.setter
	def position(self, position) -> None:
		assert len(position) >= 1
		self._position = position

	@property
	def reference_letters(self) -> ReferenceLetters:
		return self.reference_letters

	@property
	def status(self) -> str:
		return self.status

	@status.setter
	def status(self, status) -> None:
		assert len(status) >= 1
		self._status = status

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

