import decimal
from typing import List

import strawberry

from .services.bit_bitacora_service import BitacoraService
from .services.cpp_idenpara_service import CppIdenparaService
from .services.cpp_status_service import CppStatusService
from .services.par_admalm_service import ParAdmalmService
from .services.par_objetivos_service import ParObjetivosService
from .services.par_objetivosdet_service import ParObjetivosdetService
from .services.per_personaspm_service import PerPersonasPmService
from .services.per_rolespm_service import PerRolesPmService
from .services.pnc_parametrpm_service import PncParametrPmService
from .services.pnc_usuarios_service import PncUsuariosService
from .services.pnc_usuariospm_service import PncUsuariosPmService
from .types import (
    BitacoraCreateInput,
    BitacoraFilterInput,
    BitacoraType,
    BitacoraUpdateInput,
    CppIdenparaFilterInput,
    CppIdenparaType,
    CppStatusFilterInput,
    CppStatusType,
    ParAdmalmApplyAlmPermsInput,
    ParAdmalmApplyAlmPermsResponseType,
    ParAdmalmApplyTransferPermsInput,
    ParAdmalmCreateInput,
    ParAdmalmDeleteResponseType,
    ParAdmalmFilterInput,
    ParAdmalmSearchPermsFilterInput,
    ParAdmalmSearchPermsResponseType,
    ParAdmalmType,
    ParAdmalmUpdateInput,
    ParObjetivosCreateInput,
    ParObjetivosdetCreateInput,
    ParObjetivosdetFilterInput,
    ParObjetivosdetType,
    ParObjetivosdetUpdateInput,
    ParObjetivosFilterInput,
    ParObjetivosSaveInput,
    ParObjetivosType,
    ParObjetivosUpdateInput,
    PerPersonasPmFilterInput,
    PerPersonasPmType,
    PerRolesPmByPersonFilterInput,
    PerRolesPmFilterInput,
    PerRolesPmPeopleByRoleFilterInput,
    PerRolesPmPeopleByRoleResponseType,
    PerRolesPmPeopleWithRolesFilterInput,
    PerRolesPmPeopleWithRolesResponseType,
    PerRolesPmType,
    PncParametrPmCreateInput,
    PncParametrPmFilterInput,
    PncParametrPmType,
    PncParametrPmUpdateInput,
    PncUsuariosFilterInput,
    PncUsuariosPmFilterInput,
    PncUsuariosPmType,
    PncUsuariosType,
)


# Generate strawberry type "Query" from the PncParametrPm model
@strawberry.type
class PncParametrPmQuery:
    @strawberry.field
    def get_all_pnc_parametrpm_paginator(self, info, filter: PncParametrPmFilterInput) -> List[PncParametrPmType]:
        """Get all PncParametrPm instances with pagination."""
        pnc_parametrpm_service = PncParametrPmService()
        return pnc_parametrpm_service.get_pnc_parametrpm_list(filter=filter)


# Generate strawberry type "Mutation" from the PncParametrPm model
@strawberry.type
class PncParametrPmMutation:
    @strawberry.field
    def create_pnc_parametrpm(self, input: PncParametrPmCreateInput) -> PncParametrPmType:
        """Create a new PncParametrPm instance."""
        pnc_parametrpm_service = PncParametrPmService()
        return pnc_parametrpm_service.create_pnc_parametrpm(data=input)

    @strawberry.field
    def update_pnc_parametrpm(self, par_idparameter: int, input: PncParametrPmUpdateInput) -> PncParametrPmType:
        """Update an existing PncParametrPm instance."""
        pnc_parametrpm_service = PncParametrPmService()
        return pnc_parametrpm_service.update_pnc_parametrpm(par_idparameter=par_idparameter, data=input)

    @strawberry.field
    def delete_pnc_parametrpm(self, par_idparameter: int) -> ParAdmalmDeleteResponseType:
        """Delete a PncParametrPm instance."""
        pnc_parametrpm_service = PncParametrPmService()
        if pnc_parametrpm_service.delete_pnc_parametrpm(par_idparameter=par_idparameter):
            return ParAdmalmDeleteResponseType(
                success=True,
                message=f"Parámetro {par_idparameter} eliminado correctamente.",
            )
        else:
            return ParAdmalmDeleteResponseType(success=False, message=f"Parámetro {par_idparameter} no encontrado.")


