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

def write_template(file_name, source_data, bw, sf, paylen, impl_head, has_crc, cr,frames,frame_period,mean):
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
    #open template
    file_name_open = "templates/"+str(file_name)
    f_template = open(file_name_open, 'r')
    f_template_text = f_template.read()
    f_template.close()
    #subsitutes
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
