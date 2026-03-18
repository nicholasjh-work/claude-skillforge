#!/usr/bin/env bash
# install-skill.sh
# Copies a skill from this repo into ~/.claude/skills/<skill-name>/
#
# Usage:
#   ./install-skill.sh email-writer
#   ./install-skill.sh resume-bullet-rewriter
#   ./install-skill.sh all    # installs all 14 skills

set -euo pipefail

SKILLS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/skills" && pwd)"
CLAUDE_SKILLS_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

# All known skills
ALL_SKILLS=(
  email-writer
  correction-email-writer
  resume-writer
  resume-editor
  technical-writer
  incident-summary-writer
  stakeholder-update-writer
  requirements-doc-writer
  meeting-notes-to-decision-memo
  linkedin-message-writer
  cover-letter-writer
  resume-bullet-rewriter
  executive-brief-writer
  executive-summary-writer
)

install_skill() {
  local skill="$1"
  local src="$SKILLS_DIR/$skill"
  local dst="$CLAUDE_SKILLS_DIR/$skill"

  if [[ ! -d "$src" ]]; then
    echo "ERROR: Skill not found: $src" >&2
    exit 1
  fi

  mkdir -p "$CLAUDE_SKILLS_DIR"
  cp -r "$src" "$dst"
  echo "Installed: $skill → $dst"
}

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <skill-name> | all"
  echo "Available skills:"
  for s in "${ALL_SKILLS[@]}"; do echo "  $s"; done
  exit 1
fi

if [[ "$1" == "all" ]]; then
  for skill in "${ALL_SKILLS[@]}"; do
    install_skill "$skill"
  done
  echo "All skills installed to $CLAUDE_SKILLS_DIR"
else
  install_skill "$1"
fi
