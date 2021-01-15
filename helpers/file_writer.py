import os
import re


def from_dict(dct):
    """[summary]

    Args:
        dct ([type]): [description]
    """
    def lookup(match):
        key = match.group(1)
        return dct.get(key, f'<{key} not found>')
    return lookup

def write_template_single(file_name, source_data, bw, sf, paylen, impl_head, has_crc, cr,frames,frame_period,mean):
    """[summary]

    Args:
        file_name ([type]): [description]
        source_data ([type]): [description]
        bw ([type]): [description]
        sf ([type]): [description]
        paylen ([type]): [description]
        impl_head ([type]): [description]
        has_crc (bool): [description]
        cr ([type]): [description]
        frames ([type]): [description]
        frame_period ([type]): [description]
    """
    # open template and read template into variable
    file_name_open = "templates/"+str(file_name)
    f_template = open(file_name_open, 'r')
    f_template_text = f_template.read()
    f_template.close()
    # subsitutes placeholder values with values from run
    subs = {
        "source_data": str(source_data),
        "bw": str(bw),
        "sf": str(sf),
        "pay_len": str(paylen),
        "impl_head": str(impl_head),
        "has_crc": str(has_crc),
        "cr": str(cr),
        "n_frame" : str(frames),
        "frame_period" : str(frame_period),
        "mean" : str(mean)
    }
    #replace placeholder values with real values
    replaced_text = re.sub('@@(.*?)@@', from_dict(subs), f_template_text)
    temp_file = "temp/flowgraph.py"
    #write temp file
    f = open(temp_file, "w")
    f.write(replaced_text)
    f.close()

def write_template_multi(file_name, source_data, bw, paylen, impl_head, has_crc, cr, frames, frame_period, mean,
                          delay_sf1, delay_sf2, delay_sf3, delay_sf4, delay_sf5, delay_sf6):
    """[summary]

    Args:
        file_name ([type]): [description]
        source_data ([type]): [description]
        bw ([type]): [description]
        paylen ([type]): [description]
        impl_head ([type]): [description]
        has_crc (bool): [description]
        cr ([type]): [description]
        frames ([type]): [description]
        frame_period ([type]): [description]
        mean ([type]): [description]
        delay_sf1 ([type]): [description]
        delay_sf2 ([type]): [description]
        delay_sf3 ([type]): [description]
        delay_sf4 ([type]): [description]
        delay_sf5 ([type]): [description]
        delay_sf6 ([type]): [description]
    """
    # open template and read template into variable
    file_name_open = "templates/"+str(file_name)
    f_template = open(file_name_open, 'r')
    f_template_text = f_template.read()
    f_template.close()
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
        'delay_sf1': str(delay_sf1),
        'delay_sf2': str(delay_sf2),
        'delay_sf3': str(delay_sf3),
        'delay_sf4': str(delay_sf4),
        'delay_sf5': str(delay_sf5),
        'delay_sf6': str(delay_sf6),
    }
    # replace placeholder values with real values
    replaced_text = re.sub('@@(.*?)@@', from_dict(subs), f_template_text)
    temp_file = "temp/flowgraph.py"
    # write temp file
    f = open(temp_file, "w")
    f.write(replaced_text)
    f.close()