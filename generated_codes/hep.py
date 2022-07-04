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
		return self.date

	@date.setter
	def date(self, date) -> None:
		assert len(date) >= 1
		self._date = date

	@property
	def defense_date(self) -> str:
		return self.defense_date

	@defense_date.setter
	def defense_date(self, defense_date) -> None:
		assert len(defense_date) >= 1
		self._defense_date = defense_date

	@property
	def degree_type(self) -> str:
		return self.degree_type

	@degree_type.setter
	def degree_type(self, degree_type) -> None:
		assert len(degree_type) >= 1
		self._degree_type = degree_type



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
		return self.CDS

	@CDS.setter
	def CDS(self, CDS) -> None:
		self._CDS = CDS

	@property
	def HAL(self) -> bool:
		return self.HAL

	@HAL.setter
	def HAL(self, HAL) -> None:
		self._HAL = HAL



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
		return self.acquisition_source

	@property
	def citeable(self) -> bool:
		return self.citeable

	@citeable.setter
	def citeable(self, citeable) -> None:
		self._citeable = citeable

	@property
	def core(self) -> bool:
		return self.core

	@core.setter
	def core(self, core) -> None:
		self._core = core

	@property
	def curated(self) -> bool:
		return self.curated

	@curated.setter
	def curated(self, curated) -> None:
		self._curated = curated

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
	def preprint_date(self) -> str:
		return self.preprint_date

	@preprint_date.setter
	def preprint_date(self, preprint_date) -> None:
		assert len(preprint_date) >= 1
		self._preprint_date = preprint_date

	@property
	def refereed(self) -> bool:
		return self.refereed

	@refereed.setter
	def refereed(self, refereed) -> None:
		self._refereed = refereed

	@property
	def rpp(self) -> bool:
		return self.rpp

	@rpp.setter
	def rpp(self, rpp) -> None:
		self._rpp = rpp

	@property
	def thesis_info(self) -> ThesisInfo:
		return self.thesis_info

	@property
	def withdrawn(self) -> bool:
		return self.withdrawn

	@withdrawn.setter
	def withdrawn(self, withdrawn) -> None:
		self._withdrawn = withdrawn

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
	def export_to(self) -> ExportTo:
		return self.export_to

	@property
	def self_(self) -> Self:
		return self.self_

