import typing


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
			return ShortDescription(
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
		return self._closing_date

	@closing_date.setter
	def closing_date(self, closing_date) -> None:
		if closing_date is not None:
			assert len(closing_date) >= 1
			pass
		self._closing_date = closing_date

	@property
	def cnum(self) -> str:
		return self._cnum

	@cnum.setter
	def cnum(self, cnum) -> None:
		if cnum is not None:
			assert len(cnum) >= 1
			pass
		self._cnum = cnum

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
	def opening_date(self) -> str:
		return self._opening_date

	@opening_date.setter
	def opening_date(self, opening_date) -> None:
		if opening_date is not None:
			assert len(opening_date) >= 1
			pass
		self._opening_date = opening_date

	@property
	def short_description(self) -> ShortDescription:
		return self._short_description

	@short_description.setter
	def short_description(self, short_description) -> None:
		pass
		self._short_description = short_description

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
			return Conferences(
				closing_date=data.get('closing_date', None),
				cnum=data.get('cnum', None),
				core=data.get('core', None),
				deleted=data.get('deleted', None),
				legacy_creation_date=data.get('legacy_creation_date', None),
				legacy_version=data.get('legacy_version', None),
				new_record=NewRecord().set_from_dict(data=data.get('new_record', None)),
				opening_date=data.get('opening_date', None),
				short_description=ShortDescription().set_from_dict(data=data.get('short_description', None)),
				schema=data.get('$schema', None),
				bucket=data.get('_bucket', None),
				self_=Self().set_from_dict(data=data.get('self', None)),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'closing_date:  '
		s += self.closing_date.__str__() if (self.closing_date is not None) else ''
		s += '\n'
		s += 'cnum:  '
		s += self.cnum.__str__() if (self.cnum is not None) else ''
		s += '\n'
		s += 'core:  '
		s += self.core.__str__() if (self.core is not None) else ''
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
		s += 'new_record:  '
		s += self.new_record.__str__() if (self.new_record is not None) else ''
		s += '\n'
		s += 'opening_date:  '
		s += self.opening_date.__str__() if (self.opening_date is not None) else ''
		s += '\n'
		s += 'short_description:  '
		s += self.short_description.__str__() if (self.short_description is not None) else ''
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