# Generate strawberry type "Query" from the ParAdmalm model
@strawberry.type
class ParAdmalmQuery:
    # Generate strawberry field "get_all_par_admalm_paginator" from the model
    @strawberry.field
    def get_all_par_admalm_paginator(self, info, filter: ParAdmalmFilterInput) -> List[ParAdmalmType]:
        par_admalm_service = ParAdmalmService()
        return par_admalm_service.get_par_admalm_list(filter=filter)

    @strawberry.field
    def get_par_admalm_search_perms(
        self, info, filter: ParAdmalmSearchPermsFilterInput
    ) -> List[ParAdmalmSearchPermsResponseType]:
        par_admalm_service = ParAdmalmService()
        return par_admalm_service.get_par_admalm_search_perms(filter=filter)


# Generate strawberry type "Mutation" from the ParAdmalm model
@strawberry.type
class ParAdmalmMutation:
    # Generate strawberry field "create_par_admalm" from the model
    @strawberry.field
    def create_par_admalm(self, par_admalm_input: ParAdmalmCreateInput) -> ParAdmalmType:
        par_admalm_service = ParAdmalmService()
        return par_admalm_service.create_par_admalm(input=par_admalm_input)

    # Generate strawberry field "update_par_admalm" from the model
    @strawberry.field
    def update_par_admalm(
        self, adm_idpersona: decimal.Decimal, adm_almacen: str, par_admalm_input: ParAdmalmUpdateInput
    ) -> ParAdmalmType:
        par_admalm_service = ParAdmalmService()
        return par_admalm_service.update_par_admalm(
            adm_idpersona=adm_idpersona, adm_almacen=adm_almacen, input=par_admalm_input
        )

    # Generate strawberry field "delete_par_admalm" from the model
    @strawberry.field
    def delete_par_admalm(self, adm_idpersona: decimal.Decimal, adm_almacen: str) -> ParAdmalmDeleteResponseType:
        par_admalm_service = ParAdmalmService()
        if par_admalm_service.delete_par_admalm(adm_idpersona=adm_idpersona, adm_almacen=adm_almacen):
            return ParAdmalmDeleteResponseType(
                success=True,
                message=f"Administrador de almacen {adm_idpersona} y almacen {adm_almacen} eliminado correctamente.",
            )
        else:
            return ParAdmalmDeleteResponseType(
                success=False,
                message=f"Administrador de almacen {adm_idpersona} y almacen {adm_almacen} no encontrado.",
            )

    @strawberry.field
    def apply_par_admalm_perms(self, input: ParAdmalmApplyAlmPermsInput) -> ParAdmalmApplyAlmPermsResponseType:
        par_admalm_service = ParAdmalmService()
        return par_admalm_service.apply_par_admalm_perms(input=input)

    @strawberry.field
    def apply_par_admalm_transfer_perms(self, input: ParAdmalmApplyTransferPermsInput) -> List[ParAdmalmType]:
        par_admalm_service = ParAdmalmService()
        return par_admalm_service.apply_par_admalm_transfer_perms(input=input)


# Generate strawberry type "Query" from the ParObjetivos model
@strawberry.type
class ParObjetivosQuery:
    @strawberry.field
    # Generate strawberry field "get_all_par_objetivos_paginator" from the model
    def get_all_par_objetivos_paginator(self, info, filter: ParObjetivosFilterInput) -> List[ParObjetivosType]:
        par_objetivos_service = ParObjetivosService()
        return par_objetivos_service.get_par_objetivos_list(filter=filter)


# Generate strawberry type "Mutation" from the ParObjetivos model
@strawberry.type
class ParObjetivosMutation:
    # Generate strawberry field "create_par_objetivos" from the model
    @strawberry.field
    def create_par_objetivos(self, par_objetivos_input: ParObjetivosCreateInput) -> ParObjetivosType:
        par_objetivos_service = ParObjetivosService()
        return par_objetivos_service.create_par_objetivos(input=par_objetivos_input)

    # Generate strawberry field "update_par_objetivos" from the model
    @strawberry.field
    def update_par_objetivos(
        self,
        obm_ano: decimal.Decimal,
        obm_vendedor: decimal.Decimal,
        par_objetivos_input: ParObjetivosUpdateInput,
    ) -> ParObjetivosType:
        par_objetivos_service = ParObjetivosService()
        return par_objetivos_service.update_par_objetivos(
            obm_ano=obm_ano, obm_vendedor=obm_vendedor, par_objetivos_input=par_objetivos_input
        )

    # Generate strawberry field "delete_par_objetivos" from the model
    @strawberry.field
    def delete_par_objetivos(
        self, obm_ano: decimal.Decimal, obm_vendedor: decimal.Decimal
    ) -> ParAdmalmDeleteResponseType:
        par_objetivos_service = ParObjetivosService()
        if par_objetivos_service.delete_par_objetivos(obm_ano=obm_ano, obm_vendedor=obm_vendedor):
            return ParAdmalmDeleteResponseType(
                success=True,
                message=f"Objetivo {obm_ano}-{obm_vendedor} eliminado correctamente.",
            )
        else:
            return ParAdmalmDeleteResponseType(
                success=False,
                message=f"Objetivo {obm_ano}-{obm_vendedor} no encontrado.",
            )

    # Generate strawberry field "save_par_objetivos" from the model
    @strawberry.field
    def save_par_objetivos(self, input: ParObjetivosSaveInput) -> ParObjetivosType:
        par_objetivos_service = ParObjetivosService()
        return par_objetivos_service.save_par_objetivos(input=input)


