<p><img src="https://vignette2.wikia.nocookie.net/logopedia/images/6/6a/Java-logo.jpg" alt="java logo" title="java" align="right" height="60" /></p>

Ansible Role: java
==================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-java.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-java) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.java-blue.svg)](https://galaxy.ansible.com/SoInteractive/java/) [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-java.svg)](https://github.com/SoInteractive/ansible-java/tags) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

JVM installation

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.java
```

Role can be also run as unprivileged user without ability to use `yum` or `apt`
```yaml
- hosts: all
  roles:
    - SoInteractive.java
  vars:
    java_user_install: true
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.

TODO
----

- Tests, tests, tests
- CentOS7 support
- Tests for user-based install
