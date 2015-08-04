set -e
set -x

# Install packages with brew
brew update >/dev/null
brew outdated pyenv || brew upgrade --quiet pyenv
