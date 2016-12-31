# -*- coding: utf-8 -*-
import os

import shutil

from config import STATIC_GIT_REPO
from environment import STATIC_DIST_GIT_PATH
from git import Repo, exc
try:
    import local_properties
    _git_repo = STATIC_GIT_REPO.replace('https://', 'https://%s:%s@' % (local_properties.GITHUB_USERNAME, local_properties.GITHUB_TOKEN))
except Exception as e:
    print(e)
    _git_repo = STATIC_GIT_REPO

_env = {'PATH': STATIC_DIST_GIT_PATH}
try:
    _repo = Repo(STATIC_DIST_GIT_PATH)
except:
    shutil.rmtree(STATIC_DIST_GIT_PATH)
    _repo = Repo.clone_from(_git_repo, STATIC_DIST_GIT_PATH)


def check_git_repo():
    if not os.path.exists(os.path.join(STATIC_DIST_GIT_PATH, '.git')):
        print(_repo.clone(STATIC_GIT_REPO))


def push():
    try:
        remote = _repo.remote('origin')
        # _repo.git.checkout('-f')
        _repo.git.add('.')
        try:
            _repo.git.commit('-m "committed by system"')
        except exc.GitCommandError as e:
            print(e)
        remote.pull()
        # auth ssh keys needed
        # ssh -vvT git@github.com
        remote.push()
    except Exception as e:
        print(e)
        return
