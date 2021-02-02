# Canary Demo

1. Build image with `docker build -t coalmine .`
2. Use `kubectl apply -f coalmine.yaml` to deploy it on local k8s.
3. Use `kubectl get ingress` to check if k8s has allocated IP to ingress, it takes ~30s.
4. Put an entry in hosts file for `coalmine.local` pointing to ip from last step
5. Use `curl -v  -X GET -u canaryuser:password coalmine.local` to make request.

   For all basic auth users other than ones starting with `canary`,
   return value will have value for key `canary` set to false.
