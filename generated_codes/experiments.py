import typing


class Record:

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
			return Record(
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


class Accelerator:

	def __init__(
		self,
		curated_relation: bool  = None,
		record: Record  = None,
		value: str  = None,
		) -> None:
		self.curated_relation = curated_relation
		self.record = record
		self.value = value

	@property
	def curated_relation(self) -> bool:
		return self._curated_relation

	@curated_relation.setter
	def curated_relation(self, curated_relation) -> None:
		if curated_relation is not None:
			pass
		self._curated_relation = curated_relation

	@property
	def record(self) -> Record:
		return self._record

	@record.setter
	def record(self, record) -> None:
		pass
		self._record = record

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
			return Accelerator(
				curated_relation=data.get('curated_relation', None),
				record=Record().set_from_dict(data=data.get('record', None)),
				value=data.get('value', None),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'curated_relation:  '
		s += self.curated_relation.__str__() if (self.curated_relation is not None) else ''
		s += '\n'
		s += 'record:  '
		s += self.record.__str__() if (self.record is not None) else ''
		s += '\n'
		s += 'value:  '
		s += self.value.__str__() if (self.value is not None) else ''
		s += '\n'
		return s


class Record:

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
			return Record(
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


class Collaboration:

	def __init__(
		self,
		curated_relation: bool  = None,
		record: Record  = None,
		value: str  = None,
		) -> None:
		self.curated_relation = curated_relation
		self.record = record
		self.value = value

	@property
	def curated_relation(self) -> bool:
		return self._curated_relation

	@curated_relation.setter
	def curated_relation(self, curated_relation) -> None:
		if curated_relation is not None:
			pass
		self._curated_relation = curated_relation

	@property
	def record(self) -> Record:
		return self._record

	@record.setter
	def record(self, record) -> None:
		pass
		self._record = record

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
			return Collaboration(
				curated_relation=data.get('curated_relation', None),
				record=Record().set_from_dict(data=data.get('record', None)),
				value=data.get('value', None),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'curated_relation:  '
		s += self.curated_relation.__str__() if (self.curated_relation is not None) else ''
		s += '\n'
		s += 'record:  '
		s += self.record.__str__() if (self.record is not None) else ''
		s += '\n'
		s += 'value:  '
		s += self.value.__str__() if (self.value is not None) else ''
		s += '\n'
		return s


class Experiment:

	def __init__(
		self,
		short_name: str  = None,
		value: str  = None,
		) -> None:
		self.short_name = short_name
		self.value = value

	@property
	def short_name(self) -> str:
		return self._short_name

	@short_name.setter
	def short_name(self, short_name) -> None:
		if short_name is not None:
			assert len(short_name) >= 1
			pass
		self._short_name = short_name

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
			return Experiment(
				short_name=data.get('short_name', None),
				value=data.get('value', None),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'short_name:  '
		s += self.short_name.__str__() if (self.short_name is not None) else ''
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


class Experiments:

	def __init__(
		self,
		accelerator: Accelerator  = None,
		collaboration: Collaboration  = None,
		core: bool  = None,
		date_approved: str  = None,
		date_cancelled: str  = None,
		date_completed: str  = None,
		date_proposed: str  = None,
		date_started: str  = None,
		deleted: bool  = None,
		description: str  = None,
		experiment: Experiment  = None,
		legacy_creation_date: str  = None,
		legacy_name: str  = None,
		legacy_version: str  = None,
		long_name: str  = None,
		new_record: NewRecord  = None,
		schema: str  = None,
		bucket: str  = None,
		full_ingestion: bool  = None,
		self_: Self  = None,
		) -> None:
		self.accelerator = accelerator
		self.collaboration = collaboration
		self.core = core
		self.date_approved = date_approved
		self.date_cancelled = date_cancelled
		self.date_completed = date_completed
		self.date_proposed = date_proposed
		self.date_started = date_started
		self.deleted = deleted
		self.description = description
		self.experiment = experiment
		self.legacy_creation_date = legacy_creation_date
		self.legacy_name = legacy_name
		self.legacy_version = legacy_version
		self.long_name = long_name
		self.new_record = new_record
		self.schema = schema
		self.bucket = bucket
		self.full_ingestion = full_ingestion
		self.self_ = self_

	@property
	def accelerator(self) -> Accelerator:
		return self._accelerator

	@accelerator.setter
	def accelerator(self, accelerator) -> None:
		pass
		self._accelerator = accelerator

	@property
	def collaboration(self) -> Collaboration:
		return self._collaboration

	@collaboration.setter
	def collaboration(self, collaboration) -> None:
		pass
		self._collaboration = collaboration

	@property
	def core(self) -> bool:
		return self._core

	@core.setter
	def core(self, core) -> None:
		if core is not None:
			pass
		self._core = core

	@property
	def date_approved(self) -> str:
		return self._date_approved

	@date_approved.setter
	def date_approved(self, date_approved) -> None:
		if date_approved is not None:
			assert len(date_approved) >= 1
			pass
		self._date_approved = date_approved

	@property
	def date_cancelled(self) -> str:
		return self._date_cancelled

	@date_cancelled.setter
	def date_cancelled(self, date_cancelled) -> None:
		if date_cancelled is not None:
			assert len(date_cancelled) >= 1
			pass
		self._date_cancelled = date_cancelled

	@property
	def date_completed(self) -> str:
		return self._date_completed

	@date_completed.setter
	def date_completed(self, date_completed) -> None:
		if date_completed is not None:
			assert len(date_completed) >= 1
			pass
		self._date_completed = date_completed

	@property
	def date_proposed(self) -> str:
		return self._date_proposed

	@date_proposed.setter
	def date_proposed(self, date_proposed) -> None:
		if date_proposed is not None:
			assert len(date_proposed) >= 1
			pass
		self._date_proposed = date_proposed

	@property
	def date_started(self) -> str:
		return self._date_started

	@date_started.setter
	def date_started(self, date_started) -> None:
		if date_started is not None:
			assert len(date_started) >= 1
			pass
		self._date_started = date_started

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
	def experiment(self) -> Experiment:
		return self._experiment

	@experiment.setter
	def experiment(self, experiment) -> None:
		pass
		self._experiment = experiment

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
	def legacy_name(self) -> str:
		return self._legacy_name

	@legacy_name.setter
	def legacy_name(self, legacy_name) -> None:
		if legacy_name is not None:
			assert len(legacy_name) >= 1
			pass
		self._legacy_name = legacy_name

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
	def long_name(self) -> str:
		return self._long_name

	@long_name.setter
	def long_name(self, long_name) -> None:
		if long_name is not None:
			assert len(long_name) >= 1
			pass
		self._long_name = long_name

	@property
	def new_record(self) -> NewRecord:
		return self._new_record

	@new_record.setter
	def new_record(self, new_record) -> None:
		pass
		self._new_record = new_record

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
	def full_ingestion(self) -> bool:
		return self._full_ingestion

	@full_ingestion.setter
	def full_ingestion(self, full_ingestion) -> None:
		if full_ingestion is not None:
			pass
		self._full_ingestion = full_ingestion

	@property
	def self_(self) -> Self:
		return self._self_

	@self_.setter
	def self_(self, self_) -> None:
		pass
		self._self_ = self_

	def set_from_dict(self, data: dict):
		if data is not None:
			return Experiments(
				accelerator=Accelerator().set_from_dict(data=data.get('accelerator', None)),
				collaboration=Collaboration().set_from_dict(data=data.get('collaboration', None)),
				core=data.get('core', None),
				date_approved=data.get('date_approved', None),
				date_cancelled=data.get('date_cancelled', None),
				date_completed=data.get('date_completed', None),
				date_proposed=data.get('date_proposed', None),
				date_started=data.get('date_started', None),
				deleted=data.get('deleted', None),
				description=data.get('description', None),
				experiment=Experiment().set_from_dict(data=data.get('experiment', None)),
				legacy_creation_date=data.get('legacy_creation_date', None),
				legacy_name=data.get('legacy_name', None),
				legacy_version=data.get('legacy_version', None),
				long_name=data.get('long_name', None),
				new_record=NewRecord().set_from_dict(data=data.get('new_record', None)),
				schema=data.get('$schema', None),
				bucket=data.get('_bucket', None),
				full_ingestion=data.get('_full_ingestion', None),
				self_=Self().set_from_dict(data=data.get('self', None)),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'accelerator:  '
		s += self.accelerator.__str__() if (self.accelerator is not None) else ''
		s += '\n'
		s += 'collaboration:  '
		s += self.collaboration.__str__() if (self.collaboration is not None) else ''
		s += '\n'
		s += 'core:  '
		s += self.core.__str__() if (self.core is not None) else ''
		s += '\n'
		s += 'date_approved:  '
		s += self.date_approved.__str__() if (self.date_approved is not None) else ''
		s += '\n'
		s += 'date_cancelled:  '
		s += self.date_cancelled.__str__() if (self.date_cancelled is not None) else ''
		s += '\n'
		s += 'date_completed:  '
		s += self.date_completed.__str__() if (self.date_completed is not None) else ''
		s += '\n'
		s += 'date_proposed:  '
		s += self.date_proposed.__str__() if (self.date_proposed is not None) else ''
		s += '\n'
		s += 'date_started:  '
		s += self.date_started.__str__() if (self.date_started is not None) else ''
		s += '\n'
		s += 'deleted:  '
		s += self.deleted.__str__() if (self.deleted is not None) else ''
		s += '\n'
		s += 'description:  '
		s += self.description.__str__() if (self.description is not None) else ''
		s += '\n'
		s += 'experiment:  '
		s += self.experiment.__str__() if (self.experiment is not None) else ''
		s += '\n'
		s += 'legacy_creation_date:  '
		s += self.legacy_creation_date.__str__() if (self.legacy_creation_date is not None) else ''
		s += '\n'
		s += 'legacy_name:  '
		s += self.legacy_name.__str__() if (self.legacy_name is not None) else ''
		s += '\n'
		s += 'legacy_version:  '
		s += self.legacy_version.__str__() if (self.legacy_version is not None) else ''
		s += '\n'
		s += 'long_name:  '
		s += self.long_name.__str__() if (self.long_name is not None) else ''
		s += '\n'
		s += 'new_record:  '
		s += self.new_record.__str__() if (self.new_record is not None) else ''
		s += '\n'
		s += 'schema:  '
		s += self.schema.__str__() if (self.schema is not None) else ''
		s += '\n'
		s += 'bucket:  '
		s += self.bucket.__str__() if (self.bucket is not None) else ''
		s += '\n'
		s += 'full_ingestion:  '
		s += self.full_ingestion.__str__() if (self.full_ingestion is not None) else ''
		s += '\n'
		s += 'self_:  '
		s += self.self_.__str__() if (self.self_ is not None) else ''
		s += '\n'
		return s
