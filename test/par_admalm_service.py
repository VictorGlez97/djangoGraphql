import datetime
import decimal
from typing import List

from django.db import transaction

from ..models import ParAdmalm, PerPersonasPm, PncParametrPm
from ..types import (
    ParAdmalmApplyAlmPermsInput,
    ParAdmalmApplyAlmPermsResponseType,
    ParAdmalmApplyTransferPermsInput,
    ParAdmalmCreateInput,
    ParAdmalmFilterInput,
    ParAdmalmSearchPermsFilterInput,
    ParAdmalmSearchPermsResponseType,
    ParAdmalmUpdateInput,
)


class ParAdmalmService:
    def get_par_admalm_list(self, filter: ParAdmalmFilterInput) -> List[ParAdmalm]:
        """Get all ParAdmalm objects based on the filter."""

        # Get all objects from the model
        queryset = ParAdmalm.objects.all()
        # Filter the objects based on the input parameters
        if filter.search:
            queryset = queryset.filter(adm_almacen__icontains=filter.search)
        if filter.adm_idpersona is not None:
            queryset = queryset.filter(adm_idpersona=filter.adm_idpersona)
        if filter.adm_almacen is not None:
            queryset = queryset.filter(adm_almacen=filter.adm_almacen)
        if filter.adm_tmov is not None:
            queryset = queryset.filter(adm_tmov=filter.adm_tmov)
        if filter.adm_status is not None:
            queryset = queryset.filter(adm_status=filter.adm_status)
        if filter.adm_fechaact is not None:
            queryset = queryset.filter(adm_fechaact=filter.adm_fechaact)
        if filter.adm_cveusu is not None:
            queryset = queryset.filter(adm_cveusu=filter.adm_cveusu)
        if filter.adm_fechope is not None:
            queryset = queryset.filter(adm_fechope=filter.adm_fechope)
        if filter.adm_almdefault is not None:
            queryset = queryset.filter(adm_almdefault=filter.adm_almdefault)
        if filter.adm_edorepemi is not None:
            queryset = queryset.filter(adm_edorepemi=filter.adm_edorepemi)
        if filter.adm_uninegemi is not None:
            queryset = queryset.filter(adm_uninegemi=filter.adm_uninegemi)
        if filter.adm_perfil is not None:
            queryset = queryset.filter(adm_perfil=filter.adm_perfil)
        if filter.adm_edoreprec is not None:
            queryset = queryset.filter(adm_edoreprec=filter.adm_edoreprec)
        if filter.adm_uninegrec is not None:
            queryset = queryset.filter(adm_uninegrec=filter.adm_uninegrec)
        if filter.adm_almrecept is not None:
            queryset = queryset.filter(adm_almrecept=filter.adm_almrecept)
        if filter.adm_ordencompra is not None:
            queryset = queryset.filter(adm_ordencompra=filter.adm_ordencompra)

        # Paginate the results
        offset = (filter.page - 1) * filter.per_page
        # Return the paginated results
        return queryset[offset : offset + filter.per_page]

    def get_par_admalm_search_perms(
        self, filter: ParAdmalmSearchPermsFilterInput
    ) -> List[ParAdmalmSearchPermsResponseType]:
        """Get all ParAdmalm objects based on the filter."""

        # Init data response
        data_response = []

        # Get allowed adm_almacens
        allowed_almacens = filter.adm_almacen__in

        # Get Adm_almacens
        adm_almacens = ParAdmalm.objects.filter(
            adm_perfil=filter.adm_perfil, adm_status=filter.adm_status, adm_almacen__in=allowed_almacens
        ).distinct("adm_idpersona")

        # Iterate over the adm_almacens
        for adm_almacen in adm_almacens:
            # Get per_person_pm
            per_person_pm = PerPersonasPm.objects.filter(per_idpersona=adm_almacen.adm_idpersona).first()

            # Get almacen value
            almacen = (
                PncParametrPm.objects.filter(par_tipopara="SA", par_idenpara=adm_almacen.adm_almacen)
                .first()
                .values("par_descrip1")
            )

            # Get movimiento value
            movimiento = (
                PncParametrPm.objects.filter(par_tipopara="MP", par_idenpara=adm_almacen.adm_tmov)
                .first()
                .values("par_descrip1")
            )

            # Get perfil value
            perfil = (
                PncParametrPm.objects.filter(par_tipopara="PERFREFA", par_idenpara=adm_almacen.adm_perfil)
                .first()
                .values("par_descrip1")
            )

            # Get estado_rec value
            estado_rec = (
                PncParametrPm.objects.filter(par_tipopara="EQUIEDO", par_idenpara=adm_almacen.adm_edoreprec)
                .first()
                .values("par_descrip1")
            )

            # Get unegocio_rec value
            unegocio_rec = (
                PncParametrPm.objects.filter(par_tipopara="UNINEG", par_descrip5=adm_almacen.adm_uninegrec)
                .first()
                .values("par_descrip1")
            )

            # Add data to data_response
            data_response.append(
                ParAdmalmSearchPermsResponseType(
                    per_paterno=per_person_pm.per_paterno if per_person_pm.per_paterno else "",
                    per_materno=per_person_pm.per_materno if per_person_pm.per_materno else "",
                    per_nomrazon=per_person_pm.per_nomrazon if per_person_pm.per_nomrazon else "",
                    adm_almdefault=adm_almacen.adm_almdefault if adm_almacen.adm_almdefault else "",
                    adm_tmov=adm_almacen.adm_tmov if adm_almacen.adm_tmov else "",
                    adm_almrecept=adm_almacen.adm_almrecept if adm_almacen.adm_almrecept else "",
                    adm_uninegrec=adm_almacen.adm_uninegrec if adm_almacen.adm_uninegrec else "",
                    persona=f"{per_person_pm.per_paterno} {per_person_pm.per_materno} {per_person_pm.per_nomrazon}"
                    if per_person_pm
                    else "",
                    almacen=almacen if almacen else "",
                    movimiento=movimiento if movimiento else "",
                    perfil=perfil if perfil else "",
                    estado_rec=estado_rec if estado_rec else "",
                    unegocio_rec=unegocio_rec if unegocio_rec else "",
                )
            )

        return data_response

    def create_par_admalm(self, input: ParAdmalmCreateInput) -> ParAdmalm:
        """Create a new ParAdmalm object."""

        par_admalm = ParAdmalm(
            adm_idpersona=input.adm_idpersona,
            adm_almacen=input.adm_almacen,
            adm_tmov=input.adm_tmov,
            adm_status=input.adm_status,
            adm_fechaact=datetime.datetime.now().date(),
            adm_cveusu=input.adm_cveusu,
            adm_fechope=datetime.datetime.now().date(),
            adm_almdefault=input.adm_almdefault,
            adm_edorepemi=input.adm_edorepemi,
            adm_uninegemi=input.adm_uninegemi,
            adm_perfil=input.adm_perfil,
            adm_edoreprec=input.adm_edoreprec,
            adm_uninegrec=input.adm_uninegrec,
            adm_almrecept=input.adm_almrecept,
            adm_ordencompra=input.adm_ordencompra,
        )
        par_admalm.save()
        return par_admalm

    def update_par_admalm(
        self, adm_idpersona: decimal.Decimal, adm_almacen: str, input: ParAdmalmUpdateInput
    ) -> ParAdmalm:
        """Update a ParAdmalm object."""

        par_admalm = ParAdmalm.objects.get(adm_idpersona=adm_idpersona, adm_almacen=adm_almacen)
        if input.adm_tmov is not None:
            par_admalm.adm_tmov = input.adm_tmov
        if input.adm_status is not None:
            par_admalm.adm_status = input.adm_status
        if input.adm_cveusu is not None:
            par_admalm.adm_cveusu = input.adm_cveusu
        if input.adm_almdefault is not None:
            par_admalm.adm_almdefault = input.adm_almdefault
        if input.adm_edorepemi is not None:
            par_admalm.adm_edorepemi = input.adm_edorepemi
        if input.adm_uninegemi is not None:
            par_admalm.adm_uninegemi = input.adm_uninegemi
        if input.adm_perfil is not None:
            par_admalm.adm_perfil = input.adm_perfil
        if input.adm_edoreprec is not None:
            par_admalm.adm_edoreprec = input.adm_edoreprec
        if input.adm_uninegrec is not None:
            par_admalm.adm_uninegrec = input.adm_uninegrec
        if input.adm_almrecept is not None:
            par_admalm.adm_almrecept = input.adm_almrecept
        if input.adm_ordencompra is not None:
            par_admalm.adm_ordencompra = input.adm_ordencompra
        par_admalm.adm_fechaact = datetime.datetime.now().date()
        par_admalm.adm_fechope = datetime.datetime.now().date()
        par_admalm.save()
        return par_admalm

    def apply_par_admalm_perms(self, input: ParAdmalmApplyAlmPermsInput) -> ParAdmalmApplyAlmPermsResponseType:
        """Apply par_admalm permissions for a user."""

        # Init transaction
        with transaction.atomic():
            try:
                # Init par_adm_object_list
                par_adm_objects = []
                # Delete existing par_admalm objects
                ParAdmalm.objects.filter(
                    adm_idpersona=input.adm_idpersona, adm_almacen=input.adm_almacen, adm_perfil=input.adm_perfil
                ).delete()

                # Delete existing pnc_parametr_pm objects
                PncParametrPm.objects.filter(par_tipopara=input.par_tipopara, par_descrip1=input.par_descrip1).delete()

                # Update par_admalm information if is_default_alm is True
                if input.is_default_alm:
                    ParAdmalm.objects.filter(adm_idpersona=input.adm_idpersona, adm_perfil=input.adm_perfil).exclude(
                        adm_almacen=input.adm_almacen
                    ).update(adm_almdefault=0)

                # Iterate par_adm_list
                for par_adm_input in input.par_adm_list:
                    # Create new par_admalm object
                    par_admalm = ParAdmalm(
                        adm_idpersona=par_adm_input.adm_idpersona,
                        adm_almacen=par_adm_input.adm_almacen,
                        adm_tmov=par_adm_input.adm_tmov,
                        adm_status=par_adm_input.adm_status,
                        adm_fechaact=datetime.datetime.now().date(),
                        adm_cveusu=par_adm_input.adm_cveusu,
                        adm_fechope=datetime.datetime.now().date(),
                        adm_almdefault=par_adm_input.adm_almdefault,
                        adm_perfil=par_adm_input.adm_perfil,
                        adm_edorepemi=par_adm_input.adm_edorepemi,
                        adm_uninegemi=par_adm_input.adm_uninegemi,
                        adm_edoreprec=par_adm_input.adm_edoreprec,
                        adm_uninegrec=par_adm_input.adm_uninegrec,
                        adm_almrecept=par_adm_input.adm_almrecept,
                        adm_ordencompra=par_adm_input.adm_ordencompra,
                    )
                    par_admalm.save()
                    # Add par_admalm to par_adm_objects
                    par_adm_objects.append(par_admalm)

                # Init response pnc_parametr_object_list
                pnc_parametr_objects = []

                # Iterate pnc_parametr_list
                for pnc_parametr_input in input.pnc_parametr_list:
                    # Create new pnc_parametr_pm object
                    pnc_parametr = PncParametrPm(
                        par_tipopara=pnc_parametr_input.par_tipopara,
                        par_idenpara=pnc_parametr_input.par_idenpara,
                        par_idmodulo=pnc_parametr_input.par_idmodulo,
                        par_descrip1=pnc_parametr_input.par_descrip1,
                        par_descrip2=pnc_parametr_input.par_descrip2,
                        par_descrip3=pnc_parametr_input.par_descrip3,
                        par_descrip4=pnc_parametr_input.par_descrip4,
                        par_descrip5=pnc_parametr_input.par_descrip5,
                        par_idstatus=pnc_parametr_input.par_idstatus,
                        par_importe1=pnc_parametr_input.par_importe1,
                        par_importe2=pnc_parametr_input.par_importe2,
                        par_importe3=pnc_parametr_input.par_importe3,
                        par_importe4=pnc_parametr_input.par_importe4,
                        par_importe5=pnc_parametr_input.par_importe5,
                        par_fecha1=pnc_parametr_input.par_fecha1,
                        par_fecha2=pnc_parametr_input.par_fecha2,
                        par_fecha3=pnc_parametr_input.par_fecha3,
                        par_hora1=pnc_parametr_input.par_hora1,
                        par_hora2=pnc_parametr_input.par_hora2,
                        par_hora3=pnc_parametr_input.par_hora3,
                        par_idcveusu=pnc_parametr_input.par_idcveusu,
                        par_fechope=datetime.datetime.now().date(),
                        par_horaope=datetime.datetime.now().time(),
                    )
                    pnc_parametr.save()
                    # Add pnc_parametr to pnc_parametr_objects
                    pnc_parametr_objects.append(pnc_parametr)

                # Return the response type
                return ParAdmalmApplyAlmPermsResponseType(
                    par_adm_list=par_adm_objects, pnc_parametr_list=pnc_parametr_objects
                )
            except Exception as e:
                transaction.rollback()
                raise e

    def apply_par_admalm_transfer_perms(self, input: ParAdmalmApplyTransferPermsInput) -> List[ParAdmalm]:
        """Apply par_admalm transfer permissions for a user."""

        # Init transaction
        with transaction.atomic():
            try:
                # Init par_admalm_list
                par_admalm_list = []
                # Get pnc_parametr_pm par_idenpara list
                par_idenpara_list = PncParametrPm.objects.filter(
                    par_tipopara=input.par_tipopara, par_descrip2__in=[input.par_descrip2]
                ).values_list("par_idenpara__caip_enpara", flat=True)
                if input.te_exists:
                    # Delete existing par_admalm objects
                    ParAdmalm.objects.filter(
                        adm_idpersona=input.adm_idpersona,
                        adm_almacen=input.adm_almacen,
                        adm_perfil=input.adm_perfil,
                        adm_tmov__in=par_idenpara_list,
                    ).delete()
                if input.ts_exists:
                    # Delete existing par_admalm objects
                    ParAdmalm.objects.filter(
                        adm_idpersona=input.adm_idpersona,
                        adm_almacen=input.adm_almacen,
                        adm_perfil=input.adm_perfil,
                        adm_uninegrec=input.adm_uninegrec,
                        adm_tmov__in=par_idenpara_list,
                    ).delete()

                # Iterate par_adm_list
                for par_adm_input in input.par_adm_list:
                    # Create new par_admalm object
                    par_admalm = ParAdmalm(
                        adm_idpersona=par_adm_input.adm_idpersona,
                        adm_almacen=par_adm_input.adm_almacen,
                        adm_tmov=par_adm_input.adm_tmov,
                        adm_status=par_adm_input.adm_status,
                        adm_fechaact=datetime.datetime.now().date(),
                        adm_cveusu=par_adm_input.adm_cveusu,
                        adm_fechope=datetime.datetime.now().date(),
                        adm_almdefault=par_adm_input.adm_almdefault,
                        adm_perfil=par_adm_input.adm_perfil,
                        adm_edorepemi=par_adm_input.adm_edorepemi,
                        adm_uninegemi=par_adm_input.adm_uninegemi,
                        adm_edoreprec=par_adm_input.adm_edoreprec,
                        adm_uninegrec=par_adm_input.adm_uninegrec,
                        adm_almrecept=par_adm_input.adm_almrecept,
                        adm_ordencompra=par_adm_input.adm_ordencompra,
                    )
                    par_admalm.save()
                    # Add par_admalm to par_admalm_list
                    par_admalm_list.append(par_admalm)

                # Return the par_admalm_list
                return par_admalm_list
            except Exception as e:
                transaction.rollback()
                raise e

    def delete_par_admalm(self, adm_idpersona: decimal.Decimal, adm_almacen: str) -> dict:
        """Delete a ParAdmalm object."""

        try:
            par_admalm = ParAdmalm.objects.get(adm_idpersona=adm_idpersona, adm_almacen=adm_almacen)
            par_admalm.delete()
            return True
        except ParAdmalm.DoesNotExist:
            return False
