#!/tools/bash -l

source /Users/${USER}/.bash_profile

PACKAGE="com.nytimes.android"


function uninstall_build () {
  echo "[BUILD] Uninstalling existing package/APK."
  adb uninstall $PACKAGE
  STATUS= check_package_state $PACKAGE
  if [ $STATUS == true ]; then
    echo "[BUILD] WARN: Package not successfully uninstalled."
  else
    echo "[BUILD] Successfully uninstalled build."
  echo "[BUILD] APK installation finished."
}

function check_package_state () {
  STATUS=`adb shell pm list packages | grep $1`
  if [[ $STATUS == *$PACKAGE_MAIN* ]]; then
    return true
  else
    return false
  fi
}

