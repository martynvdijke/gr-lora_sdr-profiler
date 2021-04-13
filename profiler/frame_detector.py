from . import run_flowgraph
from . import file_writer
from . import get_config
from . import file_saver
from . import get_cpu_load


def main(args, _logger: object):
    _logger.debug("Running frame detector")
    filename = args.filename
    timeout = args.timeout

    # parse the config for the values to use
    input_data, sf_list, frames_list, impl_head_list, has_crc_list, cr_list, time_wait_list, threshold_list, noise_list = get_config.parse_config_data(
        args.config[0], "frame_detector", _logger)

    save = file_saver.FileSaver(args, "frame_detector", _logger)
    times = len(input_data)*len(sf_list)*len(frames_list)*len(impl_head_list)*len(has_crc_list)*len(cr_list)*len(time_wait_list)*len(threshold_list)*len(noise_list)
    _logger.info("Needing to run the flowgraph {} times".format(times))
    # loop over all values that needs to be runned
    for noise in noise_list:
        for threshold in threshold_list:
            for time_wait in time_wait_list:
                for cr in cr_list:
                    for has_crc in has_crc_list:
                        for impl_head in impl_head_list:
                            for frames in frames_list:
                                for sf in sf_list:
                                    _logger.debug("Starting another run")
                                    # write template file
                                    try:
                                        file_writer.write_template_frame_detector(filename, input_data, sf, impl_head,
                                                                                  has_crc, cr, frames, time_wait,
                                                                                  threshold, noise, _logger)
                                    except:
                                        _logger.debug("Writing frame_detector error")
                                    # run the flowgraph
                                    try:
                                        num_right, num_dec, time, snr = run_flowgraph.profile_flowgraph(input_data, timeout, "frame_detector",
                                                                                                   _logger)
                                    except:
                                        _logger.debug("Error executing flowgraph of frame_detector")
                                    # get the average load
                                    load_1min, load_5min, load_15min = get_cpu_load.load_all()
                                    # calculate the derived values
                                    num_per = num_right / frames * 100
                                    paylen = len(input_data)
                                    data_rate = (paylen * frames) / time
                                    # setup data frame to hold all data
                                    data = {
                                        'template': "frame_detector",
                                        'time_wait': time_wait,
                                        'input_data': input_data,
                                        'sf': sf,
                                        'paylen': paylen,
                                        'impl_head': impl_head,
                                        'has_crc': has_crc,
                                        'cr': cr,
                                        'frames': frames,
                                        'num_right': num_right,
                                        'num_total': frames,
                                        'num_dec': num_dec,
                                        'time': time,
                                        'load_1min': load_1min,
                                        'load_5min': load_5min,
                                        'load_15min': load_15min,
                                        'num_per': num_per,
                                        'data_rate': data_rate,
                                        'threshold': threshold,
                                        'noise': noise,
                                        'avg_snr': snr,
                                    }
                                    #
                                    save.saver(data)


    save.finish()
