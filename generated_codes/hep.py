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


class ThesisInfo:

	def __init__(
		self,
		date: str  = None,
		defense_date: str  = None,
		degree_type: str  = None,
		) -> None:
		self.date = date
		self.defense_date = defense_date
		self.degree_type = degree_type

	@property
	def date(self) -> str:
		return self._date

	@date.setter
	def date(self, date) -> None:
		if date is not None:
			assert len(date) >= 1
			pass
		self._date = date

	@property
	def defense_date(self) -> str:
		return self._defense_date

	@defense_date.setter
	def defense_date(self, defense_date) -> None:
		if defense_date is not None:
			assert len(defense_date) >= 1
			pass
		self._defense_date = defense_date

	@property
	def degree_type(self) -> str:
		return self._degree_type

	@degree_type.setter
	def degree_type(self, degree_type) -> None:
		if degree_type is not None:
			assert len(degree_type) >= 1
			pass
		self._degree_type = degree_type

	def set_from_dict(self, data: dict):
		if data is not None:
			return ThesisInfo(
				date=data.get('date', None),
				defense_date=data.get('defense_date', None),
				degree_type=data.get('degree_type', None),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'date:  '
		s += self.date.__str__() if (self.date is not None) else ''
		s += '\n'
		s += 'defense_date:  '
		s += self.defense_date.__str__() if (self.defense_date is not None) else ''
		s += '\n'
		s += 'degree_type:  '
		s += self.degree_type.__str__() if (self.degree_type is not None) else ''
		s += '\n'
		return s


class ExportTo:

	def __init__(
		self,
		CDS: bool  = None,
		HAL: bool  = None,
		) -> None:
		self.CDS = CDS
		self.HAL = HAL

	@property
	def CDS(self) -> bool:
		return self._CDS

	@CDS.setter
	def CDS(self, CDS) -> None:
		if CDS is not None:
			pass
		self._CDS = CDS

	@property
	def HAL(self) -> bool:
		return self._HAL

	@HAL.setter
	def HAL(self, HAL) -> None:
		if HAL is not None:
			pass
		self._HAL = HAL

	def set_from_dict(self, data: dict):
		if data is not None:
			return ExportTo(
				CDS=data.get('CDS', None),
				HAL=data.get('HAL', None),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'CDS:  '
		s += self.CDS.__str__() if (self.CDS is not None) else ''
		s += '\n'
		s += 'HAL:  '
		s += self.HAL.__str__() if (self.HAL is not None) else ''
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


class Hep:

	def __init__(
		self,
		acquisition_source: AcquisitionSource  = None,
		citeable: bool  = None,
		core: bool  = None,
		curated: bool  = None,
		deleted: bool  = None,
		legacy_creation_date: str  = None,
		legacy_version: str  = None,
		new_record: NewRecord  = None,
		preprint_date: str  = None,
		refereed: bool  = None,
		rpp: bool  = None,
		thesis_info: ThesisInfo  = None,
		withdrawn: bool  = None,
		schema: str  = None,
		bucket: str  = None,
		export_to: ExportTo  = None,
		self_: Self  = None,
		) -> None:
		self.acquisition_source = acquisition_source
		self.citeable = citeable
		self.core = core
		self.curated = curated
		self.deleted = deleted
		self.legacy_creation_date = legacy_creation_date
		self.legacy_version = legacy_version
		self.new_record = new_record
		self.preprint_date = preprint_date
		self.refereed = refereed
		self.rpp = rpp
		self.thesis_info = thesis_info
		self.withdrawn = withdrawn
		self.schema = schema
		self.bucket = bucket
		self.export_to = export_to
		self.self_ = self_

	@property
	def acquisition_source(self) -> AcquisitionSource:
		return self._acquisition_source

	@acquisition_source.setter
	def acquisition_source(self, acquisition_source) -> None:
		pass
		self._acquisition_source = acquisition_source

	@property
	def citeable(self) -> bool:
		return self._citeable

	@citeable.setter
	def citeable(self, citeable) -> None:
		if citeable is not None:
			pass
		self._citeable = citeable

	@property
	def core(self) -> bool:
		return self._core

	@core.setter
	def core(self, core) -> None:
		if core is not None:
			pass
		self._core = core

	@property
	def curated(self) -> bool:
		return self._curated

	@curated.setter
	def curated(self, curated) -> None:
		if curated is not None:
			pass
		self._curated = curated

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
	def preprint_date(self) -> str:
		return self._preprint_date

	@preprint_date.setter
	def preprint_date(self, preprint_date) -> None:
		if preprint_date is not None:
			assert len(preprint_date) >= 1
			pass
		self._preprint_date = preprint_date

	@property
	def refereed(self) -> bool:
		return self._refereed

	@refereed.setter
	def refereed(self, refereed) -> None:
		if refereed is not None:
			pass
		self._refereed = refereed

	@property
	def rpp(self) -> bool:
		return self._rpp

	@rpp.setter
	def rpp(self, rpp) -> None:
		if rpp is not None:
			pass
		self._rpp = rpp

	@property
	def thesis_info(self) -> ThesisInfo:
		return self._thesis_info

	@thesis_info.setter
	def thesis_info(self, thesis_info) -> None:
		pass
		self._thesis_info = thesis_info

	@property
	def withdrawn(self) -> bool:
		return self._withdrawn

	@withdrawn.setter
	def withdrawn(self, withdrawn) -> None:
		if withdrawn is not None:
			pass
		self._withdrawn = withdrawn

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
	def export_to(self) -> ExportTo:
		return self._export_to

	@export_to.setter
	def export_to(self, export_to) -> None:
		pass
		self._export_to = export_to

	@property
	def self_(self) -> Self:
		return self._self_

	@self_.setter
	def self_(self, self_) -> None:
		pass
		self._self_ = self_

	def set_from_dict(self, data: dict):
		if data is not None:
			return Hep(
				acquisition_source=AcquisitionSource().set_from_dict(data=data.get('acquisition_source', None)),
				citeable=data.get('citeable', None),
				core=data.get('core', None),
				curated=data.get('curated', None),
				deleted=data.get('deleted', None),
				legacy_creation_date=data.get('legacy_creation_date', None),
				legacy_version=data.get('legacy_version', None),
				new_record=NewRecord().set_from_dict(data=data.get('new_record', None)),
				preprint_date=data.get('preprint_date', None),
				refereed=data.get('refereed', None),
				rpp=data.get('rpp', None),
				thesis_info=ThesisInfo().set_from_dict(data=data.get('thesis_info', None)),
				withdrawn=data.get('withdrawn', None),
				schema=data.get('$schema', None),
				bucket=data.get('_bucket', None),
				export_to=ExportTo().set_from_dict(data=data.get('_export_to', None)),
				self_=Self().set_from_dict(data=data.get('self', None)),
			)
		else:
			return None

	def __str__(self):
		s = ''
		s += 'acquisition_source:  '
		s += self.acquisition_source.__str__() if (self.acquisition_source is not None) else ''
		s += '\n'
		s += 'citeable:  '
		s += self.citeable.__str__() if (self.citeable is not None) else ''
		s += '\n'
		s += 'core:  '
		s += self.core.__str__() if (self.core is not None) else ''
		s += '\n'
		s += 'curated:  '
		s += self.curated.__str__() if (self.curated is not None) else ''
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
		s += 'preprint_date:  '
		s += self.preprint_date.__str__() if (self.preprint_date is not None) else ''
		s += '\n'
		s += 'refereed:  '
		s += self.refereed.__str__() if (self.refereed is not None) else ''
		s += '\n'
		s += 'rpp:  '
		s += self.rpp.__str__() if (self.rpp is not None) else ''
		s += '\n'
		s += 'thesis_info:  '
		s += self.thesis_info.__str__() if (self.thesis_info is not None) else ''
		s += '\n'
		s += 'withdrawn:  '
		s += self.withdrawn.__str__() if (self.withdrawn is not None) else ''
		s += '\n'
		s += 'schema:  '
		s += self.schema.__str__() if (self.schema is not None) else ''
		s += '\n'
		s += 'bucket:  '
		s += self.bucket.__str__() if (self.bucket is not None) else ''
		s += '\n'
		s += 'export_to:  '
		s += self.export_to.__str__() if (self.export_to is not None) else ''
		s += '\n'
		s += 'self_:  '
		s += self.self_.__str__() if (self.self_ is not None) else ''
		s += '\n'
		return s
