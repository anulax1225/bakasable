def get(name) -> str:
    return '''workspace "''' + name + '''"
    architecture "x64"
    configurations { "Debug", "Release" }
    startproject "App"

    flags
    {
        "MultiProcessorCompile"
    }
    toolset "clang"
    linkgroups "On"
outputdir = "%{cfg.system}-%{cfg.architecture}-%{cfg.buildcfg}"

include "dependencies.lua"

group "App"
    include "app"
group ""
    '''