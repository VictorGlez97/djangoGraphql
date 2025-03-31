import datetime
import decimal
from enum import Enum
from typing import List, Optional

import strawberry


def id_resolver(obj, field_name: str) -> int:
    """Get ID value from a related object"""
    if obj is None:
        return None
    value = getattr(obj, field_name, None)
    if hasattr(value, "pk"):
        return value.pk
    return value


### CppIdenpara ###
@strawberry.type
class CppIdenparaType:
    """Type representation for CppIdenpara model."""

    caip_idenpara: int
    caip_enpara: str
    caip_idstatus: int
    caip_idcveusu: int
    caip_fechope: datetime.datetime


@strawberry.input
class CppIdenparaFilterInput:
    """Filter input for CppIdenpara model."""

    page: Optional[int] = 1
    per_page: Optional[int] = 10
    caip_idenpara: Optional[int] = None
    caip_enpara: Optional[str] = None
    caip_idstatus: Optional[int] = None
    caip_idcveusu: Optional[int] = None


### CppModulos ###
@strawberry.type
class CppModulosType:
    """Type representation for CppModulos model."""

    camd_idmodulo: int
    camd_modulo: str
    camd_idstatus: int
    camd_idcveusu: Optional[int] = None
    camd_fechope: Optional[datetime.datetime] = None


### CppStatus ###
@strawberry.type
class CppStatusType:
    """Type representation for CppStatus model."""

    cast_idstatus: int
    cast_cvstatus: str
    cast_idmodulo: int
    cast_status: str
    cast_descrip2: str
    cast_descrip3: str
    cast_descrip4: str
    cast_descrip5: str
    # Keep the ID resolver for basic compatibility
    cast_idstatu_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "cast_idstatu"))

    # Add nested type field for self-referencing ForeignKey relationship
    @strawberry.field
    def cast_idstatu(self) -> "CppStatusType":
        """Get related CppStatus object."""
        return getattr(self, "cast_idstatu", None)

    cast_importe1: decimal.Decimal
    cast_importe2: decimal.Decimal
    cast_importe3: decimal.Decimal
    cast_importe4: decimal.Decimal
    cast_importe5: decimal.Decimal
    cast_fecha1: datetime.datetime
    cast_fecha2: datetime.datetime
    cast_fecha3: datetime.datetime
    cast_hora1: datetime.time
    cast_hora2: datetime.time
    cast_hora3: datetime.time
    cast_idcveusu: int
    cast_fechope: datetime.datetime
    cast_horaope: datetime.datetime


@strawberry.input
class CppStatusFilterInput:
    """Filter type for CppStatus model."""

    page: Optional[int] = 1
    per_page: Optional[int] = 10
    cast_idstatus: Optional[int] = None
    cast_cvstatus: Optional[str] = None


### CppDepto ###
@strawberry.type
class CppDeptoType:
    """Type representation for CppDepto model."""

    cade_iddepto: int
    cade_cvdepto: str
    cade_depto: str
    # Keep the ID resolver for basic compatibility
    cade_idstatus_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "cade_idstatus"))

    # Add nested type field for ForeignKey relationship
    @strawberry.field
    def cade_idstatus(self) -> CppStatusType:
        """Get related CppStatus object."""
        return getattr(self, "cade_idstatus", None)

    cade_idcveusu: int
    cade_fechope: datetime.datetime


### CppPuesto ###
@strawberry.type
class CppPuestoType:
    """Type representation for CppPuesto model."""

    capu_idpuesto: int
    capu_cvpuesto: str
    capu_puesto: str
    # Keep the ID resolver for basic compatibility
    capu_idstatus_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "capu_idstatus"))

    # Add nested type field for ForeignKey relationship
    @strawberry.field
    def capu_idstatus(self) -> CppStatusType:
        """Get related CppStatus object."""
        return getattr(self, "capu_idstatus", None)

    capu_idcveusu: int
    capu_fechope: datetime.datetime


### CppEmpresa ###
@strawberry.type
class CppEmpresaType:
    """Type representation for CppEmpresa model."""

    caem_idempresa: int
    caem_cvempresa: str
    caem_empresa: str
    # Keep the ID resolver for basic compatibility
    caem_idstatus_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "caem_idstatus"))

    # Add nested type field for ForeignKey relationship
    @strawberry.field
    def caem_idstatus(self) -> CppStatusType:
        """Get related CppStatus object."""
        return getattr(self, "caem_idstatus", None)

    caem_idcveusu: int
    caem_fechope: datetime.datetime


