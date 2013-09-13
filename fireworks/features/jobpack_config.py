'''
A set of global variables for job packing
'''
from multiprocessing.managers import BaseManager
from fireworks.core.fw_config import singleton

__author__ = 'Xiaohui Qu, Anubhav Jain'
__copyright__ = 'Copyright 2013, The Material Project & The Electrolyte Genome Project'
__version__ = '0.1'
__maintainer__ = 'Xiaohui Qu'
__email__ = 'xqu@lbl.gov'
__date__ = 'Sep 2, 2013'


@singleton
class JPConfig(object):
    def __init__(self):
        self.MULTIPROCESSING = None # default single process framework

        self.PACKING_MANAGER_PORT = '27016'   # the internet port of the packing manager service

        self.PACKING_MANAGER_PASSWORD ='123'  # the password to connect to packing manager service

        self.PROCESS_LOCK = None  # the shared Lock between processes

        self.NODE_LIST = None  # the node list for sub jobs

        self.SUB_NPROCS = None  # the number of process of the sub job

        self.PACKING_MANAGER = None  # the shared object manager


class DataServer(BaseManager):
    """
    Provide a server that can host shared objects between multiprocessing
    Processes (that normally can't share data). For example, a common LaunchPad is
    shared between processes and pinging launches is coordinated to limit DB hits.
    """
    pass

# These variables will be regise
DataServer.register('LaunchPad')
DataServer.register('Running_IDs')


def acquire_jp_lock():
    jp_conf = JPConfig()
    if jp_conf.MULTIPROCESSING:
        jp_conf.PROCESS_LOCK.acquire()


def release_jp_lock():
    jp_conf = JPConfig()
    if jp_conf.MULTIPROCESSING:
        jp_conf.PROCESS_LOCK.release()