# The following five lines of boilerplate have to be in your project's
# CMakeLists in this exact order for cmake to work correctly
cmake_minimum_required(VERSION 3.5)

<<<<<<< HEAD
include($ENV{IDF_PATH}/tools/cmake/project.cmake)

set(EXTRA_COMPONENT_DIRS ../../../SensorLib)

=======
set(EXTRA_COMPONENT_DIRS ../../../SensorLib)

include($ENV{IDF_PATH}/tools/cmake/project.cmake)
>>>>>>> a3fcd92 (fix QMI8658 read FIFO value casting bug and add new functions)
project(ESP_IDF_TouchDrv_Example)