### PncUsuariosPm ###
@strawberry.type
class PncUsuariosPmType:
    """Type representation for PncUsuariosPm model."""

    usu_idusuario: int
    usu_idusuari: str
    usu_apusuari: Optional[str] = None
    usu_amusuari: Optional[str] = None
    usu_nousuari: Optional[str] = None
    # Keep the ID resolvers for basic compatibility
    usu_iddepto_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "usu_iddepto"))
    usu_idstatus_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "usu_idstatus"))
    usu_idcveusu_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "usu_idcveusu"))
    usu_idpuesto_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "usu_idpuesto"))
    usu_idempresa_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "usu_idempresa"))

    # Add nested type fields for ForeignKey relationships
    @strawberry.field
    def usu_iddepto(self) -> CppDeptoType:
        """Get related CppDepto object."""
        return getattr(self, "usu_iddepto", None)

    @strawberry.field
    def usu_idstatus(self) -> CppStatusType:
        """Get related CppStatus object."""
        return getattr(self, "usu_idstatus", None)

    @strawberry.field
    def usu_idcveusu(self) -> "PncUsuariosPmType":
        """Get related PncUsuariosPm object (self-reference)."""
        return getattr(self, "usu_idcveusu", None)

    @strawberry.field
    def usu_idpuesto(self) -> CppPuestoType:
        """Get related CppPuesto object."""
        return getattr(self, "usu_idpuesto", None)

    @strawberry.field
    def usu_idempresa(self) -> CppEmpresaType:
        """Get related CppEmpresa object."""
        return getattr(self, "usu_idempresa", None)

    usu_cveacces: Optional[str] = None
    usu_fechope: Optional[datetime.datetime] = None
    usu_cveemp: Optional[str] = None
    usu_fecha: Optional[datetime.datetime] = None
    usu_dias: Optional[int] = None
    usu_idpersona: Optional[int] = None
    usu_cvemovil: Optional[str] = None
    usu_usuarionombre: Optional[str] = strawberry.field(
        resolver=lambda root: f"{root.usu_nousuari} {root.usu_apusuari} {root.usu_amusuari}"
    )


@strawberry.input
class PncUsuariosPmFilterInput:
    """Filter input for PncUsuariosPm model."""

    page: Optional[int] = 1
    per_page: Optional[int] = 10
    usu_idusuario: Optional[int] = None
    usu_idusuari: Optional[str] = None
    usu_apusuari: Optional[str] = None
    usu_amusuari: Optional[str] = None
    usu_nousuari: Optional[str] = None
    usu_iddepto: Optional[int] = None
    usu_idstatus: Optional[int] = None
    usu_idstatus_cvstatus: Optional[str] = "A"
    usu_idcveusu: Optional[int] = None
    usu_idpuesto: Optional[int] = None
    usu_idempresa: Optional[int] = None
    usu_cveacces: Optional[str] = None
    usu_fechope: Optional[str] = None
    usu_cveemp: Optional[str] = None
    usu_fecha: Optional[str] = None
    usu_dias: Optional[int] = None
    usu_idpersona: Optional[int] = None
    usu_cvemovil: Optional[str] = None


### PncParametrPm ###
@strawberry.type
class PncParametrPmType:
    """Type representation for PncParametrPm model."""

    par_idparameter: int
    par_tipopara: str
    # Keep the ID resolvers for basic compatibility
    par_idenpara_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "par_idenpara"))
    par_idmodulo_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "par_idmodulo"))
    par_idstatus_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "par_idstatus"))
    par_idcveusu_id: Optional[int] = strawberry.field(resolver=lambda root: id_resolver(root, "par_idcveusu"))

    # Add nested type fields for ForeignKey relationships
    @strawberry.field
    def par_idenpara(self) -> CppIdenparaType:
        """Get related CppIdenpara object."""
        return getattr(self, "par_idenpara", None)

    @strawberry.field
    def par_idmodulo(self) -> CppModulosType:
        """Get related CppModulos object."""
        return getattr(self, "par_idmodulo", None)

    @strawberry.field
    def par_idstatus(self) -> CppStatusType:
        """Get related CppStatus object."""
        return getattr(self, "par_idstatus", None)

    @strawberry.field
    def par_idcveusu(self) -> PncUsuariosPmType:
        """Get related PncUsuariosPm object."""
        return getattr(self, "par_idcveusu", None)

    par_descrip1: str
    par_descrip2: str
    par_descrip3: str
    par_descrip4: str
    par_descrip5: str
    par_importe1: Optional[decimal.Decimal] = None
    par_importe2: Optional[decimal.Decimal] = None
    par_importe3: Optional[decimal.Decimal] = None
    par_importe4: Optional[decimal.Decimal] = None
    par_importe5: Optional[decimal.Decimal] = None
    par_fecha1: Optional[str] = None
    par_fecha2: Optional[str] = None
    par_fecha3: Optional[str] = None
    par_hora1: Optional[str] = None
    par_hora2: Optional[str] = None
    par_hora3: Optional[str] = None
    par_fechope: Optional[datetime.datetime] = None
    par_horaope: Optional[datetime.time] = None


