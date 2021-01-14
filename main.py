import pandas as pd
from helpers import file_writer
from helpers import profiler


def main():
    templates_list = ["lora_sim_blocks", "lora_sim_chain", "lora_sim_multi1", "lora_sim_multi2",
                      "lora_sim_multi3", "lora_sim_multi4", "lora_sim_multi5", "lora_sim_multi6"]
    templates_list = ["lora_sim_blocks"]

    # list values to generate profiling cases for
    source_data_list = [
        "PKdhtXMmr18n2L9K88eMlGn7CcctT9RwKSB1FebW397VI5uG1yhc3uavuaOb9vyJ"]
    bw_list = [250000]
    sf_list = [7, 8, 9, 10, 11, 12]
    paylen_list = [64]
    # impl_head_list = [True]
    # has_crc_list = [False]
    # cr_list = [0]
    frames_list = [10]
    frame_period_list = [200]
    impl_head_list = [True]
    has_crc_list = [False]
    cr_list = [0]
    mean_list = [200]

    colums_names = ['template', 'mean', 'source_data', 'bw', 'sf', 'paylen', 'impl_head', 'has_crc', 'cr', 'frames',
                    'frame_period', 'num_right', 'num_total', 'time']
    df = pd.DataFrame(columns=colums_names)
    num_tx = 1
    # loop over all templates to profile
    for template in templates_list:
        print(template)
        if (template == "lora_sim_blocks"):
            num_tx = 1
        if (template == "lora_sim_chain"):
            num_tx = 1
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
                                            for sf in sf_list:
                                                # write new template config
                                                file_writer.write_template(
                                                    template, source_data, bw, sf, paylen, impl_head, has_crc, cr, frames,
                                                    frame_period, mean)

                                                num_right, time = profiler.profile(
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
                                                    'num_total': num_tx * frames,
                                                    'time': time,
                                                }
                                                # append newly created data to dataframe
                                                df = df.append(
                                                    data, ignore_index=True)
                                                print("Executed loop once.")
                                                # save dataframe to file
                                                df.to_csv(
                                                    "results/profiled.csv")
                                                exit()
                                                # if multi case run only once for this sf, increasing the sf is of no use.
                                                if (template == "lora_sim_multi2"):
                                                    break
                                                if (template == "lora_sim_multi3"):
                                                    break
                                                if (template == "lora_sim_multi4"):
                                                    break
                                                if (template == "lora_sim_multi5"):
                                                    break
                                                if (template == "lora_sim_multi6"):
                                                    break

    print("Done!")
    print("Exiting..")


main()
