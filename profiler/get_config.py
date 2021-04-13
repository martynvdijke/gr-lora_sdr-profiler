import yaml
import numpy as np


def parse_config_colums(template, _logger):
    """
    Returns the colums names (to be used in pandas) to use for diffrent templates
    Args:
        template: name of the template currenlty in use
        _logger: logger

    Returns:
        list of colum names
    """
    # list ot hold all configs values
    config_list = []
    colum_names = []

    colum_names.extend(['template', 'time_wait', 'input_data', 'sf', 'paylen', 'impl_head', 'has_crc', 'cr', 'frames'])
    # add the derived general quantities
    colum_names.extend(
        ["time", "data_rate", "load_1min", "load_5min", "load_15min", "num_right", "num_total", "num_dec", "num_per"])

    if template == "frame_detector":
        colum_names.extend(["threshold", "ampl_noise", "avg_snr"])

    return colum_names


def parse_config_data(cfg, template, _logger):
    """
    Parses the cfg file and returns all values as a list object.
    Args:
        cfg: file name of the yml config to load
        template: template to use
        _logger: logger entity

    Returns: list of all values described in the config file

    """

    # list ot hold all configs values
    config_list = []
    # open
    with open(r'{}'.format(cfg)) as file:
        documents = yaml.full_load(file)
        config_list = documents['frame_detector']
    input_list = config_list['input_string']
    # convert all values to list form
    sf_list = np.arange(config_list['sf']['start'], config_list['sf']['end'],
                        config_list['sf']['increment'])
    frames_list = np.arange(config_list['frames']['start'], config_list['frames']['end'],
                            config_list['frames']['increment'])
    impl_head_list = [config_list['impl_head']['start'],
                      config_list['impl_head']['end']]
    has_crc_list = [config_list['has_crc']['start'],
                    config_list['has_crc']['end']]
    cr_list = np.arange(config_list['cr']['start'], config_list['cr']['end'],
                        config_list['cr']['increment'])
    time_wait_list = np.arange(config_list['time_wait']['start'], config_list['time_wait']['end'],
                               config_list['time_wait']['increment'])

    if template == "single":
        with open(r'{}'.format(cfg)) as file:
            documents = yaml.full_load(file)

    if template == "frame_detector":
        threshold_list = np.arange(config_list['threshold']['start'], config_list['threshold']['end'],
                                   config_list['threshold']['increment'])
        noise_list = np.arange(config_list['noise']['start'], config_list['noise']['end'],
                               config_list['noise']['increment'])

        return input_list, sf_list, frames_list, impl_head_list, has_crc_list, cr_list, time_wait_list, threshold_list, noise_list
