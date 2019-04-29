cmake_minimum_required(VERSION 3.4.1)

add_library(
        native-lib
        SHARED
        native-lib.cpp
)

add_library(
        intruder
        SHARED
        intruder/intruder.cpp
        ${CMAKE_SOURCE_DIR}/../../../../../../libs/frida-gumjs/${ANDROID_ABI}/frida-gumjs.h
)

find_library(
        log-lib
        log
)

target_link_libraries(
        native-lib
        ${log-lib}
)

target_include_directories(
        intruder
        PRIVATE
        ${CMAKE_SOURCE_DIR}/../../../../../../libs/frida-gumjs/${ANDROID_ABI}
)

target_link_libraries(
        intruder
        ${CMAKE_SOURCE_DIR}/../../../../../../libs/frida-gumjs/${ANDROID_ABI}/libfrida-gumjs.a
)