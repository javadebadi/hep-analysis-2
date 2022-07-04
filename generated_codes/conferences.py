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



class ShortDescription:

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



class Conferences:

	def __init__(
		self,
		closing_date: str  = None,
		cnum: str  = None,
		core: bool  = None,
		deleted: bool  = None,
		legacy_creation_date: str  = None,
		legacy_version: str  = None,
		new_record: NewRecord  = None,
		opening_date: str  = None,
		short_description: ShortDescription  = None,
		schema: str  = None,
		bucket: str  = None,
		self_: Self  = None,
		) -> None:
		self.closing_date = closing_date
		self.cnum = cnum
		self.core = core
		self.deleted = deleted
		self.legacy_creation_date = legacy_creation_date
		self.legacy_version = legacy_version
		self.new_record = new_record
		self.opening_date = opening_date
		self.short_description = short_description
		self.schema = schema
		self.bucket = bucket
		self.self_ = self_

	@property
	def closing_date(self) -> str:
		return self.closing_date

	@closing_date.setter
	def closing_date(self, closing_date) -> None:
		assert len(closing_date) >= 1
		self._closing_date = closing_date

	@property
	def cnum(self) -> str:
		return self.cnum

	@cnum.setter
	def cnum(self, cnum) -> None:
		assert len(cnum) >= 1
		self._cnum = cnum

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
	def opening_date(self) -> str:
		return self.opening_date

	@opening_date.setter
	def opening_date(self, opening_date) -> None:
		assert len(opening_date) >= 1
		self._opening_date = opening_date

	@property
	def short_description(self) -> ShortDescription:
		return self.short_description

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

