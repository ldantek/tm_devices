"""The allev commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC,
DSA70KC, DSA70KD, LPD6, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4B, MSO4K,
MSO4KB, MSO5, MSO5B, MSO5K, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ALLEv?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Allev(SCPICmdRead):
    """The ``ALLEv`` command.

    Description:
        - This query-only command prompts the instrument to return all events and their messages
          (delimited by commas), and removes the returned events from the Event Queue. Use the
          ``*ESR?`` query to enable the events to be returned. This command is similar to repeatedly
          sending ``*EVMsg?`` queries to the instrument.

    Usage:
        - Using the ``.query()`` method will send the ``ALLEv?`` query.
        - Using the ``.verify(value)`` method will send the ``ALLEv?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ALLEv?
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "ALLEv") -> None:
        super().__init__(device, cmd_syntax)