# Generate strawberry type "Query" from the ParObjetivosdet model
@strawberry.type
class ParObjetivosdetQuery:
    @strawberry.field
    # Generate strawberry field "get_all_par_objetivosdet_paginator" from the model
    def get_all_par_objetivosdet_paginator(self, info, filter: ParObjetivosdetFilterInput) -> List[ParObjetivosdetType]:
        par_objetivosdet_service = ParObjetivosdetService()
        return par_objetivosdet_service.get_par_objetivosdet_list(filter=filter)


# Generate strawberry type "Mutation" from the ParObjetivosdet model
@strawberry.type
class ParObjetivosdetMutation:
    # Generate strawberry field "create_par_objetivosdet" from the model
    @strawberry.field
    def create_par_objetivosdet(
        self,
        par_objetivosdet_input: ParObjetivosdetCreateInput,
    ) -> ParObjetivosdetType:
        par_objetivosdet_service = ParObjetivosdetService()
        return par_objetivosdet_service.create_par_objetivosdet(input=par_objetivosdet_input)

    # Generate strawberry field "update_par_objetivosdet" from the model
    @strawberry.field
    def update_par_objetivosdet(
        self,
        obd_ano: decimal.Decimal,
        obd_vendedor: decimal.Decimal,
        obd_mes: decimal.Decimal,
        par_objetivosdet_input: ParObjetivosdetUpdateInput,
    ) -> ParObjetivosdetType:
        par_objetivosdet_service = ParObjetivosdetService()
        return par_objetivosdet_service.update_par_objetivosdet(
            obd_ano=obd_ano, obd_vendedor=obd_vendedor, obd_mes=obd_mes, input=par_objetivosdet_input
        )

    # Generate strawberry field "delete_par_objetivosdet" from the model
    @strawberry.field
    def delete_par_objetivosdet(
        self,
        obd_ano: decimal.Decimal,
        obd_vendedor: decimal.Decimal,
        obd_mes: decimal.Decimal,
    ) -> ParAdmalmDeleteResponseType:
        par_objetivosdet_service = ParObjetivosdetService()
        if par_objetivosdet_service.delete_par_objetivosdet(
            obd_ano=obd_ano, obd_vendedor=obd_vendedor, obd_mes=obd_mes
        ):
            return ParAdmalmDeleteResponseType(
                success=True,
                message=f"Detalle de objetivo {obd_ano}-{obd_vendedor}-{obd_mes} eliminado correctamente.",
            )
        else:
            return ParAdmalmDeleteResponseType(
                success=False,
                message=f"Detalle de objetivo {obd_ano}-{obd_vendedor}-{obd_mes} no encontrado.",
            )


# Generate strawberry type "Query" from the Bitacora model
@strawberry.type
class BitBitacoraQuery:
    @strawberry.field
    def get_all_bitacora_paginator(self, info, filter: BitacoraFilterInput) -> List[BitacoraType]:
        # Get the bitacora service
        bitacora_service = BitacoraService()
        # Return the bitacora list
        return bitacora_service.get_bitacora_list(filter=filter)


