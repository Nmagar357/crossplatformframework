#!/tools/bash -l

source /Users/${USER}/.bash_profile
source $tools/bash/system.sh

#DEVICE_NAME="Pixel 5"

function kill_emulator () {
  echo "[EMULATOR] Terminating any running emulators..."
  adb kill-server
  adb emu kill
  kill_all_pids_by_name "$1"
  echo "[EMULATOR] Complete."
}

function start_emulator () {
  echo "[EMULATOR] Starting emulator instance for: ${DEVICE_NAME}"
  emu_is_running=false
  while true; do
    adb start-server
    call_emu_startup
    is_emu_running
    if [[ $emu_is_running == true ]]; then
      echo "[EMULATOR] Clearing caches. Removing bad attributes."
      adb shell pm clear io.appium.settings
      adb shell pm clear io.appium.uiautomator2.server
      adb shell settings delete global debug_view_attributes
      adb shell settings delete global debug_view_attributes_application_package
      break
    fi
  done;
  echo "[EMULATOR] Complete."
}

#kill_emulator "Pixel"
#start_emulator