@strawberry.enum
class PncParametrPmOrderByField(Enum):
    """Order by field for PncParametrPm model."""

    par_idparameter = "par_idparameter"
    par_descrip1 = "par_descrip1"
    par_idenpara = "par_idenpara"


@strawberry.enum
class PncParametrPmOrderByDirection(Enum):
    """Order by direction for PncParametrPm model."""

    asc = "asc"
    desc = "desc"


@strawberry.input
class PncParametrPmOrderByInput:
    """Order by input for PncParametrPm model."""

    field: Optional[PncParametrPmOrderByField] = None
    direction: Optional[PncParametrPmOrderByDirection] = PncParametrPmOrderByDirection.asc


@strawberry.input
class PncParametrPmFilterInput:
    """Filter input for PncParametrPm model."""

    page: Optional[int] = 1
    per_page: Optional[int] = 10
    par_idparameter: Optional[int] = None
    par_tipopara: Optional[str] = None
    par_idenpara: Optional[int] = None
    par_idenpara__in: Optional[List[int]] = None
    par_idenpara__ne: Optional[int] = None
    par_idmodulo: Optional[int] = None
    par_descrip1: Optional[str] = None
    par_descrip2: Optional[str] = None
    par_descrip2__in: Optional[List[str]] = None
    par_descrip2__not_in: Optional[List[str]] = None
    par_descrip3: Optional[str] = None
    par_descrip3__in: Optional[List[str]] = None
    par_descrip4: Optional[str] = None
    par_descrip5: Optional[str] = None
    par_idstatus: Optional[int] = None
    par_idstatus_cvstatus: Optional[str] = "A"
    par_importe1: Optional[decimal.Decimal] = None
    par_importe1__ne: Optional[decimal.Decimal] = None
    par_importe2: Optional[decimal.Decimal] = None
    par_importe3: Optional[decimal.Decimal] = None
    par_importe4: Optional[decimal.Decimal] = None
    par_importe5: Optional[decimal.Decimal] = None
    par_fecha1: Optional[str] = None
    par_fecha2: Optional[str] = None
    par_fecha3: Optional[str] = None
    par_hora1: Optional[str] = None
    par_hora2: Optional[str] = None
    par_hora3: Optional[str] = None
    par_idcveusu: Optional[int] = None
    par_fechope: Optional[str] = None
    par_horaope: Optional[str] = None
    order_by: Optional[List[PncParametrPmOrderByInput]] = None


@strawberry.input
class PncParametrPmCreateInput:
    """Input for creating a new PncParametrPm instance."""

    par_tipopara: str
    par_idenpara: int
    par_idmodulo: int
    par_descrip1: str
    par_descrip2: str
    par_descrip3: str
    par_descrip4: str
    par_descrip5: str
    par_idstatus: int
    par_importe1: Optional[decimal.Decimal] = None
    par_importe2: Optional[decimal.Decimal] = None
    par_importe3: Optional[decimal.Decimal] = None
    par_importe4: Optional[decimal.Decimal] = None
    par_importe5: Optional[decimal.Decimal] = None
    par_fecha1: Optional[str] = None
    par_fecha2: Optional[str] = None
    par_fecha3: Optional[str] = None
    par_hora1: Optional[str] = None
    par_hora2: Optional[str] = None
    par_hora3: Optional[str] = None
    par_idcveusu: Optional[int] = None


