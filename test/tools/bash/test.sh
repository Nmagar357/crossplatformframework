#!/tools/bash -l

function check_status () {
  STATUS=`adb shell pm list packages | grep $1`

  if [[ $STATUS == *$PACKAGE_MAIN* ]]; then
    echo true
  else
    echo false
  fi
}

STATE= check_status "com.nytimes.android"

if [[ $STATE == true ]]; then
  echo OK
fi