"""MDO4KB device driver module."""

from tm_devices.commands import MDO4KBMixin
from tm_devices.drivers.scopes.tekscope_3k_4k.mdo4k import MDO4K


class MDO4KB(MDO4KBMixin, MDO4K):  # pyright: ignore[reportIncompatibleVariableOverride]
    """MDO4KB device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################