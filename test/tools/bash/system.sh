#!/tools/bash -l

function call_emu_startup () {
  echo "[SYSTEM] Launching: Emulator instance: ${DEVICE_NAME}"
  emulator @"${DEVICE_NAME}" > /Users/"${USER}"/Desktop/appium_out.txt > /dev/null 2>&1 & sleep 60  #-no-snapshot-load
}

function call_server_startup () {
  echo "[SYSTEM] Launching: Appium server instance: 0.0.0.0:4723"
  appium -p 4723 --log-timestamp --log-level debug:info --session-override --debug-log-spacing > /Users/${USER}/Desktop/appium_server_txt.log & sleep 20
}

function is_emu_running () {
  iter=0
  while sleep 1; do
    emu_state=$(adb devices | grep "emulator" | awk '{print $2}')
    if [[ $emu_state == "device" ]]
    then
      echo "[SYSTEM] Emulator has started up."
      emu_is_running=true
      break
    elif [[ $iter == 60 ]] # Emu startup timeout
    then
      emu_is_running=false
      break
    else
      echo "[SYSTEM] Waiting for emulator response... (${iter}+1)"
      iter=$((iter+1))
    fi
  done
}

function is_server_running () {
  iter=0
  while sleep 1; do
    server_state=$(curl http://0.0.0.0:4723/wd/hub/status)
    if [[ $server_state == *"status"* ]]
    then
      echo "[SYSTEM] Server has started up."
      server_is_running=true
      break
    elif [[ $iter == 30 ]] # Server startup timeout
    then
      server_is_running=false
      break
    else
      echo "[SYSTEM] Waiting for server response... (${iter}+1)"
      iter=$((iter+1))
    fi
  done
}

function kill_all_pids_by_name () {
  while true; do
    result=$(pgrep -f "$1" | head -n1)
    echo "$result"
    if [[ "$result" =~ [0-9] ]]; then
      echo "[SYSTEM] Found $1 PID: $result. Attempting to kill..."
      kill -9 "$result"
      sleep 1
    else
      echo "[SYSTEM] Killed all PIDs for: $1"
      break
    fi
  done
}
