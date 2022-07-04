import typing


class Record:

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
		return self.curated_relation

	@curated_relation.setter
	def curated_relation(self, curated_relation) -> None:
		self._curated_relation = curated_relation

	@property
	def record(self) -> Record:
		return self.record

	@property
	def value(self) -> str:
		return self.value

	@value.setter
	def value(self, value) -> None:
		assert len(value) >= 1
		self._value = value



class Record:

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
		return self.curated_relation

	@curated_relation.setter
	def curated_relation(self, curated_relation) -> None:
		self._curated_relation = curated_relation

	@property
	def record(self) -> Record:
		return self.record

	@property
	def value(self) -> str:
		return self.value

	@value.setter
	def value(self, value) -> None:
		assert len(value) >= 1
		self._value = value



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
		return self.short_name

	@short_name.setter
	def short_name(self, short_name) -> None:
		assert len(short_name) >= 1
		self._short_name = short_name

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
		return self.accelerator

	@property
	def collaboration(self) -> Collaboration:
		return self.collaboration

	@property
	def core(self) -> bool:
		return self.core

	@core.setter
	def core(self, core) -> None:
		self._core = core

	@property
	def date_approved(self) -> str:
		return self.date_approved

	@date_approved.setter
	def date_approved(self, date_approved) -> None:
		assert len(date_approved) >= 1
		self._date_approved = date_approved

	@property
	def date_cancelled(self) -> str:
		return self.date_cancelled

	@date_cancelled.setter
	def date_cancelled(self, date_cancelled) -> None:
		assert len(date_cancelled) >= 1
		self._date_cancelled = date_cancelled

	@property
	def date_completed(self) -> str:
		return self.date_completed

	@date_completed.setter
	def date_completed(self, date_completed) -> None:
		assert len(date_completed) >= 1
		self._date_completed = date_completed

	@property
	def date_proposed(self) -> str:
		return self.date_proposed

	@date_proposed.setter
	def date_proposed(self, date_proposed) -> None:
		assert len(date_proposed) >= 1
		self._date_proposed = date_proposed

	@property
	def date_started(self) -> str:
		return self.date_started

	@date_started.setter
	def date_started(self, date_started) -> None:
		assert len(date_started) >= 1
		self._date_started = date_started

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
	def experiment(self) -> Experiment:
		return self.experiment

	@property
	def legacy_creation_date(self) -> str:
		return self.legacy_creation_date

	@legacy_creation_date.setter
	def legacy_creation_date(self, legacy_creation_date) -> None:
		assert len(legacy_creation_date) >= 1
		self._legacy_creation_date = legacy_creation_date

	@property
	def legacy_name(self) -> str:
		return self.legacy_name

	@legacy_name.setter
	def legacy_name(self, legacy_name) -> None:
		assert len(legacy_name) >= 1
		self._legacy_name = legacy_name

	@property
	def legacy_version(self) -> str:
		return self.legacy_version

	@legacy_version.setter
	def legacy_version(self, legacy_version) -> None:
		assert len(legacy_version) >= 1
		self._legacy_version = legacy_version

	@property
	def long_name(self) -> str:
		return self.long_name

	@long_name.setter
	def long_name(self, long_name) -> None:
		assert len(long_name) >= 1
		self._long_name = long_name

	@property
	def new_record(self) -> NewRecord:
		return self.new_record

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
	def full_ingestion(self) -> bool:
		return self.full_ingestion

	@full_ingestion.setter
	def full_ingestion(self, full_ingestion) -> None:
		self._full_ingestion = full_ingestion

	@property
	def self_(self) -> Self:
		return self.self_