@strawberry.input
class PncParametrPmUpdateInput:
    """Input for updating an existing PncParametrPm instance."""

    par_tipopara: Optional[str] = None
    par_idenpara: Optional[int] = None
    par_idmodulo: Optional[int] = None
    par_descrip1: Optional[str] = None
    par_descrip2: Optional[str] = None
    par_descrip3: Optional[str] = None
    par_descrip4: Optional[str] = None
    par_descrip5: Optional[str] = None
    par_idstatus: Optional[int] = None
    par_importe1: Optional[decimal.Decimal] = None
    par_importe2: Optional[decimal.Decimal] = None
    par_importe3: Optional[decimal.Decimal] = None
    par_importe4: Optional[decimal.Decimal] = None
    par_importe5: Optional[decimal.Decimal] = None
    par_fecha1: Optional[str] = None
    par_fecha2: Optional[str] = None
    par_fecha3: Optional[str] = None
    par_hora1: Optional[str] = None
    par_hora2: Optional[str] = None
    par_hora3: Optional[str] = None
    par_idcveusu: Optional[int] = None


###  ParAdmalm ###
@strawberry.type
class ParAdmalmType:
    """Type representation for ParAdmalm model."""

    adm_idpersona: decimal.Decimal
    adm_almacen: str
    adm_tmov: str
    adm_status: Optional[str] = None
    adm_fechaact: Optional[str] = None
    adm_cveusu: Optional[str] = None
    adm_fechope: Optional[str] = None
    adm_almdefault: Optional[decimal.Decimal] = None
    adm_edorepemi: Optional[int] = None
    adm_uninegemi: Optional[str] = None
    adm_perfil: Optional[int] = None
    adm_edoreprec: Optional[int] = None
    adm_uninegrec: Optional[str] = None
    adm_almrecept: Optional[str] = None
    adm_ordencompra: Optional[str] = None


@strawberry.input
class ParAdmalmFilterInput:
    """Filter input for ParAdmalm model."""

    page: Optional[int] = 1
    per_page: Optional[int] = 10
    search: Optional[str] = None
    adm_idpersona: Optional[decimal.Decimal] = None
    adm_almacen: Optional[str] = None
    adm_tmov: Optional[str] = None
    adm_status: Optional[str] = None
    adm_fechaact: Optional[str] = None
    adm_cveusu: Optional[str] = None
    adm_fechope: Optional[str] = None
    adm_almdefault: Optional[decimal.Decimal] = None
    adm_edorepemi: Optional[str] = None
    adm_uninegemi: Optional[str] = None
    adm_perfil: Optional[int] = None
    adm_edoreprec: Optional[int] = None
    adm_uninegrec: Optional[str] = None
    adm_almrecept: Optional[str] = None
    adm_ordencompra: Optional[str] = None


@strawberry.input
class ParAdmalmSearchPermsFilterInput:
    """Filter input for ParAdmalm model."""

    page: Optional[int] = 1
    per_page: Optional[int] = 10
    adm_perfil: Optional[int] = None
    adm_almacen__in: Optional[List[str]] = None
    adm_status: Optional[str] = None


@strawberry.type
class ParAdmalmSearchPermsResponseType:
    """Response type for ParAdmalm model."""

    per_paterno: Optional[str] = None
    per_materno: Optional[str] = None
    per_nomrazon: Optional[str] = None
    adm_almdefault: Optional[str] = None
    adm_tmov: Optional[str] = None
    adm_almrecept: Optional[str] = None
    adm_uninegrec: Optional[str] = None
    persona: Optional[str] = None
    almacen: Optional[str] = None
    movimiento: Optional[str] = None
    perfil: Optional[str] = None
    estado_rec: Optional[str] = None
    unegocio_rec: Optional[str] = None


@strawberry.input
class ParAdmalmCreateInput:
    """Input for creating a new ParAdmalm instance."""

    adm_idpersona: decimal.Decimal
    adm_almacen: str
    adm_tmov: str
    adm_status: Optional[str] = None
    adm_cveusu: Optional[str] = None
    adm_almdefault: Optional[decimal.Decimal] = None
    adm_edorepemi: Optional[int] = None
    adm_uninegemi: Optional[str] = None
    adm_perfil: Optional[int] = None
    adm_edoreprec: Optional[int] = None
    adm_uninegrec: Optional[str] = None
    adm_almrecept: Optional[str] = None
    adm_ordencompra: Optional[str] = None


