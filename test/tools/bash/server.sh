#!/tools/bash -l

source $JENK_SCRIPTS_HOME/system.sh
source /Users/${USER}/.bash_profile

function kill_server () {
  echo "[SERVER] Terminating running appium servers..."
  killall node
  kill_all_pids_by_name "appium"
  echo "[SERVER] Complete."
}

function start_server () {
  echo "[SERVER] Starting up server..."
  server_is_running=false
  while true; do
    call_server_startup
    is_server_running
    if [[ $server_is_running == true ]]; then
      break
    fi
  done;
  echo "[SERVER] Complete."
}

#kill_server "appium"
#start_server