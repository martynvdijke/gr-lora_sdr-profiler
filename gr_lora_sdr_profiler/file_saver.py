"""
Simple file saver class that can save to pandas file or to wandb or both
"""
import logging
import pandas
import wandb
from . import get_config

_logger = logging.getLogger(__name__)


class FileSaver:
    """
    File saver class holds all the actual data, either in pandas data frames
    or as wandb data frames
    """

    # pylint: disable=R0902

    def __init__(self, args, template):
        self.logger = _logger
        self.logger.debug("Making new FileSaver class")
        self.modus = args.save
        self.name = args.name
        if args.save == "pandas":
            colum_names = get_config.parse_config_colums(template)
            self.data_frame = pandas.DataFrame(columns=colum_names)
            self.output = args.output
        if args.save == "wandb":
            wandb.init(project="lora_sdr-profiler", name=args.name)
            self.config = wandb.config
        if args.save == "both":
            colum_names = get_config.parse_config_colums(template)
            self.data_frame = pandas.DataFrame(columns=colum_names)
            self.output = args.output
            wandb.init(project="lora_sdr-profiler")
            self.config = wandb.config

    def saver(self, data):
        """
        Main saver function that spawns pandas saving or wandb saving or both
        Args:
            data: input data (int he form of a dict)

        Returns:

        """
        if self.modus == "pandas":
            self.pandas_saver(data)
        if self.modus == "wandb":
            self.wandb_saver(data)
        if self.modus == "both":
            self.pandas_saver(data)
            self.wandb_saver(data)

    def wandb_saver(self, data):
        """
        Saves the input dataa to wandb
        Args:
            data: dict with the data

        Returns:

        """
        self.logger.debug("Adding input data to wandb frame")
        wandb.log(data)

    def pandas_saver(self, data):
        """
        Saves the input data to update the pandas dataframe
        Args:
            data: dict with the data

        Returns:

        """
        self.logger.debug("Adding input data to pandas frame")
        self.data_frame = self.data_frame.append(data, ignore_index=True)

    def finish(self):
        """
        Saves the pandas dataframe to file or upload the wandb frame
        Returns:

        """
        self.logger.info("Saving files")
        if self.modus == "pandas":
            self.data_frame.to_csv(self.output)
        if self.modus == "wandb":
            wandb.finish()
        if self.modus == "both":
            self.data_frame.to_csv(self.output)
            wandb.finish()
