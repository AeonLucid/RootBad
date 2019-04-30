@echo off

adb push ..\src\RootBad\.externalNativeBuild\cmake\debug\arm64-v8a\injector /data/local/tmp/rootbad_injector
adb shell chmod 555 /data/local/tmp/rootbad_injector

cls

echo Killing previous injector instance gracefully.
adb shell pkill -f rootbad_injector
timeout 2
adb shell pkill -9 -f rootbad_injector

cls

echo Running injector.
adb shell /data/local/tmp/rootbad_injector