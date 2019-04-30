#!/usr/local/bin/python3
import os
import tarfile

import requests

version_frida = '12.4.8'

path_base = os.path.abspath(os.path.dirname(__file__))
path_cache = os.path.abspath(os.path.join(path_base, 'cache'))
path_libs = os.path.abspath(os.path.join(path_base, '..', 'libs'))


def download_file(url, filename):
    dest = os.path.join(path_cache, filename)

    if not os.path.exists(dest):
        print("Downloading '%s' to '%s'." % (url, dest))
        r = requests.get(url, allow_redirects=True)
        with open(dest, 'wb') as f:
            f.write(r.content)
    else:
        print("Using cached file of '%s'." % dest)

    return dest


def download_frida():
    download_frida_devkit("armeabi-v7a", "arm", "frida-gumjs")
    download_frida_devkit("arm64-v8a", "arm64", "frida-gumjs")
    download_frida_devkit("x86", "x86", "frida-gumjs")
    download_frida_devkit("x86_64", "x86_64", "frida-gumjs")


def download_frida_devkit(arch, arch_frida, name):
    asset_name = "%s-devkit-%s-android-%s.tar.xz" % (name, version_frida, arch_frida)
    url = "https://github.com/frida/frida/releases/download/%s/%s" % (version_frida, asset_name)
    file = download_file(url, asset_name)
    dest = os.path.join(path_libs, name, arch)

    with tarfile.open(file) as f:
        f.extractall(dest)


def main():
    if not os.path.exists(path_libs):
        os.mkdir(path_libs)

    if not os.path.exists(path_cache):
        os.mkdir(path_cache)

    download_frida()


if __name__ == "__main__":
    main()
