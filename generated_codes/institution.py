import typing


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



class Institution:

	def __init__(
		self,
		core: bool  = None,
		deleted: bool  = None,
		inactive: bool  = None,
		legacy_ICN: str  = None,
		legacy_creation_date: str  = None,
		legacy_version: str  = None,
		new_record: NewRecord  = None,
		schema: str  = None,
		bucket: str  = None,
		self_: Self  = None,
		) -> None:
		self.core = core
		self.deleted = deleted
		self.inactive = inactive
		self.legacy_ICN = legacy_ICN
		self.legacy_creation_date = legacy_creation_date
		self.legacy_version = legacy_version
		self.new_record = new_record
		self.schema = schema
		self.bucket = bucket
		self.self_ = self_

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
	def inactive(self) -> bool:
		return self.inactive

	@inactive.setter
	def inactive(self, inactive) -> None:
		self._inactive = inactive

	@property
	def legacy_ICN(self) -> str:
		return self.legacy_ICN

	@legacy_ICN.setter
	def legacy_ICN(self, legacy_ICN) -> None:
		assert len(legacy_ICN) >= 1
		self._legacy_ICN = legacy_ICN

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

