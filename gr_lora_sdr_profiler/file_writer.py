import re
import logging

_logger = logging.getLogger(__name__)


def from_dict(dct):
    """Replaces template files variables (denoted by @@<var>@@) with the variable value

    Args:
        dct ([type]): dict to replace
    """

    def lookup(match):
        key = match.group(1)
        return dct.get(key, f"<{key} not found>")

    return lookup


# needs cleaning
def write_template_single(
    file_name, source_data, bw, sf, paylen, impl_head, has_crc, cr, frames, frame_period, mean
):
    """
    Writes the temporary single chain template

    Args:
        file_name ([type]): filename
        source_data ([type]): input string to use
        bw ([type]): bandwith
        sf ([type]): spreading factor
        paylen ([type]): paylen
        impl_head ([type]): impl head
        has_crc (bool): has_crc
        cr ([type]): coding rate
        frames ([type]): number of frames to run
        frame_period ([type]): frame_period
    """
    # open template and read template into variable
    file_name_open = "templates/" + str(file_name)
    f_template = open(file_name_open, "r")
    f_template_text = f_template.read()
    f_template.close()
    delay_sf1 = 0
    delay_sf2 = 0
    delay_sf3 = 0
    delay_sf4 = 0
    delay_sf5 = 0
    delay_sf6 = 0
    # subsitutes placeholder values with values from run
    if file_name == "lora_sim_multi1":
        # subsitutes placeholder values with values from run
        subs = {
            "source_data": str(source_data),
            "bw": str(bw),
            "pay_len": str(paylen),
            "impl_head": str(impl_head),
            "has_crc": str(has_crc),
            "cr": str(cr),
            "sf": str(sf),
            "n_frame": str(frames),
            "frame_period": str(frame_period),
            "mean": str(mean),
            "delay_sf1": str(delay_sf1),
            "delay_sf2": str(delay_sf2),
            "delay_sf3": str(delay_sf3),
            "delay_sf4": str(delay_sf4),
            "delay_sf5": str(delay_sf5),
            "delay_sf6": str(delay_sf6),
        }
    else:
        # subsitutes placeholder values with values from run
        subs = {
            "source_data": str(source_data),
            "bw": str(bw),
            "sf": str(sf),
            "pay_len": str(paylen),
            "impl_head": str(impl_head),
            "has_crc": str(has_crc),
            "cr": str(cr),
            "n_frame": str(frames),
            "frame_period": str(frame_period),
            "mean": str(mean),
        }
    # replace placeholder values with real values
    replaced_text = re.sub("@@(.*?)@@", from_dict(subs), f_template_text)
    temp_file = "temp/flowgraph.py"
    # write temp file
    f = open(temp_file, "w")
    f.write(replaced_text)
    f.close()


# needs cleaning
def write_template_multi_stream(
    file_name,
    source_data,
    bw,
    paylen,
    impl_head,
    has_crc,
    cr,
    frames,
    frame_period,
    mean,
    delay_sf1,
    delay_sf2,
    delay_sf3,
    delay_sf4,
    delay_sf5,
    delay_sf6,
):
    """Writes the multi stream gateway template

    Args:
        file_name ([type]): template to use
        source_data ([type]): input string to use
        bw ([type]): bandwith
        paylen ([type]): payload length
        impl_head ([type]): impl_head mode
        has_crc (bool): has_crc
        cr ([type]): coding rate
        frames ([type]): number of frames to use
        frame_period ([type]): frame period
        mean ([type]): time between frames
        delay_sf1 ([type]): delay of block1
        delay_sf3 ([type]): delay of block2
        delay_sf4 ([type]): delay of block3
        delay_sf5 ([type]): delay of block4
        delay_sf6 ([type]): delay of block5
        delay_sf2 ([type]): delay of block6
    """
    # open template and read template into variable
    file_name_open = "templates/" + str(file_name)
    f_template = open(file_name_open, "r")
    f_template_text = f_template.read()
    f_template.close()

    if file_name == "lora_sim_multi1":
        sf = 7
        # subsitutes placeholder values with values from run
        subs = {
            "source_data": str(source_data),
            "bw": str(bw),
            "pay_len": str(paylen),
            "impl_head": str(impl_head),
            "has_crc": str(has_crc),
            "cr": str(cr),
            "sf": str(sf),
            "n_frame": str(frames),
            "frame_period": str(frame_period),
            "mean": str(mean),
            "delay_sf1": str(delay_sf1),
            "delay_sf2": str(delay_sf2),
            "delay_sf3": str(delay_sf3),
            "delay_sf4": str(delay_sf4),
            "delay_sf5": str(delay_sf5),
            "delay_sf6": str(delay_sf6),
        }
    else:
        # subsitutes placeholder values with values from run
        subs = {
            "source_data": str(source_data),
            "bw": str(bw),
            "pay_len": str(paylen),
            "impl_head": str(impl_head),
            "has_crc": str(has_crc),
            "cr": str(cr),
            "n_frame": str(frames),
            "frame_period": str(frame_period),
            "mean": str(mean),
            "delay_sf1": str(delay_sf1),
            "delay_sf2": str(delay_sf2),
            "delay_sf3": str(delay_sf3),
            "delay_sf4": str(delay_sf4),
            "delay_sf5": str(delay_sf5),
            "delay_sf6": str(delay_sf6),
        }
    # replace placeholder values with real values
    replaced_text = re.sub("@@(.*?)@@", from_dict(subs), f_template_text)
    temp_file = "temp/flowgraph.py"
    # write temp file
    f = open(temp_file, "w")
    f.write(replaced_text)
    f.close()


def write_template_frame_detector(
    file_name, input_data, sf, impl_head, has_crc, cr, frames, time_wait, threshold, noise
):
    """
    Writes the frame_detector template using the arguments
    Args:
        file_name: template to use
        input: input data string for the flowgraph
        bw: bandiwth to use in the flowgraph
        paylen: payload length of the flowgraph
        impl_head: impl_head mode variable of the flowgraph
        has_crc: has_crc mode variable of the flowgraph
        cr: coding rate of the flowgraph
        frames: number of frames of the flowgraph
        time_wait: time between frames
        threshold: thesshold value to use
        noise: noise level
    Returns:
        writen template file
    """
    _logger.debug("Writing new template filer {0}".format(file_name))
    _logger.debug(
        "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(
            input_data, impl_head, has_crc, cr, frames, time_wait, threshold, noise
        )
    )
    file_template = "templates/" + str(file_name)
    f_template = open(file_template, "r")
    f_template_text = f_template.read()
    f_template.close()
    subs = {
        "input_data": str(input_data),
        "impl_head": str(impl_head),
        "has_crc": str(has_crc),
        "cr": str(cr),
        "sf": str(sf),
        "n_frame": str(frames),
        "time_wait": str(time_wait),
        "threshold": str(threshold),
        "noise": str(noise),
    }

    # serach the template text for @@ which hold the variables that need to be recplaced
    replaced_text = re.sub("@@(.*?)@@", from_dict(subs), f_template_text)
    temp_file = "temp/flowgraph.py"
    # write temp file
    f = open(temp_file, "w")
    f.write(replaced_text)
    f.close()
