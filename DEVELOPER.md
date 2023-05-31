# Building and Testing python-game-prototypes

This document describes how to set up your development environment to build and test the project.
It also explains the basic mechanics of using `git`, `python`, and `pip`.

* [Prerequisite Software](#prerequisite-software)
* [Getting the Sources](#getting-the-sources)
* [Installing NPM Modules](#installing-npm-modules)
* [Building](#building)
* [Running Tests Locally](#running-tests-locally)
* [Formatting your Source Code](#formatting-your-source-code)
* [Linting/verifying your Source Code](#lintingverifying-your-source-code)

See the [contribution guidelines](https://github.com/remi-boivin/python-game-prototypes/blob/master/CONTRIBUTING.md)
if you'd like to contribute to the project.

## Prerequisite Software

Before you can build and test the project, you must install and configure the
following products on your development machine:

* [Git](https://git-scm.com/) and/or the [**GitHub app**](https://desktop.github.com/) (for Mac and Windows);
  [GitHub's Guide to Installing Git](https://help.github.com/articles/set-up-git) is a good source of information.\
  **Windows Users**: Git Bash or an equivalent shell is required\
  *Windows Powershell and cmd shells are not supported [#46780](https://github.com/remi-boivin/python-game-prototypes/issues/46780) so some commands might fail*

* [Python](https://www.python.org/): 3.9.x which is use as main language.
* [pip](https://pip.pypa.io/en/stable/): 20.3.x which is use as python package installer.

## Getting the Sources

Fork and clone the project repository:

1. Login to your GitHub account or create one by following the instructions given [here](https://github.com/signup/free).
2. [Fork](https://help.github.com/forking) the [main python game prototypes](https://github.com/remi-boivin/python-game-prototypes).
3. Clone your fork of the repository and define an `upstream` remote pointing back to
   the project repository that you forked in the first place.

```shell
# Clone your GitHub repository:
git clone git@github.com:<github username>/python-game-prototypes.git
# Go to the project directory:
cd python-game-prototypes

# Add the main project repository as an upstream remote to your repository:
git remote add upstream https://github.com/remi-boivin/python-game-prototypes.git
```

## Installing Python packages

Next, install the Python packages needed to build and test the project:

```shell
# Install project dependencies (package.json)
pip3 install -r requirements.txt
```

## Install git hooks

The git hooks allow to run task on specific job. For exemple on the commit
To install it run:

```shell
python3  tools/SetupTools.py -l python
```

### Hooks features

For now git hooks support

- Add emoji on commit
- Lint the commits according to the git commit convention (please read [conventionnal commits](https://www.conventionalcommits.org/en/v1.0.0/)) to know more
- Show a warning message if we push on master. By default you can't push.
- Block force push on master
- Disable the merge on master. You can allow it by setting GIT_COMMIT_TO_MASTER=true

## Using

To use the project run:

```shell
python3 sample/core.py
```

### Building and serving a project

## Formatting your source code

python-game-prototypes uses [yapf](https://pypi.org/project/yapf/) to format the source code.
If the source code is not properly formatted, the CI will fail and the PR cannot be merged.

You can automatically format your code by running:
- `yapf -i -r <files..>`: format only provided files

A better way is to set up your IDE to format the changed file on each file save.

### VS Code
1. Install [yapf](yapf) python module.
2. Create the folder `.vscode/`.
3. Create a new file in the folder `.vscode/` called `settings.json` and put

```json
{
    "python.linting.enabled": true,
    "python.linting.pylintPath": "pylint",
    "editor.formatOnSave": true,
    "python.formatting.provider": "yapf",
    "python.linting.pylintEnabled": true,
}
```

## Linting/verifying your Source Code

You can check that your code is properly formatted and adheres to coding style by running:

``` shell
$ pylint --recursive y --jobs -n 0 sample/*.py
```