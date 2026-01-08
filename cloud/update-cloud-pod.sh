# First do: chmod +x update-cloud-pod.sh
#
#!/usr/bin/env bash
set -euo pipefail

POD_NAME="cloud-pod"
YAML="cloud-pod.yaml"
IMAGE_REDIS="docker.io/library/redis:latest"
IMAGE_IMMICH_ML="ghcr.io/immich-app/immich-machine-learning:release"
IMAGE_IMMICH_SERVER="ghcr.io/immich-app/immich-server:release"

echo "Pulling latest images..."
podman pull "$IMAGE_REDIS"
podman pull "$IMAGE_IMMICH_ML"
podman pull "$IMAGE_IMMICH_SERVER"

echo "Removing existing pod..."
podman pod rm -f "$POD_NAME" || true

echo "Recreating pod from YAML..."
podman kube play "$YAML"

echo "Update complete."
