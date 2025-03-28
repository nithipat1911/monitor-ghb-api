https://console.cloud.google.com/home/dashboard?project=monitor-ghb-api


gcloud functions deploy check_api --runtime python39 --trigger-http  --allow-unauthenticated



gcloud scheduler jobs create http check-api-job  --schedule "*/5 * * * *"  --uri "https://us-central1-monitor-ghb-api.cloudfunctions.net/check_api" --http-method=GET   --time-zone "Asia/Bangkok"

gcloud scheduler jobs create http check-api-job --schedule "*/5 * * * *"  --uri "https://us-central1-monitor-ghb-api.cloudfunctions.net/check_api"  --http-method=GET  --time-zone "Asia/Bangkok"  --location=us-central1


D:\mydev\gcloud\monitor-ghb-api>gcloud scheduler jobs create http check-api-job --schedule "*/5 * * * *"  --uri "https://us-central1-monitor-ghb-api.cloudfunctions.net/check_api"  --http-method=GET  --time-zone "Asia/Bangkok"  --location=us-central1
attemptDeadline: 180s
httpTarget:
  headers:
    User-Agent: Google-Cloud-Scheduler
  httpMethod: GET
  uri: https://us-central1-monitor-ghb-api.cloudfunctions.net/check_api
name: projects/monitor-ghb-api/locations/us-central1/jobs/check-api-job
retryConfig:
  maxBackoffDuration: 3600s
  maxDoublings: 16
  maxRetryDuration: 0s
  minBackoffDuration: 5s
schedule: '*/5 * * * *'
state: ENABLED
timeZone: Asia/Bangkok
userUpdateTime: '2025-03-20T09:13:36Z'