# Generate strawberry type "Mutation" from the Bitacora model
@strawberry.type
class BitBitacoraMutation:
    # Generate strawberry field "create_bitacora" from the model
    @strawberry.field
    def create_bitacora(self, bitacora_input: BitacoraCreateInput) -> BitacoraType:
        # Get the bitacora service
        bitacora_service = BitacoraService()
        # Return the bitacora
        return bitacora_service.create_bitacora(data=bitacora_input)

    # Generate strawberry field "update_bitacora" from the model
    @strawberry.field
    def update_bitacora(self, bit_id: int, bitacora_input: BitacoraUpdateInput) -> BitacoraType:
        # Get the bitacora service
        bitacora_service = BitacoraService()
        # Return the bitacora
        return bitacora_service.update_bitacora(bit_id=bit_id, data=bitacora_input)

    # Generate strawberry field "delete_bitacora" from the model
    @strawberry.field
    def delete_bitacora(self, bit_id: int) -> ParAdmalmDeleteResponseType:
        # Get the bitacora service
        bitacora_service = BitacoraService()
        # Return the bitacora
        if bitacora_service.delete_bitacora(bit_id=bit_id):
            return ParAdmalmDeleteResponseType(success=True, message=f"Bitacora {bit_id} eliminada correctamente.")
        else:
            return ParAdmalmDeleteResponseType(success=False, message=f"Bitacora {bit_id} no encontrada.")


# Generate strawberry type "Query" from the PerPersonasPm model
@strawberry.type
class PerPersonasPmQuery:
    @strawberry.field
    def get_all_per_personaspm_paginator(self, info, filter: PerPersonasPmFilterInput) -> List[PerPersonasPmType]:
        per_personaspm_service = PerPersonasPmService()
        return per_personaspm_service.get_per_personaspm_list(filter=filter)


# Generate strawberry type "Query" from the PncUsuarios model
@strawberry.type
class PncUsuariosQuery:
    @strawberry.field
    def get_all_pnc_usuarios_paginator(self, info, filter: PncUsuariosFilterInput) -> List[PncUsuariosType]:
        pnc_usuarios_service = PncUsuariosService()
        return pnc_usuarios_service.get_pnc_usuarios_list(filter=filter)


# Generate strawberry type "Query" from the CppStatus model
@strawberry.type
class CppStatusQuery:
    @strawberry.field
    def get_all_cpp_status_paginator(self, info, filter: CppStatusFilterInput) -> List[CppStatusType]:
        cpp_status_service = CppStatusService()
        return cpp_status_service.get_cpp_status_list(filter=filter)


# Generate strawberry type "Query" from the PerRolesPm model
@strawberry.type
class PerRolesPmQuery:
    @strawberry.field
    def get_all_per_rolespm_paginator(self, info, filter: PerRolesPmFilterInput) -> List[PerRolesPmType]:
        per_rolespm_service = PerRolesPmService()
        return per_rolespm_service.get_per_rolespm_list(filter=filter)

    @strawberry.field
    def get_per_rolespm_by_person(self, info, filter: PerRolesPmByPersonFilterInput) -> List[PerRolesPmType]:
        per_rolespm_service = PerRolesPmService()
        return per_rolespm_service.get_per_rolespm_by_person(filter=filter)

    @strawberry.field
    def get_per_rolespm_people_with_roles(
        self, info, filter: PerRolesPmPeopleWithRolesFilterInput
    ) -> List[PerRolesPmPeopleWithRolesResponseType]:
        per_rolespm_service = PerRolesPmService()
        return per_rolespm_service.get_per_rolespm_people_with_roles(filter=filter)

    @strawberry.field
    def get_per_rolespm_people_by_role(
        self, info, filter: PerRolesPmPeopleByRoleFilterInput
    ) -> List[PerRolesPmPeopleByRoleResponseType]:
        per_rolespm_service = PerRolesPmService()
        return per_rolespm_service.get_per_rolespm_people_by_role(filter=filter)


# Generate strawberry type "Query" from the PncUsuariosPm model
@strawberry.type
class PncUsuariosPmQuery:
    @strawberry.field
    def get_all_pnc_usuariospm_paginator(self, info, filter: PncUsuariosPmFilterInput) -> List[PncUsuariosPmType]:
        pnc_usuariospm_service = PncUsuariosPmService()
        return pnc_usuariospm_service.get_pnc_usuariospm_list(filter=filter)


# Generate strawberry type "Query" from the CppIdenpara model
@strawberry.type
class CppIdenparaQuery:
    @strawberry.field
    def get_all_cpp_idenpara_paginator(self, info, filter: CppIdenparaFilterInput) -> List[CppIdenparaType]:
        cpp_idenpara_service = CppIdenparaService()
        return cpp_idenpara_service.get_cpp_idenpara_list(filter=filter)
