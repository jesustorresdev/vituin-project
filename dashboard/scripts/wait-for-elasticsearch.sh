#!/bin/bash
# Basado en: https://github.com/elastic/elasticsearch-py/issues/778#issuecomment-384389668
set -e

PROGRAM_NAME="$(basename "$0")"

function usage() {
	cat <<-EOF
	Usage: $PROGRAM_NAME URL [-h | --help ] [-- COMMAND ARGS]
	Options:
	  -h | --help               Show help about options.
	Arguments:
	  URL                       Base URL of Elasticsearch service.
	  -- COMMAND ARGS           Execute command with args after the test finishes.
	EOF
}

error_exit() {
    echo "$PROGRAM_NAME: error: ${2:-'unknown error'}" 1>&2
	exit "${1:-1}"
}

warning() {
    echo "$PROGRAM_NAME: warning: ${1:-'unknown error'}" 1>&2
}

check_elasticsearch() {
    case "$1" in
        connection )
            curl --silent --output /dev/null --head --fail "$BASE_URL"
            ;;
        response )
            curl --silent --output /dev/null --write-out '%{http_code}' "$BASE_URL"
            ;;
        health )
            # trim whitespace (otherwise we'll have "green ")
            curl -fsSL "$BASE_URL/_cat/health?h=status" |  sed -r 's/^[[:space:]]+|[[:space:]]+$//g'
            ;;
    esac
}

# Check required commands
type -P curl &> /dev/null || error_exit "curl is not installed"

BASE_URL="http://localhost:9200"
COMMAND=
while [[ $# -gt 0 ]]
do
    case "$1" in
        http://* | https://* )
            BASE_URL="$1"
            shift
            ;;
        -h | --help)
            usage
            exit 0
            ;;
        -- )
            shift
            COMMAND=("$@")
            break
            ;;
        * )
            error_exit 1 "unknown option '$OPTARG'."
            ;;
    esac
done

# First wait until Elastisearch answer on its port
until $(check_elasticsearch connection); do
    echo -n '.'
    sleep 1
done

# Next wait for Elastisearch to start...
until [[ $(check_elasticsearch response) == "200" ]]; do
    >&2 echo "Elasticsearch is unavailable - sleeping"
    sleep 1
done

# Next wait for Elastisearch status to turn to Green
until [[ " yellow green " =~ " $(check_elasticsearch health) " ]]; do
    >&2 echo "Elasticsearch is unavailable - sleeping"
    sleep 1
done

>&2 echo "Elasticsearch is up"
if [[ "$COMMAND" != "" ]]; then
    exec ${COMMAND[@]}
fi

# vim: set ts=4 sw=4 tw=0 noet :