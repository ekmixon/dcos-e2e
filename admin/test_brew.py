"""
"""

from pathlib import Path

from dulwich.porcelain import archive
from dulwich.repo import Repo
from py.path import local  # pylint: disable=no-name-in-module, import-error


def test_brew(tmpdir: local) -> None:
    """
    XXX
    """
    local_repository = Repo('.')
    committish = b'HEAD'
    archive_file = Path(str(tmpdir.join('archive.tar.gz')))
    archive_file.touch()

    with archive_file.open('wb') as outstream:
        archive(
            repo=local_repository,
            committish=committish,
            outstream=outstream,
        )
    import pdb; pdb.set_trace()

    # TODO make archive - test can you do archive from file:///
    # git archive --format=tar.gz -o /tmp/my-repo.tar.gz --prefix=my-repo/ master
    # If so, this probably needs to be in the container
    # TODO admin/homebrew
    # TODO write file
    # TODO start container
    # docker run -it linuxbrew/linuxbrew
    # TODO send file to container
    # TODO install from Linuxbrew
    # dcos-docker help

    # TODO move this to tests/
