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


class ReferenceLetters:

	def __init__(
		self,
		) -> None:
		pass

	def set_from_dict(self, data: dict):
		if data is not None:
			return ReferenceLetters(
			)
		else:
			return None

	def __str__(self):
		s = ''
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
		return self._acquisition_source

	@acquisition_source.setter
	def acquisition_source(self, acquisition_source) -> None:
		pass
		self._acquisition_source = acquisition_source

	@property
	def deadline_date(self) -> str:
		return self._deadline_date

	@deadline_date.setter
	def deadline_date(self, deadline_date) -> None:
		if deadline_date is not None:
			assert len(deadline_date) >= 1
			pass
		self._deadline_date = deadline_date

	@property
	def deleted(self) -> bool:
		return self._deleted

	@deleted.setter
	def deleted(self, deleted) -> None:
		if deleted is not None:
			pass
		self._deleted = deleted

	@property
	def description(self) -> str:
		return self._description

	@description.setter
	def description(self, description) -> None:
		if description is not None:
			assert len(description) >= 1
			pass
		self._description = description

	@property
	def external_job_identifier(self) -> str:
		return self._external_job_identifier

	@external_job_identifier.setter
	def external_job_identifier(self, external_job_identifier) -> None:
		if external_job_identifier is not None:
			assert len(external_job_identifier) >= 1
			pass
		self._external_job_identifier = external_job_identifier

	@property
	def legacy_creation_date(self) -> str:
		return self._legacy_creation_date

	@legacy_creation_date.setter
	def legacy_creation_date(self, legacy_creation_date) -> None:
		if legacy_creation_date is not None:
			assert len(legacy_creation_date) >= 1
			pass
		self._legacy_creation_date = legacy_creation_date

	@property
	def legacy_version(self) -> str:
		return self._legacy_version

	@legacy_version.setter
	def legacy_version(self, legacy_version) -> None:
		if legacy_version is not None:
			assert len(legacy_version) >= 1
			pass
		self._legacy_version = legacy_version

	@property
	def new_record(self) -> NewRecord:
		return self._new_record

	@new_record.setter
	def new_record(self, new_record) -> None:
		pass
		self._new_record = new_record

	@property
	def position(self) -> str:
		return self._position

	@position.setter
	def position(self, position) -> None:
		if position is not None:
			assert len(position) >= 1
			pass
		self._position = position

	@property
	def reference_letters(self) -> ReferenceLetters:
		return self._reference_letters

	@reference_letters.setter
	def reference_letters(self, reference_letters) -> None:
		pass
		self._reference_letters = reference_letters

	@property
	def status(self) -> str:
		return self._status

	@status.setter
	def status(self, status) -> None:
		if status is not None:
			assert len(status) >= 1
			pass
		self._status = status

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
	def bucket(self) -> str:
		return self._bucket

	@bucket.setter
	def bucket(self, bucket) -> None:
		if bucket is not None:
			assert len(bucket) >= 1
			pass
		self._bucket = bucket

	@property
	def self_(self) -> Self:
		return self._self_

	@self_.setter
	def self_(self, self_) -> None:
		pass
		self._self_ = self_

	def set_from_dict(self, data: dict):
		if data is not None:
			return Jobs(
				acquisition_source=AcquisitionSource().set_from_dict(data=data.get('acquisition_source', None)),
				deadline_date=data.get('deadline_date', None),
				deleted=data.get('deleted', None),
				description=data.get('description', None),
				external_job_identifier=data.get('external_job_identifier', None),
				legacy_creation_date=data.get('legacy_creation_date', None),
				legacy_version=data.get('legacy_version', None),
				new_record=NewRecord().set_from_dict(data=data.get('new_record', None)),
				position=data.get('position', None),
				reference_letters=ReferenceLetters().set_from_dict(data=data.get('reference_letters', None)),
				status=data.get('status', None),
				schema=data.get('$schema', None),
				bucket=data.get('_bucket', None),
				self_=Self().set_from_dict(data=data.get('self', None)),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'acquisition_source:  '
		s += self.acquisition_source.__str__() if (self.acquisition_source is not None) else ''
		s += '\n'
		s += 'deadline_date:  '
		s += self.deadline_date.__str__() if (self.deadline_date is not None) else ''
		s += '\n'
		s += 'deleted:  '
		s += self.deleted.__str__() if (self.deleted is not None) else ''
		s += '\n'
		s += 'description:  '
		s += self.description.__str__() if (self.description is not None) else ''
		s += '\n'
		s += 'external_job_identifier:  '
		s += self.external_job_identifier.__str__() if (self.external_job_identifier is not None) else ''
		s += '\n'
		s += 'legacy_creation_date:  '
		s += self.legacy_creation_date.__str__() if (self.legacy_creation_date is not None) else ''
		s += '\n'
		s += 'legacy_version:  '
		s += self.legacy_version.__str__() if (self.legacy_version is not None) else ''
		s += '\n'
		s += 'new_record:  '
		s += self.new_record.__str__() if (self.new_record is not None) else ''
		s += '\n'
		s += 'position:  '
		s += self.position.__str__() if (self.position is not None) else ''
		s += '\n'
		s += 'reference_letters:  '
		s += self.reference_letters.__str__() if (self.reference_letters is not None) else ''
		s += '\n'
		s += 'status:  '
		s += self.status.__str__() if (self.status is not None) else ''
		s += '\n'
		s += 'schema:  '
		s += self.schema.__str__() if (self.schema is not None) else ''
		s += '\n'
		s += 'bucket:  '
		s += self.bucket.__str__() if (self.bucket is not None) else ''
		s += '\n'
		s += 'self_:  '
		s += self.self_.__str__() if (self.self_ is not None) else ''
		s += '\n'
		return s
