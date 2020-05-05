import yaml
import os
import logging


def read_conf():

    root_path = root_path = os.path.abspath(
        os.path.dirname(__file__)).split('utils')[0]
    conf_file_path = os.path.join(root_path,'conf','slurm.yaml')
    logging.info("slurm_sim conf path is {}".format(conf_file_path))
    with open(conf_file_path,'r',encoding='utf-8') as conf_file:
        return yaml.safe_load(conf_file)



if __name__ == '__main__':

    print(read_conf())