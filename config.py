#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser

# Load repo/repo.conf as repo_config
repo_config = ConfigParser.ConfigParser()
repo_config.read("repo/repo.ini")

# Repo git config
git_username = repo_config.get("repo", "git_username")
git_email = repo_config.get("repo", "git_email") 

# Load config sections
sections = repo_config.sections()

# Remove repo config
sections.remove("repo")

# Parse section items to dict
repos = []
for section in sections:
    repo = dict(repo_config.items(section))
    repos.append(repo)