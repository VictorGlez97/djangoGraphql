import datetime
from typing import List

from ..models import Bitacora
from ..types import BitacoraCreateInput, BitacoraFilterInput, BitacoraUpdateInput


class BitacoraService:
    def get_bitacora_list(self, filter: BitacoraFilterInput) -> List[Bitacora]:
        # Get all objects from the model
        queryset = Bitacora.objects.all()
        # Filter the objects based on the input parameters
        if filter.bit_id:
            queryset = queryset.filter(bit_id=filter.bit_id)
        if filter.par_idparameter:
            queryset = queryset.filter(par_idparameter=filter.par_idparameter)
        if filter.bit_adm_idpersona:
            queryset = queryset.filter(bit_adm_idpersona=filter.bit_adm_idpersona)
        if filter.bit_adm_almacen:
            queryset = queryset.filter(bit_adm_almacen=filter.bit_adm_almacen)
        if filter.bit_observaciones:
            queryset = queryset.filter(bit_observaciones__icontains=filter.bit_observaciones)
        if filter.bit_cveusu:
            queryset = queryset.filter(bit_cveusu=filter.bit_cveusu)
        if filter.bit_fechaope:
            queryset = queryset.filter(bit_fechaope=filter.bit_fechaope)
        offset = (filter.page - 1) * filter.per_page
        # Return the paginated results
        return queryset[offset : offset + filter.per_page]

    def create_bitacora(self, data: BitacoraCreateInput) -> Bitacora:
        bitacora = Bitacora(
            par_idparameter=data.par_idparameter,
            bit_adm_idpersona=data.bit_adm_idpersona,
            bit_adm_almacen=data.bit_adm_almacen,
            bit_observaciones=data.bit_observaciones,
            bit_cveusu=data.bit_cveusu,
            bit_fechaope=datetime.datetime.now().date(),
            bit_horaope=datetime.datetime.now().time(),
        )
        bitacora.save()
        return bitacora

    def update_bitacora(self, bit_id: int, data: BitacoraUpdateInput) -> Bitacora:
        bitacora = Bitacora.objects.get(bit_id=bit_id)
        if data.par_idparameter is not None:
            bitacora.par_idparameter = data.par_idparameter
        if data.bit_adm_idpersona is not None:
            bitacora.bit_adm_idpersona = data.bit_adm_idpersona
        if data.bit_adm_almacen is not None:
            bitacora.bit_adm_almacen = data.bit_adm_almacen
        if data.bit_observaciones is not None:
            bitacora.bit_observaciones = data.bit_observaciones
        if data.bit_cveusu is not None:
            bitacora.bit_cveusu = data.bit_cveusu
        bitacora.save()
        return bitacora

    def delete_bitacora(self, bit_id: int) -> bool:
        try:
            bitacora = Bitacora.objects.get(bit_id=bit_id)
            bitacora.delete()
            return True
        except Bitacora.DoesNotExist:
            return False
        except Exception as e:
            print(e)
            return False
