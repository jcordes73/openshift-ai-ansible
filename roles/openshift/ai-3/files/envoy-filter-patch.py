import json, sys
ef = json.load(sys.stdin)
ef['spec'].pop('targetRefs', None)
ef['spec']['workloadSelector'] = {'labels': {'gateway.networking.k8s.io/gateway-name': 'maas-default-gateway'}}
for cp in ef['spec'].get('configPatches', []):
  sf = cp.get('match',{}).get('listener',{}).get('filterChain',{}).get('filter',{}).get('subFilter',{})
  if sf.get('name','').startswith('extensions.istio.io/wasmplugin'):
    sf['name'] = 'envoy.filters.http.wasm'
ef['metadata'].pop('resourceVersion', None)
json.dump(ef, sys.stdout)
