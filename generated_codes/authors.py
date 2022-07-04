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
		return self._numeration

	@numeration.setter
	def numeration(self, numeration) -> None:
		if numeration is not None:
			assert len(numeration) >= 1
			pass
		self._numeration = numeration

	@property
	def preferred_name(self) -> str:
		return self._preferred_name

	@preferred_name.setter
	def preferred_name(self, preferred_name) -> None:
		if preferred_name is not None:
			assert len(preferred_name) >= 1
			pass
		self._preferred_name = preferred_name

	@property
	def title(self) -> str:
		return self._title

	@title.setter
	def title(self, title) -> None:
		if title is not None:
			assert len(title) >= 1
			pass
		self._title = title

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
			return Name(
				numeration=data.get('numeration', None),
				preferred_name=data.get('preferred_name', None),
				title=data.get('title', None),
				value=data.get('value', None),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'numeration:  '
		s += self.numeration.__str__() if (self.numeration is not None) else ''
		s += '\n'
		s += 'preferred_name:  '
		s += self.preferred_name.__str__() if (self.preferred_name is not None) else ''
		s += '\n'
		s += 'title:  '
		s += self.title.__str__() if (self.title is not None) else ''
		s += '\n'
		s += 'value:  '
		s += self.value.__str__() if (self.value is not None) else ''
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
		return self._acquisition_source

	@acquisition_source.setter
	def acquisition_source(self, acquisition_source) -> None:
		pass
		self._acquisition_source = acquisition_source

	@property
	def birth_date(self) -> str:
		return self._birth_date

	@birth_date.setter
	def birth_date(self, birth_date) -> None:
		if birth_date is not None:
			assert len(birth_date) >= 1
			pass
		self._birth_date = birth_date

	@property
	def death_date(self) -> str:
		return self._death_date

	@death_date.setter
	def death_date(self, death_date) -> None:
		if death_date is not None:
			assert len(death_date) >= 1
			pass
		self._death_date = death_date

	@property
	def deleted(self) -> bool:
		return self._deleted

	@deleted.setter
	def deleted(self, deleted) -> None:
		if deleted is not None:
			pass
		self._deleted = deleted

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
	def name(self) -> Name:
		return self._name

	@name.setter
	def name(self, name) -> None:
		pass
		self._name = name

	@property
	def new_record(self) -> NewRecord:
		return self._new_record

	@new_record.setter
	def new_record(self, new_record) -> None:
		pass
		self._new_record = new_record

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
	def stub(self) -> bool:
		return self._stub

	@stub.setter
	def stub(self, stub) -> None:
		if stub is not None:
			pass
		self._stub = stub

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
			return Authors(
				acquisition_source=AcquisitionSource().set_from_dict(data=data.get('acquisition_source', None)),
				birth_date=data.get('birth_date', None),
				death_date=data.get('death_date', None),
				deleted=data.get('deleted', None),
				legacy_creation_date=data.get('legacy_creation_date', None),
				legacy_version=data.get('legacy_version', None),
				name=Name().set_from_dict(data=data.get('name', None)),
				new_record=NewRecord().set_from_dict(data=data.get('new_record', None)),
				status=data.get('status', None),
				stub=data.get('stub', None),
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
		s += 'birth_date:  '
		s += self.birth_date.__str__() if (self.birth_date is not None) else ''
		s += '\n'
		s += 'death_date:  '
		s += self.death_date.__str__() if (self.death_date is not None) else ''
		s += '\n'
		s += 'deleted:  '
		s += self.deleted.__str__() if (self.deleted is not None) else ''
		s += '\n'
		s += 'legacy_creation_date:  '
		s += self.legacy_creation_date.__str__() if (self.legacy_creation_date is not None) else ''
		s += '\n'
		s += 'legacy_version:  '
		s += self.legacy_version.__str__() if (self.legacy_version is not None) else ''
		s += '\n'
		s += 'name:  '
		s += self.name.__str__() if (self.name is not None) else ''
		s += '\n'
		s += 'new_record:  '
		s += self.new_record.__str__() if (self.new_record is not None) else ''
		s += '\n'
		s += 'status:  '
		s += self.status.__str__() if (self.status is not None) else ''
		s += '\n'
		s += 'stub:  '
		s += self.stub.__str__() if (self.stub is not None) else ''
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
