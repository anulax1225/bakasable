def get(name) -> str:
    return '''workspace "''' + name + '''"
    architecture "x64"
    configurations { "Debug", "Release" }
    startproject "App"

    flags
    {
        "MultiProcessorCompile"
    }

    linkgroups "On"
outputdir = "%{cfg.system}-%{cfg.architecture}-%{cfg.buildcfg}"

include "deps.lua"

group "App"
    include "app"
group ""
    '''