@strawberry.input
class ParAdmalmUpdateInput:
    """Input for updating an existing ParAdmalm instance."""

    adm_idpersona: decimal.Decimal
    adm_almacen: str
    adm_tmov: str
    adm_status: Optional[str] = None
    adm_cveusu: Optional[str] = None
    adm_almdefault: Optional[decimal.Decimal] = None
    adm_edorepemi: Optional[int] = None
    adm_uninegemi: Optional[str] = None
    adm_perfil: Optional[int] = None
    adm_edoreprec: Optional[int] = None
    adm_uninegrec: Optional[str] = None
    adm_almrecept: Optional[str] = None
    adm_ordencompra: Optional[str] = None


@strawberry.input
class ParAdmalmApplyAlmPermsInput:
    """Input for applying ALM permissions for a user."""

    adm_idpersona: decimal.Decimal
    adm_almacen: str
    adm_perfil: int
    par_tipopara: str = "VENRP"
    par_descrip1: str
    par_adm_list: Optional[List[ParAdmalmCreateInput]] = None
    pnc_parametr_list: Optional[List[PncParametrPmCreateInput]] = None
    is_default_alm: Optional[bool] = False


@strawberry.type
class ParAdmalmApplyAlmPermsResponseType:
    """Response type for applying ALM permissions for a user."""

    par_adm_list: Optional[List[ParAdmalmType]] = None
    pnc_parametr_list: Optional[List[PncParametrPmType]] = None


@strawberry.input
class ParAdmalmApplyTransferPermsInput:
    """Input for applying transfer permissions for a user."""

    adm_idpersona: Optional[decimal.Decimal] = None
    adm_almacen: Optional[str] = None
    adm_perfil: Optional[int] = None
    adm_tmov__in: Optional[List[str]] = None
    par_tipopara: Optional[str] = None
    par_descrip2: Optional[str] = None
    te_exists: Optional[bool] = False
    ts_exists: Optional[bool] = False
    adm_uninegrec: Optional[str] = None
    par_adm_list: Optional[List[ParAdmalmCreateInput]] = None


### PncUsuarios ###
@strawberry.type
class PncUsuariosType:
    """Type representation for PncUsuarios model."""

    usu_idusuari: str
    usu_apusuari: Optional[str] = None
    usu_amusuari: Optional[str] = None
    usu_nousuari: Optional[str] = None
    usu_depto: str
    usu_cveacces: Optional[str] = None
    usu_status: str
    usu_cveusu: str
    usu_fechope: Optional[str] = None
    usu_cveemp: Optional[str] = None
    usu_puesto: str
    usu_fecha: Optional[str] = None
    usu_dias: Optional[int] = None
    usu_idpersona: Optional[int] = None
    usu_idempresa: str
    usu_cvemovil: Optional[str] = None


@strawberry.input
class PncUsuariosFilterInput:
    """Filter input for PncUsuarios model."""

    page: Optional[int] = 1
    per_page: Optional[int] = 10
    usu_idusuari: Optional[str] = None
    usu_apusuari: Optional[str] = None
    usu_amusuari: Optional[str] = None
    usu_nousuari: Optional[str] = None
    usu_depto: Optional[str] = None
    usu_cveacces: Optional[str] = None
    usu_status: Optional[str] = None
    usu_cveusu: Optional[str] = None
    usu_fechope: Optional[str] = None
    usu_cveemp: Optional[str] = None
    usu_puesto: Optional[str] = None
    usu_fecha: Optional[str] = None
    usu_dias: Optional[int] = None
    usu_idpersona: Optional[int] = None
    usu_idempresa: Optional[str] = None
    usu_cvemovil: Optional[str] = None


### ParObjetivosdet ###
@strawberry.type
class ParObjetivosdetType:
    """Type representation for ParObjetivosdet model."""

    obd_ano: decimal.Decimal
    obd_vendedor: decimal.Decimal
    obd_mes: decimal.Decimal
    obd_venta: Optional[decimal.Decimal] = None
    obd_comision: Optional[decimal.Decimal] = None
    obd_fechope: Optional[str] = None
    obd_horaope: Optional[str] = None
    obd_cveusu: Optional[str] = None
    obd_areavta: Optional[str] = None


