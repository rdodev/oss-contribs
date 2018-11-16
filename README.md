# Usage

## For all

1. `git clone` this repo
1. `cd oss-contribs`

## For that gritty close-to-the-metal feel

1. open `gh-repo-oss-contrib-xls.py` and fill in the `token` variable with your GH personal token.
1. `pipenv install`
1. `pipenv run python gh-repo-oss-contrib-xls.py`

## For the lazy

1. `docker run -ti -v ${PWD}:/oss quay.io/rdodev/oss:1`


# Requirements
 * python 3.7
 * pipenv

 Or

 * Docker 1.17+