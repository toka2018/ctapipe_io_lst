"""
Container structures for data that should be read or written to disk
"""
from astropy import units as u

from ctapipe.core import Container, Field, Map
from ctapipe.io.containers import DataContainer, MonitoringContainer


__all__ = [
    'LSTEventContainer',
    'LSTMonitoringContainer',
    'LSTServiceContainer',
    'LSTCameraContainer',
    'LSTContainer',
    'LSTMonitoringContainer',
    'LSTDataContainer'
]


class LSTServiceContainer(Container):
    """
    Container for Fields that are specific to each LST camera configuration
    """

    # Data from the CameraConfig table
    telescope_id = Field(-1, "telescope id")
    cs_serial = Field(None, "serial number of the camera server")
    configuration_id = Field(None, "id of the CameraConfiguration")
    date = Field(None, "NTP start of run date")
    num_pixels = Field(-1, "number of pixels")
    num_samples = Field(-1, "num samples")
    pixel_ids = Field([], "id of the pixels in the waveform array")
    data_model_version = Field(None, "data model version")

    idaq_version = Field(0o0, "idaq version")
    cdhs_version = Field(0o0, "cdhs version")
    algorithms = Field(None, "algorithms")
    pre_proc_algorithms = Field(None, "pre processing algorithms")
    module_ids = Field([], "module ids")
    num_modules = Field(-1, "number of modules")


class LSTEventContainer(Container):
    """
    Container for Fields that are specific to each LST event
    """

    # Data from the CameraEvent table
    configuration_id = Field(None, "id of the CameraConfiguration")
    event_id = Field(None, "local id of the event")
    tel_event_id = Field(None, "global id of the event")
    pixel_status = Field([], "status of the pixels (n_pixels)")
    ped_id = Field(None, "tel_event_id of the event used for pedestal substraction")
    module_status = Field([], "status of the modules (n_modules)")
    extdevices_presence = Field(None, "presence of data for external devices")

    tib_event_counter = Field(None, "TIB event counter")
    tib_pps_counter = Field(None, "TIB pps counter")
    tib_tenMHz_counter = Field(None, "TIB 10 MHz counter")
    tib_stereo_pattern = Field(None, "TIB stereo pattern")
    tib_masked_trigger = Field(None, "TIB trigger mask")

    ucts_event_counter =  Field(None, "UCTS event counter")
    ucts_pps_counter = Field(None, "UCTS pps counter")
    ucts_clock_counter = Field(None, "UCTS clock counter")
    ucts_timestamp = Field(None, "UCTS timestamp")
    ucts_camera_timestamp = Field(None, "UCTS camera timestamp")
    ucts_trigger_type = Field(None, "UCTS trigger type")
    ucts_white_rabbit_status = Field(None, "UCTS whiteRabbit status")

    #cdts_data = Field([], "CDTS data array")
    swat_data = Field([], "SWAT data array")

    pps_counter= Field([], "Dragon pulse per second counter (n_modules)")
    tenMHz_counter = Field([], "Dragon 10 MHz counter (n_modules)")
    event_counter = Field([], "Dragon event counter (n_modules)")
    trigger_counter = Field([], "Dragon trigger counter (n_modules)")
    local_clock_counter = Field([], "Dragon local 133 MHz counter (n_modules)")

    chips_flags = Field([], "chips flags")
    first_capacitor_id = Field([], "first capacitor id")
    drs_tag_status = Field([], "DRS tag status")
    drs_tag = Field([], "DRS tag")


class LSTMonitoringContainer(Container):
    """
    Container for Fields/containers that are specific for the LST monitoring
    e.g. the pointing data
    """

class LSTCameraContainer(Container):
    """
    Container for Fields that are specific to each LST camera
    """
    evt = Field(LSTEventContainer(), "LST specific event Information")
    svc = Field(LSTServiceContainer(), "LST specific camera_config Information")
    mon = Field(LSTMonitoringContainer(), "LST specific monitoring Information")


class LSTContainer(Container):
    """
    Storage for the LSTCameraContainer for each telescope
    """
    tels_with_data = Field([], "list of telescopes with data")

    # create the camera container
    tel = Field(
        Map(LSTCameraContainer),
        "map of tel_id to LSTTelContainer")


class LSTDataContainer(DataContainer):
    """
    Data container including LST and monitoring information
    """
    lst = Field(LSTContainer(), "LST specific Information")
    mon = Field(MonitoringContainer(), "container for LST monitoring data (MON)")