@strawberry.input
class ParObjetivosdetFilterInput:
    """Filter input for ParObjetivosdet model."""

    page: Optional[int] = 1
    per_page: Optional[int] = 10
    search: Optional[str] = None
    obd_ano: Optional[decimal.Decimal] = None
    obd_vendedor: Optional[decimal.Decimal] = None
    obd_mes: Optional[decimal.Decimal] = None
    obd_venta: Optional[decimal.Decimal] = None
    obd_comision: Optional[decimal.Decimal] = None
    obd_fechope: Optional[str] = None
    obd_horaope: Optional[str] = None
    obd_cveusu: Optional[str] = None
    obd_areavta: Optional[str] = None


@strawberry.input
class ParObjetivosdetCreateInput:
    """Input for creating a new ParObjetivosdet instance."""

    obd_ano: decimal.Decimal
    obd_vendedor: decimal.Decimal
    obd_mes: decimal.Decimal
    obd_venta: Optional[decimal.Decimal] = None
    obd_comision: Optional[decimal.Decimal] = None
    obd_cveusu: Optional[str] = None
    obd_areavta: Optional[str] = None


@strawberry.input
class ParObjetivosdetUpdateInput:
    """Input for updating an existing ParObjetivosdet instance."""

    obd_venta: Optional[decimal.Decimal] = None
    obd_comision: Optional[decimal.Decimal] = None
    obd_cveusu: Optional[str] = None
    obd_areavta: Optional[str] = None


### ParObjetivos ###
@strawberry.type
class ParObjetivosType:
    """Type representation for ParObjetivos model."""

    obm_ano: decimal.Decimal
    obm_vendedor: decimal.Decimal
    obm_sueldo: Optional[decimal.Decimal] = None
    obm_fechope: Optional[str] = None
    obm_horaope: Optional[str] = None
    obm_cveusu: Optional[str] = None
    # obm_areavta: Optional[str] = None


@strawberry.input
class ParObjetivosFilterInput:
    """Filter input for ParObjetivos model."""

    page: Optional[int] = 1
    per_page: Optional[int] = 10
    search: Optional[str] = None
    obm_ano: Optional[decimal.Decimal] = None
    obm_vendedor: Optional[decimal.Decimal] = None
    obm_sueldo: Optional[decimal.Decimal] = None
    obm_fechope: Optional[str] = None
    obm_horaope: Optional[str] = None
    obm_cveusu: Optional[str] = None
    # obm_areavta: Optional[str] = None


@strawberry.input
class ParObjetivosCreateInput:
    """Input for creating a new ParObjetivos instance."""

    obm_ano: decimal.Decimal
    obm_vendedor: decimal.Decimal
    obm_sueldo: Optional[decimal.Decimal] = None
    obm_cveusu: Optional[str] = None
    # obm_areavta: Optional[str] = None


@strawberry.input
class ParObjetivosUpdateInput:
    """Input for updating an existing ParObjetivos instance."""

    obm_sueldo: Optional[decimal.Decimal] = None
    obm_cveusu: Optional[str] = None
    # obm_areavta: Optional[str] = None


@strawberry.input
class ParObjetivosSaveInput:
    """Input for saving a new ParObjetivos instance and ParObjetivosdet instances."""

    obm_ano: decimal.Decimal
    obm_vendedor: decimal.Decimal
    obm_sueldo: Optional[decimal.Decimal] = None
    obm_cveusu: Optional[str] = None
    # obm_areavta: Optional[str] = None
    obd_list: Optional[List[ParObjetivosdetCreateInput]] = None


### PerRolesPm ###
@strawberry.type
class PerRolesPmType:
    """Type representation for PerRolesPm model."""

    rol_idroles: int
    rol_idpersona: int = strawberry.field(resolver=lambda root: id_resolver(root, "rol_idpersona"))
    rol_idrol: str
    rol_idcveusu: int = strawberry.field(resolver=lambda root: id_resolver(root, "rol_idcveusu"))
    rol_fechope: Optional[str] = None
    rol_idrolsucursal: int = strawberry.field(resolver=lambda root: id_resolver(root, "rol_idrolsucursal"))
    rol_idrolestatus: int


@strawberry.type
class PerRolesPmLiteType:
    """Type representation for PerRolesPmLite model."""

    rol_idrol: str


