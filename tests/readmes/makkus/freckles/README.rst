===================================================
Overview
===================================================

.. image:: https://img.shields.io/pypi/v/freckles.svg
        :target: https://pypi.python.org/pypi/freckles

.. image:: https://img.shields.io/travis/makkus/freckles.svg
        :target: https://travis-ci.org/makkus/freckles

.. image:: https://readthedocs.org/projects/freckles/badge/?version=latest
        :target: https://freckles.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/makkus/freckles/shield.svg
     :target: https://pyup.io/repos/github/makkus/freckles/
     :alt: Updates


*a cute dotfile manager; all over the place*

At its heart, *freckles* is a dotfile manager. You point it to the configuration files of the applications you use, and it makes sure to replicate those configurations across your machines, virtual or not. It also can, if you want it to, do more than that. For example, it can install all the packages you generally use and/or ensure certain folders exists.


*freckles* tries to make it easy to record and replicate the configuration and setup of your working environment (or parts thereof). It's built on top of ansible_, and is meant to be used on a single machine (or VM, or container), not as much for configuring a set of remote machines like typical configuration management systems. It is centered around packages and configurations to re-create working or project environments, rather than setting up infrastructure and/or services on a connected set of boxes.

*freckles* is written in Python, and GPL v3 licensed

Documentation: https://freckles.readthedocs.io.

Features
--------

* one-line setup of a new environment, including freckles bootstrap
* minimal and (hopefully) intuitive config file format, using ``yaml`` syntax
* supports Linux & MacOS X (and probably the Ubuntu subsystem on Windows 10)
* share the same configuration for your Linux and MacOS workstation as well as Vagrant machines, containers, etc.
* support for systems where you don't have root/sudo access via the nix_ package manager or conda_ (or if you just think it's a good idea to use any of them)
* direct support for all ansible_ modules and roles

What, ...why?
-------------

I re-installed a new (or recently bricked) laptop or VM or container this one time too often, and I was annoyed that there is no real easy and quick way to re-create my working environment in those fresh environments, without having to write shell-scripts that sooner or later turn out unmaintainable and are fairly unflexible to begin with. Now, of course, that's what configuration management tools are for, and I do quite like ansible_ and have a bit of experience with it. What I don't like is how one usually needs a set of configuration files to describe a setup, even for simple use-cases like setting up a single, local machine. And I didn't want to install `ansible` itself manually every time before I can run my playbooks and roles. Basically, I wanted a thing that allows me to run one line of code, pointing to one configuration file, and after a while I have the same setup as I have on my other machines.

This is what `freckles` now is, sorta. As a result of my tendency to over-engineer everything in my way along with me having a bit of time on my hands -- it now can do a few other things which I didn't consider before I started working on it, and which may or may not be useful to somebody else. Either way. If you want a simple and lightweight script to manage your machine, you better run, fast. But if you don't mind a bit of what angry oldish IT folk and/or minimalism-hipsters would probably call 'bloat', and you think that a bit of harddrive-space is a good trade-off for saving a few minutes/hours every once in a while, give this here a go and tell me what you think.

Really quick-start
-----------------

.. code-block:: console

   curl -sL https://get.frkl.io | bash -s -- --help

This bootstraps *freckles*, runs it, and displays help information. All files that are installed live under the ``$HOME/.freckles`` folder, which can be deleted without affecting anything else. This also adds a line to your ``$HOME/.profile`` file to add `freckles` to your path.

Quickstart
----------

**Warning: run this only after you read what it does, as it installs some packages onto your computer you might not want. Should not do any real harm though.**

For its most basic use-case -- which is installing and configuring packages -- *freckles* needs:

 - one or more *configuration file(s)*
 - *curl* (or *wget*) -> for bootstrapping (well, technically it also needs *bash*)
 - optionally, a *dotfile repository* -> if some of the applications you want *freckles* to install have configuration files

At the moment (and that might change in the future), the easiest way to install *freckles* is to bootstrap it (more details: :ref:`Bootstrap`) using curl and bash. The bootstrap process can optionally also execute the first *freckles* run, which makes it possible to setup a machine with one line in your shell. Like:

.. code-block:: console

   curl -sL https://get.frkl.io | bash -s -- apply gh:makkus/freckles/examples/quickstart.yml

The config file I've choosen as an example is a bit more complicated than it'd need to be, but I wanted to show off how *freckles* can use the same config file for different platforms. If you only work on one platform, the same config would look quite a bit tidier. Check out the same example for (only) Debian/Ubuntu: `quickstart-debian.yml <https://github.com/makkus/freckles/blob/master/examples/quickstart-debian.yml>`_.

Either, way, the above command applies the following (fairly) simple configuration to your machine:

.. code-block:: yaml

  vars:
    dotfiles:
       - base_dir: ~/dotfiles-quickstart
         remote: https://github.com/makkus/freckles-quickstart.git

  tasks:
    - checkout-dotfiles
    - install:
        use_dotfiles: true
        packages:
          - epel-release:
              pkgs:
                yum:
                  - epel-release
          - htop
          - fortune:
              pkgs:
                apt:
                  - fortunes
                  - fortunes-off
                  - fortunes-mario
                yum:
                  - fortune-mod
                homebrew:
                  - fortune

    - stow
    - create-folder: ~/.backups/zile



What this does:

 - checks out the repository of dotfile(s) at `https://github.com/makkus/freckles-quickstart.git <https://github.com/makkus/freckles-quickstart>`_
 - on Mac OS X, installs homebrew_ if it is not installed already
 - installs the ``epel`` repo if on a RPM-based platform
 - installs all the applications/packages that are configured in this repo (only the emacs-like editor ``zile`` in this case)
 - also installs a few other packages that don't require configuration which is the reason they are not included in the dotfiles repo (``htop`` and, depending on which platform this is run on one or some more packages for the `fortune` tool)
 - `stows <https://www.gnu.org/software/stow/>`_ all the dotfiles in the above repository into the users home directory (again, only for *zile* in this case)
 - creates a folder ``$HOME/.backups/zile`` if it doesn't exist already (needed because it is configured in the ``.zile`` config-file -- contained in the repo we checked out and 'stowed' (means symbolic-linked) to the user home directory -- to be used as backup directory. *zile* does not create that dir itself and errors out if it doesn't exist)

To read how all that works in more detail, please read the full documentation at: :ref:`Usage`

You don't like executing random scripts on the internet? Yeah, me neither. Read here: :ref:`Trust`

Supported platforms
-------------------

Currently tested and supported
++++++++++++++++++++++++++++++

- Debian

  - Jessie

- Ubuntu

  - 16.04
  - 16.10


Planned / Partially supported
+++++++++++++++++++++++++++++

- MacOS X (should mostly work)
- Windows 10 (Ubuntu on Windows)


License
-------

Freckles is free software under the GNU General Public License v3.


Credits
---------

This package was created using, amongst others:

- ansible_
- Cookiecutter_
- nix_
- conda_
- ansible-nix_

.. _ansible: https://ansible.com
.. _nix: https://nixos.org/nix/
.. _conda: https://conda.io
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _ansible-nix: https://github.com/AdamFrey/nix-ansible
.. _homebrew: https://brew.sh/
