from . import run_flowgraph
from . import file_writer
from . import get_config
from . import file_saver
from . import get_cpu_load

import logging

_logger = logging.getLogger(__name__)


def main(args):
    _logger.debug("Running frame detector runner")
    filename = args.filename
    timeout = args.timeout

    # parse the config for the values to use
    (
        input_data,
        sf_list,
        frames_list,
        impl_head_list,
        has_crc_list,
        cr_list,
        time_wait_list,
        threshold_list,
        noise_list,
    ) = get_config.parse_config_data(args.config[0], "frame_detector")
    # initilize a saver object
    save = file_saver.FileSaver(args, "frame_detector")
    n_times = (
        len(noise_list)
        * len(threshold_list)
        * len(cr_list)
        * len(has_crc_list)
        * len(impl_head_list)
        * len(frames_list)
        * len(sf_list)
    )
    _logger.info("Flowgraph needs to run {}".format(n_times))

    # loop over all values that needs to be runned
    for noise in noise_list:
        for threshold in threshold_list:
            for time_wait in time_wait_list:
                for cr in cr_list:
                    for has_crc in has_crc_list:
                        for impl_head in impl_head_list:
                            for frames in frames_list:
                                for sf in sf_list:
                                    _logger.info("Starting new run")
                                    # write template file
                                    try:
                                        file_writer.write_template_frame_detector(
                                            filename,
                                            input_data,
                                            sf,
                                            impl_head,
                                            has_crc,
                                            cr,
                                            frames,
                                            time_wait,
                                            threshold,
                                            noise,
                                        )
                                    except (RuntimeError, TypeError, NameError):
                                        _logger.debug("Writing frame_detector error")
                                    # run the flowgraph
                                    try:
                                        (
                                            num_right,
                                            num_dec,
                                            time,
                                            snr,
                                            signal_power,
                                            noise_power,
                                        ) = run_flowgraph.profile_flowgraph(
                                            input_data, timeout, "frame_detector"
                                        )
                                    except (RuntimeError, TypeError, NameError):
                                        _logger.debug("Error executing flowgraph of frame_detector")
                                    # get the average load
                                    try:
                                        load_1min, load_5min, load_15min = get_cpu_load.load_all()
                                        # calculate the derived values
                                        num_per = min(num_right / frames * 100, 100)
                                        paylen = len(input_data)
                                        data_rate = (paylen * frames) / time
                                    except (RuntimeError, TypeError, NameError):
                                        _logger.debug(
                                            "Error in getting the cpu load values of the system"
                                        )
                                    # setup data frame to hold all data
                                    data = {
                                        "template": "frame_detector",
                                        "time_wait": time_wait,
                                        "input_data": input_data,
                                        "sf": sf,
                                        "paylen": paylen,
                                        "impl_head": impl_head,
                                        "has_crc": has_crc,
                                        "cr": cr,
                                        "frames": frames,
                                        "num_right": num_right,
                                        "num_total": frames,
                                        "num_dec": num_dec,
                                        "time": time,
                                        "load_1min": load_1min,
                                        "load_5min": load_5min,
                                        "load_15min": load_15min,
                                        "num_per": num_per,
                                        "data_rate": data_rate,
                                        "threshold": threshold,
                                        "noise": noise,
                                        "avg_snr": snr,
                                        "avg_signal_power": signal_power,
                                        "avg_noise_power": noise_power,
                                    }
                                    # save data to pandas or wandb
                                    save.saver(data)

                                    save.finish()