@strawberry.type
class PerRolesPmPeopleWithRolesResponseType:
    """Type representation for PerRolesPmPeopleWithRolesResponseType model."""

    per_idpersona: Optional[int] = strawberry.field(resolver=lambda root: id_resolver(root, "per_idpersona"))
    per_nomrazon: Optional[str] = None
    per_paterno: Optional[str] = None
    per_materno: Optional[str] = None
    vendedor: str = strawberry.field(
        resolver=lambda root: f"{root.per_nomrazon} {root.per_paterno} {root.per_materno} - {root.per_idpersona}"
    )


@strawberry.type
class PerRolesPmPeopleByRoleResponseType:
    """Type representation for PerRolesPmPeopleByRoleResponseType model."""

    per_idpersona: Optional[int] = strawberry.field(resolver=lambda root: id_resolver(root, "per_idpersona"))
    per_nomrazon: Optional[str] = None
    per_paterno: Optional[str] = None
    per_materno: Optional[str] = None
    vendedor: str = strawberry.field(resolver=lambda root: f"{root.per_nomrazon} {root.per_paterno} {root.per_materno}")


@strawberry.input
class PerRolesPmPeopleByRoleFilterInput:
    """Filter input for PerRolesPmPeopleByRoleResponseType model."""

    page: Optional[int] = 1
    per_page: Optional[int] = 10
    rol_idrol: Optional[str] = None


@strawberry.input
class PerRolesPmFilterInput:
    """Filter input for PerRolesPm model."""

    page: Optional[int] = 1
    per_page: Optional[int] = 10
    search: Optional[str] = None
    rol_idroles: Optional[int] = None
    rol_idpersona: Optional[int] = None
    rol_idrol: Optional[str] = None
    rol_idcveusu: Optional[int] = None
    rol_fechope: Optional[str] = None
    rol_idrolsucursal: Optional[int] = None
    rol_idrolestatus: Optional[int] = None


@strawberry.input
class PerRolesPmByPersonFilterInput:
    """Filter input for PerRolesPm model by person."""

    page: Optional[int] = 1
    per_page: Optional[int] = 10
    par_tipopara: Optional[str] = None
    par_idenpara__in: Optional[List[str]] = None
    par_idstatus_cvstatus: Optional[str] = "A"
    rol_idrolestatus: Optional[int] = None
    rol_idpersona: Optional[int] = None


@strawberry.enum
class PerRolesPmPeopleWithRolesOrderByField(Enum):
    """Order by field for PerRolesPm model by person."""

    per_idpersona = "per_idpersona"
    per_nomrazon = "per_nomrazon"
    per_paterno = "per_paterno"
    per_materno = "per_materno"


@strawberry.enum
class PerRolesPmPeopleWithRolesOrderByDirection(Enum):
    """Order by direction for PerRolesPm model by person."""

    asc = "asc"
    desc = "desc"


@strawberry.input
class PerRolesPmPeopleWithRolesOrderByInput:
    """Order by input for PerRolesPm model by person."""

    field: Optional[PerRolesPmPeopleWithRolesOrderByField] = None
    direction: Optional[PerRolesPmPeopleWithRolesOrderByDirection] = PerRolesPmPeopleWithRolesOrderByDirection.asc


@strawberry.input
class PerRolesPmPeopleWithRolesFilterInput:
    """Filter input for PerRolesPm model by person."""

    page: Optional[int] = 1
    per_page: Optional[int] = 10
    par_tipopara: Optional[str] = None
    par_idenpara__in: Optional[List[str]] = None
    par_idstatus_cvstatus: Optional[str] = "A"
    rol_idrolestatus: Optional[int] = None
    rol_idpersona: Optional[int] = None
    order_by: Optional[List[PerRolesPmPeopleWithRolesOrderByInput]] = None


### DeleteResponseType ###
@strawberry.type
class ParAdmalmDeleteResponseType:
    """Delete response type for ParAdmalm model."""

    success: bool
    message: Optional[str] = None


### Bitacora ###
@strawberry.type
class BitacoraType:
    """Type representation for Bitacora model."""

    bit_id: str
    par_idparameter: Optional[decimal.Decimal] = None
    bit_adm_idpersona: Optional[decimal.Decimal] = None
    bit_adm_almacen: Optional[str] = None
    bit_observaciones: Optional[str] = None
    bit_cveusu: Optional[str] = None
    bit_fechaope: Optional[datetime.datetime] = None
    bit_horaope: Optional[datetime.time] = None


