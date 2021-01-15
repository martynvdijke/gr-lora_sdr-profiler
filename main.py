import pandas as pd
from helpers import file_writer
from helpers import profiler


def main_single():
    """[summary]
    """
    templates_list = ["lora_sim_blocks", "lora_sim_chain", "lora_sim_multi1"]

    # list values to generate profiling cases for
    source_data_list = [
        "PKdhtXMmr18n2L9K88eMlGn7CcctT9RwKSB1FebW397VI5uG1yhc3uavuaOb9vyJ"]
    bw_list = [250000]
    sf_list = [7, 8, 9, 10, 11, 12]
    paylen_list = [64]
    frames_list = [10]
    frame_period_list = [200]
    impl_head_list = [True]
    has_crc_list = [False]
    cr_list = [0]
    mean_list = [200]

    colums_names = ['template', 'mean', 'source_data', 'bw', 'sf', 'paylen', 'impl_head', 'has_crc', 'cr', 'frames',
                    'frame_period', 'num_right', 'num_total', 'num_dec', 'time']
    df = pd.DataFrame(columns=colums_names)
    num_tx = 1
    # loop over all templates to profile
    for template in templates_list:
        print(template)

        # loop over all values and make the test cases and the reference file
        for mean in mean_list:
            for source_data in source_data_list:
                for bw in bw_list:
                    for paylen in paylen_list:
                        for impl_head in impl_head_list:
                            for has_crc in has_crc_list:
                                for cr in cr_list:
                                    for frames in frames_list:
                                        for frame_period in frame_period_list:
                                            for sf in sf_list:
                                                # write new template config
                                                file_writer.write_template_single(
                                                    template, source_data, bw, sf, paylen, impl_head, has_crc, cr, frames,
                                                    frame_period, mean)

                                                num_right, num_dec, time = profiler.profile(
                                                    source_data)

                                                data = {
                                                    'template': str(template),
                                                    'mean': mean,
                                                    'source_data': source_data,
                                                    'bw': bw,
                                                    'sf': sf,
                                                    'paylen': paylen,
                                                    'impl_head': impl_head,
                                                    'has_crc': has_crc,
                                                    'cr': cr,
                                                    'frames': frames,
                                                    'frame_period': frame_period,
                                                    'num_right': num_right,
                                                    'num_total': frames,
                                                    'num_dec' : num_dec,
                                                    'time': time,
                                                }
                                                # append newly created data to dataframe
                                                df = df.append(
                                                    data, ignore_index=True)
                                                print("Executed loop once.")
                                                # save dataframe to file
                                                df.to_csv(
                                                    "results/profiled_single.csv")


def main_multi():
    """[summary]
    """
    templates_list = ["lora_sim_multi1", "lora_sim_multi2",
                      "lora_sim_multi3", "lora_sim_multi4", "lora_sim_multi5", "lora_sim_multi6"]

    # list values to generate profiling cases for
    source_data_list = [
        "PKdhtXMmr18n2L9K88eMlGn7CcctT9RwKSB1FebW397VI5uG1yhc3uavuaOb9vyJ"]
    bw_list = [250000]
    sf_list = [7, 8, 9, 10, 11, 12]
    paylen_list = [64]
    frames_list = [10]
    frame_period_list = [200]
    impl_head_list = [True]
    has_crc_list = [False]
    cr_list = [0]
    mean_list = [200]
    delay_sf1_list = [0]
    delay_sf2_list = [0]
    delay_sf3_list = [0]
    delay_sf4_list = [0]
    delay_sf5_list = [0]
    delay_sf6_list = [0]

    colums_names = ['template', 'mean', 'source_data', 'bw', 'paylen', 'impl_head', 'has_crc', 'cr', 'frames',
                    'frame_period', 'delay_sf1', 'delay_sf2', 'delay_sf3', 'delay_sf4', 'delay_sf5', 'delay_sf6',
                    'num_right', 'num_total', 'num_dec', 'time']
    df = pd.DataFrame(columns=colums_names)
    num_tx = 1
    # loop over all templates to profile
    for template in templates_list:
        print(template)
        if (template == "lora_sim_multi1"):
            num_tx = 1
        if (template == "lora_sim_multi2"):
            num_tx = 2
        if (template == "lora_sim_multi3"):
            num_tx = 3
        if (template == "lora_sim_multi4"):
            num_tx = 4
        if (template == "lora_sim_multi5"):
            num_tx = 5
        if (template == "lora_sim_multi6"):
            num_tx = 6

        # loop over all values and make the test cases and the reference file
        for mean in mean_list:
            for source_data in source_data_list:
                for bw in bw_list:
                    for paylen in paylen_list:
                        for impl_head in impl_head_list:
                            for has_crc in has_crc_list:
                                for cr in cr_list:
                                    for frames in frames_list:
                                        for frame_period in frame_period_list:
                                            for delay_sf1 in delay_sf1_list:
                                                for delay_sf2 in delay_sf2_list:
                                                    for delay_sf3 in delay_sf3_list:
                                                        for delay_sf4 in delay_sf4_list:
                                                            for delay_sf5 in delay_sf5_list:
                                                                for delay_sf6 in delay_sf6_list:
                                                                    # write new template config
                                                                    file_writer.write_template_multi(
                                                                        template,source_data, bw, paylen, impl_head, has_crc, cr, frames, frame_period, mean,
                                                                        delay_sf1, delay_sf2, delay_sf3, delay_sf4, delay_sf5, delay_sf6)

                                                                    num_right, num_dec, time = profiler.profile(
                                                                        source_data)

                                                                    data = {
                                                                        'template': str(template),
                                                                        'mean': mean,
                                                                        'source_data': source_data,
                                                                        'bw': bw,
                                                                        'paylen': paylen,
                                                                        'impl_head': impl_head,
                                                                        'has_crc': has_crc,
                                                                        'cr': cr,
                                                                        'frames': frames,
                                                                        'frame_period': frame_period,
                                                                        'delay_sf1': delay_sf1,
                                                                        'delay_sf2': delay_sf2,
                                                                        'delay_sf3': delay_sf3,
                                                                        'delay_sf4': delay_sf4,
                                                                        'delay_sf5': delay_sf5,
                                                                        'delay_sf6': delay_sf6,
                                                                        'num_right': num_right,
                                                                        'num_dec': num_dec,
                                                                        'num_total': num_tx * frames,
                                                                        'time': time,
                                                                    }
                                                                    # append newly created data to dataframe
                                                                    df = df.append(
                                                                        data, ignore_index=True)
                                                                    print(
                                                                        "Executed loop once.")
                                                                    # save dataframe to file
                                                                    df.to_csv(
                                                                        "results/profiled_multi.csv")


def main():
    print("Starting the gr-lora_sdr profiler...")
    print("Starting the single run, stay tuned...")
    main_single()
    print("Single run done!")
    print("Starting multi gateway run..")
    main_multi()
    print("Multi gateway run done!")
    print("Exiting..")

main()