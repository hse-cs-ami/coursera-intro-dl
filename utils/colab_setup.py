import os
from abc import ABC
from abc import abstractmethod


def download_github_code(path):
    filename = path.rsplit('/')[-1]
    os.system('shred -u {}'.format(filename))
    os.system('wget -q https://raw.githubusercontent.com/hse-cs-ami/coursera-intro-dl/main/{} -O {}'.format(path, filename))


def download_github_release(path):
    filename = path.rsplit('/')[-1]
    os.system('shred -u {}'.format(filename))
    os.system('wget -q https://github.com/hse-cs-ami/coursera-intro-dl/releases/download/{} -O {}'.format(path, filename))


class WeekSetup(ABC):

    def __init__(self):
        download_github_code('utils/testing.py')  # TODO: make actual grading file

    @abstractmethod
    def setup(self):
        pass


class Week02CNN1(WeekSetup):

    def setup(self):
        pass


class Week03CNN2(WeekSetup):

    def __init__(self):
        super().__init__()
        self.dataset_name = 'birbs.tar.gz'

    def setup(self):
        download_github_release('dataset/' + self.dataset_name)
        os.system(f'tar -xf {self.dataset_name}')