@strawberry.input
class BitacoraFilterInput:
    """Filter type for Bitacora model."""

    page: Optional[int] = 1
    per_page: Optional[int] = 10
    search: Optional[str] = None
    bit_id: Optional[str] = None
    par_idparameter: Optional[decimal.Decimal] = None
    bit_adm_idpersona: Optional[decimal.Decimal] = None
    bit_adm_almacen: Optional[str] = None
    bit_observaciones: Optional[str] = None
    bit_cveusu: Optional[str] = None
    bit_fechaope: Optional[datetime.datetime] = None
    bit_horaope: Optional[datetime.time] = None


@strawberry.input
class BitacoraCreateInput:
    """Input for creating a new Bitacora instance."""

    par_idparameter: Optional[decimal.Decimal] = None
    bit_adm_idpersona: Optional[decimal.Decimal] = None
    bit_adm_almacen: Optional[str] = None
    bit_observaciones: Optional[str] = None
    bit_cveusu: Optional[str] = None


@strawberry.input
class BitacoraUpdateInput:
    """Input for updating an existing Bitacora instance."""

    par_idparameter: Optional[decimal.Decimal] = None
    bit_adm_idpersona: Optional[decimal.Decimal] = None
    bit_adm_almacen: Optional[str] = None
    bit_observaciones: Optional[str] = None
    bit_cveusu: Optional[str] = None


@strawberry.type
class PerPersonasPmType:
    """Type representation for PerPersonasPm model."""

    per_idpersona: decimal.Decimal
    per_rfc: Optional[str] = None
    per_idtipo_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "per_idtipo"))
    per_idtipmoral_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "per_idtipmoral"))
    per_idtitulo_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "per_idtitulo"))
    per_paterno: Optional[str] = None
    per_materno: Optional[str] = None
    per_nomrazon: Optional[str] = None
    per_curp: Optional[str] = None
    per_fecnac: Optional[datetime.datetime] = None
    per_idsexo_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "per_idsexo"))
    per_idedocivil_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "per_idedocivil"))
    per_idsucursal_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "per_idsucursal"))
    per_idmodulalta_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "per_idmodulalta"))
    per_vendedor: str
    per_idcveusu_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "per_idcveusu"))
    per_fechope: Optional[datetime.datetime] = None
    per_vive: Optional[bool] = None
    per_idocupacion_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "per_idocupacion"))
    per_lugnac: Optional[str] = None
    per_idnacionalidad_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "per_idnacionalidad"))
    per_clicon: Optional[str] = None
    per_dealerid: Optional[str] = None
    per_status: str
    per_tpocteref: Optional[str] = None
    per_numprov: Optional[str] = None
    per_lt: Optional[decimal.Decimal] = None
    per_idclientepla: Optional[str] = None
    per_idaviso_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "per_idaviso"))
    per_envio: Optional[bool] = None
    per_rfcnomina: Optional[str] = None
    per_avpriv: Optional[bool] = None
    per_idforpagopred_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "per_idforpagopred"))
    per_ctapagopred: Optional[str] = None
    per_codfan: Optional[int] = None
    per_numife: Optional[str] = None
    per_fecing: Optional[datetime.datetime] = None
    per_horing: Optional[datetime.time] = None
    per_idcveusuing_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "per_idcveusuing"))
    per_idmediocontacto_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "per_idmediocontacto"))
    per_contfav: Optional[str] = None
    per_fechainsc: Optional[datetime.datetime] = None
    per_cveife: Optional[str] = None
    per_idsitpersona_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "per_idsitpersona"))
    per_horaprefcon: Optional[datetime.time] = None
    per_extranjera: Optional[int] = None
    per_horaprefcon2: Optional[datetime.time] = None
    per_idlealtad: Optional[str] = None
    per_metodocontacto: Optional[str] = None
    per_idregimenfiscal_id: int = strawberry.field(resolver=lambda root: id_resolver(root, "per_idregimenfiscal"))
    per_clienteaaa: Optional[bool] = None
    per_relacionsuite: Optional[int] = None
    per_cif: Optional[str] = None


@strawberry.input
class PerPersonasPmFilterInput:
    """Filter type for PerPersonasPm model."""

    page: Optional[int] = 1
    per_page: Optional[int] = 10
    per_idpersona: Optional[decimal.Decimal] = None
