cmake_minimum_required(VERSION 3.20)
project(crud)

set(CMAKE_CXX_STANDARD 17)

add_library(crud-lib STATIC
    src/App.cpp 
)

target_include_directories(crud-lib PUBLIC src)

find_package(oatpp 1.4.0 REQUIRED)
target_link_libraries(crud-lib PUBLIC oatpp::oatpp)

if(CMAKE_SYSTEM_NAME MATCHES Linux)
    find_package(Threads REQUIRED)
    target_link_libraries(crud-lib INTERFACE Threads::Threads ${CMAKE_DL_LIBS})
endif()

add_executable(crud-exe src/App.cpp)
target_link_libraries(crud-exe PRIVATE crud-lib)
