from . import run_flowgraph
from . import file_writer
from . import get_config




def main(args,_logger):
    _logger.debug("Running frame detector")
    filename = args.filename
    input_list, sf_list, frames_list, impl_head_list, has_crc_list, cr_list, time_wait_list, threshold_list, noise_list = get_config.parse_config(args.config[0],"frame_detector",_logger)

    #loop over all values that needs to be runned
    for noise in noise_list:
        for threshold in threshold_list:
            for time_wait in time_wait_list:
                for cr in cr_list:
                    for has_crc in has_crc_list:
                        for impl_head in impl_head_list:
                            for frames in frames_list:
                                for sf in sf_list:
                                    for input in input_list:

                                        file_writer.write_template_frame_detector(filename,input, sf,impl_head, has_crc, cr, frames, time_wait,threshold,noise, _logger)

