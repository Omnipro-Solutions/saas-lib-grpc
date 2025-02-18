from .catalogs.template import ProductRPCFunction
from .catalogs.template import __all__ as ctemplate
from .clients.address import AddressRPCFunction
from .clients.address import __all__ as caddress
from .clients.client import ClientRPCFunction
from .clients.client import __all__ as cclient
from .rule.compute import ComputeRPCFunction
from .rule.compute import __all__ as rcompute
from .rule.delivery_method import DeliveryMethodRPCFunction
from .rule.delivery_method import __all__ as rdelivery_method
from .sales.order import OrderRPCFunction
from .sales.order import __all__ as sorder
from .stock.picking import PickingRPCFunction
from .stock.picking import __all__ as spicking
from .stock.warehouse import WarehouseRPCFunction
from .stock.warehouse import __all__ as swarehouse
from .users.user import UserRPCFunction
from .users.user import __all__ as uuser
from .utilities.dashboard import DashboardRPCFucntion
from .utilities.dashboard import __all__ as udashboard
from .utilities.event import EventRPCFucntion
from .utilities.event import __all__ as uevent
from .utilities.method import MethodRPCFunction
from .utilities.method import __all__ as umethod
from .utilities.mirror import MirrorModelRPCFucntion
from .utilities.mirror import __all__ as umirror
from .utilities.model import ModelRPCFucntion
from .utilities.model import __all__ as umodel
from .utilities.ms import MicroServiceRPCFunction
from .utilities.ms import __all__ as ums
from .utilities.table_temp import TableTempRPCFunction
from .utilities.table_temp import __all__ as utable_temp
from .utilities.template import TemplateNotificationRPCFucntion
from .utilities.template import __all__ as utemplate
from .utilities.webhook import WebhookRPCFucntion
from .utilities.webhook import __all__ as uwebhook

__all__ = (
    ctemplate
    + caddress
    + cclient
    + rcompute
    + rdelivery_method
    + sorder
    + spicking
    + swarehouse
    + uuser
    + udashboard
    + uevent
    + umethod
    + umirror
    + umodel
    + ums
    + utemplate
    + uwebhook
    + utable_temp
)
