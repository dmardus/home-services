# First do: chmod +x update-cloudflare-pod.sh
#
#!/usr/bin/env bash
set -euo pipefail

POD_NAME="cloudflare-pod"
YAML="cloudflare-pod.yaml"
IMAGE="docker.io/cloudflare/cloudflared:latest"

echo "Pulling latest image..."
podman pull "$IMAGE"

echo "Removing existing pod..."
podman pod rm -f "$POD_NAME" || true

echo "Recreating pod from YAML..."
podman kube play "$YAML"

echo "Update complete."
