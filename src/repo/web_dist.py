# -*- coding: utf-8 -*-
import os

import shutil

from config import STATIC_GIT_REPO
from environment import STATIC_DIST_GIT_PATH
from git import Repo, exc

_env = {'PATH': STATIC_DIST_GIT_PATH}
try:
    _repo = Repo(STATIC_DIST_GIT_PATH)
except:
    shutil.rmtree(STATIC_DIST_GIT_PATH)
    _repo = Repo.clone_from(STATIC_GIT_REPO, STATIC_DIST_GIT_PATH)


def check_git_repo():
    if not os.path.exists(os.path.join(STATIC_DIST_GIT_PATH, '.git')):
        print(_repo.clone(STATIC_GIT_REPO))


def push():
    try:
        import local_properties
        remote_url = STATIC_GIT_REPO.replace('https://', 'https://%s:%s@' % local_properties.GITHUB_USERNAME, local_properties.GITHUB_TOKEN)
        remote = _repo.remote(remote_url)
        # _repo.git.checkout('-f')
        _repo.git.add('.')
        try:
            _repo.git.commit('-m "committed by system"')
        except exc.GitCommandError as e:
            print(e)
        remote.pull()
        remote.push()
    except:
        return