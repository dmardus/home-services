# First do: chmod +x update-media-pod.sh
#
#!/usr/bin/env bash
set -euo pipefail

POD_NAME="media-pod"
YAML="media-pod.yaml"
IMAGE_PLEX="docker.io/linuxserver/plex:latest"
IMAGE_JELLYFIN="docker.io/linuxserver/jellyfin:latest"

echo "Pulling latest images..."
podman pull "$IMAGE_PLEX"
podman pull "$IMAGE_JELLYFIN"

echo "Removing existing pod..."
podman pod rm -f "$POD_NAME" || true

echo "Recreating pod from YAML..."
podman kube play "$YAML"

echo "Update complete."
