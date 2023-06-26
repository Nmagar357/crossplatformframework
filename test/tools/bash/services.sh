#!/tools/bash -l

function check_site_services() {
  echo "[SERVICES] Checking if services are running for site: $1"
}

function check_pm_service() {
  SERVICE_STATE=`curl $URL`
  echo $SERVICE_STATE
}

check_site_services '0.0.0.0:4723'