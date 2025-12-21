#! /bin/bash

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
APP_PATH="$PROJECT_ROOT/app.py"
VENV="$PROJECT_ROOT/.venv/bin/activate"
RUNNING=1
PORT=8000

clean_up () {
	RUNNING=0
	reset_ufw
	kill $(jobs -p) 2> /dev/null || true
	exit 0
}

keep_alive () {
	while [[ $RUNNING -eq 1 ]]; do
  	sudo -v
  	sleep 60
	done
}

setup_ufw () {
	sudo ufw allow $PORT
	sudo ufw disable || true
	sudo ufw enable || true
	sudo systemctl restart ufw
}

reset_ufw () {
	local last_index=$(sudo ufw status numbered \
	  | awk -F'[][]' '{print $2}' \
  	| sort -n \
  	| tail -1)

	if [ -z "$last_index" ]; then
		sudo ufw disable || true
		sudo ufw enable || true
		return
	fi

	for ((i=1; i<=last_index; i++));
		do
			echo y | sudo ufw delete 1
		done

	sudo ufw disable || true
	sudo ufw enable || true
}

set -e
trap clean_up SIGINT

if [[ $(id -u) -ne 0 ]]; then
  echo Failed to run script.
	echo Are you root?
  exit 1
fi

keep_alive&
setup_ufw
source "$VENV"
cd "$PROJECT_ROOT"
python3 "$APP_PATH"
EXIT_CODE=$?

if [ "$EXIT_CODE" -eq 0 ]; then
  echo "Process finished successfuly."
	clean_up
else
  echo "Process failed with exit code $EXIT_CODE"
	clean_up
fi
