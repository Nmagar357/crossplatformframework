#!/tools/bash -l

echo "# Starting shell runner..."

#for file in "$(find . -maxdepth 1 -name '*.sh' -print -quit)"; do source $file; done

source /Users/${USER}/.bash_profile
source "$TOOLS"/bash/build.sh
source "$TOOLS"/bash/device.sh
source "$TOOLS"/bash/server.sh
source "$TOOLS"/bash/system.sh

echo "Device name: ${DEVICE_NAME}"

kill_emulator "@${DEVICE_NAME}"
kill_server "appium"
get_last_rc_number
copy_remote_build
start_emulator
uninstall_build
install_build
start_server
run_tests
set_build_info
report_results
kill_emulator "@${DEVICE_NAME}"
kill_server "appium"

echo "# Finished shell runner."
