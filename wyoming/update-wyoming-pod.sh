# First do: chmod +x update-wyoming-pod.sh
#
#!/usr/bin/env bash
set -euo pipefail

POD_NAME="wyoming-pod"
YAML="wyoming-pod.yaml"
IMAGE_WHISPER="docker.io/rhasspy/wyoming-whisper:latest"
IMAGE_PIPER="docker.io/rhasspy/wyoming-piper:latest"

echo "Pulling latest images..."
podman pull "$IMAGE_WHISPER"
podman pull "$IMAGE_PIPER"

echo "Removing existing pod..."
podman pod rm -f "$POD_NAME" || true

echo "Recreating pod from YAML..."
podman kube play "$YAML"

echo "Update complete."
